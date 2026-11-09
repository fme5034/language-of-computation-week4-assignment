#!/usr/bin/env python3
"""Load books.csv into books.db, following rules.md ("Rules for loading
books.csv / books-batch2.csv (final, as implemented)").

Usage:
    python ingest.py

The input file is the constant CSV_FILENAME below, not a command-line
argument, so a run is always exactly reproducible from this file alone
(rules.md, Operational details). To load a different file, change
CSV_FILENAME, save, and run again. books.db and ingestion-log.json are
written to the current working directory.

Python 3 standard library only. No network, no AI, no randomness: the same
input file always produces the same result. Every row is checked on every
run, and books are matched by goodreads_book_id, so running the same file
twice never creates duplicates.

The rules in short:
  * Identity is goodreads_book_id alone (section 2).
  * A bad or missing ISBN never rejects the row: the field is nulled, a
    warning is attached, and the row is loaded (section 1).
  * Repairs are only made when they are deterministic and checksum-verifiable.
  * Only an ISBN collision, an identity-field conflict, or a row that fails
    to parse rejects a row (sections 1-3).
  * Each row is saved as it is processed. FAILED is a status label, not a
    rollback guarantee (section 4).
"""

import csv
import hashlib
import io
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

CSV_FILENAME = "books.csv"
DB_FILE = "books.db"
LOG_FILE = "ingestion-log.json"
RULES = "rules.md (final, as implemented)"

# The 23 fields from the source CSV, in file order (section 5). The header must
# match this exactly, or the run is FAILED (section 4).
COLUMNS = (
    "book_id", "goodreads_book_id", "best_book_id", "work_id", "books_count", "isbn", "isbn13",
    "authors", "original_publication_year", "original_title", "title", "language_code",
    "average_rating", "ratings_count", "work_ratings_count", "work_text_reviews_count",
    "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5", "image_url", "small_image_url",
)

# Section 3. original_title is in neither list, so it is stored on first load
# and never compared or updated afterwards.
VOLATILE_FIELDS = (
    "average_rating", "ratings_count", "work_ratings_count", "work_text_reviews_count",
    "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5", "books_count",
    "image_url", "small_image_url", "best_book_id", "book_id",
)
IDENTITY_FIELDS = ("title", "authors", "original_publication_year", "work_id", "language_code",
                   "isbn", "isbn13")

# Section 5: two tables. Every books column is TEXT.
EXTRA_COLUMNS = ("identity_key", "fallback_key", "source_file", "first_loaded_at", "last_updated_at")
BOOK_COLUMNS = COLUMNS + EXTRA_COLUMNS
SCHEMA = f"""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    {", ".join(f"{c} TEXT" for c in BOOK_COLUMNS)}
);
CREATE UNIQUE INDEX IF NOT EXISTS books_goodreads_book_id ON books(goodreads_book_id);
CREATE INDEX IF NOT EXISTS books_identity_key ON books(identity_key);
CREATE INDEX IF NOT EXISTS books_isbn ON books(isbn);
CREATE INDEX IF NOT EXISTS books_isbn13 ON books(isbn13);
CREATE TABLE IF NOT EXISTS warnings (
    id INTEGER PRIMARY KEY,
    book_row_id INTEGER NOT NULL REFERENCES books(id),
    field TEXT,
    raw_value TEXT,
    reason TEXT,
    recorded_at TEXT
);
CREATE INDEX IF NOT EXISTS warnings_book_row_id ON warnings(book_row_id);
"""

# Run status (section 4).
SUCCESS, WITH_ISSUES, FAILED = "SUCCESS", "COMPLETED WITH ISSUES", "FAILED"
FAILED_NOTE = ("Status: FAILED - no atomicity guarantee is implemented for this pipeline; "
               "rows loaded before the failure may already be saved.")

# Reason codes. Rejections:
STRUCTURAL_PARSE_ERROR = "structural-parse-error"
ISBN_COLLISION = "isbn-collision"
IDENTITY_FIELD_CONFLICT = "identity-field-conflict"
# Skip:
DUPLICATE_UNCHANGED = "duplicate-unchanged"
# Warnings:
NO_USABLE_ISBN = "no-usable-isbn"
LOST_PRECISION = "lost-precision"
BAD_PREFIX = "bad-prefix"
BAD_CHECKSUM = "bad-checksum"
BAD_LENGTH = "bad-length"
BAD_CHARACTERS = "bad-characters"
UNPARSEABLE = "unparseable"
# Repairs:
FORMATTING_REMOVED = "formatting-removed"
FLOAT_FORMAT_REMOVED = "float-format-removed"
LEADING_ZEROS_RESTORED = "leading-zeros-restored"
STRIPPED_978_RESTORED = "stripped-978-restored"
ISBN13_MOVED_FROM_ISBN = "isbn13-moved-from-isbn"
ISBN13_DERIVED_FROM_ISBN = "isbn13-derived-from-isbn"
ISBN_DERIVED_FROM_ISBN13 = "isbn-derived-from-isbn13"

REJECT_CODES = (STRUCTURAL_PARSE_ERROR, ISBN_COLLISION, IDENTITY_FIELD_CONFLICT)
WARNING_CODES = (NO_USABLE_ISBN, LOST_PRECISION, BAD_PREFIX, BAD_CHECKSUM, BAD_LENGTH,
                 BAD_CHARACTERS, UNPARSEABLE)
SKIP_CODES = (DUPLICATE_UNCHANGED,)

LOADED, UPDATED, SKIPPED, REJECTED = "loaded", "updated", "skipped", "rejected"
WARNING_ACTION = {
    LOADED: "loaded; field stored as empty (raw value kept in the warnings table)",
    UPDATED: "updated; field stored as empty (raw value kept in the warnings table)",
    SKIPPED: "skipped (duplicate-unchanged); the warning still applies",
}
REJECT_ACTION = "rejected: not loaded; flagged for manual review"


class IngestError(Exception):
    """A problem that makes the run FAILED."""


# --------------------------------------------------------------------------
# ISBN checks and repairs (section 1)
# --------------------------------------------------------------------------

SEPARATOR_RE = re.compile(r"[\s\-]")
NUMBER_RE = re.compile(r"\d+(?:\.\d*)?(?:[eE]\+?\d+)?")


def clean(raw):
    """Strip separators (spaces, hyphens); uppercase a final x."""
    s = SEPARATOR_RE.sub("", raw.strip())
    return s[:-1] + "X" if s.endswith("x") else s


def isbn10_check_char(first9):
    total = sum((10 - i) * int(d) for i, d in enumerate(first9))
    check = (11 - total % 11) % 11
    return "X" if check == 10 else str(check)


def isbn13_check_digit(first12):
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(first12))
    return str((10 - total % 10) % 10)


def is_valid_isbn10(s):
    return bool(re.fullmatch(r"\d{9}[\dX]", s)) and isbn10_check_char(s[:9]) == s[9]


def has_valid_mod10(s):
    return bool(re.fullmatch(r"\d{13}", s)) and isbn13_check_digit(s[:12]) == s[12]


def is_valid_isbn13(s):
    """Correct checksum and a 978/979 prefix."""
    return has_valid_mod10(s) and s.startswith(("978", "979"))


def isbn10_to_isbn13(isbn10):
    first12 = "978" + isbn10[:9]
    return first12 + isbn13_check_digit(first12)


def isbn13_to_isbn10(isbn13):
    """Only 978 ISBN-13s have an ISBN-10 form."""
    first9 = isbn13[3:12]
    return first9 + isbn10_check_char(first9)


def repair(field, code, original, new):
    return {"field": field, "reason": code, "original": original, "new": new}


def reasons_for(s, expected_length):
    """Every reason a cleaned value isn't a usable ISBN (section 1, multi-reason row)."""
    if not re.search(r"\d", s):
        return [UNPARSEABLE]
    allowed = r"\d+X?" if expected_length == 10 else r"\d+"
    out = []
    if not re.fullmatch(allowed, s):
        out.append(BAD_CHARACTERS)
    if len(s) != expected_length:
        out.append(BAD_LENGTH)
    if expected_length == 13 and len(s) == 13 and s.isdigit():
        if not s.startswith(("978", "979")):
            out.append(BAD_PREFIX)
        if not has_valid_mod10(s):
            out.append(BAD_CHECKSUM)
    if expected_length == 10 and not out:
        out.append(BAD_CHECKSUM)
    return out


def stripped_978(candidate, column, repairs):
    """A 10-digit candidate that fails its own checksum, but 978 + it is a valid
    ISBN-13: recompute the ISBN-10 check digit. Returns the repaired value or None."""
    if len(candidate) == 10 and candidate.isdigit() and is_valid_isbn13("978" + candidate):
        fixed = candidate[:9] + isbn10_check_char(candidate[:9])
        repairs.append(repair(column, STRIPPED_978_RESTORED, candidate, fixed))
        return fixed
    return None


def check_isbn_column(raw):
    """The `isbn` (ISBN-10) column. Returns (isbn10, isbn13_found_here, reasons, repairs).
    Repairs are only kept when the value ends up usable."""
    if raw is None or not raw.strip():
        return None, None, [], []
    s = clean(raw)
    repairs = [repair("isbn", FORMATTING_REMOVED, raw, s)] if s != raw.strip() else []

    if is_valid_isbn13(s):  # a valid ISBN-13 sitting in the ISBN-10 column
        return None, s, [], repairs
    if len(s) == 10 and is_valid_isbn10(s):
        return s, None, [], repairs
    if len(s) == 10:
        fixed = stripped_978(s, "isbn", repairs)
        if fixed:
            return fixed, None, [], repairs
    if 7 <= len(s) <= 9 and s.isdigit():  # leading zeros stripped (all-numeric)
        padded = "0" * (10 - len(s)) + s
        if is_valid_isbn10(padded):
            return padded, None, [], repairs + [repair("isbn", LEADING_ZEROS_RESTORED, s, padded)]
        # The padded value is a 10-digit candidate: try the stripped-978 repair on it.
        trial = [repair("isbn", LEADING_ZEROS_RESTORED, s, padded)]
        fixed = stripped_978(padded, "isbn", trial)
        if fixed:
            return fixed, None, [], repairs + trial
        return None, None, [BAD_CHECKSUM], []
    return None, None, reasons_for(s, 10), []


def digits_shown(number_text):
    """Significant digits actually written in a number like '9.78043902348e+12'."""
    return len(re.split(r"[eE]", number_text)[0].replace(".", "").lstrip("0"))


def check_isbn13_column(raw):
    """The `isbn13` column. Returns (isbn13, reasons, repairs, is_float).
    is_float is True when the value was stored as scientific notation or a float."""
    if raw is None or not raw.strip():
        return None, [], [], False
    s = clean(raw)
    repairs = [repair("isbn13", FORMATTING_REMOVED, raw, s)] if s != raw.strip() else []

    if not s.isdigit() and NUMBER_RE.fullmatch(s):
        try:
            n = Decimal(s)
        except InvalidOperation:
            return None, [BAD_CHARACTERS], [], True
        if n != n.to_integral_value():
            return None, [BAD_CHARACTERS], [], True
        digits = str(int(n))
        if digits_shown(s) < len(digits):
            found = [LOST_PRECISION]  # the real digits are permanently lost
            if len(digits) != 13:
                found.append(BAD_LENGTH)
            elif not digits.startswith(("978", "979")):
                found.append(BAD_PREFIX)
            return None, found, [], True
        if is_valid_isbn13(digits):  # every digit survived and the checksum proves it
            return digits, [], repairs + [repair("isbn13", FLOAT_FORMAT_REMOVED, s, digits)], True
        return None, reasons_for(digits, 13), [], True

    if is_valid_isbn13(s):
        return s, [], repairs, False
    return None, reasons_for(s, 13), [], False


def add_reason(warnings, field, code):
    warnings.setdefault(field, [])
    if code not in warnings[field]:
        warnings[field].append(code)


def resolve_isbns(raw_isbn, raw_isbn13):
    """Decide which ISBN-10 and ISBN-13 a row gets (section 1).
    Returns (isbn10, isbn13, warnings {field: [codes]}, repairs)."""
    v10, found13, r10, rep10 = check_isbn_column(raw_isbn)
    v13, r13, rep13, is_float = check_isbn13_column(raw_isbn13)
    repairs = rep10 + rep13
    warnings = {}
    if r10:
        warnings["isbn"] = list(r10)
    if r13:
        warnings["isbn13"] = list(r13)

    if found13:
        if v13 is None:
            # Move the value into isbn13 and null isbn. If isbn13 held an unusable
            # value it keeps its warning, except a float, which is a repair.
            repairs.append(repair("isbn13", ISBN13_MOVED_FROM_ISBN, raw_isbn, found13))
            v13 = found13
            if is_float:
                warnings.pop("isbn13", None)
        elif v13 != found13:
            # isbn13 already holds a different valid ISBN-13, so there is nowhere to
            # move this one: a 13-character value in the ISBN-10 column is the
            # wrong length (warn, null).
            add_reason(warnings, "isbn", BAD_LENGTH)

    if v10 and not v13:
        # isbn13 is blank, or stored as scientific notation / float: derive it from
        # the valid isbn (repair, no warning for the float).
        v13 = isbn10_to_isbn13(v10)
        repairs.append(repair("isbn13", ISBN13_DERIVED_FROM_ISBN, raw_isbn13 or "", v13))
        if is_float:
            warnings.pop("isbn13", None)
    if v13 and not v10 and v13.startswith("978"):
        v10 = isbn13_to_isbn10(v13)
        repairs.append(repair("isbn", ISBN_DERIVED_FROM_ISBN13, raw_isbn or "", v10))

    if blank(raw_isbn) and blank(raw_isbn13):
        add_reason(warnings, "isbn13", NO_USABLE_ISBN)  # both columns blank
    return v10, v13, warnings, repairs


# --------------------------------------------------------------------------
# One row
# --------------------------------------------------------------------------

def blank(value):
    return value is None or not str(value).strip()


def normalize_text(text):
    """Lowercase, strip punctuation and extra whitespace (section 2)."""
    text = re.sub(r"[^\w\s]", "", (text or "").casefold())
    return " ".join(text.split())


def fallback_key(title, authors):
    """Informational normalized title+author string, not used for matching (section 5)."""
    return f"{normalize_text(title)}|{normalize_text(authors)}"


def same_value(field, old, new):
    if field == "title":
        return normalize_text(old) == normalize_text(new)
    return old == new


def analyse_row(raw):
    """Apply section 1 to one parsed row. Returns (record, warnings, repairs);
    warnings is a list of (field, raw_value, [codes])."""
    record = {c: (None if blank(raw.get(c)) else raw[c]) for c in COLUMNS}
    record["goodreads_book_id"] = (raw.get("goodreads_book_id") or "").strip()
    v10, v13, found, repairs = resolve_isbns(raw.get("isbn"), raw.get("isbn13"))
    record["isbn"], record["isbn13"] = v10, v13
    warnings = [(f, raw.get(f) or "", found[f]) for f in ("isbn", "isbn13") if f in found]
    return record, warnings, repairs


# --------------------------------------------------------------------------
# Reading the CSV
# --------------------------------------------------------------------------

def read_rows(path):
    """All data rows as (line_number, dict-or-None, problem). Line 1 is the header;
    line numbers are file line numbers."""
    try:
        with open(path, "rb") as f:
            text = f.read().decode("utf-8-sig")
    except FileNotFoundError:
        raise IngestError(f"file not found: {path}")
    except OSError as e:
        raise IngestError(f"file could not be read: {e}")
    except UnicodeDecodeError as e:
        raise IngestError(f"file could not be read as UTF-8 text: {e}")

    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    try:
        header = next(reader)
    except (StopIteration, csv.Error):
        raise IngestError("the file has no readable header row")
    if header != list(COLUMNS):
        missing = [c for c in COLUMNS if c not in header]
        extra = [c for c in header if c not in COLUMNS]
        detail = []
        if missing:
            detail.append("missing: " + ", ".join(missing))
        if extra:
            detail.append("unexpected: " + ", ".join(extra))
        if not detail:
            detail.append("columns are in a different order")
        raise IngestError("the header didn't match the 23 expected columns (" + "; ".join(detail) + ")")

    rows = []
    prev_end = reader.line_num
    while True:
        start = prev_end + 1
        try:
            fields = next(reader)
        except StopIteration:
            break
        except csv.Error as e:
            prev_end = reader.line_num
            rows.append((start, None, f"broken quoting: {e}"))
            continue
        prev_end = reader.line_num
        if not fields:
            continue  # a completely blank line is not a row
        row = dict(zip(header, fields))
        if len(fields) != len(header):
            rows.append((start, row, f"wrong number of fields ({len(fields)}, expected {len(header)})"))
        else:
            rows.append((start, row, None))
    return rows


# --------------------------------------------------------------------------
# One run
# --------------------------------------------------------------------------

def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Run:
    def __init__(self, conn, source_file, stamp):
        self.conn, self.source_file, self.stamp = conn, source_file, stamp
        self.outcomes = []  # (outcome, had_warning) per row
        self.rejections, self.warnings, self.repairs, self.updates, self.skips = [], [], [], [], []
        self.problem_counts = {}

    def ref(self, line, raw, **extra):
        raw = raw or {}
        return {"source_file": self.source_file, "row_number": line,
                "goodreads_book_id": raw.get("goodreads_book_id"), "title": raw.get("title"),
                **extra}

    def count(self, code):
        self.problem_counts[code] = self.problem_counts.get(code, 0) + 1

    def reject(self, line, raw, code, detail):
        self.count(code)
        raw = raw or {}
        self.rejections.append(self.ref(line, raw, raw_isbn=raw.get("isbn"),
                                        raw_isbn13=raw.get("isbn13"), reason=code,
                                        detail=detail, action=REJECT_ACTION))
        self.outcomes.append((REJECTED, False))

    def save_warnings(self, book_row_id, warnings):
        """A book's warnings are replaced when it is loaded or updated."""
        self.conn.execute("DELETE FROM warnings WHERE book_row_id = ?", (book_row_id,))
        self.conn.executemany(
            "INSERT INTO warnings (book_row_id, field, raw_value, reason, recorded_at) "
            "VALUES (?, ?, ?, ?, ?)",
            [(book_row_id, f, raw_value, ",".join(codes), self.stamp)
             for f, raw_value, codes in warnings])

    def process(self, line, raw, problem):
        if problem:
            return self.reject(line, raw, STRUCTURAL_PARSE_ERROR, problem)
        record, warnings, repairs = analyse_row(raw)
        gid = record["goodreads_book_id"]

        # Collision rule: a valid ISBN that already belongs to a different
        # goodreads_book_id rejects the row, whether or not this row's own
        # goodreads_book_id is already on file (section 2).
        for f in ("isbn13", "isbn"):
            if record[f]:
                other = self.conn.execute(
                    f"SELECT goodreads_book_id, title FROM books "
                    f"WHERE {f} = ? AND goodreads_book_id != ?", (record[f], gid)).fetchone()
                if other:
                    return self.reject(line, raw, ISBN_COLLISION,
                                       f"{f} {record[f]} already belongs to goodreads_book_id "
                                       f"{other[0]} ('{other[1]}')")

        old = self.conn.execute("SELECT * FROM books WHERE goodreads_book_id = ?", (gid,)).fetchone()
        if old is None:
            outcome = self.create(record, warnings)
        else:
            outcome = self.compare(line, raw, record, warnings, dict(old))
        if outcome == REJECTED:
            return

        for f, raw_value, codes in warnings:
            for code in codes:
                self.count(code)
            self.warnings.append(self.ref(line, raw, field=f, raw_value=raw_value,
                                          reason=",".join(codes), action=WARNING_ACTION[outcome]))
        if outcome != SKIPPED:  # repairs are only listed when they were saved
            for r in repairs:
                self.count(r["reason"])
                self.repairs.append(self.ref(line, raw, **r))
        self.outcomes.append((outcome, bool(warnings)))

    def create(self, record, warnings):
        values = dict(record, identity_key=record["goodreads_book_id"],
                      fallback_key=fallback_key(record["title"], record["authors"]),
                      source_file=self.source_file, first_loaded_at=self.stamp,
                      last_updated_at=None)
        cur = self.conn.execute(
            f"INSERT INTO books ({', '.join(BOOK_COLUMNS)}) "
            f"VALUES ({', '.join('?' * len(BOOK_COLUMNS))})",
            [values[c] for c in BOOK_COLUMNS])
        self.save_warnings(cur.lastrowid, warnings)
        return LOADED

    def compare(self, line, raw, record, warnings, old):
        changes, conflicts = [], []
        for f in IDENTITY_FIELDS:
            new, cur = record[f], old[f]
            if new is None or same_value(f, cur, new):
                continue  # a blank never erases existing information
            if cur is None:
                changes.append((f, cur, new))  # fill the gap
            else:
                conflicts.append(f"{f}: on file '{cur}', incoming '{new}'")
        if conflicts:
            self.reject(line, raw, IDENTITY_FIELD_CONFLICT, "; ".join(conflicts))
            return REJECTED

        changes += [(f, old[f], record[f]) for f in VOLATILE_FIELDS if record[f] != old[f]]
        if not changes:
            self.count(DUPLICATE_UNCHANGED)
            self.skips.append(self.ref(line, raw, reason=DUPLICATE_UNCHANGED,
                                       action="skipped: already on file, nothing changed"))
            return SKIPPED
        for f, cur, new in changes:
            self.conn.execute(f"UPDATE books SET {f} = ? WHERE id = ?", (new, old["id"]))
            self.updates.append(self.ref(line, raw, field=f, old=cur, new=new))
        title = record["title"] if old["title"] is None else old["title"]
        authors = record["authors"] if old["authors"] is None else old["authors"]
        self.conn.execute("UPDATE books SET last_updated_at = ?, fallback_key = ? WHERE id = ?",
                          (self.stamp, fallback_key(title, authors), old["id"]))
        self.save_warnings(old["id"], warnings)
        return UPDATED


def problem_order(item):
    code, count = item
    kind = (0 if code in REJECT_CODES else 1 if code in WARNING_CODES
            else 2 if code in SKIP_CODES else 3)
    return kind, -count, code


def ingest(csv_path):
    """Run one file and return its log entry."""
    started = utc_now()
    sha = None
    if os.path.isfile(csv_path):
        with open(csv_path, "rb") as f:
            sha = hashlib.sha256(f.read()).hexdigest()

    run = Run(None, os.path.basename(csv_path), started)
    rows_read, status, error = 0, FAILED, None
    conn = None
    try:
        rows = read_rows(csv_path)  # a header mismatch fails before books.db is opened
        rows_read = len(rows)
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        conn.executescript(SCHEMA)
        run.conn = conn
        for line, raw, problem in rows:
            run.process(line, raw, problem)
            conn.commit()  # each row is saved as it is processed
        if len(run.outcomes) != rows_read:
            raise IngestError(f"counts don't add up: read {rows_read} rows "
                              f"but processed {len(run.outcomes)}")
        status = SUCCESS if not run.rejections and not run.warnings else WITH_ISSUES
    except Exception as e:  # anything that stops the run
        if conn is not None:
            conn.rollback()  # undoes only the row in progress; earlier rows stay saved
        error = str(e) if isinstance(e, IngestError) else f"unexpected error: {e!r}"
    finally:
        if conn is not None:
            conn.close()

    n = {o: sum(1 for out, _ in run.outcomes if out == o) for o in (LOADED, UPDATED, SKIPPED, REJECTED)}
    loaded_warned = sum(1 for out, warned in run.outcomes if out == LOADED and warned)
    return {
        "started_at": started,
        "finished_at": utc_now(),
        "file": os.path.basename(csv_path),
        "file_sha256": sha,
        "rules": RULES,
        "status": status,
        "status_note": FAILED_NOTE if status == FAILED else None,
        "error": error,
        "counts": {
            "rows_read": rows_read,
            "loaded": n[LOADED],
            "loaded_clean": n[LOADED] - loaded_warned,
            "loaded_with_warning": loaded_warned,
            "updated": n[UPDATED],
            "skipped": n[SKIPPED],
            "rejected": n[REJECTED],
            "rows_with_warning": sum(1 for _, warned in run.outcomes if warned),
            "rows_repaired": len({x["row_number"] for x in run.repairs}),
        },
        "counts_add_up": rows_read == sum(n.values()),
        "problem_counts": dict(sorted(run.problem_counts.items(), key=problem_order)),
        "needs_attention": run.rejections,
        "warnings": run.warnings,
        "updates": run.updates,
        "skipped": run.skips,
        "repairs": run.repairs,
    }


# --------------------------------------------------------------------------
# The log
# --------------------------------------------------------------------------

def load_log():
    """Earlier runs, or [] when the log doesn't exist yet. Stops without changing
    anything if the log exists but can't be read, so no prior entry is ever lost."""
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        sys.exit(f"ERROR: {LOG_FILE} exists but can't be read ({e}). "
                 "Nothing was changed. Fix or move the file and run again.")
    if not isinstance(data, list):
        sys.exit(f"ERROR: {LOG_FILE} is not a JSON list of runs. "
                 "Nothing was changed. Fix or move the file and run again.")
    return data


def write_log(runs):
    """Written to a temp file and swapped in, so the log is never left half-written."""
    tmp = LOG_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(runs, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, LOG_FILE)


def main(argv):
    if len(argv) != 1:
        print("ingest.py takes no arguments. To load a different file, change CSV_FILENAME "
              "at the top of ingest.py.", file=sys.stderr)
        return 2
    runs = load_log()  # checked before anything is changed
    entry = ingest(CSV_FILENAME)
    runs.append(entry)
    write_log(runs)

    c = entry["counts"]
    print(f"{entry['status']}: {entry['file']} at {entry['started_at']}")
    if entry["error"]:
        print(f"  error: {entry['error']}")
        print(f"  {entry['status_note']}")
    print(f"  read {c['rows_read']}: loaded {c['loaded']} ({c['loaded_clean']} clean, "
          f"{c['loaded_with_warning']} with a warning), updated {c['updated']}, "
          f"skipped {c['skipped']}, rejected {c['rejected']}")
    print(f"  rows with a warning {c['rows_with_warning']}, rows repaired {c['rows_repaired']}")
    print(f"  log: {LOG_FILE}")
    return 1 if entry["status"] == FAILED else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
