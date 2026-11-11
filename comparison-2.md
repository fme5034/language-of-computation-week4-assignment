# Comparison: Anthony's books.db vs. Abigail's books.db

**Headline: SAME DATA**

- Anthony's book count: 10,013
- Abigail's book count: 10,013
- Books only in Anthony's database: **0**
- Books only in Abigail's database: **0**
- Books in both with differing field values: **0** (0 total field-level differences across 0 books)
- Books with differing warnings: **0**

## Methodology

- **Identity:** `goodreads_book_id` alone (rules.md Section 2).
- **Columns compared (23):** `book_id`, `goodreads_book_id`, `best_book_id`, `work_id`, `books_count`, `isbn`, `isbn13`, `authors`, `original_publication_year`, `original_title`, `title`, `language_code`, `average_rating`, `ratings_count`, `work_ratings_count`, `work_text_reviews_count`, `ratings_1`, `ratings_2`, `ratings_3`, `ratings_4`, `ratings_5`, `image_url`, `small_image_url`.
- **Columns excluded (6, load metadata):** `id`, `identity_key`, `fallback_key`, `source_file`, `first_loaded_at`, `last_updated_at`.
- **Warnings:** compared as sets of `(field, reason, raw_value)` tuples per `goodreads_book_id`. Excludes `warnings.id` and `warnings.recorded_at`.

## Books only in Anthony's database (0)

_None._

## Books only in Abigail's database (0)

_None._

## Books with different field values (0 books, 0 differences)

_None._

## Books with different warnings (0)

_None._

## Why our data differs

When I compared my database with Abigail's, I found that our results were exactly the same. We both had all 10,013 books, and after comparing all 23 columns, there were no differences between our databases.

I also checked the warnings for all 707 books that had them, and those matched as well. We recorded the same fields, used the same warning codes, and kept the same original values.

What stood out to me was that Abigail and I worked on our implementations separately, but we still ended up with the same results by following the merged rules.md file.

This was especially interesting because some of the differences I found when comparing my database with Kristina's didn't show up here.

For example, Abigail and I both used SQL NULL for missing or invalid values, which follows Section 1 of rules.md where it says to "null the field." We also used the same warning codes, such as `lost-precision`, `bad-characters`, and `no-usable-isbn`.

Another thing I noticed was that we attached the `no-usable-isbn` warning to the same column when both ISBN fields were blank. We also handled rows with multiple problems the same way by recording the warnings consistently.

Because of this, there weren't any differences in how our data was stored or how the warnings were recorded.

### Overall Assessment

After reviewing the comparison, I think Abigail's results help show that we both understood and applied the merged rules in the same way.

At the same time, I wouldn't say this proves our code would always produce identical results with every possible CSV file. There could still be situations or unusual values that weren't included in the files we tested.

What I can say is that for the two files we were assigned, `books.csv` and `books-batch2.csv`, our databases matched completely.

To me, this shows how important it is to have clear rules and follow them consistently. Even though Abigail and I wrote our code independently, we were able to produce the same results.

The biggest thing I took away from this comparison is that when the rules, tests, and code line up, it's possible for two separate implementations to produce identical results. Comparing my work with Abigail's gave me more confidence that my implementation was handling the assigned data correctly.
