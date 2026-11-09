"""Tests that ingest.py does what rules.md says.

rules.md is the only source of truth. Every test comes from a rule and cites
its section in a comment above the test function and in its docstring.

Clarifications agreed before writing (2026-11-09):
  * Section 1's 18-row problem table is the examples table.
  * Row 4 (stripped-978) is only tested on raw 10-digit values.
  * Row 8: a scientific-notation / float isbn13 with no usable isbn must warn
    and be nulled, with no exception for floats whose digits form a valid
    ISBN-13. That test is expected to fail against the current ingest.py.
  * Reason codes are checked for presence only, never order.
  * Only reason codes named in rules.md are asserted (no-usable-isbn,
    bad-prefix, bad-checksum, isbn-collision, identity-field-conflict,
    duplicate-unchanged). Other section 1 rows check that a warning with the
    raw value exists for the field, whatever its code.
  * "The report" is ingestion-log.json.

All tests run in a temporary folder with test.db; see conftest.py.
"""

import csv

import ingest
from conftest import (
    BOOKS_EXTRA_COLUMNS, CSV_COLUMNS, FAILED, HEADLINE_COUNT_KEYS, HG_ISBN10, HG_ISBN13,
    SUCCESS, WARNINGS_COLUMNS, WITH_ISSUES, is_valid_isbn10, is_valid_isbn13, isbn10_check,
    make_ean13, make_isbn10, make_row, to_isbn13,
)


def codes_of(reason):
    """Reason codes from a comma-separated reason string (order ignored)."""
    return {c.strip() for c in (reason or "").split(",") if c.strip()}


def assert_loaded_with_warning(pipeline, gid, field, raw_value, code=None):
    """Section 1: the row is loaded, the field is NULL, and the warning keeps the raw value."""
    book = pipeline.book(gid)
    assert book is not None, "a bad ISBN must never reject the row"
    assert book[field] is None, f"{field} must be NULL, not {book[field]!r}"
    warnings = pipeline.warnings_for(gid, field)
    assert warnings, f"expected a warning on {field}"
    assert raw_value in [w["raw_value"] for w in warnings], "the raw value must be kept for audit"
    if code:
        assert code in set().union(*(w["codes"] for w in warnings))


# ===========================================================================
# Section 1: repairs
# ===========================================================================

class TestISBNRepair:

    # rules.md §1, row 1: already a valid ISBN-10 or ISBN-13 -> load, no warning
    def test_valid_isbn10_and_isbn13_load_as_is_without_warning(self, pipeline):
        """rules.md §1 row 1: valid ISBNs (978/979 prefix, correct checksum) load unchanged, no warning."""
        pipeline.run([make_row(1, isbn=HG_ISBN10, isbn13=HG_ISBN13)])
        book = pipeline.book(1)
        assert (book["isbn"], book["isbn13"]) == (HG_ISBN10, HG_ISBN13)
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 2: valid but formatted with hyphens/spaces -> strip separators
    def test_hyphens_and_spaces_are_stripped_from_valid_isbns(self, pipeline):
        """rules.md §1 row 2: separators are removed; the checksum is unaffected; no warning."""
        pipeline.run([make_row(1, isbn="0-439-02348-3", isbn13=" 978 0 439 02348 1 ")])
        book = pipeline.book(1)
        assert (book["isbn"], book["isbn13"]) == (HG_ISBN10, HG_ISBN13)
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 3: isbn with leading zero(s) stripped (7-9 digits) -> zero-pad
    def test_leading_zeros_are_restored_when_the_padded_isbn10_passes(self, pipeline):
        """rules.md §1 row 3: a 7-9 digit all-numeric isbn is zero-padded to 10 when that passes the checksum."""
        pipeline.run([make_row(1, isbn="439023483", isbn13=HG_ISBN13)])
        assert pipeline.book(1)["isbn"] == HG_ISBN10
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 4: 10-digit isbn fails, but 978 + it passes -> recompute check digit
    def test_stripped_978_check_digit_is_recomputed_for_raw_10_digit_isbn(self, pipeline):
        """rules.md §1 row 4: a raw 10-digit isbn whose 978-prefixed form is a valid ISBN-13 gets its ISBN-10 check digit recomputed."""
        raw = "1416913184"
        assert not is_valid_isbn10(raw) and is_valid_isbn13("978" + raw)  # precondition
        pipeline.run([make_row(1, isbn=raw, isbn13="")])
        book = pipeline.book(1)
        assert book["isbn"] == "141691318" + isbn10_check("141691318")  # 1416913181
        assert book["isbn13"] == "978" + raw  # row 6 then derives isbn13 from the repaired isbn
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 5: isbn13 in scientific notation / float + valid isbn -> derive isbn13
    def test_scientific_notation_isbn13_is_derived_from_valid_isbn(self, pipeline):
        """rules.md §1 row 5: a scientific-notation isbn13 is replaced by 978 + the valid isbn + check digit, no warning."""
        pipeline.run([make_row(1, isbn=HG_ISBN10, isbn13="9.78043902348e+12")])
        assert pipeline.book(1)["isbn13"] == HG_ISBN13
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 6: isbn13 blank + valid isbn -> derive isbn13
    def test_blank_isbn13_is_derived_from_valid_isbn(self, pipeline):
        """rules.md §1 row 6: isbn13 must be populated whenever a valid ISBN exists."""
        pipeline.run([make_row(1, isbn=HG_ISBN10, isbn13="")])
        assert pipeline.book(1)["isbn13"] == to_isbn13(HG_ISBN10)
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 7: isbn blank/unusable, valid 978 isbn13 -> derive isbn
    def test_blank_isbn_is_derived_from_valid_978_isbn13(self, pipeline):
        """rules.md §1 row 7: a valid 978-prefixed ISBN-13 determines exactly one ISBN-10."""
        pipeline.run([make_row(1, isbn="", isbn13=HG_ISBN13)])
        assert pipeline.book(1)["isbn"] == HG_ISBN10
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 7: 979-prefixed ISBN-13s have no ISBN-10 form -> left blank
    def test_isbn_is_left_blank_for_979_isbn13(self, pipeline):
        """rules.md §1 row 7: a 979-prefixed ISBN-13 has no ISBN-10 form, so isbn stays blank."""
        isbn979 = "9798351220413"
        assert is_valid_isbn13(isbn979)  # precondition
        pipeline.run([make_row(1, isbn="", isbn13=isbn979)])
        book = pipeline.book(1)
        assert book["isbn"] is None
        assert book["isbn13"] == isbn979
        assert pipeline.warnings_for(1) == []

    # rules.md §1, row 13: a valid ISBN-13 in the isbn column -> move to isbn13
    def test_isbn13_found_in_isbn_column_is_moved_to_isbn13(self, pipeline):
        """rules.md §1 row 13: move the value into isbn13 and null isbn; row 7 may then re-populate isbn."""
        pipeline.run([make_row(1, isbn=HG_ISBN13, isbn13="")])
        book = pipeline.book(1)
        assert book["isbn13"] == HG_ISBN13
        assert book["isbn"] == HG_ISBN10  # re-populated by the row 7 reverse derivation
        assert pipeline.warnings_for(1) == []


# ===========================================================================
# Section 1: load with a warning
# ===========================================================================

class TestISBNWarning:

    # rules.md §1, row 8: isbn13 in scientific notation / float, no usable isbn -> warn, NULL
    def test_float_isbn13_without_usable_isbn_is_warned_and_nulled(self, pipeline):
        """rules.md §1 row 8: with no usable isbn, a scientific-notation or float isbn13 is
        nulled with a warning and the raw text kept, including a float whose digits happen
        to form a valid ISBN-13 (no exception). Expected to fail against the current ingest.py."""
        pipeline.run([
            make_row(1, isbn="", isbn13="9.78043902348e+12"),
            make_row(2, isbn="", isbn13="9780439023481.0"),
        ])
        assert_loaded_with_warning(pipeline, 1, "isbn13", "9.78043902348e+12")
        assert_loaded_with_warning(pipeline, 2, "isbn13", "9780439023481.0")

    # rules.md §1, row 9: right length/characters, wrong check digit, no repair -> warn, NULL
    def test_wrong_check_digit_is_warned_and_nulled(self, pipeline):
        """rules.md §1 row 9: a wrong check digit that no repair fixes is nulled with a bad-checksum warning."""
        raw = "0439023484"
        assert not is_valid_isbn10(raw) and not is_valid_isbn13("978" + raw)  # no repair applies
        pipeline.run([make_row(1, isbn=raw, isbn13="")])
        assert_loaded_with_warning(pipeline, 1, "isbn", raw, code="bad-checksum")

    # rules.md §1, row 10: invalid character -> warn, NULL
    def test_letter_inside_isbn_is_warned_and_nulled(self, pipeline):
        """rules.md §1 row 10: a letter where only a digit or trailing X belongs is nulled with a warning."""
        pipeline.run([make_row(1, isbn="04390A3483", isbn13="")])
        assert_loaded_with_warning(pipeline, 1, "isbn", "04390A3483")

    # rules.md §1, row 11: wrong length that isn't a leading-zero case -> warn, NULL
    def test_wrong_length_isbn_is_warned_and_nulled(self, pipeline):
        """rules.md §1 row 11: an 11-digit isbn has no single deterministic correction."""
        pipeline.run([make_row(1, isbn="15287463097", isbn13="")])
        assert_loaded_with_warning(pipeline, 1, "isbn", "15287463097")

    # rules.md §1, row 12: 13 digits, valid checksum, prefix not 978/979 -> warn, NULL
    def test_non_978_979_prefix_is_warned_and_nulled(self, pipeline):
        """rules.md §1 row 12: a 13-digit value with a valid checksum but another prefix is not an ISBN-13."""
        raw = make_ean13("123456789012")  # correct checksum, prefix 123
        pipeline.run([make_row(1, isbn="", isbn13=raw)])
        assert_loaded_with_warning(pipeline, 1, "isbn13", raw, code="bad-prefix")

    # rules.md §1, row 14: both isbn and isbn13 blank -> load with no-usable-isbn
    def test_both_isbn_columns_blank_loads_with_no_usable_isbn(self, pipeline):
        """rules.md §1 row 14: the row still loads, identified by goodreads_book_id, with a no-usable-isbn warning."""
        pipeline.run([make_row(1, isbn="", isbn13="")])
        book = pipeline.book(1)
        assert book is not None
        assert book["isbn"] is None and book["isbn13"] is None
        codes = set().union(*(w["codes"] for w in pipeline.warnings_for(1)))
        assert "no-usable-isbn" in codes

    # rules.md §1, row 16: completely unparseable value -> warn, NULL
    def test_unparseable_isbn_is_warned_and_nulled(self, pipeline):
        """rules.md §1 row 16: letters/symbols only is not a repairable format."""
        pipeline.run([make_row(1, isbn="N/A!!", isbn13="")])
        assert_loaded_with_warning(pipeline, 1, "isbn", "N/A!!")

    # rules.md §1, row 17: more than one problem at once -> list every reason
    def test_every_applicable_reason_is_listed_for_one_field(self, pipeline):
        """rules.md §1 row 17: a value with a bad prefix and a bad checksum lists both reasons (order not checked)."""
        good = make_ean13("123456789012")
        raw = good[:12] + str((int(good[12]) + 1) % 10)  # same digits, wrong check digit
        pipeline.run([make_row(1, isbn="", isbn13=raw)])
        warnings = pipeline.warnings_for(1, "isbn13")
        assert warnings, "expected a warning on isbn13"
        codes = set().union(*(w["codes"] for w in warnings))
        assert {"bad-prefix", "bad-checksum"} <= codes


# ===========================================================================
# Section 1: rejections
# ===========================================================================

class TestRejection:

    # rules.md §1, row 15: a valid ISBN already belongs to a different goodreads_book_id -> reject
    def test_isbn_already_belonging_to_another_book_rejects_the_row(self, pipeline):
        """rules.md §1 row 15: the incoming row is rejected as isbn-collision; the first book is kept."""
        entry = pipeline.run([
            make_row(1, isbn=HG_ISBN10, isbn13=HG_ISBN13),
            make_row(2, isbn=HG_ISBN10, isbn13=HG_ISBN13),
        ])
        assert pipeline.book(1)["isbn13"] == HG_ISBN13
        assert pipeline.book(2) is None
        rejected = [r for r in entry["needs_attention"] if str(r["goodreads_book_id"]) == "2"]
        assert rejected and "isbn-collision" in codes_of(rejected[0]["reason"])

    # rules.md §1, row 18: the row fails to parse as CSV -> reject, reason recorded
    def test_row_with_wrong_field_count_is_rejected_with_a_reason(self, pipeline):
        """rules.md §1 row 18: a row with the wrong field count is rejected and its reason recorded; other rows load."""
        good = make_row(1)
        header = ",".join(CSV_COLUMNS)
        pipeline.write_text(header + "\n" + ",".join(good[c] for c in CSV_COLUMNS) + "\n"
                            + "99,98,97\n")
        entry = pipeline.run()
        assert pipeline.book(1) is not None
        assert pipeline.book(98) is None
        assert entry["counts"]["rejected"] == 1
        rejection = entry["needs_attention"][0]
        assert rejection["row_number"] == 3
        assert rejection["reason"]


# ===========================================================================
# Section 2: identity (invariant 1)
# ===========================================================================

class TestIdentity:

    # rules.md §2: identity is goodreads_book_id alone; no fuzzy title/author matching
    def test_same_title_and_author_with_different_goodreads_ids_are_two_books(self, pipeline):
        """rules.md §2: rows are never matched by title/author, so different goodreads_book_ids are different books."""
        pipeline.run([
            make_row(1, title="Twin", original_title="Twin", authors="Same Author"),
            make_row(2, title="Twin", original_title="Twin", authors="Same Author"),
        ])
        assert pipeline.book(1) is not None
        assert pipeline.book(2) is not None

    # rules.md §2 and §5: one books row per goodreads_book_id; identity_key mirrors it
    def test_goodreads_book_id_is_the_key_and_identity_key_mirrors_it(self, pipeline):
        """rules.md §2/§5: a goodreads_book_id appears once in books, and identity_key equals it."""
        pipeline.run([make_row(7), make_row(7)])
        rows = pipeline.books_with_gid(7)
        assert len(rows) == 1
        assert rows[0]["identity_key"] == "7"


# ===========================================================================
# Section 2: case-insensitive title comparison (invariant 2)
# ===========================================================================

class TestTitleComparison:

    # rules.md §2: title comparison is case-insensitive
    def test_capitalization_only_title_change_is_not_a_change(self, pipeline):
        """rules.md §2: a capitalization-only difference is never treated as a change."""
        pipeline.run([make_row(1, title="The Hunger Games")])
        entry = pipeline.run([make_row(1, title="THE HUNGER GAMES")])
        assert entry["counts"]["rejected"] == 0
        assert entry["counts"]["skipped"] == 1
        assert pipeline.book(1)["title"] == "The Hunger Games"

    # rules.md §2: punctuation and extra whitespace are stripped before comparing
    def test_punctuation_and_whitespace_only_title_change_is_not_a_change(self, pipeline):
        """rules.md §2: titles are compared with punctuation and extra whitespace stripped."""
        pipeline.run([make_row(1, title="The Hunger Games")])
        entry = pipeline.run([make_row(1, title="  The Hunger   Games! ")])
        assert entry["counts"]["rejected"] == 0
        assert entry["counts"]["skipped"] == 1
        assert pipeline.book(1)["title"] == "The Hunger Games"

    # rules.md §2 and §3: a real title change is an identity-field conflict
    def test_real_title_change_is_rejected_as_identity_field_conflict(self, pipeline):
        """rules.md §2/§3: a title that differs beyond case/whitespace rejects the incoming row; the stored title is kept."""
        pipeline.run([make_row(1, title="The Hunger Games")])
        entry = pipeline.run([make_row(1, title="Catching Fire")])
        assert entry["counts"]["rejected"] == 1
        assert "identity-field-conflict" in codes_of(entry["needs_attention"][0]["reason"])
        assert pipeline.book(1)["title"] == "The Hunger Games"


# ===========================================================================
# Section 3: re-ingestion
# ===========================================================================

class TestReingestion:

    # rules.md §3: nothing different -> skip, logged as duplicate-unchanged
    def test_unchanged_book_is_skipped_as_duplicate_unchanged(self, pipeline):
        """rules.md §3: a book that arrives again with nothing different is skipped as duplicate-unchanged."""
        pipeline.run([make_row(1)])
        entry = pipeline.run([make_row(1)])
        assert entry["counts"]["skipped"] == 1
        assert any("duplicate-unchanged" in codes_of(s["reason"]) for s in entry["skipped"])

    # rules.md §3: a volatile-metadata field differs -> update, log old -> new
    def test_volatile_field_change_updates_and_logs_old_and_new(self, pipeline):
        """rules.md §3: a changed volatile field (ratings_count) is updated and its old -> new diff logged."""
        pipeline.run([make_row(1, ratings_count="100")])
        entry = pipeline.run([make_row(1, ratings_count="250")])
        assert entry["counts"]["updated"] == 1
        assert pipeline.book(1)["ratings_count"] == "250"
        diffs = [u for u in entry["updates"] if u["field"] == "ratings_count"]
        assert diffs and (diffs[0]["old"], diffs[0]["new"]) == ("100", "250")

    # rules.md §3: identity-relevant field was empty and the new row fills it -> update
    def test_empty_identity_field_is_filled_by_a_later_row(self, pipeline):
        """rules.md §3: fill-the-gap only: an empty language_code is filled by the next row."""
        pipeline.run([make_row(1, language_code="")])
        entry = pipeline.run([make_row(1, language_code="eng")])
        assert entry["counts"]["updated"] == 1
        assert pipeline.book(1)["language_code"] == "eng"

    # rules.md §3: identity-relevant field already populated and new row disagrees -> reject
    def test_conflicting_identity_field_rejects_and_leaves_book_untouched(self, pipeline):
        """rules.md §3: a different authors value rejects the incoming row (identity-field-conflict); the existing record is untouched."""
        pipeline.run([make_row(1, authors="Suzanne Collins")])
        entry = pipeline.run([make_row(1, authors="Someone Else", ratings_count="999")])
        assert entry["counts"]["rejected"] == 1
        assert "identity-field-conflict" in codes_of(entry["needs_attention"][0]["reason"])
        book = pipeline.book(1)
        assert book["authors"] == "Suzanne Collins"
        assert book["ratings_count"] == "100"  # nothing from the rejected row was saved

    # rules.md §3: identity-relevant field populated and the new row is blank -> no-op
    def test_blank_identity_field_in_new_row_changes_nothing(self, pipeline):
        """rules.md §3: missing information never erases existing information, and isn't a conflict."""
        pipeline.run([make_row(1, language_code="eng")])
        entry = pipeline.run([make_row(1, language_code="")])
        assert entry["counts"]["rejected"] == 0
        assert pipeline.book(1)["language_code"] == "eng"

    # rules.md §2 and §3: incoming ISBN matches a different goodreads_book_id -> reject
    def test_isbn_collision_rejects_even_when_own_goodreads_id_exists(self, pipeline):
        """rules.md §2/§3: isbn-collision applies regardless of whether the row's own goodreads_book_id is on file."""
        other10 = make_isbn10("030734813")
        pipeline.run([make_row(1, isbn=HG_ISBN10, isbn13=HG_ISBN13),
                      make_row(2, isbn=other10, isbn13=to_isbn13(other10))])
        entry = pipeline.run([make_row(1, isbn=other10, isbn13=to_isbn13(other10))])
        assert entry["counts"]["rejected"] == 1
        assert "isbn-collision" in codes_of(entry["needs_attention"][0]["reason"])
        assert pipeline.book(1)["isbn"] == HG_ISBN10


# ===========================================================================
# "No invented information" (invariant 3)
# ===========================================================================

class TestNoInventedInformation:

    # rules.md §1 governing principle, row 9: an unrepairable value is never guessed
    def test_unrepairable_isbn_stays_null_and_nothing_is_derived_from_it(self, pipeline):
        """rules.md §1 principle and row 9: a bad check digit is not corrected, no ISBN-13 is derived from it, and the raw text is kept."""
        raw = "0439023484"
        pipeline.run([make_row(1, isbn=raw, isbn13="")])
        book = pipeline.book(1)
        assert book["isbn"] is None
        assert book["isbn13"] is None
        assert raw in [w["raw_value"] for w in pipeline.warnings_for(1, "isbn")]

    # rules.md §1 governing principle, row 8: lost digits are never reconstructed
    def test_lost_isbn13_digits_are_not_reconstructed_without_isbn(self, pipeline):
        """rules.md §1 principle and row 8: with no usable isbn, a rounded isbn13 is not rebuilt by guessing its lost digits."""
        raw = "9.78043902348e+12"
        pipeline.run([make_row(1, isbn="", isbn13=raw)])
        book = pipeline.book(1)
        assert book["isbn13"] is None
        assert book["isbn"] is None
        assert raw in [w["raw_value"] for w in pipeline.warnings_for(1, "isbn13")]

    # rules.md §3: missing information never erases existing information
    def test_blank_value_never_erases_a_stored_value(self, pipeline):
        """rules.md §3: a later blank original_publication_year leaves the stored year in place."""
        pipeline.run([make_row(1, original_publication_year="2008.0")])
        pipeline.run([make_row(1, original_publication_year="")])
        assert pipeline.book(1)["original_publication_year"] == "2008.0"


# ===========================================================================
# Section 4: the report (invariant 4)
# ===========================================================================

class TestReporting:

    @staticmethod
    def mixed_rows():
        """One clean row, one warned row (both ISBNs blank), one rejected row (ISBN collision)."""
        return [
            make_row(1, isbn=HG_ISBN10, isbn13=HG_ISBN13),
            make_row(2, isbn="", isbn13=""),
            make_row(3, isbn=HG_ISBN10, isbn13=HG_ISBN13),
        ]

    # rules.md §4: SUCCESS -- every row loaded with no warnings
    def test_status_is_success_when_every_row_loads_clean(self, pipeline):
        """rules.md §4: SUCCESS means every row loaded with no warnings."""
        entry = pipeline.run([make_row(1), make_row(2)])
        assert entry["status"] == SUCCESS

    # rules.md §4: COMPLETED WITH ISSUES -- something carries a warning
    def test_status_is_completed_with_issues_when_a_row_has_a_warning(self, pipeline):
        """rules.md §4: a run with a warning is COMPLETED WITH ISSUES, never a plain success."""
        entry = pipeline.run([make_row(1), make_row(2, isbn="", isbn13="")])
        assert entry["status"] == WITH_ISSUES

    # rules.md §4: COMPLETED WITH ISSUES -- something was rejected
    def test_status_is_completed_with_issues_when_a_row_is_rejected(self, pipeline):
        """rules.md §4: a run with a rejection is COMPLETED WITH ISSUES, never a plain success."""
        entry = pipeline.run([make_row(1, isbn=HG_ISBN10, isbn13=HG_ISBN13),
                              make_row(2, isbn=HG_ISBN10, isbn13=HG_ISBN13)])
        assert entry["counts"]["rejected"] == 1
        assert entry["status"] == WITH_ISSUES

    # rules.md §4: FAILED -- the header didn't match (missing or extra column), with the no-rollback note
    def test_status_is_failed_when_header_is_missing_or_has_extra_columns(self, pipeline):
        """rules.md §4: a header with a missing or an extra column is FAILED, and the report says rows may already be saved."""
        missing = [c for c in CSV_COLUMNS if c != "isbn13"]
        entry = pipeline.run([make_row(1)], header=missing)
        assert entry["status"] == FAILED
        assert "may already be saved" in (entry["status_note"] or "")

        extra = CSV_COLUMNS + ["unexpected_column"]
        entry = pipeline.run([make_row(2)], header=extra)
        assert entry["status"] == FAILED
        assert "may already be saved" in (entry["status_note"] or "")

    # rules.md §4: FAILED -- the file couldn't be read
    def test_status_is_failed_when_the_file_cannot_be_read(self, pipeline, monkeypatch):
        """rules.md §4: a file that can't be read makes the run FAILED."""
        monkeypatch.setattr(ingest, "CSV_FILENAME", str(pipeline.folder / "does-not-exist.csv"))
        ingest.main(["ingest.py"])
        entry = pipeline.log()[-1]
        assert entry["status"] == FAILED
        assert "may already be saved" in (entry["status_note"] or "")

    # rules.md §4: headline counts, broken out separately
    def test_headline_counts_are_reported_and_add_up(self, pipeline):
        """rules.md §4: rows read, loaded, updated, skipped, rejected and rows with a warning are all reported."""
        entry = pipeline.run(self.mixed_rows())
        counts = entry["counts"]
        for key in HEADLINE_COUNT_KEYS:
            assert key in counts, f"missing headline count {key}"
        assert counts["rows_read"] == 3
        assert (counts["loaded"], counts["updated"], counts["skipped"], counts["rejected"]) == (2, 0, 0, 1)
        assert counts["rows_with_warning"] == 1
        assert counts["loaded"] + counts["updated"] + counts["skipped"] + counts["rejected"] == counts["rows_read"]

    # rules.md §4: rejections kept visibly separate from routine warnings
    def test_rejections_are_kept_separate_from_warnings(self, pipeline):
        """rules.md §4: the rejected row is listed with rejections only; the warned row with warnings only."""
        entry = pipeline.run(self.mixed_rows())
        assert {str(r["goodreads_book_id"]) for r in entry["needs_attention"]} == {"3"}
        assert {str(w["goodreads_book_id"]) for w in entry["warnings"]} == {"2"}

    # rules.md §4: per-row detail for every row that wasn't a clean load
    def test_warned_row_detail_names_file_row_title_value_rule_and_action(self, pipeline):
        """rules.md §4: file, row number, title, original offending value, rule hit, and what the system did."""
        raw = "0439023484"
        entry = pipeline.run([make_row(1, isbn=raw, isbn13="", title="Detail Book")])
        details = [w for w in entry["warnings"] if w["field"] == "isbn"]
        assert details, "expected per-row detail for the warned isbn"
        d = details[0]
        assert d["source_file"] == "test.csv"
        assert d["row_number"] == 2
        assert d["title"] == "Detail Book"
        assert d["raw_value"] == raw
        assert "bad-checksum" in codes_of(d["reason"])
        assert d["action"]

    # rules.md §4: every run appends one entry; no prior entry is overwritten
    def test_each_run_appends_and_never_overwrites_earlier_entries(self, pipeline):
        """rules.md §4: the log grows by one entry per run and earlier entries stay as they were."""
        pipeline.run([make_row(1)])
        first = pipeline.log()[0]
        pipeline.run([make_row(1)])
        log = pipeline.log()
        assert len(log) == 2
        assert log[0] == first


# ===========================================================================
# Section 5: schema
# ===========================================================================

class TestSchema:

    # rules.md §5: books holds the 23 CSV fields plus identity_key, fallback_key,
    # source_file, first_loaded_at, last_updated_at
    def test_books_table_has_every_required_column(self, pipeline):
        """rules.md §5: the books table has the 23 source fields and the five tracking columns."""
        pipeline.run([make_row(1)])
        columns = set(pipeline.table_columns("books"))
        missing = [c for c in CSV_COLUMNS + BOOKS_EXTRA_COLUMNS if c not in columns]
        assert missing == []

    # rules.md §5: warnings holds book_row_id, field, raw_value, reason, recorded_at
    def test_warnings_table_has_every_required_column(self, pipeline):
        """rules.md §5: the warnings table has book_row_id, field, raw_value, reason and recorded_at."""
        pipeline.run([make_row(1)])
        columns = set(pipeline.table_columns("warnings"))
        missing = [c for c in WARNINGS_COLUMNS if c not in columns]
        assert missing == []


# ===========================================================================
# Operational details
# ===========================================================================

class TestOperational:

    # rules.md, Operational details: the CSV path is a fixed constant, not a command-line argument
    def test_csv_path_comes_from_constant_not_command_line(self, pipeline):
        """rules.md Operational details: ingest.py loads CSV_FILENAME, never a file named on the command line."""
        assert isinstance(ingest.CSV_FILENAME, str)
        other = pipeline.folder / "other.csv"
        with open(other, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            w.writeheader()
            w.writerow(make_row(5))
        ingest.main(["ingest.py", str(other)])
        assert pipeline.book(5) is None

    # rules.md, Operational details: same input file -> same result
    def test_same_file_gives_the_same_database_contents(self, pipeline, monkeypatch):
        """rules.md Operational details: no randomness: the same file loaded into two fresh databases gives identical data (timestamps aside)."""
        pipeline.write_csv([
            make_row(1),
            make_row(2, isbn="439023483", isbn13="9.78043902348e+12"),
            make_row(3, isbn="", isbn13=""),
            make_row(4, isbn="0439023484", isbn13=""),
        ])
        ingest.main(["ingest.py"])
        first_books = pipeline.table_rows("books", exclude={"first_loaded_at", "last_updated_at"})
        first_warnings = pipeline.table_rows("warnings", exclude={"recorded_at"})

        second_db = pipeline.folder / "test-second.db"
        monkeypatch.setattr(ingest, "DB_FILE", str(second_db))
        ingest.main(["ingest.py"])
        pipeline.db_path = second_db
        assert pipeline.table_rows("books", exclude={"first_loaded_at", "last_updated_at"}) == first_books
        assert pipeline.table_rows("warnings", exclude={"recorded_at"}) == first_warnings
