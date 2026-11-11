# Comparison: Anthony's books.db vs. Kristina's books.db

**Headline: DIFFERENT DATA**

- Anthony's book count: 10,013
- Kristina's book count: 10,013
- Books only in Anthony's database: **0**
- Books only in Kristina's database: **0**
- Books in both with differing field values: **2142** (3136 total field-level differences across 2142 books)
- Books with differing warnings: **706**

## Methodology

- **Identity:** `goodreads_book_id` alone (rules.md Section 2).
- **Columns compared (23):** `book_id`, `goodreads_book_id`, `best_book_id`, `work_id`, `books_count`, `isbn`, `isbn13`, `authors`, `original_publication_year`, `original_title`, `title`, `language_code`, `average_rating`, `ratings_count`, `work_ratings_count`, `work_text_reviews_count`, `ratings_1`, `ratings_2`, `ratings_3`, `ratings_4`, `ratings_5`, `image_url`, `small_image_url`.
- **Columns excluded (6, load metadata):** `id`, `identity_key`, `fallback_key`, `source_file`, `first_loaded_at`, `last_updated_at`.
- **Warnings:** compared as sets of `(field, reason, raw_value)` tuples per `goodreads_book_id`. Excludes `warnings.id` and `warnings.recorded_at`.

## Books only in Anthony's database (0)

_None._

## Books only in Kristina's database (0)

_None._

## Books with different field values (2142 books, 3136 differences)

| goodreads_book_id | column | Anthony's value | Kristina's value |
|---|---|---|---|
| 1001896 | `language_code` | None |  |
| 10058 | `language_code` | None |  |
| 10088913 | `isbn` | None |  |
| 10088913 | `isbn13` | None |  |
| 10092 | `language_code` | None |  |
| 1009996 | `original_title` | None |  |
| 10111087 | `original_title` | None |  |
| 10155 | `language_code` | None |  |
| 10161216 | `original_title` | None |  |
| 10169662 | `isbn` | None |  |
| 10169662 | `isbn13` | None |  |
| 10209997 | `original_title` | None |  |
| 10211494 | `original_title` | None |  |
| 102954 | `language_code` | None |  |
| 10295484 | `isbn` | None |  |
| 10295484 | `isbn13` | None |  |
| 102958 | `original_title` | None |  |
| 10305231 | `language_code` | None |  |
| 103111 | `original_title` | None |  |
| 10327303 | `language_code` | None |  |
| 10335318 | `original_title` | None |  |
| 1034605 | `language_code` | None |  |
| 10365 | `language_code` | None |  |
| 10365343 | `original_title` | None |  |
| 10374 | `isbn` | None |  |
| 10374 | `isbn13` | None |  |
| 103902 | `language_code` | None |  |
| 10395 | `language_code` | None |  |
| 10421530 | `language_code` | None |  |
| 1044141 | `original_publication_year` | None |  |
| 1044141 | `original_title` | None |  |
| 1045757 | `language_code` | None |  |
| 10468258 | `isbn` | None |  |
| 10468258 | `isbn13` | None |  |
| 10473214 | `original_title` | None |  |
| 104734 | `language_code` | None |  |
| 10506 | `language_code` | None |  |
| 10508526 | `original_title` | None |  |
| 105189 | `isbn` | None |  |
| 105189 | `isbn13` | None |  |
| 1052 | `original_title` | None |  |
| 10537195 | `original_title` | None |  |
| 10538 | `language_code` | None |  |
| 1055617 | `language_code` | None |  |
| 1056627 | `original_publication_year` | None |  |
| 1056627 | `original_title` | None |  |
| 1056627 | `language_code` | None |  |
| 105760 | `language_code` | None |  |
| 10586539 | `isbn` | None |  |
| 10586539 | `isbn13` | None |  |
| 10592 | `language_code` | None |  |
| 10594929 | `original_title` | None |  |
| 1059680 | `language_code` | None |  |
| 10599302 | `isbn` | None |  |
| 10599302 | `isbn13` | None |  |
| 10604115 | `original_title` | None |  |
| 10604115 | `language_code` | None |  |
| 106131 | `language_code` | None |  |
| 10618 | `original_title` | None |  |
| 10659536 | `language_code` | None |  |
| 10661081 | `original_title` | None |  |
| 10664113 | `isbn` | None |  |
| 10664113 | `isbn13` | None |  |
| 10706934 | `isbn` | None |  |
| 10706934 | `isbn13` | None |  |
| 10710392 | `original_title` | None |  |
| 107195 | `language_code` | None |  |
| 107291 | `language_code` | None |  |
| 10762697 | `original_title` | None |  |
| 107664 | `language_code` | None |  |
| 107670 | `language_code` | None |  |
| 10776793 | `isbn` | None |  |
| 10776793 | `isbn13` | None |  |
| 10778410 | `original_title` | None |  |
| 10778410 | `language_code` | None |  |
| 107821 | `language_code` | None |  |
| 10785687 | `language_code` | None |  |
| 10790276 | `language_code` | None |  |
| 10790376 | `isbn` | None |  |
| 10790376 | `isbn13` | None |  |
| 10801027 | `isbn` | None |  |
| 10801027 | `isbn13` | None |  |
| 10813469 | `isbn` | None |  |
| 10813469 | `isbn13` | None |  |
| 10813469 | `original_title` | None |  |
| 10813480 | `isbn` | None |  |
| 10813480 | `isbn13` | None |  |
| 10830444 | `isbn` | None |  |
| 10830444 | `isbn13` | None |  |
| 10868182 | `language_code` | None |  |
| 10875239 | `language_code` | None |  |
| 10907 | `language_code` | None |  |
| 10913 | `language_code` | None |  |
| 109515 | `language_code` | None |  |
| 10960383 | `original_title` | None |  |
| 10970532 | `language_code` | None |  |
| 10975 | `isbn` | None |  |
| 10975 | `isbn13` | None |  |
| 1099097 | `language_code` | None |  |
| 11051889 | `original_title` | None |  |
| 11051889 | `language_code` | None |  |
| 110692 | `language_code` | None |  |
| 1107001 | `language_code` | None |  |
| 11076177 | `original_title` | None |  |
| 11096647 | `isbn` | None |  |
| 11096647 | `isbn13` | None |  |
| 11101772 | `original_title` | None |  |
| 11104030 | `original_title` | None |  |
| 11104933 | `language_code` | None |  |
| 111126 | `language_code` | None |  |
| 1111600 | `language_code` | None |  |
| 111220 | `original_title` | None |   |
| 1113545 | `language_code` | None |  |
| 11198480 | `original_title` | None |  |
| 11201007 | `isbn` | None |  |
| 11201007 | `isbn13` | None |  |
| 11227040 | `isbn` | None |  |
| 11227040 | `isbn13` | None |  |
| 11227041 | `isbn` | None |  |
| 11227041 | `isbn13` | None |  |
| 11227043 | `isbn` | None |  |
| 11227043 | `isbn13` | None |  |
| 11227043 | `original_title` | None |  |
| 112292 | `language_code` | None |  |
| 11237412 | `isbn` | None |  |
| 11237412 | `isbn13` | None |  |
| 11239856 | `isbn` | None |  |
| 11239856 | `isbn13` | None |  |
| 11239856 | `original_title` | None |  |
| 11260526 | `original_title` | None |  |
| 11262424 | `isbn` | None |  |
| 11262424 | `isbn13` | None |  |
| 11266880 | `original_title` | None |  |
| 11281852 | `original_title` | None |  |
| 112872 | `language_code` | None |  |
| 112874 | `language_code` | None |  |
| 1129315 | `original_title` | None |  |
| 11306337 | `original_title` | None |  |
| 11306337 | `language_code` | None |  |
| 11312 | `language_code` | None |  |
| 11318 | `original_publication_year` | None |  |
| 11324166 | `isbn` | None |  |
| 11324166 | `isbn13` | None |  |
| 11337912 | `language_code` | None |  |
| 113429 | `language_code` | None |  |
| 11350430 | `isbn` | None |  |
| 11350430 | `isbn13` | None |  |
| 113576 | `language_code` | None |  |
| 11381910 | `language_code` | None |  |
| 11382346 | `isbn` | None |  |
| 11382346 | `isbn13` | None |  |
| 11389341 | `original_title` | None |  |
| 11391817 | `original_title` | None |  |
| 11395597 | `language_code` | None |  |
| 11401915 | `language_code` | None |  |
| 11408650 | `isbn` | None |  |
| 11408650 | `isbn13` | None |  |
| 11413 | `original_title` | None |  |
| 114170 | `isbn` | None |  |
| 114170 | `isbn13` | None |  |
| 11422 | `original_title` | None |  |
| 114345 | `language_code` | None |  |
| 11436 | `isbn` | None |  |
| 11436 | `isbn13` | None |  |
| 11445880 | `original_title` | None |  |
| 11450591 | `isbn` | None |  |
| 11450591 | `isbn13` | None |  |
| 11479285 | `isbn` | None |  |
| 11479285 | `isbn13` | None |  |
| 1149440 | `language_code` | None |  |
| 114954 | `isbn` | None |  |
| 114954 | `isbn13` | None |  |
| 11505797 | `isbn` | None |  |
| 11505797 | `isbn13` | None |  |
| 11512688 | `original_title` | None |  |
| 11525 | `language_code` | None |  |
| 11561469 | `isbn` | None |  |
| 11561469 | `isbn13` | None |  |
| 11564 | `language_code` | None |  |
| 116020 | `original_title` | None |  |
| 116236 | `language_code` | None |  |
| 116295 | `original_title` | None |  |
| 116356 | `language_code` | None |  |
| 116494 | `language_code` | None |  |
| 11665750 | `isbn` | None |  |
| 11665750 | `isbn13` | None |  |
| 11713 | `language_code` | None |  |
| 117251 | `original_title` | None |  |
| 11737313 | `original_title` | None |  |
| 11742691 | `original_title` | None |  |
| 11757975 | `isbn` | None |  |
| 11757975 | `isbn13` | None |  |
| 117835 | `language_code` | None |  |
| 11784281 | `isbn` | None |  |
| 11784281 | `isbn13` | None |  |
| 11808919 | `isbn` | None |  |
| 11808919 | `isbn13` | None |  |
| 11821514 | `isbn` | None |  |
| 11821514 | `isbn13` | None |  |
| 11851522 | `isbn` | None |  |
| 11851522 | `isbn13` | None |  |
| 11851522 | `original_title` | None |  |
| 11873368 | `original_title` | None |  |
| 11908 | `language_code` | None |  |
| 119091 | `language_code` | None |  |
| 1191 | `language_code` | None |  |
| 11913681 | `isbn` | None |  |
| 11913681 | `isbn13` | None |  |
| 11913681 | `original_title` | None |  |
| 1192 | `language_code` | None |  |
| 11942408 | `isbn` | None |  |
| 11942408 | `isbn13` | None |  |
| 11947156 | `isbn` | None |  |
| 11947156 | `isbn13` | None |  |
| 11970096 | `isbn` | None |  |
| 11970096 | `isbn13` | None |  |
| 11970096 | `original_title` | None |  |
| 11970747 | `isbn` | None |  |
| 11970747 | `isbn13` | None |  |
| 119760 | `original_title` | None |  |
| 11981168 | `isbn` | None |  |
| 11981168 | `isbn13` | None |  |
| 11981168 | `original_title` | None |  |
| 11985631 | `isbn` | None |  |
| 11985631 | `isbn13` | None |  |
| 11995136 | `isbn` | None |  |
| 11995136 | `isbn13` | None |  |
| 11996019 | `original_title` | None |  |
| 12000020 | `language_code` | None |  |
| 12002819 | `original_title` | None |  |
| 12017 | `language_code` | None |  |
| 12019355 | `language_code` | None |  |
| 120230 | `language_code` | None |  |
| 12037026 | `language_code` | None |  |
| 12039943 | `language_code` | None |  |
| 120461 | `language_code` | None |  |
| 12063467 | `original_title` | None |  |
| 12065943 | `original_title` | None |  |
| 12067972 | `isbn` | None |  |
| 12067972 | `isbn13` | None |  |
| 12072362 | `original_title` | None |  |
| 1207980 | `language_code` | None |  |
| 120840 | `language_code` | None |  |
| 12107920 | `original_title` | None |  |
| 12107920 | `language_code` | None |  |
| 12107925 | `original_title` | None |  |
| 12107927 | `original_title` | None |  |
| 12158480 | `language_code` | None |  |
| 12171769 | `original_title` | None |  |
| 121792 | `language_code` | None |  |
| 1219103 | `language_code` | None |  |
| 12191246 | `isbn` | None |  |
| 12191246 | `isbn13` | None |  |
| 12191246 | `language_code` | None |  |
| 12204 | `language_code` | None |  |
| 122212 | `language_code` | None |  |
| 12254379 | `isbn` | None |  |
| 12254379 | `isbn13` | None |  |
| 122574 | `language_code` | None |  |
| 12287209 | `isbn` | None |  |
| 12287209 | `isbn13` | None |  |
| 12288282 | `isbn` | None |  |
| 12288282 | `isbn13` | None |  |
| 122967 | `original_title` | None |  |
| 12299419 | `isbn` | None |  |
| 12299419 | `isbn13` | None |  |
| 123063 | `language_code` | None |  |
| 1231511 | `original_title` | None |  |
| 1231511 | `language_code` | None |  |
| 123170 | `language_code` | None |  |
| 12326627 | `isbn` | None |  |
| 12326627 | `isbn13` | None |  |
| 12331767 | `language_code` | None |  |
| 12341557 | `isbn` | None |  |
| 12341557 | `isbn13` | None |  |
| 12351649 | `isbn` | None |  |
| 12351649 | `isbn13` | None |  |
| 12357 | `language_code` | None |  |
| 12389310 | `original_title` | None |  |
| 12390650 | `isbn` | None |  |
| 12390650 | `isbn13` | None |  |
| 12413836 | `original_title` | None |  |
| 12413836 | `language_code` | None |  |
| 12413949 | `original_title` | None |  |
| 12415695 | `isbn` | None |  |
| 12415695 | `isbn13` | None |  |
| 12458287 | `isbn` | None |  |
| 12458287 | `isbn13` | None |  |
| 12458287 | `original_title` | None |  |
| 12475019 | `original_title` | None |  |
| 12499 | `language_code` | None |  |
| 12513614 | `isbn` | None |  |
| 12513614 | `isbn13` | None |  |
| 12535 | `language_code` | None |  |
| 12543 | `language_code` | None |  |
| 125540 | `language_code` | None |  |
| 125542 | `language_code` | None |  |
| 125564 | `language_code` | None |  |
| 12583975 | `isbn` | None |  |
| 12583975 | `isbn13` | None |  |
| 125955 | `language_code` | None |  |
| 125958 | `language_code` | None |  |
| 125963 | `language_code` | None |  |
| 12598982 | `language_code` | None |  |
| 12602078 | `isbn` | None |  |
| 12602078 | `isbn13` | None |  |
| 12602078 | `original_title` | None |  |
| 12605157 | `original_title` | None |  |
| 12611073 | `original_title` | None |  |
| 12611073 | `language_code` | None |  |
| 126185 | `language_code` | None |  |
| 126381 | `language_code` | None |  |
| 12647642 | `isbn` | None |  |
| 12647642 | `isbn13` | None |  |
| 12652457 | `isbn` | None |  |
| 12652457 | `isbn13` | None |  |
| 12659 | `language_code` | None |  |
| 12667194 | `isbn` | None |  |
| 12667194 | `isbn13` | None |  |
| 12675109 | `isbn` | None |  |
| 12675109 | `isbn13` | None |  |
| 12675109 | `original_title` | None |  |
| 1268348 | `language_code` | None |  |
| 1268479 | `isbn` | None |  |
| 1268479 | `isbn13` | None |  |
| 12706435 | `isbn` | None |  |
| 12706435 | `isbn13` | None |  |
| 12712435 | `language_code` | None |  |
| 12716010 | `isbn` | None |  |
| 12716010 | `isbn13` | None |  |
| 12716613 | `language_code` | None |  |
| 12737118 | `language_code` | None |  |
| 127451 | `language_code` | None |  |
| 1275105 | `language_code` | None |  |
| 12755792 | `isbn` | None |  |
| 12755792 | `isbn13` | None |  |
| 12755792 | `language_code` | None |  |
| 12758317 | `language_code` | None |  |
| 127586 | `language_code` | None |  |
| 12760903 | `isbn` | None |  |
| 12760903 | `isbn13` | None |  |
| 12760903 | `original_title` | None |  |
| 127970 | `language_code` | None |  |
| 12799058 | `isbn` | None |  |
| 12799058 | `isbn13` | None |  |
| 128066 | `language_code` | None |  |
| 12839 | `language_code` | None |  |
| 12842134 | `isbn` | None |  |
| 12842134 | `isbn13` | None |  |
| 12867423 | `original_title` | None |  |
| 12867423 | `language_code` | None |  |
| 128711 | `isbn` | None |  |
| 128711 | `isbn13` | None |  |
| 128755 | `language_code` | None |  |
| 128759 | `language_code` | None |  |
| 12878300 | `original_title` | None |  |
| 12878300 | `language_code` | None |  |
| 12881141 | `isbn` | None |  |
| 12881141 | `isbn13` | None |  |
| 12900174 | `isbn` | None |  |
| 12900174 | `isbn13` | None |  |
| 12902549 | `isbn` | None |  |
| 12902549 | `isbn13` | None |  |
| 12922320 | `isbn` | None |  |
| 12922320 | `isbn13` | None |  |
| 12923 | `original_title` | None |  |
| 12924261 | `original_title` | None |  |
| 12926804 | `original_title` | None |  |
| 129510 | `language_code` | None |  |
| 129565 | `language_code` | None |  |
| 12958487 | `isbn` | None |  |
| 12958487 | `isbn13` | None |  |
| 1298171 | `language_code` | None |  |
| 1298205 | `language_code` | None |  |
| 12987640 | `original_title` | None |  |
| 129947 | `language_code` | None |  |
| 13023 | `original_title` | None |  |
| 130260 | `language_code` | None |  |
| 13027304 | `original_title` | None |  |
| 1303 | `language_code` | None |  |
| 13031445 | `original_title` | None |  |
| 1305 | `language_code` | None |  |
| 13051316 | `isbn` | None |  |
| 13051316 | `isbn13` | None |  |
| 13057939 | `language_code` | None |  |
| 13063 | `original_title` | None |  |
| 13063 | `language_code` | None |  |
| 13065142 | `isbn` | None |  |
| 13065142 | `isbn13` | None |  |
| 13065142 | `original_title` | None |  |
| 13069213 | `original_title` | None |  |
| 13070346 | `isbn` | None |  |
| 13070346 | `isbn13` | None |  |
| 13096848 | `original_title` | None |  |
| 13125947 | `language_code` | None |  |
| 13129925 | `language_code` | None |  |
| 131304 | `language_code` | None |  |
| 13132 | `language_code` | None |  |
| 13132816 | `isbn` | None |  |
| 13132816 | `isbn13` | None |  |
| 13146214 | `isbn` | None |  |
| 13146214 | `isbn13` | None |  |
| 13151283 | `isbn` | None |  |
| 13151283 | `isbn13` | None |  |
| 13151637 | `isbn` | None |  |
| 13151637 | `isbn13` | None |  |
| 13152194 | `language_code` | None |  |
| 13152998 | `language_code` | None |  |
| 13153693 | `language_code` | None |  |
| 13154952 | `language_code` | None |  |
| 13167062 | `original_title` | None |  |
| 13167847 | `original_title` | None |  |
| 13167847 | `language_code` | None |  |
| 13168 | `language_code` | None |  |
| 1317181 | `original_title` | None |  |
| 1317181 | `language_code` | None |  |
| 13178410 | `isbn` | None |  |
| 13178410 | `isbn13` | None |  |
| 131830 | `language_code` | None |  |
| 13184572 | `isbn` | None |  |
| 13184572 | `isbn13` | None |  |
| 13184572 | `language_code` | None |  |
| 13184992 | `isbn` | None |  |
| 13184992 | `isbn13` | None |  |
| 13184992 | `original_title` | None |  |
| 13188676 | `isbn` | None |  |
| 13188676 | `isbn13` | None |  |
| 132152 | `language_code` | None |  |
| 13223520 | `isbn` | None |  |
| 13223520 | `isbn13` | None |  |
| 13223520 | `original_title` | None |  |
| 13226173 | `original_title` | None |  |
| 13230263 | `original_title` | None |  |
| 13235 | `language_code` | None |  |
| 13235689 | `language_code` | None |  |
| 13241659 | `original_title` | None |  |
| 13256064 | `language_code` | None |  |
| 13272498 | `language_code` | None |  |
| 13281637 | `original_title` | None |  |
| 13312527 | `isbn` | None |  |
| 13312527 | `isbn13` | None |  |
| 13323842 | `isbn` | None |  |
| 13323842 | `isbn13` | None |  |
| 13330603 | `language_code` | None |  |
| 13330761 | `language_code` | None |  |
| 13331184 | `language_code` | None |  |
| 13331199 | `original_title` | None |  |
| 13331199 | `language_code` | None |  |
| 133445 | `language_code` | None |  |
| 13345975 | `isbn` | None |  |
| 13345975 | `isbn13` | None |  |
| 13350 | `language_code` | None |  |
| 13362536 | `language_code` | None |  |
| 13363270 | `isbn` | None |  |
| 13363270 | `isbn13` | None |  |
| 13369678 | `isbn` | None |  |
| 13369678 | `isbn13` | None |  |
| 13372690 | `isbn` | None |  |
| 13372690 | `isbn13` | None |  |
| 13376 | `original_title` | None |  |
| 133906 | `language_code` | None |  |
| 133954 | `language_code` | None |  |
| 13402447 | `isbn` | None |  |
| 13402447 | `isbn13` | None |  |
| 13412515 | `isbn` | None |  |
| 13412515 | `isbn13` | None |  |
| 13415554 | `isbn` | None |  |
| 13415554 | `isbn13` | None |  |
| 13417946 | `original_title` | None |  |
| 13417946 | `language_code` | None |  |
| 13419891 | `isbn` | None |  |
| 13419891 | `isbn13` | None |  |
| 13425393 | `original_title` | None |  |
| 13425393 | `language_code` | None |  |
| 13425570 | `language_code` | None |  |
| 13431827 | `isbn` | None |  |
| 13431827 | `isbn13` | None |  |
| 13431827 | `original_title` | None |  |
| 134360 | `language_code` | None |  |
| 13448656 | `isbn` | None |  |
| 13448656 | `isbn13` | None |  |
| 13451 | `language_code` | None |  |
| 13453029 | `isbn` | None |  |
| 13453029 | `isbn13` | None |  |
| 1347837 | `original_title` | None |  |
| 13489517 | `isbn` | None |  |
| 13489517 | `isbn13` | None |  |
| 13489518 | `isbn` | None |  |
| 13489518 | `isbn13` | None |  |
| 134958 | `language_code` | None |  |
| 13496084 | `isbn` | None |  |
| 13496084 | `isbn13` | None |  |
| 13496738 | `isbn` | None |  |
| 13496738 | `isbn13` | None |  |
| 1350249 | `original_title` | None |  |
| 13502963 | `isbn` | None |  |
| 13502963 | `isbn13` | None |  |
| 13502963 | `original_title` | None |  |
| 13502970 | `isbn` | None |  |
| 13502970 | `isbn13` | None |  |
| 13507011 | `isbn` | None |  |
| 13507011 | `isbn13` | None |  |
| 13508607 | `language_code` | None |  |
| 13519844 | `original_title` | None |  |
| 13521299 | `language_code` | None |  |
| 13522957 | `isbn` | None |  |
| 13522957 | `isbn13` | None |  |
| 13523061 | `language_code` | None |  |
| 13530981 | `language_code` | None |  |
| 13531832 | `original_title` | None |  |
| 13540215 | `language_code` | None |  |
| 13545075 | `language_code` | None |  |
| 13545345 | `language_code` | None |  |
| 13546173 | `isbn` | None |  |
| 13546173 | `isbn13` | None |  |
| 13547234 | `language_code` | None |  |
| 13547241 | `original_title` | None |  |
| 13560262 | `original_title` | None |  |
| 13565676 | `isbn` | None |  |
| 13565676 | `isbn13` | None |  |
| 13565914 | `isbn` | None |  |
| 13565914 | `isbn13` | None |  |
| 13568322 | `original_title` | None |  |
| 13568619 | `isbn` | None |  |
| 13568619 | `isbn13` | None |  |
| 13569581 | `isbn` | None |  |
| 13569581 | `isbn13` | None |  |
| 13573236 | `language_code` | None |  |
| 13573795 | `isbn` | None |  |
| 13573795 | `isbn13` | None |  |
| 13580846 | `isbn` | None |  |
| 13580846 | `isbn13` | None |  |
| 13584236 | `original_title` | None |  |
| 13584236 | `language_code` | None |  |
| 13586743 | `language_code` | None |  |
| 13588356 | `language_code` | None |  |
| 13589182 | `language_code` | None |  |
| 13593526 | `original_title` | None |  |
| 13593526 | `language_code` | None |  |
| 13593553 | `original_title` | None |  |
| 13593553 | `language_code` | None |  |
| 13593555 | `original_title` | None |  |
| 13600318 | `isbn` | None |  |
| 13600318 | `isbn13` | None |  |
| 13601550 | `isbn` | None |  |
| 13601550 | `isbn13` | None |  |
| 13601550 | `original_title` | None |  |
| 13603717 | `isbn` | None |  |
| 13603717 | `isbn13` | None |  |
| 13605723 | `original_title` | None |  |
| 13605727 | `language_code` | None |  |
| 13612739 | `isbn` | None |  |
| 13612739 | `isbn13` | None |  |
| 13612739 | `original_title` | None |  |
| 13621 | `language_code` | None |  |
| 13623012 | `language_code` | None |  |
| 13624367 | `isbn` | None |  |
| 13624367 | `isbn13` | None |  |
| 13628812 | `original_title` | None |  |
| 13634927 | `isbn` | None |  |
| 13634927 | `isbn13` | None |  |
| 13638570 | `isbn` | None |  |
| 13638570 | `isbn13` | None |  |
| 13640229 | `isbn` | None |  |
| 13640229 | `isbn13` | None |  |
| 13642929 | `original_title` | None |  |
| 13643567 | `isbn` | None |  |
| 13643567 | `isbn13` | None |  |
| 13649056 | `isbn` | None |  |
| 13649056 | `isbn13` | None |  |
| 136640 | `language_code` | None |  |
| 13667 | `language_code` | None |  |
| 136977 | `language_code` | None |  |
| 1372055 | `language_code` | None |  |
| 1375896 | `language_code` | None |  |
| 13765729 | `isbn` | None |  |
| 13765729 | `isbn13` | None |  |
| 137792 | `language_code` | None |  |
| 13809 | `language_code` | None |  |
| 13817 | `language_code` | None |  |
| 13891 | `original_title` | None |  |
| 139004 | `language_code` | None |  |
| 139220 | `language_code` | None |  |
| 140091 | `original_title` | None |  |
| 140131 | `language_code` | None |  |
| 140302 | `isbn` | None |  |
| 140302 | `isbn13` | None |  |
| 14060046 | `isbn` | None |  |
| 14060046 | `isbn13` | None |  |
| 14060046 | `original_title` | None |  |
| 141019 | `language_code` | None |  |
| 141077 | `language_code` | None |  |
| 14118 | `language_code` | None |  |
| 141526 | `language_code` | None |  |
| 141565 | `language_code` | None |  |
| 14165516 | `isbn` | None |  |
| 14165516 | `isbn13` | None |  |
| 142108 | `language_code` | None |  |
| 1422926 | `language_code` | None |  |
| 142900 | `language_code` | None |  |
| 14316 | `language_code` | None |  |
| 14367051 | `original_title` | None |  |
| 14367051 | `language_code` | None |  |
| 14469 | `language_code` | None |  |
| 144773 | `language_code` | None |  |
| 14480 | `language_code` | None |  |
| 14481 | `language_code` | None |  |
| 1464757 | `isbn` | None |  |
| 1464757 | `isbn13` | None |  |
| 147074 | `language_code` | None |  |
| 14740588 | `isbn` | None |  |
| 14740588 | `isbn13` | None |  |
| 14744381 | `original_title` | None |  |
| 14745338 | `isbn` | None |  |
| 14745338 | `isbn13` | None |  |
| 14745338 | `original_title` | None |  |
| 14758 | `language_code` | None |  |
| 14781501 | `language_code` | None |  |
| 147941 | `language_code` | None |  |
| 148337 | `language_code` | None |  |
| 14889780 | `language_code` | None |  |
| 14905 | `original_title` | None |  |
| 1491906 | `language_code` | None |  |
| 149196 | `language_code` | None |  |
| 14963 | `language_code` | None |  |
| 14965 | `language_code` | None |  |
| 1499952 | `isbn` | None |  |
| 1499952 | `isbn13` | None |  |
| 1503274 | `language_code` | None |  |
| 15034320 | `language_code` | None |  |
| 15055 | `isbn` | None |  |
| 15055 | `isbn13` | None |  |
| 15059301 | `isbn` | None |  |
| 15059301 | `isbn13` | None |  |
| 15059301 | `original_title` | None |  |
| 15062217 | `isbn` | None |  |
| 15062217 | `isbn13` | None |  |
| 15171 | `language_code` | None |  |
| 15283043 | `original_title` | None |  |
| 153136 | `language_code` | None |  |
| 153175 | `language_code` | None |  |
| 153492 | `language_code` | None |  |
| 153542 | `language_code` | None |  |
| 153781 | `language_code` | None |  |
| 153785 | `isbn` | None |  |
| 153785 | `isbn13` | None |  |
| 153795 | `isbn` | None |  |
| 153795 | `isbn13` | None |  |
| 153800 | `isbn` | None |  |
| 153800 | `isbn13` | None |  |
| 153800 | `language_code` | None |  |
| 15398 | `language_code` | None |  |
| 1540 | `original_title` | None |  |
| 15433 | `language_code` | None |  |
| 15447 | `language_code` | None |  |
| 15513156 | `original_title` | None |  |
| 155370 | `language_code` | None |  |
| 15549 | `language_code` | None |  |
| 15561 | `language_code` | None |  |
| 155981 | `language_code` | None |  |
| 15645 | `language_code` | None |  |
| 15676 | `language_code` | None |  |
| 15704001 | `isbn` | None |  |
| 15704001 | `isbn13` | None |  |
| 157076 | `language_code` | None |  |
| 15717721 | `isbn` | None |  |
| 15717721 | `isbn13` | None |  |
| 15722284 | `isbn` | None |  |
| 15722284 | `isbn13` | None |  |
| 15723286 | `isbn` | None |  |
| 15723286 | `isbn13` | None |  |
| 15724654 | `isbn` | None |  |
| 15724654 | `isbn13` | None |  |
| 15728921 | `isbn` | None |  |
| 15728921 | `isbn13` | None |  |
| 15729261 | `isbn` | None |  |
| 15729261 | `isbn13` | None |  |
| 15730101 | `isbn` | None |  |
| 15730101 | `isbn13` | None |  |
| 15733346 | `original_title` | None |  |
| 15733851 | `language_code` | None |  |
| 15734464 | `isbn` | None |  |
| 15734464 | `isbn13` | None |  |
| 15737147 | `original_title` | None |  |
| 15738951 | `isbn` | None |  |
| 15738951 | `isbn13` | None |  |
| 15739018 | `isbn` | None |  |
| 15739018 | `isbn13` | None |  |
| 15739018 | `original_title` | None |  |
| 15742039 | `isbn` | None |  |
| 15742039 | `isbn13` | None |  |
| 15743078 | `original_title` | None |  |
| 15745371 | `original_title` | None |  |
| 15748335 | `isbn` | None |  |
| 15748335 | `isbn13` | None |  |
| 15748335 | `original_title` | None |  |
| 15749186 | `isbn` | None |  |
| 15749186 | `isbn13` | None |  |
| 15752 | `language_code` | None |  |
| 15752757 | `isbn` | None |  |
| 15752757 | `isbn13` | None |  |
| 15752757 | `original_title` | None |  |
| 15757434 | `isbn` | None |  |
| 15757434 | `isbn13` | None |  |
| 15760 | `language_code` | None |  |
| 15760001 | `isbn` | None |  |
| 15760001 | `isbn13` | None |  |
| 15761241 | `isbn` | None |  |
| 15761241 | `isbn13` | None |  |
| 15762657 | `isbn` | None |  |
| 15762657 | `isbn13` | None |  |
| 15762975 | `isbn` | None |  |
| 15762975 | `isbn13` | None |  |
| 15764 | `language_code` | None |  |
| 15766776 | `original_title` | None |  |
| 15768191 | `original_title` | None |  |
| 15768536 | `isbn` | None |  |
| 15768536 | `isbn13` | None |  |
| 15768536 | `original_title` | None |  |
| 15771862 | `isbn` | None |  |
| 15771862 | `isbn13` | None |  |
| 15776904 | `isbn` | None |  |
| 15776904 | `isbn13` | None |  |
| 15778138 | `isbn` | None |  |
| 15778138 | `isbn13` | None |  |
| 15779 | `original_title` | None |  |
| 15783307 | `isbn` | None |  |
| 15783307 | `isbn13` | None |  |
| 15784909 | `isbn` | None |  |
| 15784909 | `isbn13` | None |  |
| 15786110 | `original_title` | None |  |
| 15791403 | `language_code` | None |  |
| 15793165 | `original_title` | None |  |
| 15797722 | `original_title` | None |  |
| 15801668 | `original_title` | None |  |
| 15811495 | `original_title` | None |  |
| 15811520 | `original_title` | None |  |
| 15820492 | `language_code` | None |  |
| 15820748 | `language_code` | None |  |
| 15828714 | `isbn` | None |  |
| 15828714 | `isbn13` | None |  |
| 15832316 | `isbn` | None |  |
| 15832316 | `isbn13` | None |  |
| 15835685 | `isbn` | None |  |
| 15835685 | `isbn13` | None |  |
| 15843166 | `original_title` | None |  |
| 15843166 | `language_code` | None |  |
| 15849910 | `original_title` | None |  |
| 158516 | `language_code` | None |  |
| 15852756 | `isbn` | None |  |
| 15852756 | `isbn13` | None |  |
| 158944 | `language_code` | None |  |
| 15902792 | `original_title` | None |  |
| 159418 | `original_title` | None |  |
| 159760 | `language_code` | None |  |
| 15981894 | `isbn` | None |  |
| 15981894 | `isbn13` | None |  |
| 15993374 | `isbn` | None |  |
| 15993374 | `isbn13` | None |  |
| 16001443 | `isbn` | None |  |
| 16001443 | `isbn13` | None |  |
| 16001893 | `isbn` | None |  |
| 16001893 | `isbn13` | None |  |
| 16007855 | `original_title` | None |  |
| 160194 | `language_code` | None |  |
| 16031620 | `isbn` | None |  |
| 16031620 | `isbn13` | None |  |
| 16031679 | `language_code` | None |  |
| 1603923 | `language_code` | None |  |
| 16041169 | `original_title` | None |  |
| 16042305 | `isbn` | None |  |
| 16042305 | `isbn13` | None |  |
| 16042305 | `original_title` | None |  |
| 16045144 | `language_code` | None |  |
| 16045855 | `isbn` | None |  |
| 16045855 | `isbn13` | None |  |
| 16045855 | `original_title` | None |  |
| 16047244 | `isbn` | None |  |
| 16047244 | `isbn13` | None |  |
| 16053316 | `isbn` | None |  |
| 16053316 | `isbn13` | None |  |
| 16055 | `original_title` | None |  |
| 16056862 | `isbn` | None |  |
| 16056862 | `isbn13` | None |  |
| 16058610 | `original_title` | None |  |
| 16066586 | `isbn` | None |  |
| 16066586 | `isbn13` | None |  |
| 16066586 | `original_title` | None |  |
| 16068905 | `isbn` | None |  |
| 16068905 | `isbn13` | None |  |
| 16068905 | `original_title` | None |  |
| 16070018 | `original_title` | None |  |
| 16070521 | `isbn` | None |  |
| 16070521 | `isbn13` | None |  |
| 16070903 | `isbn` | None |  |
| 16070903 | `isbn13` | None |  |
| 16076787 | `isbn` | None |  |
| 16076787 | `isbn13` | None |  |
| 16079228 | `isbn` | None |  |
| 16079228 | `isbn13` | None |  |
| 16081202 | `isbn` | None |  |
| 16081202 | `isbn13` | None |  |
| 16081754 | `isbn` | None |  |
| 16081754 | `isbn13` | None |  |
| 16081961 | `isbn` | None |  |
| 16081961 | `isbn13` | None |  |
| 16084702 | `isbn` | None |  |
| 16084702 | `isbn13` | None |  |
| 16084702 | `original_title` | None |  |
| 160848 | `language_code` | None |  |
| 16090636 | `isbn` | None |  |
| 16090636 | `isbn13` | None |  |
| 16090636 | `original_title` | None |  |
| 16090981 | `isbn` | None |  |
| 16090981 | `isbn13` | None |  |
| 16093188 | `isbn` | None |  |
| 16093188 | `isbn13` | None |  |
| 16096873 | `isbn` | None |  |
| 16096873 | `isbn13` | None |  |
| 16102880 | `isbn` | None |  |
| 16102880 | `isbn13` | None |  |
| 16102880 | `original_title` | None |  |
| 16109563 | `isbn` | None |  |
| 16109563 | `isbn13` | None |  |
| 16113791 | `isbn` | None |  |
| 16113791 | `isbn13` | None |  |
| 16114861 | `isbn` | None |  |
| 16114861 | `isbn13` | None |  |
| 16114861 | `original_title` | None |  |
| 16114862 | `isbn` | None |  |
| 16114862 | `isbn13` | None |  |
| 16114862 | `original_title` | None |  |
| 16117182 | `isbn` | None |  |
| 16117182 | `isbn13` | None |  |
| 16117804 | `isbn` | None |  |
| 16117804 | `isbn13` | None |  |
| 16119079 | `original_title` | None |  |
| 16122163 | `original_title` | None |  |
| 16122643 | `isbn` | None |  |
| 16122643 | `isbn13` | None |  |
| 16124019 | `isbn` | None |  |
| 16124019 | `isbn13` | None |  |
| 16130986 | `isbn` | None |  |
| 16130986 | `isbn13` | None |  |
| 16131484 | `isbn` | None |  |
| 16131484 | `isbn13` | None |  |
| 16134551 | `isbn` | None |  |
| 16134551 | `isbn13` | None |  |
| 16134782 | `isbn` | None |  |
| 16134782 | `isbn13` | None |  |
| 16136959 | `isbn` | None |  |
| 16136959 | `isbn13` | None |  |
| 16139641 | `isbn` | None |  |
| 16139641 | `isbn13` | None |  |
| 16140036 | `isbn` | None |  |
| 16140036 | `isbn13` | None |  |
| 161415 | `language_code` | None |  |
| 16141924 | `language_code` | None |  |
| 16143347 | `isbn` | None |  |
| 16143347 | `isbn13` | None |  |
| 16148398 | `isbn` | None |  |
| 16148398 | `isbn13` | None |  |
| 16148938 | `isbn` | None |  |
| 16148938 | `isbn13` | None |  |
| 16148938 | `original_title` | None |  |
| 16150119 | `isbn` | None |  |
| 16150119 | `isbn13` | None |  |
| 16150119 | `original_title` | None |  |
| 16150996 | `isbn` | None |  |
| 16150996 | `isbn13` | None |  |
| 16150996 | `original_title` | None |  |
| 16151178 | `isbn` | None |  |
| 16151178 | `isbn13` | None |  |
| 16152943 | `original_title` | None |  |
| 16163690 | `isbn` | None |  |
| 16163690 | `isbn13` | None |  |
| 16170522 | `isbn` | None |  |
| 16170522 | `isbn13` | None |  |
| 16170625 | `isbn` | None |  |
| 16170625 | `isbn13` | None |  |
| 16174197 | `isbn` | None |  |
| 16174197 | `isbn13` | None |  |
| 16175040 | `isbn` | None |  |
| 16175040 | `isbn13` | None |  |
| 1617875 | `language_code` | None |  |
| 16182601 | `original_title` | None |  |
| 16204 | `language_code` | None |  |
| 16218778 | `original_title` | None |  |
| 16233105 | `isbn` | None |  |
| 16233105 | `isbn13` | None |  |
| 16248139 | `original_title` | None |  |
| 16248196 | `language_code` | None |  |
| 16277248 | `original_title` | None |  |
| 16279715 | `isbn` | None |  |
| 16279715 | `isbn13` | None |  |
| 1629007 | `original_title` | None |  |
| 16299256 | `isbn` | None |  |
| 16299256 | `isbn13` | None |  |
| 16299256 | `original_title` | None |  |
| 16299991 | `isbn` | None |  |
| 16299991 | `isbn13` | None |  |
| 16299991 | `original_title` | None |  |
| 16301111 | `isbn` | None |  |
| 16301111 | `isbn13` | None |  |
| 1635 | `original_title` | None |  |
| 16429619 | `isbn` | None |  |
| 16429619 | `isbn13` | None |  |
| 16431 | `original_title` | None |  |
| 164323 | `language_code` | None |  |
| 16479439 | `language_code` | None |  |
| 164836 | `language_code` | None |  |
| 165030 | `language_code` | None |  |
| 165053 | `language_code` | None |  |
| 1662160 | `language_code` | None |  |
| 16704759 | `isbn` | None |  |
| 16704759 | `isbn13` | None |  |
| 16704759 | `original_title` | None |  |
| 167216 | `language_code` | None |  |
| 1672727 | `language_code` | None |  |
| 168571 | `isbn` | None |  |
| 168571 | `isbn13` | None |  |
| 168571 | `original_title` | None |  |
| 169718 | `language_code` | None |  |
| 169848 | `original_title` | None |  |
| 169848 | `language_code` | None |  |
| 169871 | `original_title` | None |  |
| 169875 | `original_title` | None |  |
| 169879 | `original_title` | None |  |
| 170171 | `original_title` | None |  |
| 17032328 | `isbn` | None |  |
| 17032328 | `isbn13` | None |  |
| 170618 | `language_code` | None |  |
| 170619 | `language_code` | None |  |
| 171102 | `language_code` | None |  |
| 17136 | `language_code` | None |  |
| 17158513 | `isbn` | None |  |
| 17158513 | `isbn13` | None |  |
| 17158596 | `isbn` | None |  |
| 17158596 | `isbn13` | None |  |
| 17166702 | `isbn` | None |  |
| 17166702 | `isbn13` | None |  |
| 17167042 | `isbn` | None |  |
| 17167042 | `isbn13` | None |  |
| 17167042 | `original_title` | None |  |
| 17181905 | `isbn` | None |  |
| 17181905 | `isbn13` | None |  |
| 17181905 | `original_title` | None |  |
| 17190226 | `isbn` | None |  |
| 17190226 | `isbn13` | None |  |
| 17191012 | `isbn` | None |  |
| 17191012 | `isbn13` | None |  |
| 17191012 | `original_title` | None |  |
| 17200687 | `isbn` | None |  |
| 17200687 | `isbn13` | None |  |
| 17201095 | `isbn` | None |  |
| 17201095 | `isbn13` | None |  |
| 17201104 | `isbn` | None |  |
| 17201104 | `isbn13` | None |  |
| 17201110 | `isbn` | None |  |
| 17201110 | `isbn13` | None |  |
| 17201110 | `original_title` | None |  |
| 17204568 | `isbn` | None |  |
| 17204568 | `isbn13` | None |  |
| 17204860 | `isbn` | None |  |
| 17204860 | `isbn13` | None |  |
| 17225311 | `language_code` | None |  |
| 1722717 | `language_code` | None |  |
| 17228280 | `isbn` | None |  |
| 17228280 | `isbn13` | None |  |
| 17235347 | `isbn` | None |  |
| 17235347 | `isbn13` | None |  |
| 17255186 | `original_title` | None |  |
| 17255265 | `isbn` | None |  |
| 17255265 | `isbn13` | None |  |
| 17255435 | `original_title` | None |  |
| 17257484 | `isbn` | None |  |
| 17257484 | `isbn13` | None |  |
| 17257990 | `isbn` | None |  |
| 17257990 | `isbn13` | None |  |
| 17257990 | `original_title` | None |  |
| 17257993 | `isbn` | None |  |
| 17257993 | `isbn13` | None |  |
| 17267122 | `isbn` | None |  |
| 17267122 | `isbn13` | None |  |
| 17286162 | `isbn` | None |  |
| 17286162 | `isbn13` | None |  |
| 17287009 | `original_title` | None |  |
| 17287028 | `original_title` | None |  |
| 17306293 | `isbn` | None |  |
| 17306293 | `isbn13` | None |  |
| 17314410 | `isbn` | None |  |
| 17314410 | `isbn13` | None |  |
| 17314430 | `isbn` | None |  |
| 17314430 | `isbn13` | None |  |
| 17316075 | `isbn` | None |  |
| 17316075 | `isbn13` | None |  |
| 17317675 | `isbn` | None |  |
| 17317675 | `isbn13` | None |  |
| 17317675 | `original_title` | None |  |
| 17324 | `language_code` | None |  |
| ... | ... | ... | _(truncated, 2136 more)_ |

## Books with different warnings (706)

| goodreads_book_id | title | in Anthony's only | in Kristina's only |
|---|---|---|---|
| 10088913 | مخطوطة بن إسحاق: مدينة الموتى | (isbn13, lost-precision, 9.78977629706e+12) | (isbn13, float-precision-lost, 9.78977629706e+12) |
| 10169662 | Never Knowing | (isbn13, lost-precision, 9.78031259568e+12) | (isbn13, float-precision-lost, 9.78031259568e+12) |
| 10295484 | Heart on a Chain | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10374 | Hard-Boiled Wonderland and the End of the World | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10468258 | The Finding (Law of the Lycans, #5) | (isbn13, lost-precision,bad-prefix, 2.94001119121e+12) | (isbn13, float-precision-lost, 2.94001119121e+12) |
| 105189 | The Story of a Shipwrecked Sailor | (isbn13, lost-precision, 9.78014015755e+12) | (isbn13, float-precision-lost, 9.78014015755e+12) |
| 10586539 | Wake (Watersong #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10599302 | Head Over Heels (Lucky Harbor, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10664113 | A Dance with Dragons (A Song of Ice and Fire, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10706934 | بيكاسو وستاربكس | (isbn13, lost-precision, 9.78995356624e+12) | (isbn13, float-precision-lost, 9.78995356624e+12) |
| 10776793 | War Brides | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10790376 | A Modern Witch (A Modern Witch, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10801027 | Cross My Heart (Cross My Heart, #1) | (isbn13, lost-precision,bad-prefix, 1.2300000055e+12) | (isbn13, float-precision-lost, 1.2300000055e+12) |
| 10813469 | Rock Chick Renegade (Rock Chick, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10813480 | For You (The 'Burg, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10830444 | Guilty Wives | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 10975 | The Sound and the Fury | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11096647 | Flat-Out Love (Flat-Out Love, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11201007 | Hearts in Darkness (Hearts in Darkness, #1) | (isbn13, lost-precision,bad-prefix, 2.94001266893e+12) | (isbn13, float-precision-lost, 2.94001266893e+12) |
| 11227040 | Sweet Dreams (Colorado Mountain, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11227041 | The Gamble (Colorado Mountain, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11227043 | Rock Chick Revenge (Rock Chick, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11237412 | Six's Legacy (Lorien Legacies: The Lost Files, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11239856 | Maid for the Billionaire (Legacy Collection, #1) | (isbn13, lost-precision,bad-prefix, 2.94001248214e+12) | (isbn13, float-precision-lost, 2.94001248214e+12) |
| 11262424 | Between the Lines (Between the Lines, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11324166 | Timeless (Parasol Protectorate, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11350430 | The Mystery Knight (The Tales of Dunk and Egg, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11382346 | That Boy (That Boy, #1) | (isbn13, lost-precision, 9.78061540899e+12) | (isbn13, float-precision-lost, 9.78061540899e+12) |
| 11408650 | The Unbecoming of Mara Dyer (Mara Dyer, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 114170 | Then Came You (The Gamblers, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11436 | Rejoice (Redemption, #4) | (isbn13, lost-precision, 9.78084238688e+12) | (isbn13, float-precision-lost, 9.78084238688e+12) |
| 11450591 | The Mill River Recluse | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11479285 | Breathe (Sea Breeze, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 114954 | The Opal Deception  (Artemis Fowl, #4) | (isbn13, lost-precision, 9.781423104e+12) | (isbn13, float-precision-lost, 9.781423104e+12) |
| 11505797 | Beautiful Disaster (Beautiful, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11561469 | Reason to Breathe (Breathing, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11665750 | At Peace (The 'Burg, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11757975 | The Look of Love (San Francisco Sullivans, #1; The Sullivans, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11784281 | Take This Regret (Take This Regret, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11808919 | Maid for Love (Gansett Island Series, #1) | (isbn13, lost-precision, 9.78098347544e+12) | (isbn13, float-precision-lost, 9.78098347544e+12) |
| 11821514 | Long Time Coming | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11851522 | The Complete Works of H.P. Lovecraft | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11913681 | The Boyfriend Thief (Stolen Kiss, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11942408 | شاب كشك في رحلة البحث عن الجادون | (isbn13, lost-precision, 9.78977633759e+12) | (isbn13, float-precision-lost, 9.78977633759e+12) |
| 11947156 | Prince of Wolves (The Grey Wolves, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11970096 | Twenty-Eight and a Half Wishes (Rose Gardner Mystery, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11970747 | The Hedge Knight (The Tales of Dunk and Egg, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11981168 | The One You Love (Emma Holden Suspense Mystery, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11985631 | The Sworn Sword (The Tales of Dunk and Egg, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 11995136 | محال | (isbn13, lost-precision, 9.78977093092e+12) | (isbn13, float-precision-lost, 9.78977093092e+12) |
| 12067972 | Where You Are (Between the Lines, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12191246 | Second Son (Jack Reacher, #15.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12254379 | 1Q84 #1-2 (1Q84, #1-2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12287209 | Wool (Wool, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12288282 | Gunmetal Magic (Kate Daniels, #5.5) | (isbn13, lost-precision, 9.78110158519e+12) | (isbn13, float-precision-lost, 9.78110158519e+12) |
| 12299419 | Mystery Man (Dream Man, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12326627 | The White Princess (The Plantagenet and Tudor Novels, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12341557 | The Wind Through the Keyhole (The Dark Tower, #4.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12351649 | Perfection (Neighbor from Hell, #2) | (isbn13, lost-precision, 9.78098321255e+12) | (isbn13, float-precision-lost, 9.78098321255e+12) |
| 12390650 | Wildest Dreams (Fantasyland, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12415695 | كخه يا بابا | (isbn13, lost-precision, 9.78995356618e+12) | (isbn13, float-precision-lost, 9.78995356618e+12) |
| 12458287 | The Golden Dynasty (Fantasyland, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12513614 | Captive in the Dark (The Dark Duet, #1) | (isbn13, lost-precision,bad-prefix, 2.94001144494e+12) | (isbn13, float-precision-lost, 2.94001144494e+12) |
| 12583975 | The Billionaire Wins the Game (Billionaire Bachelors, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12602078 | The Tycoon's Revenge (Baby for the Billionaire, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12647642 | Love Unrehearsed (Love, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12652457 | The Broken Eye (Lightbringer, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12667194 | Accordance (Significance, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12675109 | Great by Choice: Uncertainty, Chaos, and Luck--Why Some Thrive Despite Them All | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 1268479 | Warbreaker (Warbreaker, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12706435 | Defiance (Significance, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12716010 | Rapture (Fallen, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12755792 | A Hidden Fire (Elemental Mysteries, #1) | (isbn13, lost-precision,bad-prefix, 2.94001328325e+12) | (isbn13, float-precision-lost, 2.94001328325e+12) |
| 12760903 | The Vision (Fallen Star, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12799058 | Summerland | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12842134 | Just One Year (Just One Day, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 128711 | The Yacoubian Building | (isbn13, lost-precision, 9.78006087814e+12) | (isbn13, float-precision-lost, 9.78006087814e+12) |
| 12881141 | Wild Man (Dream Man, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12900174 | The Vincent Boys (The Vincent Boys, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12902549 | An Invisible Thread: The True Story of an 11-Year-Old Panhandler, a Busy Sales E | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12922320 | Criminal (Will Trent, #6) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 12958487 | Lady Luck (Colorado Mountain, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13051316 | The Misremembered Man (Tailorstown #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13065142 | Rock Chick Reckoning (Rock Chick, #6) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13070346 | Blood Rites (The Grey Wolves, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13132816 | Emmy & Oliver | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13146214 | Because of Low (Sea Breeze, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13151283 | بضع ساعات في يوم ما | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13151637 | طه الغريب | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13178410 | Proper Gauge (Wool, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13184572 | The Next Best Thing | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13184992 | Rock Chick Regret (Rock Chick, #7) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13188676 | Ignite Me (Shatter Me, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13223520 | Existence (Existence Trilogy, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13312527 | The Opportunist (Love Me with Lies, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13323842 | Predestined (Existence Trilogy, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13345975 | Avoiding Commitment (Avoiding, #1) | (isbn13, lost-precision, 9.78147627142e+12) | (isbn13, float-precision-lost, 9.78147627142e+12) |
| 13363270 | Just One Drop (The Grey Wolves, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13369678 | The Vincent Brothers (The Vincent Boys, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13372690 | Slammed (Slammed, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13402447 | UnEnchanted (An Unfortunate Fairy Tale, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13412515 | Law Man (Dream Man, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13415554 | The Assassin and the Pirate Lord (Throne of Glass, #0.1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13419891 | The Assassin and the Desert (Throne of Glass, #0.3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13431827 | The Remaining (The Remaining, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13448656 | Motorcycle Man (Dream Man, #4) | (isbn13, lost-precision, 9.78147624895e+12) | (isbn13, float-precision-lost, 9.78147624895e+12) |
| 13453029 | Wool Omnibus (Silo, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13489517 | 28 حرف | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13489518 | Out of the Dark (The Grey Wolves, #4) | (isbn13, lost-precision,bad-prefix, 2.94001474615e+12) | (isbn13, float-precision-lost, 2.94001474615e+12) |
| 13496084 | Point of Retreat (Slammed, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13496738 | While It Lasts (Sea Breeze, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13502963 | Indebted (The Premonition, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13502970 | Incendiary (The Premonition, #4) | (isbn13, lost-precision, 9.78147920712e+12) | (isbn13, float-precision-lost, 9.78147920712e+12) |
| 13507011 | Low Pressure | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13522957 | Feral Sins (The Phoenix Pack, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13546173 | The Assassin and the Underworld (Throne of Glass, #0.4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13565676 | The Assassin and the Empire (Throne of Glass, #0.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13565914 | Knight (Unfinished Hero, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13568619 | The Shadowhunter's Codex | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13569581 | Blood Song (Raven's Shadow, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13573795 | Ceaseless (Existence Trilogy, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13580846 | My Life with the Walter Boys (My Life with the Walter Boys #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13600318 | Reckless (Thoughtless, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13601550 | Accidentally on Purpose (Accidentally on Purpose, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13603717 | First Shift: Legacy (Shift, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13612739 | Seduced in the Dark (The Dark Duet, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13624367 | Checkmate (Neighbor from Hell, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13634927 | A Leaf on the Wind of All Hallows (Outlander, #8.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13638570 | Out of Breath (Breathing, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13640229 | Creed (Unfinished Hero, #2) | (isbn13, lost-precision, 9.78130116082e+12) | (isbn13, float-precision-lost, 9.78130116082e+12) |
| 13643567 | The Evolution of Mara Dyer (Mara Dyer, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 13649056 | Try Me (One Night with Sole Regret, #1) | (isbn13, lost-precision,bad-prefix, 2.94001463181e+12) | (isbn13, float-precision-lost, 2.94001463181e+12) |
| 13765729 | Abducted (Lizzy Gardner #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 140302 | Poirot Investiga (Hércules Poirot, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 14060046 | Obsession | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 14165516 | The Marriage Trap (Marriage to a Billionaire, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 1464757 | Edensor (Tetralogi Laskar Pelangi, #3) | (isbn13, lost-precision, 9.78979122702e+12) | (isbn13, float-precision-lost, 9.78979122702e+12) |
| 14740588 | Notorious Nineteen (Stephanie Plum, #19) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 14745338 | Fairest (An Unfortunate Fairy Tale, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 1499952 | Daddy-Long-Legs (Daddy-Long-Legs, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15055 | Oranges Are Not the Only Fruit | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15059301 | Captured (The Captive, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15062217 | 14 | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 153785 | Page (Protector of the Small, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 153795 | Squire (Protector of the Small, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 153800 | Lady Knight (Protector of the Small, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15704001 | Seduction and Snacks (Chocolate Lovers, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15717721 | If I Were You (Inside Out, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15722284 | Saint Odd (Odd Thomas, #7) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15723286 | Curtsies & Conspiracies (Finishing School, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15724654 | The Mighty Storm (The Storm, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15728921 | Don't Let Me Go | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15729261 | The Marriage Mistake (Marriage to a Billionaire, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15730101 | The Call of Cthulhu | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15734464 | 12th of Never (Women's Murder Club, #12) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15738951 | Deep Down (Jack Reacher, #16.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15739018 | Taking Chances (Taking Chances, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15742039 | Breathe (Colorado Mountain, #4) | (isbn13, lost-precision, 9.78147614539e+12) | (isbn13, float-precision-lost, 9.78147614539e+12) |
| 15748335 | Leave Me Breathless (Ross Siblings, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15749186 | To All the Boys I've Loved Before (To All the Boys I've Loved Before, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15752757 | Rock Chick Revolution (Rock Chick, #8) | (isbn13, lost-precision, 9.78130189562e+12) | (isbn13, float-precision-lost, 9.78130189562e+12) |
| 15757434 | Crash (Crash, #1) | (isbn13, lost-precision,bad-prefix, 2.94001497963e+12) | (isbn13, float-precision-lost, 2.94001497963e+12) |
| 15760001 | On Dublin Street (On Dublin Street, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15761241 | The Wild Ones (The Wild Ones, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15762657 | Seducing Cinderella (Fighting for Love, #1) | (isbn13, lost-precision,bad-prefix, 2.94001497768e+12) | (isbn13, float-precision-lost, 2.94001497768e+12) |
| 15762975 | Wrong Bed, Right Guy (Come Undone, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15768536 | Fall From Grace (Mad World, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15771862 | Wave | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15776904 | The Beggar King (The Hangman's Daughter, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15778138 | Just for Now (Sea Breeze, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15783307 | The Perfect Game (The Perfect Game, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15784909 | This Girl (Slammed, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15828714 | Sometimes It Lasts (Sea Breeze, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15832316 | Dirty Red (Love Me with Lies, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15835685 | Clash (Crash, #2) | (isbn13, lost-precision,bad-prefix, 2.94001513629e+12) | (isbn13, float-precision-lost, 2.94001513629e+12) |
| 15852756 | Naked (The Blackstone Affair, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 15981894 | Devoured (Devoured, #1) | (isbn13, lost-precision, 9.7813001603e+12) | (isbn13, float-precision-lost, 9.7813001603e+12) |
| 15993374 | Charade (Games, #1) | (isbn13, lost-precision,bad-prefix, 2.94001549587e+12) | (isbn13, float-precision-lost, 2.94001549587e+12) |
| 16001443 | All In (The Blackstone Affair, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16001893 | Down to You (The Bad Boys, #1) | (isbn13, lost-precision, 9.78130171672e+12) | (isbn13, float-precision-lost, 9.78130171672e+12) |
| 16031620 | الفيل الأزرق | (isbn13, lost-precision, 9.78977093155e+12) | (isbn13, float-precision-lost, 9.78977093155e+12) |
| 16042305 | Love Left Behind | (isbn13, lost-precision, 9.78098847441e+12) | (isbn13, float-precision-lost, 9.78098847441e+12) |
| 16045855 | Crush (Crush, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16047244 | Rock the Heart (Black Falcon, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16053316 | Wethering the Storm (The Storm, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16056862 | The Unwanted Wife (Unwanted, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16066586 | The Cellar (The Cellar, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16068905 | Fangirl | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16070521 | Come Away with Me (With Me in Seattle, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16070903 | Fallen Too Far (Rosemary Beach, #1; Too Far, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16076787 | السنجة | (isbn13, lost-precision, 9.78999219574e+12) | (isbn13, float-precision-lost, 9.78999219574e+12) |
| 16079228 | Beautifully Damaged (Beautifully Damaged, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16081202 | Open Road Summer | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16081754 | Find You in the Dark (Find You in the Dark, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16081961 | الأسود يليق بك | (isbn13, lost-precision, 9.7899532672e+12) | (isbn13, float-precision-lost, 9.7899532672e+12) |
| 16084702 | Fifty Shades Duo: Fifty Shades Darker / Fifty Shades Freed (Fifty Shades, #2-3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16090636 | Fight with Me (With Me in Seattle, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16090981 | Thief (Love Me with Lies, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16093188 | Up to Me (The Bad Boys, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16096873 | Revealed (House of Night, #11) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16102880 | Bad Rep (Bad Rep, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16109563 | Undeniable (Undeniable, #1) | (isbn13, lost-precision,bad-prefix, 2.94004498098e+12) | (isbn13, float-precision-lost, 2.94004498098e+12) |
| 16113791 | The Coincidence of Callie & Kayden (The Coincidence, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16114861 | Unbeautifully (Undeniable, #2) | (isbn13, lost-precision, 9.78130134567e+12) | (isbn13, float-precision-lost, 9.78130134567e+12) |
| 16114862 | Unattainable (Undeniable, #3) | (isbn13, lost-precision, 9.7813019853e+12) | (isbn13, float-precision-lost, 9.7813019853e+12) |
| 16117182 | Broken Silence (Silence, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16117804 | The Proposal (The Proposition, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16122643 | Eyes Wide Open (The Blackstone Affair, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16124019 | Waking Up Married (Waking Up, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16130986 | An Innocent Client | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16131484 | The Infinite Sea (The 5th Wave, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16134551 | Fallen Crest High (Fallen Crest High, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16134782 | In Flight (Up in the Air, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16136959 | Mile High (Up in the Air, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16139641 | Grounded (Up in the Air, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16140036 | This Man (This Man, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16143347 | We Were Liars | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16148398 | Saga #1 | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16148938 | Second Shift: Order (Shift, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16150119 | Wired (Wired, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16150996 | Convicted (Consequences, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16151178 | The Sea of Tranquility | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16163690 | Own the Wind (Chaos, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16170522 | صانع الظلام | (isbn13, lost-precision, 9.78999219576e+12) | (isbn13, float-precision-lost, 9.78999219576e+12) |
| 16170625 | المانيفستو | (isbn13, lost-precision, 9.78999219584e+12) | (isbn13, float-precision-lost, 9.78999219584e+12) |
| 16174197 | Knight & Play (Knight, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16175040 | Endless Knight (The Arcana Chronicles, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16233105 | Someone to Love (Someone to Love, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16279715 | Connected (Connections, #1) | (isbn13, lost-precision, 9.78098894191e+12) | (isbn13, float-precision-lost, 9.78098894191e+12) |
| 16299256 | The Game Changer (The Perfect Game, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16299991 | A Quest of Heroes (The Sorcerer's Ring, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16301111 | Always You (Best Friend, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16429619 | The Kiss of Deception (The Remnant Chronicles, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 16704759 | Knight & Stay (Knight, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 168571 | Shadow Prey (Lucas Davenport, #2) | (isbn13, lost-precision, 9.78042520885e+12) | (isbn13, float-precision-lost, 9.78042520885e+12) |
| 17032328 | If You Stay (Beautifully Broken, #1) | (isbn13, lost-precision,bad-prefix, 2.94001624931e+12) | (isbn13, float-precision-lost, 2.94001624931e+12) |
| 17158513 | Captive Prince: Volume Two (Captive Prince, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17158596 | Collide (Collide, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17166702 | True Love Story | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17167042 | Fighting for Flight (Fighting, #1) | (isbn13, lost-precision, 9.78130112018e+12) | (isbn13, float-precision-lost, 9.78130112018e+12) |
| 17181905 | The Arrangement: The Ferro Family (The Arrangement, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17190226 | Surrender Your Love (Surrender Your Love, #1) | (isbn13, lost-precision, 9.7814823343e+12) | (isbn13, float-precision-lost, 9.7814823343e+12) |
| 17191012 | Fallen Crest Family (Fallen Crest High, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17200687 | Rule (Marked Men, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17201095 | Play with Me (With Me in Seattle, #3) | (isbn13, lost-precision,bad-prefix, 2.94001631951e+12) | (isbn13, float-precision-lost, 2.94001631951e+12) |
| 17201104 | Rock with Me (With Me in Seattle, #4) | (isbn13, lost-precision,bad-prefix, 2.94001655433e+12) | (isbn13, float-precision-lost, 2.94001655433e+12) |
| 17201110 | Safe with Me (With Me in Seattle, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17204568 | Crazy Little Thing (Bell Harbor, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17204860 | Jet (Marked Men, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17228280 | Better off Friends | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17235347 | Life Before Legend: Stories of the Criminal and the Prodigy (Legend, #0.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17255265 | This Man Confessed (This Man, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17257484 | Trouble | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17257990 | Fire Inside (Chaos, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17257993 | Raid (Unfinished Hero, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17267122 | Pulse (Collide, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17286162 | Forever Black (Forever, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17306293 | Shift (Silo, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17314410 | Beauty from Surrender (Beauty, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17314430 | Wait for You (Wait for You, #1) | (isbn13, lost-precision,bad-prefix, 2.94001623192e+12) | (isbn13, float-precision-lost, 2.94001623192e+12) |
| 17316075 | Second Chance Boyfriend (One Week Girlfriend, #2) | (isbn13, lost-precision,bad-prefix, 2.94001648708e+12) | (isbn13, float-precision-lost, 2.94001648708e+12) |
| 17317675 | Epilogue (The Dark Duet, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17333880 | Twisted Perfection (Rosemary Beach, #5; Perfection, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17337562 | Forever Too Far (Rosemary Beach, #3; Too Far, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17339590 | "حكايات فرغلي المستكاوي "حكايتى مع كفر السحلاوية | (isbn13, lost-precision, 9.7897748813e+12) | (isbn13, float-precision-lost, 9.7897748813e+12) |
| 17340050 | Losing Hope (Hopeless, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17375956 | Reaper's Property (Reapers MC, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17377032 | Bad Things (Tristan & Danika, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17401198 | Only the Innocent (DCI Tom Douglas #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17404452 | Forever You (Forever, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17406847 | Defy (Defy, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17407233 | The Submissive (Submissive, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17448960 | Falling into You (Falling, #1) | (isbn13, lost-precision,bad-prefix, 2.94001635694e+12) | (isbn13, float-precision-lost, 2.94001635694e+12) |
| 17449417 | Simple Perfection (Rosemary Beach, #6; Perfection, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17455541 | Happy, Happy, Happy | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17455585 | White Hot Kiss (The Dark Elements, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17455815 | Stone Cold Touch (The Dark Elements, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17504320 | Taking Shots (Assassins, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17524166 | نادي السيارات | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17557143 | The Billionaire's Obsession ~ Simon (The Billionaire's Obsession, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17558817 | Be with Me (Wait for You, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17560674 | The Bet (The Bet, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17563080 | Murder of Crows (The Others, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17563539 | The Egg | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17570538 | The Blood Mirror (Lightbringer, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17660 | The Tommyknockers | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17667452 | When I Found You | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17667561 | The Shadow Throne (The Ascendance Trilogy, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17673307 | Neanderthal Seeks Human (Knitting in the City, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17716 | Waiting for Godot | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 1772910 | White Nights | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17729712 | Beautiful Broken Rules (Broken, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17733861 | A Shade of Blood (A Shade of Vampire, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17788401 | Ugly Love | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17792606 | Mine (Real, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17794657 | The Lake (The Lake Trilogy #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17798233 | Rome (Marked Men, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17798287 | Driven (Driven, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17800786 | Damaged 2 (Damaged, #2) | (isbn13, lost-precision, 9.78098554735e+12) | (isbn13, float-precision-lost, 9.78098554735e+12) |
| 17810 | In the Miso Soup | (isbn13, lost-precision, 9.7801430357e+12) | (isbn13, float-precision-lost, 9.7801430357e+12) |
| 17825503 | Leo | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17830559 | Remy (Real, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17831614 | Beautiful Player (Beautiful Bastard, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17831616 | Beautiful Bitch (Beautiful Bastard, #1.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17831617 | Beautiful Bombshell (Beautiful Bastard, #2.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17831619 | Beautiful Beginning (Beautiful Bastard, #3.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17833099 | Price of a Kiss (Forbidden Men, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17835351 | Nikola Tesla: Imagination and the Man That Invented the 20th Century | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17835766 | One More Chance (Rosemary Beach, #8; Chance, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17835773 | Misbehaving (Sea Breeze, #6) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17860217 | Trust in Me (Wait for You, #1.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17880708 | Fueled (Driven, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17880714 | Crashed (Driven, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17903381 | Diary ng Panget | (isbn13, lost-precision, 9.78971057365e+12) | (isbn13, float-precision-lost, 9.78971057365e+12) |
| 17925397 | A Castle of Sand (A Shade of Vampire, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17927395 | A Court of Mist and Fury (A Court of Thorns and Roses, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17930773 | Found in You (Fixed, #2) | (isbn13, lost-precision, 9.7816270402e+12) | (isbn13, float-precision-lost, 9.7816270402e+12) |
| 17948485 | Friend-Zoned (Friend-Zoned, #1) | (isbn13, lost-precision,bad-prefix, 2.94004447015e+12) | (isbn13, float-precision-lost, 2.94004447015e+12) |
| 17950614 | UnDivided (Unwind, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17970255 | Into the Deep (Into the Deep, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17973653 | Shine Not Burn (Shine Not Burn, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17977710 | Twisted (Tangled, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17985262 | CyberStorm | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17989312 | The Sisterhood | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 17999892 | The Atlantis Gene (The Origin Mystery, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18045473 | Last Train to Istanbul | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18053782 | Take a Chance (Rosemary Beach, #7; Chance, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18071296 | Willing Captive | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18076876 | Reaper's Legacy (Reapers MC, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18080889 | Worth the Fight (MMA Fighter, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18089551 | Tall, Tatted and Tempting (The Reed Brothers, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18104607 | Beautiful Oblivion (The Maddox Brothers, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18105011 | Sweet Home (Sweet Home, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 181077 | Sadako and the Thousand Paper Cranes | (isbn13, lost-precision, 9.78069811803e+12) | (isbn13, float-precision-lost, 9.78069811803e+12) |
| 18108281 | The King (Black Dagger Brotherhood, #12) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18108795 | High Heat (Jack Reacher #17.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18108877 | Timebound (The Chronos Files, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18110808 | Fallen Crest Public (Fallen Crest High, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18111281 | A Long Way Home | (isbn13, lost-precision, 9.78067007704e+12) | (isbn13, float-precision-lost, 9.78067007704e+12) |
| 18115061 | Before Jamaica Lane (On Dublin Street, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18129852 | Rival (Fall Away, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18130 | A Wind in the Door (A Wrinkle in Time Quintet, #2) | (isbn13, lost-precision, 9.78044048762e+12) | (isbn13, float-precision-lost, 9.78044048762e+12) |
| 18134249 | Ruin (Ruin, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18138755 | Forever with You (Fixed, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18149927 | Beneath This Man (This Man, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18163646 | Falling into Place | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18191814 | A Blaze of Sun (A Shade of Vampire, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18211536 | Rush Too Far (Rosemary Beach, #4; Too Far, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18221931 | Carter Reed (Carter Reed, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18243828 | Jake Undone (Jake, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18244799 | Hardwired (Hacker, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18246727 | Mud Vein | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18282800 | The Ladies' Room | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18285151 | More Than This (More Than, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18297707 | Tangled (Tangled, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18301124 | Making Faces | (isbn13, lost-precision, 9.78130167387e+12) | (isbn13, float-precision-lost, 9.78130167387e+12) |
| 18323154 | المرحوم | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18331807 | Vain (The Seven Deadly, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18336965 | My Heart and Other Black Holes | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18337259 | A Game of Thrones: Comic Book, Issue 1 | (isbn13, lost-precision, 9.78034553615e+12) | (isbn13, float-precision-lost, 9.78034553615e+12) |
| 18340482 | Until Trevor (Until, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18341046 | Until November (Until, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18363068 | حبيبتي بكماء | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18387597 | 2 ضباط | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18405221 | Queen of Fire (Raven's Shadow, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18461986 | Deep (Stage Dive, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18468559 | Raw (RAW Family, #1) | (isbn13, lost-precision,bad-prefix, 2.94014886112e+12) | (isbn13, float-precision-lost, 2.94014886112e+12) |
| 18478222 | Twelve Years a Slave | (isbn13, lost-precision, 9.7809897948e+12) | (isbn13, float-precision-lost, 9.7809897948e+12) |
| 18500665 | End of Days (Penryn & the End of Days, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18607805 | Kindle Paperwhite User's Guide | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18668485 | The Initiate (Divergent, #0.2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18680106 | Hard as It Gets (Hard Ink, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18711993 | فلتغفري | (isbn13, lost-precision, 9.78614432065e+12) | (isbn13, float-precision-lost, 9.78614432065e+12) |
| 18718848 | Mosquitoland | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18739426 | The Bands of Mourning (Mistborn, #6) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 1876770 | Chrzest ognia (Saga o Wiedźminie, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18781540 | Until Lilly (Until, #3) | (isbn13, lost-precision, 9.78131050159e+12) | (isbn13, float-precision-lost, 9.78131050159e+12) |
| 18781543 | Until Nico (Until, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18799585 | Hidden (Bone Secrets. #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18800655 | Terms of Enlistment (Frontlines #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18806240 | Bone Gap | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18813530 | A Shadow of Light (A Shade of Vampire, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18815695 | The Pecan Man | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18819296 | Hidden | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18867685 | The Atlantis Plague (The Origin Mystery, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18892134 | The Son (Divergent, #0.3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18906484 | The Husband's Secret Free Preview | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18943009 | Rock Bottom (Tristan & Danika, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 18982011 | The Line (Witching Savannah, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 19000 | The Constant Gardener | (isbn13, lost-precision, 9.7807432872e+12) | (isbn13, float-precision-lost, 9.7807432872e+12) |
| 19030845 | Batman: The Dark Knight Returns #1 | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 190361 | Obsidian Butterfly (Anita Blake, Vampire Hunter, #9) | (isbn13, lost-precision, 9.78051513451e+12) | (isbn13, float-precision-lost, 9.78051513451e+12) |
| 19095025 | Play (Stage Dive, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 19103097 | The Magician's Land (The Magicians, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 1923820 | Holy Bible: King James Version | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 19351043 | Nimona | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 19351490 | Grimm's Fairy Tales | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 19494 | The Spy Who Came In from the Cold | (isbn13, lost-precision, 9.78074344253e+12) | (isbn13, float-precision-lost, 9.78074344253e+12) |
| 19549841 | Seraphina (Seraphina, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 19747756 | House | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20316309 | في قلبي أنثى عبرية | (isbn13, lost-precision, 9.78977637644e+12) | (isbn13, float-precision-lost, 9.78977637644e+12) |
| 20317106 | هيبتا | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20329634 | Lines of Departure (Frontlines, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20348781 | Loving Mr. Daniels | (isbn13, lost-precision, 9.78069222191e+12) | (isbn13, float-precision-lost, 9.78069222191e+12) |
| 20423680 | The Last Town (Wayward Pines, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20438825 | Vanished (Callahan & McLane #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20439328 | How to Be Both | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 204479 | Spying in High Heels (High Heels, #1) | (isbn13, lost-precision, 9.7809848574e+12) | (isbn13, float-precision-lost, 9.7809848574e+12) |
| 20509356 | Sand Omnibus (Sand, #1-5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20525628 | How to Build a Girl | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20559676 | Killing Sarai (In the Company of Killers, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20603820 | The Will (Magdalene, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20613920 | Under Locke | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20620995 | Take Me with You | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20639274 | Archer's Voice | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20646604 | Night Owl (Night Owl, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20761374 | Reasonable Doubt: Volume 1 (Reasonable Doubt, #1) | (isbn13, lost-precision,bad-prefix, 2.94014954334e+12) | (isbn13, float-precision-lost, 2.94014954334e+12) |
| 20797535 | A Better World (Brilliance Saga, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20803953 | Bully (Fall Away, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20803962 | Until You (Fall Away, #1.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20829994 | Percy Jackson's Greek Gods (A Percy Jackson and the Olympians Guide) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20874139 | I Am Livia | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20886354 | Skin Deep (Legion, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20894857 | Sleep Tight | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 20980373 | Reasonable Doubt: Volume 2 (Reasonable Doubt, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21104828 | The Lake House | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21219083 | The One That Got Away | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 2122216 | Special A, Vol. 1 (Special A, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21394850 | أقوم قيلا | (isbn13, lost-precision, 9.7860301506e+12) | (isbn13, float-precision-lost, 9.7860301506e+12) |
| 21411058 | Bad Romeo (Starcrossed, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21414439 | Truthwitch (The Witchlands, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21418017 | The Space Between (Outlander, #7.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21420473 | The Fixed Trilogy (Fixed, #1-3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21456940 | 1919 | (isbn13, lost-precision, 9.78977093293e+12) | (isbn13, float-precision-lost, 9.78977093293e+12) |
| 21473305 | Dominic (Slater Brothers, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21518647 | Axel (Corps Security, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21518679 | Cage (Corps Security, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21843117 | Scoring Wilder | (isbn13, lost-precision, 9.7809904904e+12) | (isbn13, float-precision-lost, 9.7809904904e+12) |
| 21849362 | The Shadows (Black Dagger Brotherhood, #13) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21857294 | Reasonable Doubt: Volume 3 (Reasonable Doubt, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 21956060 | Monster in His Eyes (Monster in His Eyes, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22009741 | The Woman Who Stole My Life | (isbn13, lost-precision, 9.78071815535e+12) | (isbn13, float-precision-lost, 9.78071815535e+12) |
| 22020052 | It Ain't Me, Babe (Hades Hangmen, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22027055 | One Lavender Ribbon | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22027459 | The Atlantis World (The Origin Mystery, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22131009 | Where There's Smoke | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22296542 | Addicted to You (Addicted, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22299763 | Crooked Kingdom (Six of Crows, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22319275 | Yellow Crocus | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22381326 | Half a War (Shattered Sea, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22381892 | Killing Patton: The Strange Death of World War II's Most Audacious General | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22428828 | Welcome to Shadowhunter Academy (Tales from the Shadowhunter Academy, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22443261 | The Rithmatist (The Rithmatist, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22457201 | Hardpressed (Hacker, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22471294 | Black Lies | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22474626 | Hard Limit (Hacker, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22600903 | Where I Belong (Alabama Summer, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22611920 | The Hook Up (Game On, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22669832 | Bright Side (Bright Side, #1) | (isbn13, lost-precision, 9.78099114022e+12) | (isbn13, float-precision-lost, 9.78099114022e+12) |
| 22738563 | We Should All Be Feminists | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22744701 | My Sister's Grave (Tracy Crosswhite #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22816087 | Seveneves | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22840421 | My Lady Jane (The Lady Janies, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22857396 | Sweet Addiction (Sweet Addiction, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22886612 | Nemesis Games (The Expanse, #5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22895264 | Wicked (A Wicked Saga, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22914448 | The Dead Key | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22915460 | The Glassblower | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22918050 | The Heir (The Selection, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22923997 | Overruled (The Legal Briefs, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 22931009 | Kindle User's Guide | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23122175 | The Friend Zone (Game On, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23158207 | How Google Works | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23207027 | Three Dark Crowns (Three Dark Crowns, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23212667 | All the Missing Girls | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23252517 | The Law of Moses (The Law of Moses, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23355069 | Hero (Hero, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23357188 | Bound by Honor (Born in Blood Mafia Chronicles, #1) | (isbn13, lost-precision, 9.78131173642e+12) | (isbn13, float-precision-lost, 9.78131173642e+12) |
| 23481669 | Maude | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23485372 | The Master Magician (The Paper Magician Trilogy, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23492288 | Hidden Bodies (You, #2) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23545800 | Kaleidoscope Hearts (Hearts, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23587984 | Maybe Not (Maybe, #1.5) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23675858 | Departure | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23692271 | Sapiens: A Brief History of Humankind | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23714532 | Beautiful Sacrifice (The Maddox Brothers, #3) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23714544 | Beautiful Burn (The Maddox Brothers, #4) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23743603 | Miramont's Ghost | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23745132 | Wreckage | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23745189 | The Mermaid's Sister | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 23844390 | The Pact | (isbn13, lost-precision, 9.78150572452e+12) | (isbn13, float-precision-lost, 9.78150572452e+12) |
| 24019 | The New Best Recipe | (isbn13, lost-precision, 9.78093618475e+12) | (isbn13, float-precision-lost, 9.78093618475e+12) |
| 24044596 | Kulti | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 24228353 | Trail of Broken Wings | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 24378015 | Never Never (Never Never, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 24429934 | The Einstein Prophecy | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 24445517 | Maybe Someday (Maybe, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 24473465 | The English Spy (Gabriel Allon, #15) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 24473763 | Radiance (Wraith Kings, #1) | (isbn13, no-usable-isbn, ) | (isbn, no-usable-isbn, ) |
| 24480276 | The Versions of Us | (isbn13, lost-precision, 9.78147460016e+12) | (isbn13, float-precision-lost, 9.78147460016e+12) |
| ... | ... | ... | _(truncated, 206 more)_ |

## Why our data differs

When I compared my database with Kristina's, I found that we both had the same 10,013 books. Neither database was missing any books. However, when I went through the 23 columns from the CSV files and compared the data row by row, I found 3,136 differences across 2,142 books. I also found differences in how warnings were recorded for 706 of the 707 books that had warnings.

After looking into these differences, I realized that we weren't necessarily disagreeing on the actual data. Most of the differences came down to how we chose to store certain values and record warnings.

### The Main Difference: NULL vs. Empty String

The biggest difference I found was how we handled missing or invalid information. About 3,000 of the 3,136 differences came from this one issue.

In my database, I used SQL NULL when a field was missing or couldn't be corrected. Kristina used an empty string ('') instead.

I went back to Section 1 of our rules.md file, and it specifically says to "null the field" in situations like invalid characters, incorrect lengths, bad checksums, and scientific notation that can't be recovered. Based on those instructions, my ingest.py uses Python None, which SQLite stores as NULL.

Kristina's code uses an empty string for those same situations.

Even though both values basically mean the information isn't available, SQLite doesn't treat NULL and an empty string as the same thing. That's why so many differences showed up in the comparison.

For example, if I run SELECT isbn FROM books WHERE isbn IS NULL on my database, I get the same books that Kristina would get by running SELECT isbn FROM books WHERE isbn = '' on hers.

So we're identifying the same missing information. We're just storing it differently.

When I looked at where this difference came from, I found three things:
1. The rules were already clear about using NULL.
2. Our tests didn't specifically check whether missing values were stored as NULL or empty strings. Because of that, Kristina's code could still pass the tests.
3. The actual difference happened in ingest.py, where Kristina used an empty string instead of NULL.

To me, this is something our tests should have caught because the rules already explained how those fields should be handled.

### Differences in Warnings

The other differences I found were related to how we recorded warnings.

We both identified the same 138 rows with scientific notation issues, the same 566 rows with missing ISBNs, and the same 4 rows with bad checksums. This tells me that we were catching the same problems, but we weren't always recording them the same way.

There were three main differences:

1. **We used different names for the same warnings.**
   For example, I used `lost-precision`, `bad-characters`, and `bad-length`. Kristina used `float-precision-lost`, `invalid-characters`, and `wrong-length`. These warnings describe the same issues, but the wording is different. Our rules.md explains the types of problems we should identify, but it doesn't tell us exactly what each warning code should be named. Our tests also didn't check for specific warning names, so we both ended up using different labels.

2. **We handled multiple warnings differently.**
   When a row had more than one problem, I recorded all the reasons together, separated by commas. For example, if a row had lost precision and an invalid prefix, I included both reasons. Kristina's code only recorded the main reason. I checked rules.md again, and it doesn't clearly explain how multiple warnings should be recorded. Our merge-meeting notes did mention that my approach of recording multiple codes should be implemented, but Kristina's version still used a single warning code.

3. **We attached some warnings to different columns.**
   When both `isbn` and `isbn13` were blank, I attached the `no-usable-isbn` warning to the `isbn13` column. Kristina attached it to the `isbn` column. Section 1 of rules.md tells us to create that warning when both ISBN fields are blank, but it doesn't say which column the warning should be connected to.

### Overall Assessment

After going through the comparison, I don't see these differences as actual data bugs. Both databases contain the same 10,013 books, and we both identified the same problem rows and handled the corrections the same way.

The main differences were how missing values were stored, what names we used for warnings, and which columns certain warnings were attached to.

I think the biggest issue was the NULL versus empty string difference because Section 1 of rules.md already gave instructions for that. Our tests just didn't check it closely enough.

For the warning differences, I think the rules could have been more specific. We were both following the general instructions, but since the exact warning names and formatting weren't clearly defined, we made different choices.

Overall, I think both databases contain essentially the same information. If the comparison treated NULL and empty strings as equivalent and accounted for the different warning names, most of these differences would disappear.

The main thing I took away from this comparison is that even when two people follow the same rules, small differences in how those rules are interpreted can lead to a lot of differences in the final results. It also showed me why our tests need to check not just whether the right problems were found, but also whether the results were stored and recorded the way the rules intended.
