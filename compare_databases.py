#!/usr/bin/env python3
"""
compare_databases.py - Week 4 Part 5 database comparison tool.

Compares the local books.db against partner-1/books.db (Kristina) and
partner-2/books.db (Abigail), producing comparison-1.md and comparison-2.md
in the format required by the assignment.

Identity rule (rules.md Section 2): goodreads_book_id alone identifies a book.

Compared columns (23 CSV-derived fields):
  book_id, goodreads_book_id, best_book_id, work_id, books_count,
  isbn, isbn13, authors, original_publication_year, original_title, title,
  language_code, average_rating, ratings_count, work_ratings_count,
  work_text_reviews_count, ratings_1, ratings_2, ratings_3, ratings_4, ratings_5,
  image_url, small_image_url

Excluded columns (6 load-metadata fields):
  id, identity_key, fallback_key, source_file, first_loaded_at, last_updated_at

Warnings compared as sets of (field, reason, raw_value) per goodreads_book_id.
Excludes warnings.id and warnings.recorded_at.

Usage:
  cd ~/workspace/language-of-computation/week4-assignment
  python compare_databases.py

The script is READ-ONLY on all databases.
"""

import sqlite3
import os
import sys
from collections import defaultdict

# -------------------- Config --------------------

MY_DB = "books.db"
PARTNERS = [
    ("partner-1", "Kristina", "comparison-1.md"),
    ("partner-2", "Abigail",  "comparison-2.md"),
]

COMPARE_COLUMNS = [
    "book_id", "goodreads_book_id", "best_book_id", "work_id", "books_count",
    "isbn", "isbn13", "authors", "original_publication_year", "original_title",
    "title", "language_code", "average_rating", "ratings_count",
    "work_ratings_count", "work_text_reviews_count",
    "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5",
    "image_url", "small_image_url",
]

EXCLUDED_COLUMNS = [
    "id", "identity_key", "fallback_key", "source_file",
    "first_loaded_at", "last_updated_at",
]


# -------------------- Helpers --------------------

def load_books(db_path):
    """Return {goodreads_book_id: {column: value}} for all books."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cols_sql = ", ".join(COMPARE_COLUMNS)
    rows = conn.execute(f"SELECT {cols_sql} FROM books").fetchall()
    books = {}
    for r in rows:
        d = dict(r)
        gid = d["goodreads_book_id"]
        books[gid] = d
    conn.close()
    return books


def load_warnings(db_path):
    """Return {goodreads_book_id: set of (field, reason, raw_value)}."""
    conn = sqlite3.connect(db_path)
    rows = conn.execute("""
        SELECT b.goodreads_book_id, w.field, w.reason, w.raw_value
        FROM warnings w
        JOIN books b ON w.book_row_id = b.id
    """).fetchall()
    warnings = defaultdict(set)
    for gid, field, reason, raw in rows:
        warnings[gid].add((field, reason, raw))
    conn.close()
    return warnings


def compare_books(mine, theirs):
    """Return (only_mine, only_theirs, differing) where differing is
    a list of (gid, column, mine_value, their_value)."""
    my_ids = set(mine.keys())
    their_ids = set(theirs.keys())
    only_mine = sorted(my_ids - their_ids)
    only_theirs = sorted(their_ids - my_ids)
    differing = []
    shared = my_ids & their_ids
    for gid in sorted(shared):
        for col in COMPARE_COLUMNS:
            mv = mine[gid][col]
            tv = theirs[gid][col]
            if mv != tv:
                differing.append((gid, col, mv, tv))
    return only_mine, only_theirs, differing


def compare_warnings(mine_w, theirs_w, mine_b, theirs_b):
    """Return list of (gid, title, only_mine_set, only_theirs_set)
    for every book whose warning sets differ."""
    all_ids = set(mine_w.keys()) | set(theirs_w.keys())
    diffs = []
    for gid in sorted(all_ids):
        m = mine_w.get(gid, set())
        t = theirs_w.get(gid, set())
        if m != t:
            title = (mine_b.get(gid, {}).get("title") or
                     theirs_b.get(gid, {}).get("title") or "(unknown)")
            diffs.append((gid, title, m - t, t - m))
    return diffs


# -------------------- Report writer --------------------

def write_comparison(path, my_name, partner_name,
                     mine_books, theirs_books,
                     mine_warn, theirs_warn):
    only_mine, only_theirs, differing = compare_books(mine_books, theirs_books)
    warn_diffs = compare_warnings(mine_warn, theirs_warn, mine_books, theirs_books)

    same = (len(only_mine) == 0 and len(only_theirs) == 0
            and len(differing) == 0 and len(warn_diffs) == 0)
    headline = "SAME DATA" if same else "DIFFERENT DATA"
    diff_book_ids = {g for g, _, _, _ in differing}

    lines = []
    lines.append(f"# Comparison: {my_name}'s books.db vs. {partner_name}'s books.db")
    lines.append("")
    lines.append(f"**Headline: {headline}**")
    lines.append("")
    lines.append(f"- {my_name}'s book count: {len(mine_books):,}")
    lines.append(f"- {partner_name}'s book count: {len(theirs_books):,}")
    lines.append(f"- Books only in {my_name}'s database: **{len(only_mine)}**")
    lines.append(f"- Books only in {partner_name}'s database: **{len(only_theirs)}**")
    lines.append(f"- Books in both with differing field values: **{len(diff_book_ids)}** "
                 f"({len(differing)} total field-level differences across "
                 f"{len(diff_book_ids)} books)")
    lines.append(f"- Books with differing warnings: **{len(warn_diffs)}**")
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append("- **Identity:** `goodreads_book_id` alone (rules.md Section 2).")
    lines.append(f"- **Columns compared ({len(COMPARE_COLUMNS)}):** "
                 f"{', '.join(f'`{c}`' for c in COMPARE_COLUMNS)}.")
    lines.append(f"- **Columns excluded ({len(EXCLUDED_COLUMNS)}, load metadata):** "
                 f"{', '.join(f'`{c}`' for c in EXCLUDED_COLUMNS)}.")
    lines.append("- **Warnings:** compared as sets of `(field, reason, raw_value)` "
                 "tuples per `goodreads_book_id`. Excludes `warnings.id` and "
                 "`warnings.recorded_at`.")
    lines.append("")

    # Section: only in mine
    lines.append(f"## Books only in {my_name}'s database ({len(only_mine)})")
    lines.append("")
    if not only_mine:
        lines.append("_None._")
    else:
        lines.append("| goodreads_book_id | title |")
        lines.append("|---|---|")
        for gid in only_mine[:500]:
            title = (mine_books[gid]["title"] or "").replace("|", "\\|")
            lines.append(f"| {gid} | {title} |")
        if len(only_mine) > 500:
            lines.append(f"| ... | _(truncated, {len(only_mine) - 500} more)_ |")
    lines.append("")

    # Section: only in theirs
    lines.append(f"## Books only in {partner_name}'s database ({len(only_theirs)})")
    lines.append("")
    if not only_theirs:
        lines.append("_None._")
    else:
        lines.append("| goodreads_book_id | title |")
        lines.append("|---|---|")
        for gid in only_theirs[:500]:
            title = (theirs_books[gid]["title"] or "").replace("|", "\\|")
            lines.append(f"| {gid} | {title} |")
        if len(only_theirs) > 500:
            lines.append(f"| ... | _(truncated, {len(only_theirs) - 500} more)_ |")
    lines.append("")

    # Section: field differences
    lines.append(f"## Books with different field values ({len(diff_book_ids)} books, "
                 f"{len(differing)} differences)")
    lines.append("")
    if not differing:
        lines.append("_None._")
    else:
        lines.append(f"| goodreads_book_id | column | {my_name}'s value | "
                     f"{partner_name}'s value |")
        lines.append("|---|---|---|---|")
        for gid, col, mv, tv in differing[:1000]:
            mv_s = str(mv).replace("|", "\\|").replace("\n", " ")[:120]
            tv_s = str(tv).replace("|", "\\|").replace("\n", " ")[:120]
            lines.append(f"| {gid} | `{col}` | {mv_s} | {tv_s} |")
        if len(differing) > 1000:
            lines.append(f"| ... | ... | ... | _(truncated, {len(differing) - 1000} more)_ |")
    lines.append("")

    # Section: warning differences
    lines.append(f"## Books with different warnings ({len(warn_diffs)})")
    lines.append("")
    if not warn_diffs:
        lines.append("_None._")
    else:
        lines.append(f"| goodreads_book_id | title | in {my_name}'s only | "
                     f"in {partner_name}'s only |")
        lines.append("|---|---|---|---|")
        for gid, title, m_only, t_only in warn_diffs[:500]:
            title_s = (title or "").replace("|", "\\|")[:80]
            m_s = "; ".join(f"({f}, {r}, {rv})" for f, r, rv in sorted(m_only))
            t_s = "; ".join(f"({f}, {r}, {rv})" for f, r, rv in sorted(t_only))
            m_s = m_s.replace("|", "\\|").replace("\n", " ")[:200] or "---"
            t_s = t_s.replace("|", "\\|").replace("\n", " ")[:200] or "---"
            lines.append(f"| {gid} | {title_s} | {m_s} | {t_s} |")
        if len(warn_diffs) > 500:
            lines.append(f"| ... | ... | ... | _(truncated, {len(warn_diffs) - 500} more)_ |")
    lines.append("")

    # Placeholder for the required "Why our data differs" section
    lines.append("## Why our data differs")
    lines.append("")
    lines.append("_[WRITE THIS SECTION YOURSELF - in your own words, per the assignment.")
    lines.append("For each class of difference above, state which rule from rules.md it")
    lines.append("traces to and whether the rule, the tests, or the code let it through.")
    lines.append("If the databases are identical, say so explicitly.]_")
    lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# -------------------- Main --------------------

def main():
    # Sanity-check files exist
    missing = []
    if not os.path.isfile(MY_DB):
        missing.append(MY_DB)
    for folder, _, _ in PARTNERS:
        p = os.path.join(folder, "books.db")
        if not os.path.isfile(p):
            missing.append(p)
    if missing:
        print(f"ERROR: missing required files: {missing}", file=sys.stderr)
        print("Run this script from ~/workspace/language-of-computation/week4-assignment",
              file=sys.stderr)
        sys.exit(1)

    print(f"Loading my books from {MY_DB}...")
    mine_books = load_books(MY_DB)
    mine_warn = load_warnings(MY_DB)
    print(f"  {len(mine_books):,} books, "
          f"{sum(len(v) for v in mine_warn.values()):,} warnings "
          f"across {len(mine_warn):,} books.")

    for folder, partner_name, output_file in PARTNERS:
        partner_db = os.path.join(folder, "books.db")
        print(f"\nLoading {partner_name}'s books from {partner_db}...")
        theirs_books = load_books(partner_db)
        theirs_warn = load_warnings(partner_db)
        print(f"  {len(theirs_books):,} books, "
              f"{sum(len(v) for v in theirs_warn.values()):,} warnings "
              f"across {len(theirs_warn):,} books.")

        print(f"Comparing and writing {output_file}...")
        write_comparison(output_file, "Anthony", partner_name,
                         mine_books, theirs_books, mine_warn, theirs_warn)

        # Print summary to stdout
        only_mine, only_theirs, differing = compare_books(mine_books, theirs_books)
        warn_diffs = compare_warnings(mine_warn, theirs_warn, mine_books, theirs_books)
        diff_book_ids = {g for g, _, _, _ in differing}
        same = (not only_mine and not only_theirs
                and not differing and not warn_diffs)
        print(f"  Result: {'SAME DATA' if same else 'DIFFERENT DATA'}")
        print(f"    Only in mine: {len(only_mine)}")
        print(f"    Only in {partner_name}'s: {len(only_theirs)}")
        print(f"    Books with differing fields: {len(diff_book_ids)} "
              f"({len(differing)} total differences)")
        print(f"    Books with differing warnings: {len(warn_diffs)}")

    print("\nDone. Review comparison-1.md and comparison-2.md.")
    print("Remember: write the 'Why our data differs' section YOURSELF.")


if __name__ == "__main__":
    main()
