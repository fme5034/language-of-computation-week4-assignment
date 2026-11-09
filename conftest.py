"""Shared fixtures and helpers for test_ingest.py.

Isolation: every test runs in its own temporary folder. ingest.py's DB_FILE,
LOG_FILE and CSV_FILENAME are redirected there (test.db,
test-ingestion-log.json, test.csv) with monkeypatch, the working directory is
switched to it, and the folder is deleted when the test ends. ingest.py itself
is not edited, and no test reads or writes the real books.db or
ingestion-log.json. A session-level guard fails the run if either real file
changes.

The ISBN helpers below are written from the ISBN-10 / ISBN-13 checksum
definitions, not imported from ingest.py, so the tests never grade the code
with its own math.
"""

import csv
import json
import shutil
import sqlite3
from contextlib import closing
from pathlib import Path

import pytest

import ingest

PROJECT_DIR = Path(__file__).resolve().parent
REAL_FILES = (PROJECT_DIR / "books.db", PROJECT_DIR / "ingestion-log.json")

# rules.md section 5: the 23 fields from the source CSV.
CSV_COLUMNS = [
    "book_id", "goodreads_book_id", "best_book_id", "work_id", "books_count", "isbn", "isbn13",
    "authors", "original_publication_year", "original_title", "title", "language_code",
    "average_rating", "ratings_count", "work_ratings_count", "work_text_reviews_count",
    "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5", "image_url", "small_image_url",
]

# rules.md section 5: the extra books columns and the warnings columns.
BOOKS_EXTRA_COLUMNS = ["identity_key", "fallback_key", "source_file", "first_loaded_at",
                       "last_updated_at"]
WARNINGS_COLUMNS = ["book_row_id", "field", "raw_value", "reason", "recorded_at"]

# rules.md section 4 lists what every report must include but doesn't name the
# JSON keys. These are the keys ingest.py's ingestion-log.json uses for them;
# they are the only names the tests take from the code.
#   status, status_note            -> the three-tier run status and its note
#   counts[...]                    -> headline counts
#   needs_attention                -> rejections (kept separate)
#   warnings                       -> per-row detail for warned rows
#   updates                        -> old -> new diffs
#   skipped                        -> rows skipped as duplicate-unchanged
HEADLINE_COUNT_KEYS = ["rows_read", "loaded", "updated", "skipped", "rejected", "rows_with_warning"]

# Section 4 status values.
SUCCESS = "SUCCESS"
WITH_ISSUES = "COMPLETED WITH ISSUES"
FAILED = "FAILED"

# Values used across tests (The Hunger Games).
HG_ISBN10 = "0439023483"
HG_ISBN13 = "9780439023481"


# ---------------------------------------------------------------------------
# Independent ISBN math
# ---------------------------------------------------------------------------

def isbn10_check(first9):
    """ISBN-10 check character: weights 10..2, mod 11, 10 written as X."""
    total = sum((10 - i) * int(d) for i, d in enumerate(first9))
    check = (11 - total % 11) % 11
    return "X" if check == 10 else str(check)


def isbn13_check(first12):
    """ISBN-13 / EAN-13 check digit: weights 1,3,1,3..., mod 10."""
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(first12))
    return str((10 - total % 10) % 10)


def is_valid_isbn10(value):
    return (len(value) == 10 and value[:9].isdigit()
            and (value[9].isdigit() or value[9] == "X")
            and isbn10_check(value[:9]) == value[9])


def is_valid_isbn13(value):
    return (len(value) == 13 and value.isdigit() and value.startswith(("978", "979"))
            and isbn13_check(value[:12]) == value[12])


def make_isbn10(first9):
    return first9 + isbn10_check(first9)


def make_ean13(first12):
    """A 13-digit number with a correct checksum (any prefix)."""
    return first12 + isbn13_check(first12)


def to_isbn13(isbn10):
    first12 = "978" + isbn10[:9]
    return first12 + isbn13_check(first12)


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

def make_row(gid, **overrides):
    """One complete CSV row for goodreads_book_id `gid`, with valid, unique
    ISBNs unless overridden. Same gid + same overrides -> identical row."""
    gid = int(gid)
    isbn10 = make_isbn10(f"{gid:09d}")
    row = {
        "book_id": str(gid),
        "goodreads_book_id": str(gid),
        "best_book_id": str(gid),
        "work_id": str(5000 + gid),
        "books_count": "1",
        "isbn": isbn10,
        "isbn13": to_isbn13(isbn10),
        "authors": f"Author {gid}",
        "original_publication_year": "2000.0",
        "original_title": f"Title {gid}",
        "title": f"Title {gid}",
        "language_code": "eng",
        "average_rating": "4.0",
        "ratings_count": "100",
        "work_ratings_count": "110",
        "work_text_reviews_count": "10",
        "ratings_1": "1",
        "ratings_2": "2",
        "ratings_3": "3",
        "ratings_4": "4",
        "ratings_5": "90",
        "image_url": f"https://example.com/{gid}m.jpg",
        "small_image_url": f"https://example.com/{gid}s.jpg",
    }
    row.update(overrides)
    return row


class Pipeline:
    """Runs ingest.py against files in one temporary folder and reads the results."""

    def __init__(self, folder):
        self.folder = folder
        self.csv_path = folder / "test.csv"
        self.db_path = folder / "test.db"
        self.log_path = folder / "test-ingestion-log.json"

    # --- input -------------------------------------------------------------
    def write_csv(self, rows, header=None):
        header = header or CSV_COLUMNS
        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=header, extrasaction="ignore", restval="")
            writer.writeheader()
            writer.writerows(rows)

    def write_text(self, text):
        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            f.write(text)

    # --- running -----------------------------------------------------------
    def run(self, rows=None, header=None):
        """Write `rows` (if given) to test.csv, run ingest.py, return the new log entry."""
        if rows is not None:
            self.write_csv(rows, header)
        ingest.main(["ingest.py"])
        return self.log()[-1]

    # --- output ------------------------------------------------------------
    def log(self):
        if not self.log_path.exists():
            return []
        with open(self.log_path, encoding="utf-8") as f:
            return json.load(f)

    def _query(self, sql, params=()):
        if not self.db_path.exists():
            return []
        with closing(sqlite3.connect(self.db_path)) as conn:
            conn.row_factory = sqlite3.Row
            return [dict(r) for r in conn.execute(sql, params)]

    def book(self, gid):
        rows = self._query("SELECT * FROM books WHERE goodreads_book_id = ?", (str(gid),))
        return rows[0] if rows else None

    def books_with_gid(self, gid):
        return self._query("SELECT * FROM books WHERE goodreads_book_id = ?", (str(gid),))

    def warnings_for(self, gid, field=None):
        """The book's rows in the warnings table, each with a `codes` set."""
        rows = self._query(
            "SELECT w.* FROM warnings w JOIN books b ON b.id = w.book_row_id "
            "WHERE b.goodreads_book_id = ? ORDER BY w.id", (str(gid),))
        for r in rows:
            r["codes"] = {c.strip() for c in (r["reason"] or "").split(",") if c.strip()}
        return [r for r in rows if field is None or r["field"] == field]

    def table_columns(self, table):
        return [r["name"] for r in self._query(f"PRAGMA table_info({table})")]

    def table_rows(self, table, exclude=()):
        rows = self._query(f"SELECT * FROM {table} ORDER BY id")
        return [{k: v for k, v in r.items() if k not in exclude} for r in rows]


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _fingerprint(path):
    if not path.exists():
        return None
    st = path.stat()
    return st.st_size, st.st_mtime_ns


@pytest.fixture(scope="session", autouse=True)
def real_files_untouched():
    """Fails the session if the real books.db or ingestion-log.json changed."""
    before = {str(p): _fingerprint(p) for p in REAL_FILES}
    yield
    after = {str(p): _fingerprint(p) for p in REAL_FILES}
    assert before == after, "a test changed the real books.db or ingestion-log.json"


@pytest.fixture(autouse=True)
def pipeline(tmp_path, monkeypatch):
    """A fresh temporary folder per test, with ingest.py pointed at it.
    Autouse, so no test can run against the real files by accident."""
    work = tmp_path / "work"
    work.mkdir()
    p = Pipeline(work)
    monkeypatch.setattr(ingest, "DB_FILE", str(p.db_path))
    monkeypatch.setattr(ingest, "LOG_FILE", str(p.log_path))
    monkeypatch.setattr(ingest, "CSV_FILENAME", str(p.csv_path))
    monkeypatch.chdir(work)
    yield p
    # Teardown: leave the folder, then delete everything the test created.
    monkeypatch.undo()
    shutil.rmtree(work)  # raises if anything couldn't be deleted
