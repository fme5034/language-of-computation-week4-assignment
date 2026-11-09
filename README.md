# Language of Computation — Week 4 Assignment

This is my Module 4 assignment for MSAI-5523, with my partners Kristina Winegar and Abigail Ruby.

## Files

| File | What it is |
| --- | --- |
| `rules.md` | The ingestion rules: the only source of truth for the pipeline and the tests |
| `ingest.py` | Loads a books CSV into `books.db` and appends a run entry to `ingestion-log.json` |
| `report.html` | Opens `ingestion-log.json` in a browser and shows each run |
| `test_ingest.py` | The pytest suite: 46 tests, each citing the `rules.md` section it checks |
| `conftest.py` | Shared fixtures and helpers that keep every test isolated in a temporary folder |

`ingest.py` loads `books.csv` and `books-batch2.csv` from this folder, so copy both files in before running it.

## Setup

Requires Python 3. In Git Bash, from this folder:

```bash
python -m pip install pytest
```

`ingest.py` itself uses only the standard library; pytest is needed only for the tests.

## Running the tests

```bash
python -m pytest -v
```

To save the results to a file:

```bash
python -m pytest -v 2>&1 | tee test-results-before.txt
```

The tests never touch the real `books.db` or `ingestion-log.json`. Each test points `ingest.py` at a temporary `test.db`, `test-ingestion-log.json` and `test.csv` in its own temporary folder, and deletes that folder when it finishes. A session-level check fails the run if either real file changes.

Test classes, each mapped to `rules.md`:

| Class | Tests | rules.md |
| --- | ---: | --- |
| `TestISBNRepair` | 9 | §1 rows 1–7 and 13 |
| `TestISBNWarning` | 8 | §1 rows 8–12, 14, 16 and 17 |
| `TestRejection` | 2 | §1 rows 15 and 18 |
| `TestIdentity` | 2 | §2, §5 |
| `TestTitleComparison` | 3 | §2, §3 |
| `TestReingestion` | 6 | §3 |
| `TestNoInventedInformation` | 3 | §1 governing principle, §3 |
| `TestReporting` | 9 | §4 |
| `TestSchema` | 2 | §5 |
| `TestOperational` | 2 | Operational details |

`TestISBNWarning::test_float_isbn13_without_usable_isbn_is_warned_and_nulled` is expected to fail against the current `ingest.py`. The code treats a float `isbn13` whose digits form a valid ISBN-13 (e.g. `9780439023481.0`) as a repair, but `rules.md` §1 row 8 says it must be warned and nulled.

## Running ingest.py

`ingest.py` takes no arguments. The file it loads is the constant `CSV_FILENAME` at the top of the script (`books.csv`), as `rules.md` requires.

Load `books.csv`:

```bash
python ingest.py
```

Load `books.csv` again (every book should be skipped as `duplicate-unchanged`):

```bash
python ingest.py
```

Load `books-batch2.csv`, setting the constant for this one run without editing `ingest.py`:

```bash
python -c "import sys, ingest; ingest.CSV_FILENAME = 'books-batch2.csv'; sys.exit(ingest.main(['ingest.py']))"
```

Each run adds `books.db` rows and one `ingestion-log.json` entry in this folder. Open `report.html` in a browser and choose `ingestion-log.json` to see the runs, newest first.
