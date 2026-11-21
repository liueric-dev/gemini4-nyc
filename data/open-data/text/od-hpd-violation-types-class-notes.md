# What sets the class for HPD orders with more than one class

Source: HPD Housing Maintenance Code Violations (wvxf-dwi5), via `text/od-hpd-violation-types.csv` and the samples in `raw/od-hpd-violation-types-samples.jsonl`. Retrieved 2026-11-21.

143 of 400 order numbers appear under more than one class. For each, this file gives the per-class counts and date ranges, a pattern label, and, where the sampled descriptions show it, what differs between classes.

Pattern labels (computed):
- **time shift**: at least one class has no inspections since 2024 while another does, so the class used for the order changed over time.
- **concurrent**: two or more classes are still issued (inspections since 2024 in more than one class). Look at the description text and the probe counts.
- **rare exception**: one class holds 99% or more of the rows.

Probe counts give the number of sampled descriptions (up to the 40 most recent per class) that contain a phrase. Samples were not taken for every class (see `sample_source` in the CSV), and probes only cover a few orders.

Nothing here comes from the Housing Maintenance Code itself; check the class rules against workstream 1's law text before using them.

## Order 508: 508 - REPAIR PLASTER

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 139019 | 26797 | 1965-06-10 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| B | 800630 | 176074 | 1909-11-12 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 100891 | 20519 | 1959-10-04 | 2026-11-19 | 0 | DEFECTIVE PLASTERED SURFACES AND; OR DEFECTIVE PLASTERED SURFACES; BROKEN OR DEFECTIVE PLASTERED | 40 most recent (server-ordered) |
| I | 2 | 0 | 1998-03-03 | 1999-10-18 | 0 | 4787G; 3267G | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'PUBLIC HALL' | 'CEILING' | 'THROUGHOUT' |
|---|---|---|---|---|
| A | 40 | 0 | 27 | 0 |
| B | 40 | 0 | 33 | 0 |
| C | 40 | 0 | 39 | 0 |
| I | 2 | 0 | 0 | 0 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN A UNIFORM COLOR CEILING IN THE 2nd ROOM FROM EAST LOCATED AT APT 3F, 3rd STORY, 2nd APARTMENT FROM NORTH AT EAST , SECTION AT SOUTH
- B: § 27-2005 ADM CODE REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN A UNIFORM COLOR AT CEILING IN THE BATHROOM LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: § 27-2005 ADM CODE REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN A UNIFORM COLOR AT CEILING IN THE 3rd ROOM FROM NORTH LOCATED AT APT 53, 5th STORY, 1st APARTMENT FROM SOUTH AT WEST
- I: § 27-2005 ADM CODE REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN A UNIFORM COLOR 4787G \

## Order 501: 501 - REPAIR

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 99262 | 21928 | 1939-08-30 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| B | 522204 | 162996 | 1909-11-12 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 110407 | 47335 | 1973-06-06 | 2026-11-19 | 0 | SASH AT | 40 most recent (server-ordered) |
| I | 3 | 0 | 1983-04-01 | 1996-10-07 | 0 | CHIMNEY TOP 2 COURSES; BRICK CHIMNEY TOP 2; COURSES AT REAR OF | 3 most recent (all-rows-client-sorted) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'PUBLIC HALL' | 'WINDOW' | 'DOOR' |
|---|---|---|---|---|
| A | 40 | 1 | 4 | 2 |
| B | 40 | 8 | 15 | 14 |
| C | 40 | 9 | 15 | 19 |
| I | 3 | 0 | 0 | 0 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE MECHANICAL STOPPER AT WASH BASIN IN THE BATHROOM LOCATED AT APT 67, 6th STORY, 1st APARTMENT FROM WEST AT NORTH , SECTION ''WEST''
- B: § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE SPRING BALANCE AT LOWER SASH AT 1ST WINDOW FROM SOUTH AT WEST IN THE 5th ROOM FROM EAST AT NORTH LOCATED AT APT 22, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE LATCH AND ASSEMBLY AT COMPACTOR CLOSET DOOR AT PUBLIC HALL, 1st STORY
- I: § 27-2005 ADM CODE PROPERLY REPAIR THE BROKEN OR DEFECTIVE 4578G \ \ HHN96276

## Order 502: 502 - REPAIR WITH SIMILAR MATERIAL

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 110335 | 23815 | 1964-10-19 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| B | 550989 | 139952 | 1960-12-13 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 70419 | 24165 | 1973-05-14 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'PUBLIC HALL' | 'FIRE RETARD/RATED' | 'FLOOR' |
|---|---|---|---|---|
| A | 40 | 8 | 7 | 16 |
| B | 40 | 10 | 9 | 20 |
| C | 40 | 13 | 8 | 17 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE FIRE RETARDING MATERIAL AT CEILING, IN THE TERRACE IN THE 6th ROOM FROM EAST AT SOUTH LOCATED AT APT 9B, 9th STORY, 1st APARTMENT FROM NORTH AT EAST
- B: § 27-2005 ADM CODE PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE FIRE RATED MATERIAL AT CEILING BETWEEN 1ST AND 2ND STORY AT PUBLIC HALL STAIRS, 2nd STORY
- C: § 27-2005 ADM CODE PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE CERAMIC FLOOR TILES IN THE BATHROOM LOCATED AT APT 22, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 556: 556 - PAINT

- Category (dictionary): PAINTING; cited section (most common in samples): § 27-2013 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 576235 | 129035 | 1919-06-27 | 2026-11-19 | 0 | PAINT; PEELING PAINT SURFACES IN; PAINT SURFACES IN THE | 40 most recent (server-ordered) |
| B | 14 | 0 | 1974-01-03 | 2023-12-02 | 0 | CEILINGS; WALLS CEILINGS KITCHEN 2; THE CEILINGS AND WALLS | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 7 | 7 | 2025-09-17 | 2026-11-16 | 0 | SOUTH WALL; WALL IN THE; SOUTH WALL NORTH WALL | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: Almost entirely class A (576,235); B (14) and C (7) are rare exceptions.

One sample per class:

- A: § 27-2013 ADM CODE PAINT WITH LIGHT COLORED PAINT TO THE SATISFACTION OF THIS DEPARTMENT ALL PEELING PAINT SURFACES IN THE 1st ROOM FROM NORTH, THE BATHROOM , THE KITCHEN , THE 4th ROOM FROM NORTH, THE PRIVATE HALLWAY LOCATED AT APT C12, 3rd STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2013 ADM CODE PAINT WITH LIGHT COLORED PAINT TO THE SATISFACTION OF THIS DEPARTMENT THE CEILINGS AND WALLS AT PUBLIC HALL
- C: § 27-2013 ADM CODE PAINT WITH LIGHT COLORED PAINT TO THE SATISFACTION OF THIS DEPARTMENT CEILING, 1st DOOR FROM EAST AT SOUTH WALL, 1st DOOR FRAME FROM EAST AT SOUTH WALL, NORTH WALL IN THE BATHROOM LOCATED AT APT 1C, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 530: 530 - MAKE DOORS SELF-CLOSING

- Category (dictionary): EGRESS; cited section (most common in samples): D26-10.01, 10.05 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 21 | 0 | 1974-01-17 | 1995-02-28 | 0 | TO 1 STY PUBLICHALL.; VESTIBULE TO 1 STY; BOILER ROOM DOOR. | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 100365 | 1 | 1903-12-16 | 2024-05-31 | 0 | SELF-CLOSING; DOORS; OR REPAIR THE SELF-CLOSING | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 338176 | 188101 | 2019-05-02 | 2026-11-19 | 0 | HINGES; ENTRANCE; 1ST STORY | 40 most recent (server-ordered) |

Note: Time shift: class B rows end 2024-05 (1 since 2024); class C rows start 2019. Recent self-closing-door violations are class C.

One sample per class:

- A: D26-10.01, 10.05 ADM CODE ARRANGE AND MAKE SELF-CLOSING THE DOORS BOILER ROOM DOOR.
- B: § 27-2005, 27-2007, 27-2041.1 HMC, §238, § 309; § 107 (2) ( C) MDL AND 28 RCNY §25-171: REPLACE OR REPAIR THE SELF-CLOSING DOORS THAT IS MISSING OR DEFECTIVE VESTIBULE DOOR AT PUBLIC HALL
- C: § 27-2005, 27-2007, 27-2041.1 HMC, §238, § 309; § 107 (2) ( C) MDL AND 28 RCNY §25-171: REPLACE OR REPAIR THE SELF-CLOSING DOORS THAT IS MISSING OR DEFECTIVE HINGES IN THE ENTRANCE LOCATED AT APT 2C, 2nd STORY, 2nd APARTMENT FROM EAST AT SOUTH

## Order 550: 550 - TRACE & REPAIR THE SOURCE & ABATE THE…MOLD

- Category (dictionary): CLEANING; cited section (most common in samples): § 27-2017.3 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 123953 | 52327 | 2011-02-22 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| B | 211315 | 51845 | 2004-08-18 | 2026-11-19 | 65815 | GREATER THAN 10; LESS THAN; MORE THAN 10 | 40 most recent (server-ordered) |
| C | 40926 | 10485 | 2004-09-09 | 2026-11-19 | 11517 | GREATER THAN 30; MORE THAN 30 | 40 most recent (server-ordered) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'LESS THAN 10' | 'MORE/GREATER THAN 10' | '30' (e.g. 'LESS THAN 30') | '100' | 'UPGRADED TO CLASS' |
|---|---|---|---|---|---|---|
| A | 40 | 36 | 0 | 0 | 0 | 0 |
| B | 40 | 0 | 32 | 16 | 0 | 0 |
| C | 40 | 0 | 3 | 36 | 0 | 0 |

Note: Sampled class A descriptions state an area under 10 square feet ('LESS THAN 10 SQ FT'); class B descriptions state more than 10 (often 'MORE THAN 10 SQ FT' or 'GREATER THAN 10 LESS THAN 30'). See the probe counts for class C. Rows saying 'HAS BEEN UPGRADED TO CLASS B/C PER ADMINISTRATIVE CODE §27-2017.3a(3)(a) or (b)' are upgrades of uncorrected violations and are excluded from the order-to-class map.

One sample per class:

- A: § 27-2017.3 HMC: TRACE AND REPAIR THE SOURCE AND ABATE THE VISIBLE MOLD CONDITION... LESS THAN 10 SQFT AT CEILING IN THE BATHROOM LOCATED AT APT 67, 6th STORY, 1st APARTMENT FROM WEST AT NORTH , SECTION ''WEST''
- B: § 27-2017.3 HMC: TRACE AND REPAIR THE SOURCE AND ABATE THE VISIBLE MOLD CONDITION... MORE THAN 10 SQ FT OBSERVED AT WEST WALL IN THE 3rd ROOM FROM NORTH AT WEST LOCATED AT APT 2C, 1st STORY, 3rd APARTMENT FROM EAST AT SOUTH
- C: § 27-2017.3 HMC: TRACE AND REPAIR THE SOURCE AND ABATE THE VISIBLE MOLD CONDITION... GREATER THAN 30 SQ FT AT SOUTH WALL, SOUTH WINDOW FRAME, WEST WALL, EAST WALL CEILING IN THE BATHROOM LOCATED AT APT 4, 2nd STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 583: 583 - REPAIR THE SOURCE AND ABATE THE WATER LEAK

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2026, 2027 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 30014 | 9934 | 2012-07-09 | 2026-11-19 | 0 | AT CEILING; AT CEILING IN THE | 40 most recent (server-ordered) |
| B | 258314 | 84163 | 2012-06-25 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 52781 | 11906 | 2012-06-29 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| I | 17 | 0 | 2013-09-27 | 2013-10-02 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'ACTIVE' | 'DRIPPING' | 'CEILING' | 'ELECTRIC'/'LIGHT FIXTURE' |
|---|---|---|---|---|---|
| A | 40 | 0 | 0 | 33 | 0 |
| B | 40 | 0 | 0 | 35 | 0 |
| C | 40 | 3 | 0 | 38 | 0 |
| I | 2 | 0 | 0 | 0 | 0 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK AT CEILING IN THE BATHROOM LOCATED AT APT 2A, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK AT CEILING IN THE 5th ROOM FROM EAST AT NORTH LOCATED AT APT 22, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK AT CEILING IN THE BATHROOM LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH
- I: § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK

## Order 1503: 1503 - REPAIR OR REPLACE CO DETECTOR

- Category (dictionary): CARBON MONOXIDE DETECTING DEVICES; cited section (most common in samples): § 27-2045(B)(1)(B) HMC, § 12-06, § 12-07, § 12-09 RCNY
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 303909 | 88435 | 2004-11-02 | 2026-11-19 | 0 | IN THE; IN THE ENTIRE APARTMENT; MISSING | 40 most recent (server-ordered) |
| C | 1 | 0 | 2021-01-21 | 2021-01-21 | 0 |  | 1 most recent (server-ordered) |

Note: Class B except one 2021 class C row.

One sample per class:

- B: § 27-2045(B)(1)(B) HMC, § 12-06, § 12-07, § 12-09 RCNY REPAIR, REPLACE OR PROVIDE AN APPROVED AND OPERATIONAL CARBON MONOXIDE DETECTING DEVICE, INSTALLED IN ACCORDANCE WITH APPLICABLE LAW AND RULES MISSING IN THE ENTIRE APARTMENT LOCATED AT APT 2D, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2046.1 HMC: REPAIR OR REPLACE THE CARBON MONOXIDE DETECTING DEVICE(S). DEFECTIVE IN THE ENTIRE APARTMENT LOCATED AT APT A4, 1st STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 568: 568 - ABATE THE NUISANCE OF ROACHES

- Category (dictionary): EXTERMINATION & RODENT ERADICATION; cited section (most common in samples): § 27-2017.4 ADMIN. CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 69295 | 0 | 2009-09-30 | 2021-11-18 | 0 | CONSISTING OF ROACHES; INFESTATION CONSISTING OF ROACHES; NUISANCE CONSISTING OF ROACHES | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 232595 | 102968 | 2018-11-01 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |

Note: Time shift: class B rows run 2009 to 2021-11 and none since 2024; class C rows start 2018. Recent roach violations are class C.

One sample per class:

- B: § 27-2017.4 ADMIN. CODE: ABATE THE INFESTATION CONSISTING OF ROACHES IN THE ENTIRE APARTMENT LOCATED AT APT 1A, 1st STORY
- C: HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF ROACHES IN THE ENTIRE APARTMENT LOCATED AT APT 22, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST

## Order 569: 569 - ABATE THE NUISANCE OF MICE

- Category (dictionary): EXTERMINATION & RODENT ERADICATION; cited section (most common in samples): § 27-2017.4 ADMIN. CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 85946 | 0 | 2009-09-18 | 2019-01-20 | 0 | CONSISTING OF MICE; NUISANCE CONSISTING OF MICE; THE NUISANCE CONSISTING OF | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 193293 | 77738 | 2019-01-16 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |

Note: Time shift: class B rows run 2009 to 2019-01; class C rows start 2019. Recent mouse violations are class C.

One sample per class:

- B: § 27-2017.4 ADMIN. CODE: ABATE THE INFESTATION CONSISTING OF MICE AT BASEMENT
- C: HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF MICE IN THE ENTIRE APARTMENT LOCATED AT APT 22, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST

## Order 510: 510 - ABATE THE NUISANCE

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE & 309 M/D LAW
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 7267 | 416 | 1964-04-09 | 2026-11-17 | 0 | DISCARDED RANGES AT PUBLIC; WOOD PANELS INSTALLED AT; REG NUMBER POSTED SHOULD | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 128043 | 13648 | 1919-06-27 | 2026-11-19 | 0 | WINDOW; THE 1ST ROOM FROM; IN THE 1ST ROOM | 40 most recent (server-ordered) |
| C | 139599 | 35822 | 1973-04-06 | 2026-11-19 | 0 | ENTIRE; HOT; IN THE ENTIRE APARTMENT | 40 most recent (server-ordered) |
| I | 2 | 0 | 1996-06-08 | 1999-01-23 | 0 | OF 6886G HNN96159; OF 6628G | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'HOT WATER' ... '130' | 'WOOD(EN) PANEL' | 'ENTIRE APARTMENT' |
|---|---|---|---|---|
| A | 3 | 0 | 1 | 0 |
| B | 40 | 0 | 5 | 0 |
| C | 40 | 16 | 0 | 16 |
| I | 2 | 0 | 0 | 0 |

Note: Order 510 is a catch-all 'ABATE THE NUISANCE CONSISTING OF ...'. The condition named after 'CONSISTING OF' varies (e.g. 'HOT WATER EXCEEDING MAXIMUM OF 130 DEGREES' in class C samples), so the class follows the condition, not the order number.

One sample per class:

- A: § 27-2005 ADM CODE & 309 M/D LAW ABATE THE NUISANCE CONSISTING OF 17 DISCARDED RANGES AT PUBLIC HALL, 1st STORY
- B: § 27-2005 ADM CODE & 309 M/D LAW ABATE THE NUISANCE CONSISTING OF WOODEN PANELS AT ALL WALLS IN THE 1st ROOM FROM EAST AT NORTH LOCATED AT APT 1R, 1st STORY, 1st APARTMENT FROM NORTH AT EAST
- C: § 27-2005 ADM CODE & 309 M/D LAW ABATE THE NUISANCE CONSISTING OF HOT WATER EXCEEDING MAXIMUM OF 130 DEGREES IN THE ENTIRE APARTMENT LOCATED AT APT 3, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- I: § 27-2005 ADM CODE & 309 M/D LAW ABATE THE NUISANCE CONSISTING OF 6628G \

## Order 505: 505 - RETIRED

- Category (dictionary): RETIRED; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 24126 | 2 | 1964-10-19 | 2025-05-14 | 0 |  | 40 most recent (server-ordered) |
| B | 145864 | 22 | 1963-07-15 | 2026-09-05 | 0 |  | 40 most recent (server-ordered) |
| C | 61289 | 5 | 1973-09-28 | 2024-10-04 | 0 |  | 40 most recent (server-ordered) |
| I | 2 | 0 | 1974-12-06 | 1986-08-07 | 0 | STY APT; HEAD; SPRINKLER HEAD AT KITCHEN | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE REPLACE WITH NEW THE BROKEN OR DEFECTIVE UPPER ESCUTCHEON PLATE AT HEAT RISER AT EAST WALL IN THE 3rd ROOM FROM NORTH LOCATED AT APT 617, 6th STORY, 2nd APARTMENT FROM NORTH AT EAST
- B: § 27-2005 ADM CODE REPLACE WITH NEW THE BROKEN OR DEFECTIVE ENTRANCE DOOR IN THE 2nd ROOM FROM NORTH LOCATED AT APT 9, 4th STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: § 27-2005 ADM CODE REPLACE WITH NEW THE BROKEN OR DEFECTIVE EAST CENTER WINDOW GLASS PANE AT LOWER SASH IN THE 1st ROOM FROM NORTH LOCATED AT APT 14, 4th STORY, 1st APARTMENT FROM NORTH AT EAST
- I: D26-10.01 ADM CODE REPLACE WITH NEW THE BROKEN OR DEFECTIVE PAINTED SPRINKER HEAD IN KITCHEN 2 STY APT 12. , SECTION '' ''

## Order 506: 506 - REPLACE

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 42249 | 6363 | 1960-12-13 | 2026-11-19 | 0 | SAFETY; ELECTRICAL OUTLET; WALL AT | 40 most recent (server-ordered) |
| B | 112209 | 17056 | 1971-03-15 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 23213 | 3303 | 1973-08-31 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| I | 3 | 0 | 1985-08-21 | 1999-04-21 | 0 | FIREPROOF SELFCLOSING DOORS 2; SELFCLOSING DOORS 2 STY; ENTRANCES AT EAST WEST. | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE REPLACE WITH NEW THE MISSING TOP ESCUTHEON PLATE AT RISER IN THE BATHROOM LOCATED AT APT 6D, 4th STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2005 ADM CODE REPLACE WITH NEW THE MISSING ELECTRICAL OUTLET COVER PLATE AT WEST WALL AT PUBLIC HALL, 1st STORY, SECTION ''SOUTH''
- C: § 27-2005 ADM CODE REPLACE WITH NEW THE MISSING HEAVY DUTY LOCKSET AT THE BUILDING 'S ENTRANCE DOOR , 1st STORY
- I: D26-10.01 ADM CODE REPLACE WITH NEW THE MISSING FIREPROOF SELFCLOSING DOORS 2 STY PUB HALL APT ENTRANCES AT EAST & WEST.

## Order 579: 579 - REPAIR LEAKY FAUCETS

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2026 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 13780 | 2467 | 1966-07-06 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| B | 121028 | 25228 | 1973-06-07 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 9265 | 2588 | 1973-10-15 | 2026-11-18 | 0 | HOT WATER | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| I | 1 | 0 | 1997-09-13 | 1997-09-13 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADM CODE REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS AT WASHBASIN IN THE 1st BATHROOM FROM EAST AT NORTH LOCATED AT APT 1F, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2026 ADM CODE REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS AT WASH BASIN IN THE BATHROOM LOCATED AT APT 22, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2026 ADM CODE REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS ACTIVE FLOW AT FAUCET AT SINK IN THE KITCHEN LOCATED AT APT 4D, 4th STORY, 1st APARTMENT FROM SOUTH AT WEST
- I: SECTION 27-2026 ADM CODE REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS 2328G \

## Order 670: 670 - INADEQUATE HOT WATER

- Category (dictionary): HEAT AND HOT WATER; cited section (most common in samples): D26-17.07 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1974-04-02 | 1974-04-02 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 799 | 0 | 1968-12-06 | 2012-03-07 | 0 | WASHBASIN BATHROOM AND SINK; BATHROOM AND SINK IN; SINK IN THE KITCHEN | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 127658 | 43122 | 1973-09-28 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |

Note: Hot water: class B rows end 2012-03 and class A has one 1974 row; since 2024 every row is class C.

One sample per class:

- A: D26-17.07 ADM CODE PROVIDE HOT WATER AT ALL HOT WATER FIXTURES KITCHEN SINK 2ND STY REAR APT 4. LOCATED AT APT 4
- B: § 27-2031 ADM CODE PROVIDE HOT WATER AT ALL HOT WATER FIXTURES
- C: § 27-2031 ADM CODE PROVIDE HOT WATER AT ALL HOT WATER FIXTURES IN THE ENTIRE APARTMENT LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 529: 529 - REFIT DOORS ETC.

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 109578 | 4526 | 1963-07-15 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| B | 16164 | 12657 | 1975-10-02 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 HMC: REFIT CLOSET DOOR AT EAST WALL IN THE PRIVATE HALLWAY LOCATED AT APT 5D, 5th STORY, 2nd APARTMENT FROM EAST AT SOUTH
- B: § 27-2005 HMC: REFIT BUILDING ENTRANCE DOOR AT PUBLIC HALL, 1st STORY

## Order 507: 507 - LEAKY ROOF

- Category (dictionary): MAINTENANCE; cited section (most common in samples): D26-10.01 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1981-05-08 | 1981-05-08 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 89192 | 27558 | 1966-11-10 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 19383 | 3288 | 1973-11-02 | 2026-11-18 | 0 | PUBLIC HALL; AT PUBLIC HALL | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: D26-10.01 ADM CODE REPAIR THE ROOF SO THAT IT WILL NOT LEAK OVER 5TH STY FRONT EAST APT 5D FRONT ROOM. LOCATED AT APT 5D
- B: § 27-2005 ADM CODE REPAIR THE ROOF SO THAT IT WILL NOT LEAK OVER CEILING AT PUBLIC HALL STAIRS, 5th STORY
- C: § 27-2005 ADM CODE REPAIR THE ROOF SO THAT IT WILL NOT LEAK AT THE CEILING AT THE BULKHEAD AT PUBLIC HALL STAIRS

## Order 808: 808 - REPAIR PLASTER

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 12109 | 1968 | 1999-12-07 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| B | 78425 | 11436 | 1999-11-22 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 8794 | 1330 | 1999-11-26 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN UNIFORM COLOR AT CEILING IN THE BATHROOM LOCATED AT APT 1STFLO, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2005 ADMIN. CODE: REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN UNIFORM COLOR AT CEILING IN THE 3rd ROOM FROM NORTH AT EAST LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- C: § 27-2005 ADMIN. CODE: REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN UNIFORM COLOR THE CEILING IN THE 1st ROOM FROM EAST AT NORTH LOCATED AT APT 1STFLO LOWER LEVEL, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST

## Order 509: 509 - SECURE LOOSE MATTER

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 16916 | 2332 | 1966-07-06 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| B | 73248 | 12505 | 1971-03-15 | 2026-11-19 | 0 | PUBLIC HALL | 40 most recent (server-ordered) |
| C | 7397 | 1457 | 1975-10-31 | 2026-11-18 | 0 | FRONT; BOTTOM AT INTERMEDIATE LANDING; INTERMEDIATE LANDING GOING UP | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| I | 1 | 0 | 1992-10-02 | 1992-10-02 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE PROPERLY SECURE THE LOOSE ELECTRICAL OUTLET COVER AT SOUTH WALL IN THE 1st BATHROOM FROM NORTH LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2005 ADM CODE PROPERLY SECURE THE LOOSE WASH BASIN CABINET IN THE BATHROOM LOCATED AT APT 22, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2005 ADM CODE PROPERLY SECURE THE LOOSE 10TH, AND 11TH BALUSTER UP FROM BOTTOM AT INTERMEDIATE LANDING GOING UP AT BULKHEAD AT PUBLIC HALL STAIRS, 4th STORY
- I: D26-10.01 ADM CODE PROPERLY SECURE THE LOOSE CHAIN TO LOWER SASH WEST STAIR 4 STY CLASS A.

## Order 554: 554 - PAINT METAL

- Category (dictionary): PAINTING; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 94508 | 19637 | 1983-03-30 | 2026-11-19 | 0 | THE 1ST; FROM NORTH; AT WEST | 40 most recent (server-ordered) |
| C | 5 | 5 | 2025-03-12 | 2026-02-27 | 0 | WALL WALL 1ST RADIATOR; NORTH WALL SOUTH WALL; SOUTH IN THE KITCHEN | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2005 ADM CODE PAINT METAL IN ACCORDANCE WITH DEPT. REGULATION AT RISER IN THE 2nd ROOM FROM NORTH LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: § 27-2005 ADM CODE PAINT METAL IN ACCORDANCE WITH DEPT. REGULATION 1st CLOSET FROM EAST AT SOUTH WALL WALL, 1st RADIATOR FROM WEST AT NORTH WALL, SOUTH WALL IN THE 2nd ROOM FROM EAST LOCATED AT APT 2A, 2nd STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 539: 539 - REMOVE ENCUMBRANCE

- Category (dictionary): EGRESS; cited section (most common in samples): D26-10.01, 10.05 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1986-03-05 | 1986-03-05 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 90221 | 15480 | 1970-05-25 | 2026-11-19 | 0 | FIRE; FIRE ESCAPE; BALCONY | 40 most recent (server-ordered) |

One sample per class:

- A: D26-10.01, 10.05 ADM CODE AND DEPT. RULES AND REGULATIONS. REMOVE THE ENCUMBRANCE OBSTRUCTING EGRESS FROM FIRE ESCAPES ALL BALCONIES FIRE ESCAPES AT REAR.
- B: § 27-2005, 2007 ADM CODE AND DEPT. RULES AND REGULATIONS. REMOVE THE ENCUMBRANCE OBSTRUCTING EGRESS FROM FIRE ESCAPES AIR CONDITIONERS (2) EXTENDING MORE THAN 6 INCHES FROM WINDOW SILL AT 6TH STORY BALCONY AT STACK AT SOUTH EXTERIOR WALL AT FIRE ESCAPE

## Order 538: 538 - REMOVE ENCUMBRANCES

- Category (dictionary): EGRESS; cited section (most common in samples): D26-10.01, 10.05 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 4 | 0 | 1979-08-17 | 1988-03-25 | 0 | BICYCLE CHAIRS HOUSEHOLD ARTICLES; HOUSEHOLD ARTICLES AT SCUTTLE; CHAIRS HOUSEHOLD ARTICLES AT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 85507 | 22323 | 1968-09-13 | 2026-11-19 | 0 | AT PUBLIC HALL; ITEMS; ITEMS AT | 40 most recent (server-ordered) |
| C | 2 | 0 | 1981-01-28 | 1987-08-21 | 0 | HOUSEHOLD ARTICLES TOYS; FLOWER POTS HOUSEHOLD ARTICLES; POTS HOUSEHOLD ARTICLES TOYS | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-10.01, 10.05 ADM CODE REMOVE ALL ENCUMBRANCES CONSISTING OF BICYCLE CHAIRS & HOUSEHOLD ARTICLES AT SCUTTLE LADDER 4 STY PUBLIC HALL.
- B: § 27-2005, 2007 ADM CODE REMOVE ALL ENCUMBRANCES CONSISTING OF HOUSEHOLD ITEMS AT 1ST STORY PUBLIC HALL IN THE PUBLIC HALL LOCATED AT PUBLIC PARTS 2, 2nd STORY, 1st PUBLIC PARTS FROM EAST AT SOUTH
- C: D26-10.01, 10.05 ADM CODE REMOVE ALL ENCUMBRANCES CONSISTING OF FLOWER POTS HOUSEHOLD ARTICLES TOYS ETC PUBLIC HALL ALL STYS.

## Order 566: 566 - REMOVE VERMIN

- Category (dictionary): EXTERMINATION & RODENT ERADICATION; cited section (most common in samples): D26-13.03 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 15 | 0 | 1974-04-19 | 1989-11-20 | 0 | MICE; STY; APT 2W KITCHEN. SECTION | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 72670 | 5153 | 1960-12-13 | 2026-11-19 | 0 | IN THE; IN THE ENTIRE APARTMENT; FLIES | 40 most recent (server-ordered) |
| C | 1 | 0 | 1974-05-07 | 1974-05-07 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-13.03 ADM CODE ABATE THE NUISANCE CONSISTING OF VERMIN 2 STY SW APT 2 MICE & ROACHES. LOCATED AT APT 2
- B: 566 (B) 27-2021.4 HMC: ABATE THE NUISANCE CONSISTING OF PESTS. EVIDENCE OF FLIES IN THE ENTIRE APARTMENT LOCATED AT APT 1F, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- C: D26-13.03 ADM CODE ABATE THE NUISANCE CONSISTING OF VERMIN MICE EXCRETA 2 STY APT KITCHEN FLOOR.

## Order 526: 526 - REMOVE ILLEGAL FASTENING

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005, 2007 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 18307 | 1948 | 1970-03-01 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| C | 52528 | 6954 | 1963-07-15 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'GATE' | 'WINDOW' | 'FIRE ESCAPE' |
|---|---|---|---|---|
| B | 40 | 3 | 2 | 0 |
| C | 40 | 1 | 1 | 1 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005, 2007 ADM CODE REMOVE THE ILLEGAL FASTENING CONSISTING OF AN UNACCEPTABLE ELECTROMAGNETIC LOCKING DEVICE INSTALLED AT THE BUILDING ENTRANCE DOOR
- C: § 27-2005, 2007 ADM CODE REMOVE THE ILLEGAL FASTENING DOUBLE CYLINDER LOCK INSTALLED AT BUILDING ENTRANCE DOOR.

## Order 801: 801 - REPAIR

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 9602 | 1477 | 1999-12-07 | 2026-11-12 | 0 | BROKEN OR DEFECTIVE WOOD; REPLACE THE BROKEN OR; OR REPLACE THE BROKEN | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 55725 | 9827 | 1999-12-01 | 2026-11-19 | 0 | CEILING; LIGHT; WALL IN THE | 40 most recent (server-ordered) |
| C | 5432 | 1820 | 2000-01-14 | 2026-11-18 | 0 | LOCK; BROKEN OR DEFECTIVE WOOD; REPLACE THE BROKEN OR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE ,
- B: § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE BASEBOARD AT SOUTH WALL IN THE 1st ROOM FROM EAST AT NORTH LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE 1ST, 2ND, 3RD, 4TH, 5TH, 6TH, 7TH, 8TH, 9TH, 10TH, 11TH AND 12TH METAL TREADS FROM BOTTOM UP LEADING TO 2ND STORY AT BUILDING FRONT

## Order 742: 742 - NO GAS

- Category (dictionary): KITCHEN AND KITCHENETTES; cited section (most common in samples): § 27-2070 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 12152 | 2064 | 1972-09-06 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 45607 | 9244 | 1974-07-19 | 2026-11-19 | 0 | PROVIDE AN ADEQUATE SUPPLY; ADEQUATE SUPPLY OF GAS; AN ADEQUATE SUPPLY OF | 40 most recent (server-ordered) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'NO GAS' | 'ENTIRE APARTMENT' | 'RANGE' |
|---|---|---|---|---|
| B | 3 | 0 | 0 | 0 |
| C | 40 | 0 | 1 | 40 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2070 ADM CODE PROVIDE AN ADEQUATE SUPPLY OF GAS TO THE FIXTURES AND STOVE IN THE KITCHEN LOCATED AT APT 4D, 4th STORY
- C: § 27-2070 ADM CODE PROVIDE AN ADEQUATE SUPPLY OF GAS TO THE FIXTURES AT RANGE IN THE KITCHEN LOCATED AT APT 4, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 552: 552 - REMOVE ACCUMULATION OR RUBBISH

- Category (dictionary): CLEANING; cited section (most common in samples): § 27-2010, 2011, 2012 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 5525 | 910 | 1964-04-09 | 2026-11-18 | 0 | THE YARD; THE YARD SECTION EAST''; THE YARD YARD | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 45719 | 10164 | 1973-04-09 | 2026-11-18 | 0 | THE AT | 40 most recent (server-ordered) |
| C | 4784 | 904 | 1973-05-14 | 2026-11-18 | 0 | THE YARD; THE YARD SECTION REAR''; YARD SOUTH OF BUILDING | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| I | 1 | 0 | 1983-03-25 | 1983-03-25 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2010, 2011, 2012 ADM CODE REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE
- B: § 27-2010, 2011, 2012 ADM CODE REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE CLOTHES AND GARBAGES IN THE ENTIRE APARTMENT LOCATED AT APT A2, 2nd STORY, 2nd APARTMENT FROM EAST AT SOUTH
- C: § 27-2010, 2011, 2012 ADM CODE REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE
- I: D26-11.01, 11.03, 11.05 ADM CODE REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE ENTRANCE TO CELLAR AT REAR YARD CLASS A.

## Order 802: 802 - REPAIR WITH SIMILAR MATERIAL

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 7402 | 1325 | 1999-12-13 | 2026-11-18 | 0 | WOOD WINDOW STOOL | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 42983 | 6904 | 1999-11-26 | 2026-11-19 | 0 | IN THE KITCHEN | 40 most recent (server-ordered) |
| C | 4674 | 949 | 1999-11-27 | 2026-11-17 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE 1ST AND 2ND CONCRETE TREADS FROM BOTTOM UP AT STAIRS AT BUILDING FRONT
- B: § 27-2005 ADMIN. CODE: PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE REFRIGERATOR DOOR GASKET SEAL IN THE KITCHEN LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2005 ADMIN. CODE: PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE 10TH AND 11TH TREAD FROM BOTTOM UP AT STAIRS IN THE PRIVATE HALLWAY LOCATED AT APT 1FL , 1st STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 598: 598 - REPAIR BROKEN, LOOSE CONNECTION

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2500 | 431 | 1972-05-17 | 2026-11-14 | 0 | SECTION; STY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 42721 | 8251 | 1975-12-03 | 2026-11-19 | 0 | WASTE LINE | 40 most recent (server-ordered) |
| C | 9245 | 1963 | 1975-04-18 | 2026-11-18 | 0 | LEAK AT; ACTIVE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| I | 1 | 0 | 1996-10-07 | 1996-10-07 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADM CODE REPAIR THE BROKEN OR DEFECTIVE CONNECTION AT BASE CABINET AT NORTH WALL IN THE KITCHEN LOCATED AT APT 4A, 4th STORY, 1st APARTMENT FROM EAST AT SOUTH
- B: § 27-2026 ADM CODE REPAIR THE BROKEN OR DEFECTIVE CONNECTION AT WASTE LINE AT SINK IN THE KITCHEN LOCATED AT APT 2A, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: § 27-2026 ADM CODE REPAIR THE BROKEN OR DEFECTIVE CONNECTION ACTIVE LEAK AT DRAIN WASTE PIPE AT SINK IN THE KITCHEN LOCATED AT APT 711, 7th STORY, 2nd APARTMENT FROM SOUTH AT WEST , SECTION ''WEST''
- I: § 27-2026 ADM CODE REPAIR THE BROKEN OR DEFECTIVE CONNECTION 4578G \ HHN96276

## Order 484: 484 - IV-1. MAILBOXES PRESENT

- Category (dictionary): POSTING/SIGNAGE; cited section (most common in samples): § 329, M/D LAW
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 50226 | 9065 | 1969-09-02 | 2026-11-19 | 0 | AT PUBLIC HALL; 1ST STORY; PUBLIC HALL 1ST STORY | 40 most recent (server-ordered) |
| B | 2 | 0 | 1974-05-30 | 1975-03-06 | 0 |  | 2 most recent (server-ordered) |

One sample per class:

- A: § 329, M/D LAW AND DEPT. RULES AND REGS. PROVIDE A COMPLETED CERTIFICATE OF INSPECTION VISITS IN A PROPER FRAME AT OR NEAR MAILBOXES, BOTTOM EDGE OF FRAME BETWEEN 48-62 INCHES ABOVE FLOOR MISSING AT PUBLIC HALL, 1st STORY
- B: § 329, M/D LAW AND DEPT. RULES AND REGS. PROVIDE A COMPLETED CERTIFICATE OF INSPECTION VISITS IN A PROPER FRAME AT OR NEAR MAILBOXES, BOTTOM EDGE OF FRAME BETWEEN 48-62 INCHES ABOVE FLOOR

## Order 491: 491 - FILE PLANS OR RESTORE

- Category (dictionary): ALTERATIONS; cited section (most common in samples): § 300 M/D LAW
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 50050 | 6765 | 1909-11-12 | 2026-11-18 | 0 | IN THE; ROOM FROM; CEILING | 40 most recent (server-ordered) |
| B | 4 | 0 | 1973-10-19 | 1995-02-21 | 0 | SEALED; STY | 4 most recent (server-ordered) |

One sample per class:

- A: § 300 M/D LAW FILE PLANS AND APPLICATION AND LEGALIZE THE FOLLOWING ALTERATION OR RESTORE TO THE LEGAL CONDITION EXISTING PRIOR TO THE MAKING OF SAID ALTERATION PARTITION ERECTED FROM FLOR TO CEILING CREATING AND ADITIONAL ROOM IN THE 2nd ROOM FROM NORTH LOCATED AT APT 2D, 2nd STORY, 1st APARTMENT F
- B: § 300 M/D LAW FILE PLANS AND APPLICATION AND LEGALIZE THE FOLLOWING ALTERATION OR RESTORE TO THE LEGAL CONDITION EXISTING PRIOR TO THE MAKING OF SAID ALTERATION 12X14 ROOM CREATED ON TERRACE 11TH STY SOUTH WEST APT 11H. , SECTION '' ''

## Order 778: 778 - POST REGISTRATION SIGN

- Category (dictionary): ANNUAL PROPERTY REGISTRATION; cited section (most common in samples): § 27-2104 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 49784 | 9112 | 1970-04-20 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| B | 1 | 0 | 1988-03-16 | 1988-03-16 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2104 ADM CODE POST AND MAINTAIN A PROPER SIGN ON WALL OF ENTRANCE STORY SHOWING THE REGISTRATION NUMBER ASSIGNED BY THE DEPARTMENT AND THE ADDRESS OF THE BUILDING. AT PUBLIC HALL, 1st STORY
- B: D26-41.15 ADM CODE POST A SIGN ON WALL OF ENTRANCE STORY IDENTIFYING OWNER AND MANAGING AGENT.

## Order 649: 649 - REMOVE OBSTRUCTIONS

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): D26-16.01 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1986-03-31 | 1986-03-31 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 40862 | 10442 | 1967-12-12 | 2026-11-19 | 0 | BATHTUB; BATHTUB IN THE BATHROOM; AT BATHTUB | 40 most recent (server-ordered) |
| C | 8296 | 1911 | 1973-11-26 | 2026-11-16 | 0 | YARD | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: D26-16.01 ADM CODE REMOVE ALL OBSTRUCTIONS AND REPAIR ALL DEFECTS IN FLOOR DRAIN NORTH COURT.
- B: § 27-2026 ADM CODE REMOVE ALL OBSTRUCTIONS AND REPAIR ALL DEFECTS IN WASTE LINE AT BATHTUB IN THE BATHROOM LOCATED AT APT 5B, 5th STORY, 1st APARTMENT FROM WEST AT NORTH
- C: § 27-2026 ADM CODE REMOVE ALL OBSTRUCTIONS AND REPAIR ALL DEFECTS IN AREA DRAIN AT THE REAR AREAWAY, BASEMENT STORY AT REAR YARD

## Order 686: 686 - NO LIGHT AT ENTRANCE TO BUILDING

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2040 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1145 | 27 | 1967-04-11 | 2026-10-19 | 0 | WEST SECTION OF BUILDING; YARD | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 42849 | 322 | 1930-06-01 | 2026-11-18 | 0 | FRONT; WATTS; 100 WATTS | 40 most recent (server-ordered) |
| I | 1 | 0 | 1987-01-08 | 1987-01-08 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2040 ADM CODE PROVIDE ADEQUATE LIGHTING AT OR NEAR THE OUTSIDE OF THE FRONT ENTRANCEWAY OF THE BUILDING AND KEEP SAME BURNING FROM SUNSET EVERY DAY TO SUNRISE ON THE DAY FOLLOWING
- B: § 27-2040 ADM CODE PROVIDE ADEQUATE LIGHTING AT OR NEAR THE OUTSIDE OF THE FRONT ENTRANCEWAY OF THE BUILDING AND KEEP SAME BURNING FROM SUNSET EVERY DAY TO SUNRISE ON THE DAY FOLLOWING 100 WATTS AT BUILDING FRONT
- I: D26-19.07 ADM CODE PROVIDE ADEQUATE LIGHTING AT OR NEAR THE OUTSIDE OF THE FRONT ENTRANCEWAY OF THE BUILDING AND KEEP SAME BURNING FROM SUNSET EVERY DAY TO SUNRISE ON THE DAY FOLLOWING PROVIDE ADEQ LTG AT OR NEAR OUTSIDE OF FRNT ENTER OF BLDG.

## Order 689: 689 - REPAIR/ABATE UNSAFE WIRES

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2005, 2006, 2037 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1205 | 196 | 2012-07-11 | 2026-11-18 | 0 | PUBLIC HALL 1ST STORY; AT PUBLIC HALL 1ST | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 29277 | 5667 | 2012-07-06 | 2026-11-19 | 0 | ELECTRIC WIRING CONDITION CONSISTING; UNSAFE ELECTRIC WIRING CONDITION; WIRING CONDITION CONSISTING OF | 40 most recent (server-ordered) |
| C | 10860 | 2352 | 2012-07-03 | 2026-11-18 | 0 | 3RD ROOM FROM NORTH; WALL IN THE 3RD; THE 3RD ROOM FROM | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'EXPOSED' | 'LIVE' | 'SPLICED' |
|---|---|---|---|---|
| A | 3 | 0 | 0 | 0 |
| B | 40 | 25 | 0 | 0 |
| C | 3 | 0 | 0 | 0 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF AT CEILING AT PUBLIC HALL, 1st STORY
- B: § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF EXPOSED ELECTRICAL WIRES AT CEILING IN THE FOYER LOCATED AT APT 6B, 6th STORY, 1st APARTMENT FROM NORTH AT EAST
- C: § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF 3RD OUTLET FROM NORTH AT EAST WALL IN THE 3rd ROOM FROM NORTH LOCATED AT APT 4R, 4th STORY, 1st APARTMENT FROM NORTH AT EAST , SECTION ''56-07''

## Order 504: 504 - PROVIDE

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 4332 | 603 | 1966-01-31 | 2026-11-15 | 0 | IN THE BATHROOM; PLATE; PLATE AT | 40 most recent (server-ordered) |
| B | 26554 | 9132 | 1973-05-30 | 2026-11-19 | 0 | GLASS; APPROVED | 40 most recent (server-ordered) |
| C | 6977 | 1425 | 1973-04-11 | 2026-11-18 | 0 | TEMPORARY; SEAL; ALL | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE PROVIDE ESCUTCHEON PLATE AT UPPER RISER AT NORTH WALL IN THE BATHROOM LOCATED AT APT 5S, 5th STORY, 1st APARTMENT FROM WEST AT NORTH , SECTION ''4861''
- B: § 27-2005 ADM CODE PROVIDE HEAVY DUTY LOCKSET AT BUILDING FRONT ENTRANCE DOOR , 1st STORY
- C: § 27-2005 ADM CODE PROVIDE SECURITY IN EVENT OF A POWER OUTAGE BY MEANS OF A HEAVY DUTY KEY OPERATED LOCKSET AT BUILDING VESTIBULE DOOR AT PUBLIC HALL, 1st STORY

## Order 810: 810 - ABATE THE NUISANCE

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1026 | 50 | 1999-12-16 | 2026-09-24 | 0 |  | 40 most recent (server-ordered) |
| B | 20596 | 708 | 1999-11-23 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| C | 16239 | 2843 | 1999-11-24 | 2026-11-18 | 0 | IN THE ENTIRE APARTMENT; DEGREES; 130 DEGREES | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: ABATE THE NUISANCE CONSISTING OF EXCESSIVE VEGATION GROWTH OF GRASS AND WEEDS AT REAR AND FRONT YARDS YARD
- B: § 27-2005 ADMIN. CODE: ABATE THE NUISANCE CONSISTING OF ATTIC STORY USED FOR SLEEPING, AND USED IN CONJUNCTION WITH FLOOR BELOW AS 1 FAMILY HOUSE LOCATED AT APT, 1st STORY
- C: § 27-2005 ADMIN. CODE: ABATE THE NUISANCE CONSISTING OF SCALDING HOT WATER ABOVE 130 DEGREES IN THE ENTIRE APARTMENT LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 688: 688 - PROVIDE SUPPLY OF ELECTRICTY TO FIXTURES

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2037, 2038 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1272 | 199 | 2012-07-12 | 2026-11-02 | 0 | WEST; WEST WALL; 1ST ROOM FROM NORTH | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 22826 | 4899 | 2012-07-09 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| C | 13578 | 4779 | 2012-07-11 | 2026-11-19 | 0 | OUTLETS AND LIGHT | 40 most recent (server-ordered) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'ENTIRE APARTMENT' | 'OUTLET' | 'LIGHT' |
|---|---|---|---|---|
| A | 3 | 0 | 2 | 1 |
| B | 40 | 7 | 9 | 11 |
| C | 40 | 24 | 18 | 14 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES 1ST WALL LIGHT FIXTURE FROM WEST AT NORTH AT PUBLIC HALL, 9th STORY
- B: § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES AT ELECTRICAL LIGHT FIXTURE AT CEILING AT PUBLIC HALL, 1st STORY
- C: § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES AT CEILING AT PUBLIC HALL, 2nd STORY

## Order 521: 521 - REMOVE BARS OR GATES FROM FIRE ESCAPE WINDOW

- Category (dictionary): EGRESS; cited section (most common in samples): D26-10.01, 10.05 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2 | 0 | 1976-03-12 | 1989-06-29 | 0 | REAR ROOM.; STY; 12 REAR ROOM. SECTION | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 37085 | 1619 | 1919-06-27 | 2026-11-18 | 0 | IN THE; ROOM FROM; THE 1ST ROOM FROM | 40 most recent (server-ordered) |

One sample per class:

- A: D26-10.01, 10.05 ADM CODE FIRE EGRESS DEFECTIVE. REMOVE OBSTRUCTING BARS OR UNLAWFUL GATES FROM WINDOW TO FIRE ESCAPE OR PROVIDE APPROVED TYPE GATE 3RD STY REAR LEAST APT 12 REAR ROOM. , SECTION '' ''
- B: § 27-2005, 2007 ADM CODE FIRE EGRESS DEFECTIVE. REMOVE OBSTRUCTING BARS OR UNLAWFUL GATES FROM WINDOW TO FIRE ESCAPE OR PROVIDE APPROVED TYPE GATE IN THE 4th ROOM FROM EAST LOCATED AT APT 2R, 2nd STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 593: 593 - REPAIR FLUSHING APPARATUS OF WATER CLOSET

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 3746 | 823 | 1971-10-23 | 2026-11-19 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 29160 | 5716 | 1974-01-14 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 2578 | 562 | 1973-10-15 | 2026-11-12 | 0 | CLOSET; WATER | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADM CODE REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET AT 2ND FROM EAST IN THE BATHROOM LOCATED AT APT 906, 9th STORY, 2nd APARTMENT FROM EAST AT SOUTH
- B: § 27-2026 ADM CODE REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET IN THE BATHROOM LOCATED AT APT 5B, 5th STORY, 1st APARTMENT FROM WEST AT NORTH
- C: § 27-2026 ADM CODE REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET ACTIVE LEAK AT WATER CLOSET IN THE BATHROOM LOCATED AT APT 24, 5th STORY, 2nd APARTMENT FROM NORTH AT EAST

## Order 536: 536 - DOOR NOT SELF-CLOSING

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005, 2007 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 3484 | 0 | 1964-05-18 | 2022-06-09 | 0 | PUBLIC HALL STAIRS 1ST; HALL STAIRS 1ST STORY; AT PUBLIC HALL STAIRS | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1 | 1 | 2025-10-06 | 2025-10-06 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 25453 | 15008 | 2022-04-19 | 2026-11-19 | 0 | DOOR; DOOR AT; INSTALLED | 40 most recent (server-ordered) |

Note: Time shift: class A rows end 2022-06; class C rows start 2022.

One sample per class:

- A: § 27-2005, 2007 ADM CODE REMOVE DEVICE PREVENTING DOOR FROM BEING SELF-CLOSING ... , 1st STORY
- B: § 27-2005, 2007 ADM CODE REMOVE DEVICE PREVENTING DOOR FROM BEING SELF-CLOSING AT BULK HEAD DOOR AT PUBLIC HALL, 5th STORY
- C: § 27-2005, 2007 ADM CODE REMOVE DEVICE PREVENTING DOOR FROM BEING SELF-CLOSING BOULDER ROCK AT LAUNDRY ROOM AT PUBLIC HALL, 1st STORY

## Order 970: 970 - INADEQUATE HOT WATER

- Category (dictionary): HEAT AND HOT WATER; cited section (most common in samples): SECTION 27-2031 ADMIN. CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 476 | 0 | 1999-11-22 | 2011-10-04 | 0 |  | 40 most recent (server-ordered) |
| C | 28394 | 4029 | 1999-11-21 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |

Note: Hot water: class B rows end 2011-10; since then class C only.

One sample per class:

- B: SECTION 27-2031 ADMIN. CODE: PROVIDE HOT WATER AT ALL HOT WATER FIXTURES IN THE KITCHEN LOCATED AT APT 3FLR, 3rd STORY
- C: § 27-2031 ADMIN. CODE: PROVIDE HOT WATER AT ALL HOT WATER FIXTURES IN THE ENTIRE APARTMENT LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 596: 596 - REPLACE DEFECTIVE SINK, WATER CLOSET, WASH TUB

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 3881 | 310 | 1967-09-27 | 2026-11-18 | 0 | COVER IN THE BATHROOM; TANK COVER IN THE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 20672 | 3386 | 1974-06-26 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| C | 4172 | 1154 | 1974-11-15 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADM CODE REPLACE THE BROKEN OR DEFECTIVE AND OR MISSING WATER CLOSET TANK COVER IN THE BATHROOM LOCATED AT BSMT-APT AA, 1st BSMT-APT FROM WEST AT NORTH
- B: § 27-2026 ADM CODE REPLACE THE BROKEN OR DEFECTIVE WASH BASIN , IN THE BATHROOM LOCATED AT APT 1, 1st STORY, APARTMENT AT WEST
- C: § 27-2026 ADM CODE REPLACE THE BROKEN OR DEFECTIVE AIR VALVE AT NORTH RISER IN THE BATHROOM LOCATED AT APT 5B, 5th STORY, 2nd APARTMENT FROM WEST AT NORTH

## Order 722: 722 - POST SIGN INDICATING NAME AND ADDRESS OF JANITOR, ETC.

- Category (dictionary): POSTING/SIGNAGE; cited section (most common in samples): § 27-2053 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 27808 | 5923 | 1971-02-16 | 2026-11-19 | 0 | SUPERINTENDENT JANITOR OR HOUSEKEEPER.; TELEPHONE NUMBER OF SUPERINTENDENT; ADDRESS INCLUDING APARTMENT NUMBER | 40 most recent (server-ordered) |
| B | 1 | 0 | 1975-04-08 | 1975-04-08 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2053 ADM CODE POST SIGN ON WALL OF ENTRANCE STORY BEARING NAME, ADDRESS INCLUDING APARTMENT NUMBER IF ANY, AND TELEPHONE NUMBER OF SUPERINTENDENT, JANITOR OR HOUSEKEEPER.
- B: D26-22.03 ADM CODE POST SIGN ON WALL OF ENTRANCE STORY BEARING NAME, ADDRESS INCLUDING APARTMENT NUMBER IF ANY, AND TELEPHONE NUMBER OF SUPERINTENDENT, JANITOR OR HOUSEKEEPER.

## Order 805: 805 - RETIRED

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2469 | 1 | 1999-12-06 | 2025-11-28 | 0 | AT NORTH; ELECTRICAL OUTLET COVERS AT; OUTLET COVERS AT NORTH | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 17867 | 1 | 1999-11-24 | 2024-12-31 | 0 |  | 40 most recent (server-ordered) |
| C | 4391 | 0 | 1999-11-21 | 2023-04-05 | 0 | PANE; LOWER SASH; GLASS PANE | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: REPLACE WITH NEW THE BROKEN OR DEFECTIVE ELECTRICAL OUTLET COVERS AT NORTH AND EAST WALLS IN THE 1st ROOM FROM NORTH LOCATED AT APT 2NDFLO, 2nd STORY, 2nd APARTMENT FROM EAST AT SOUTH
- B: § 27-2005 ADMIN. CODE: REPLACE WITH NEW THE BROKEN OR DEFECTIVE VENTILATION SYSTEM AT CEILING IN THE 1st BATHROOM FROM EAST LOCATED AT APT 2, 2nd STORY
- C: § 27-2005 ADMIN. CODE: REPLACE WITH NEW THE BROKEN OR DEFECTIVE GLASS OF UPPER SASH OF WINDOW IN THE KITCHEN LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST

## Order 553: 553 - CLEANSE

- Category (dictionary): CLEANING; cited section (most common in samples): § 27-2011 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 24317 | 8627 | 1967-12-12 | 2026-11-19 | 0 | IN THE; BATHROOM; IN THE BATHROOM | 40 most recent (server-ordered) |
| B | 5 | 0 | 1973-10-01 | 1976-09-13 | 0 | THE EASTWING COMBUSTION CHAMBER.; SEWER WATER CELLAR REAR.; THE SEWER WATER CELLAR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2011 ADM CODE CLEANSE TO THE SATISFACTION OF THIS DEPARTMENT THE SOUTH AND WEST WALLS IN THE BATHROOM LOCATED AT APT C3, 3rd STORY, 2nd APARTMENT FROM WEST AT NORTH
- B: D26-11.03 ADM CODE CLEANSE TO THE SATISFACTION OF THIS DEPARTMENT THE EASTWING COMBUSTION CHAMBER.

## Order 806: 806 - REPLACE

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 4125 | 284 | 2000-01-01 | 2026-11-12 | 0 | COVER AT | 40 most recent (server-ordered) |
| B | 16493 | 1194 | 1999-11-21 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| C | 3516 | 191 | 1999-11-21 | 2026-11-04 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: REPLACE WITH NEW THE MISSING STOPPER AT WASH BASIN IN THE BATHROOM LOCATED AT APT 2ND, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2005 ADMIN. CODE: REPLACE WITH NEW THE MISSING STOPPER AT BATHTUB IN THE BATHROOM LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- C: § 27-2005 ADMIN. CODE: REPLACE WITH NEW THE MISSING SKYLIGHT AT THE CEILING IN THE 1st ROOM FROM EAST LOCATED AT APT 2 UPPER LEVEL, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST

## Order 577: 577 - INADEQUATE HOT WATER SUPPLY (VOLUME)

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2024 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 12400 | 2934 | 1970-08-17 | 2026-11-19 | 0 | BATHROOM | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 11628 | 3439 | 1975-05-16 | 2026-11-18 | 0 | IN THE ENTIRE APARTMENT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'ENTIRE APARTMENT' | 'FIXTURES' |
|---|---|---|---|
| B | 3 | 0 | 3 |
| C | 3 | 1 | 3 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2024 ADM CODE PROVIDE ADEQUATE SUPPLY OF HOT WATER FOR THE FIXTURES 2ND BATH FROM NORTH IN THE BATHROOM LOCATED AT B-ROOM S15C, 4th STORY, 2nd B-ROOM FROM SOUTH AT WEST
- C: § 27-2024 ADM CODE PROVIDE ADEQUATE SUPPLY OF HOT WATER FOR THE FIXTURES ...

## Order 567: 567 - REMOVE RODENT

- Category (dictionary): EXTERMINATION & RODENT ERADICATION; cited section (most common in samples): D26-13.03 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1999-09-28 | 1999-09-28 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1 | 0 | 1978-05-15 | 1978-05-15 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 23846 | 8782 | 1971-09-30 | 2026-11-19 | 0 | YARD; THROUGHOUT; RATS | 40 most recent (server-ordered) |

One sample per class:

- A: D26-13.03 ADM CODE ABATE THE NUISANCE CONSISTING OF RODENTS RATS AT CENTER NORTH CELLAR.
- B: D26-13.03 ADM CODE ABATE THE NUISANCE CONSISTING OF RODENTS 2ND STY FRONT EAST APT 1 KITCHEN. , SECTION '' ''
- C: 567 (C) § 27-2017, 27-2017.1, 27-2017.4, 27-2017.5, 27-2017.8, 27-2019, 27-2021 HMC: ABATE THE NUISANCE CONSISTING OF EVIDENCE OF RATS AND ALL UNDERLYING CAUSES CREATING THE PEST INFESTATIONS, BY USING INTEGRATED PEST MANAGEMENT (IPM), ELIMINATE ALL BURROW ENTRY AND PASSAGEWAYS, PEST NESTS, HOLES, G

## Order 883: 883 - REPAIR THE SOURCE AND ABATE THE WATER LEAK

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2026, 2027 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1691 | 613 | 2012-07-25 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| B | 15880 | 4533 | 2012-07-10 | 2026-11-19 | 0 |  | 40 most recent (server-ordered) |
| C | 2849 | 451 | 2012-07-10 | 2026-11-13 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK AT CEILING IN THE 5th ROOM FROM NORTH LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK AT THE CEILING CEILING IN THE BATHROOM LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- C: § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK AT CEILING IN THE 1st ROOM FROM EAST LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 807: 807 - LEAKY ROOF

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 15500 | 2897 | 1999-12-02 | 2026-11-18 | 0 | OVER; OVER CEILING; OVER CEILING IN THE | 40 most recent (server-ordered) |
| C | 3580 | 281 | 1999-12-01 | 2026-11-15 | 0 | REPAIR THE ROOF SO; THE ROOF SO THAT; THAT IT WILL NOT | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADMIN. CODE: REPAIR THE ROOF SO THAT IT WILL NOT LEAK ABOVE CEILING IN THE 1st ROOM FROM EAST AT SOUTH LOCATED AT APT 3, 3rd STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: § 27-2005 ADMIN. CODE: REPAIR THE ROOF SO THAT IT WILL NOT LEAK OVER CEILING IN THE KITCHEN LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 683: 683 - PROVIDE LIGHT - Not Less that 60 Watt incadescent

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): D26-19.05 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2 | 0 | 1984-03-26 | 1986-10-17 | 0 | STY PUBLIC; STY PUBLIC HALL FRONT.; VESTIBULE AND 1 STY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 18670 | 1763 | 1930-06-01 | 2026-11-18 | 0 | AT PUBLIC HALL; AT CEILING; FIXTURE | 40 most recent (server-ordered) |
| C | 1 | 0 | 1974-11-06 | 1974-11-06 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-19.05 ADM CODE PROVIDE ADEQUATE LIGHT OF NOT LESS THAN 60 WATTS INCANDESCENT OR EQUIVALENT ILLUMINATION 3 STY PUBLIC HALL.
- B: § 27-2039 ADM CODE PROVIDE ADEQUATE LIGHT OF NOT LESS THAN 60 WATTS INCANDESCENT OR EQUIVALENT ILLUMINATION ABOVE MAILBOX AT PUBLIC HALL 1ST STORY AT PUBLIC HALL, 1st STORY
- C: D26-19.05 ADM CODE PROVIDE ADEQUATE LIGHT OF NOT LESS THAN 60 WATTS INCANDESCENT OR EQUIVALENT ILLUMINATION PUBLIC HALL ALL STYS.

## Order 561: 561 - PAINT METAL

- Category (dictionary): PAINTING; cited section (most common in samples): § 27-2014 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 17946 | 3680 | 1970-05-25 | 2026-11-19 | 0 | AT FIRE ESCAPE; BALCONIES; BUILDING | 40 most recent (server-ordered) |
| B | 4 | 0 | 1974-06-12 | 1984-07-20 | 0 | FIRE ESCAPE ALL STORIES.; REAR FIRE ESCAPE ALL; FIRE ESCAPE AT FRONT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1 | 0 | 2019-05-22 | 2019-05-22 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2014 ADM CODE AND DEPT. RULES AND REGULATIONS. SCRAPE AND REMOVE RUST SCALES AND PAINT WITH 2 COATS OF PAINT ALL BALCONIES AT ALL STORIES AT BUILDING FRONT AT FIRE ESCAPE
- B: D26-12.03 ADM CODE AND DEPT. RULES AND REGULATIONS. SCRAPE AND REMOVE RUST SCALES AND PAINT WITH 2 COATS OF PAINT FIRE ESCAPE AT FRONT ALL STY.
- C: § 27-2014 ADM CODE AND DEPT. RULES AND REGULATIONS. SCRAPE AND REMOVE RUST SCALES AND PAINT WITH 2 COATS OF PAINT ALL PARTS AND BALCONYS AT BUILDING FRONT FIRE ESCAPE

## Order 576: 576 - INADEQUATE COLD WATER

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2024 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 467 | 96 | 1971-01-30 | 2026-11-18 | 0 | WASH BASIN | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 9542 | 2117 | 1974-05-13 | 2026-11-19 | 0 | VOLUME | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 7773 | 2348 | 1973-11-08 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2024 ADM CODE PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES AT ALL PLUMBING FIXTURES IN THE ENTIRE APARTMENT LOCATED AT APT 1M, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2024 ADM CODE PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES ALL COLD WATER FIXTURES IN THE ENTIRE APARTMENT LOCATED AT APT 16A, 16th STORY, 4th APARTMENT FROM SOUTH AT WEST
- C: § 27-2024 ADM CODE PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES ...

## Order 826: 826 - REMOVE ILLEGAL FASTENING

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 1545 | 140 | 2000-01-12 | 2026-11-14 | 0 | LOCK AT; DOUBLE CYLINDER LOCK AT | 40 most recent (server-ordered) |
| C | 14194 | 660 | 1999-12-02 | 2026-11-06 | 0 | INSTALLED ON; LOCK INSTALLED ON; DOUBLE CYLINDER LOCK INSTALLED | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADMIN. CODE: REMOVE THE ILLEGAL FASTENING CONSISTING OF KEY OPERATED DOUBLE CYLINDER LOCK INSTALLED ON LOT LINE GATE, BUILDING FRONT , 1st STORY
- C: § 27-2005 ADMIN. CODE: REMOVE THE ILLEGAL FASTENING DOUBLE CYLINDER KEY OPERATED LOCK INSTALLED AT BUILDING ENTRANCE STORM METAL DOOR AT PUBLIC HALL, 1st STORY

## Order 809: 809 - SECURE LOOSE MATTER

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1947 | 194 | 2000-02-07 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| B | 12695 | 1305 | 1999-11-23 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| C | 990 | 149 | 2000-01-03 | 2026-11-14 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: PROPERLY SECURE THE LOOSE WOOD BASE MOLDING AT EAST WALL IN THE 1st ROOM FROM EAST AT SOUTH LOCATED AT APT 1STFLO UPPER LEVEL, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2005 ADMIN. CODE: PROPERLY SECURE THE LOOSE HANDRAIL AT PUBLIC HALL STAIRS, 1st STORY
- C: § 27-2005 ADMIN. CODE: PROPERLY SECURE THE LOOSE BRICK AND MORTAR AT BUILDING FRONT AT BASEMENT LEVEL

## Order 879: 879 - REPAIR LEAKY FAUCETS

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2026 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 962 | 114 | 2000-02-18 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| B | 12369 | 1735 | 1999-11-22 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| C | 647 | 107 | 2000-01-24 | 2026-11-11 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADMIN. CODE: REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS AT WASHBASIN IN THE BATHROOM LOCATED AT APT 1STFLO UPPER LEVEL, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2026 ADMIN. CODE: REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS FAUCET AT SINK IN THE KITCHEN LOCATED AT APT 2, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST , SECTION ''730''
- C: § 27-2026 ADMIN. CODE: REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS AT WASHBASIN IN THE BATHROOM LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 106: 106 - PROVIDE SHOE FOR DROP LADDER

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 13903 | 4854 | 1972-09-21 | 2026-11-18 | 0 | AT FIRE ESCAPE; EXTERIOR WALL; NUTS AND BOLTS | 40 most recent (server-ordered) |
| B | 2 | 0 | 1983-04-25 | 1987-11-30 | 0 | FIRE ESCAPE AT EAST.; REAR FIRE ESCAPE. | 2 most recent (server-ordered) |

One sample per class:

- A: § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS. PROVIDE A SHOE PROPERLY SECURED TO BOTTOM OF STRING OF DROPLADDER (SHOE) PROPERLY SECURE BY USING APPROPRIATE NUTS AND BOLTS AT NORTH EXTERIOR WALL (RESIDENCE FRONT) AT FIRE ESCAPE
- B: SECTION 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS. PROVIDE A SHOE PROPERLY SECURED TO BOTTOM OF STRING OF DROPLADDER FIRE ESCAPE AT EAST.

## Order 513: 513 - F/E ADJUST THE DROP LADDER

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 10034 | 2084 | 1974-03-04 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 3790 | 1101 | 1975-04-24 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. ADJUST THE DROPLADDER SO THAT IT WILL SLIDE EASILY IN THE GUIDE RODS ...
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. ADJUST THE DROPLADDER SO THAT IT WILL SLIDE EASILY IN THE GUIDE RODS ..

## Order 512: 512 - FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN

- Category (dictionary): EGRESS; cited section (most common in samples): D26-10.01 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1980-10-03 | 1980-10-03 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 3781 | 805 | 1967-12-27 | 2026-11-17 | 0 | BALCONY AT 1ST FIRE; FROM EAST AT NORTH | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 9487 | 1902 | 1974-06-24 | 2026-11-19 | 0 | SUPPORT BRACKET; 10 METAL TREAD; AT SOUTH | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: D26-10.01 ADM CODE FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN, DEFECTIVE AND/OR MISSING BOLTS FOOT OF GOOSENECK LADDER REAR FIRE ESCAPE.
- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN, DEFECTIVE AND/OR MISSING 11TH METAL TREAD FROM BOTTOM AND UP AT 2ND FIRE ESCAPE FROM WEST [ BUILDING FRONT ] AT 2ND STORY BALCONY
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN, DEFECTIVE AND/OR MISSING 10 METAL TREAD FROM BOTTOM UP AT TH3 1ST FIRE ESCAPE FROM EAST AT SOUTH AT FIRE ESCAPE, 2nd STORY

## Order 1042: 1042 - NO GAS

- Category (dictionary): KITCHEN AND KITCHENETTES; cited section (most common in samples): § 27-2073 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 4915 | 380 | 1999-12-17 | 2026-11-18 | 0 |  | 40 most recent (server-ordered) |
| C | 8176 | 1253 | 1999-12-13 | 2026-11-19 | 0 | PROVIDE AN ADEQUATE SUPPLY; ADEQUATE SUPPLY OF GAS; AN ADEQUATE SUPPLY OF | 40 most recent (server-ordered) |

Probe counts (sampled descriptions containing the phrase):

| Class | Sampled | 'NO GAS' | 'ENTIRE APARTMENT' |
|---|---|---|---|
| B | 40 | 3 | 8 |
| C | 40 | 1 | 5 |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2073 ADM CODE - PROVIDE AN ADEQUATE SUPPLY OF GAS TO THE FIXTURES RANGE IN THE ENTIRE APARTMENT LOCATED AT APT HOUSE, 1st STORY, 1st APARTMENT FROM NORTH AT EAST
- C: § 27-2073 ADM CODE - PROVIDE AN ADEQUATE SUPPLY OF GAS TO THE FIXTURES NO GAS SPPLY TO GAS RANGE IN THE KITCHEN LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 765: 765 - VACATED APARTMENT(S)

- Category (dictionary): ORDER TO REPAIR/VACATE ORDER; cited section (most common in samples): § 27-2142 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 6 | 0 | 2001-07-12 | 2002-06-11 | 0 | ILLEGALLY CREATED AT CELLAR; FRONT AND REAR CELLAR; AND REAR CELLAR APT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| I | 12467 | 3456 | 1976-08-24 | 2026-11-19 | 0 | VACATE; APARTMENT; IN THE ENTIRE APARTMENT | 40 most recent (server-ordered) |

One sample per class:

- A: § 27-2142 ADM CODE APTS HAVE BEEN VACATED BY THIS DEPARTMENT AND CANNOT BE REOCCUPIED UNTIL SO ORDERED AFTER PROOF OF COMPLIANCE FOR APTS ILLEGALLY CREATED AT CELLAR
- I: § 27-2142 ADM CODE APTS HAVE BEEN VACATED BY THIS DEPARTMENT AND CANNOT BE REOCCUPIED UNTIL SO ORDERED AFTER PROOF OF COMPLIANCE FOR APTS ; APARTMENT # 12L, VACATE ORDER # 261380, DATE: 11/19/2026 IN THE ENTIRE APARTMENT LOCATED AT APT, 12th STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 988: 988 - PROVIDE SUPPLY OF ELECTRICTY TO FIXTURES

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2037, 2038 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 183 | 34 | 2012-07-12 | 2026-11-14 | 0 |  | 40 most recent (server-ordered) |
| B | 5118 | 1082 | 2012-07-09 | 2026-11-16 | 0 |  | 40 most recent (server-ordered) |
| C | 5254 | 1201 | 2012-07-09 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES CEILING LIGHT FIXTURE IN THE 4th ROOM FROM NORTH LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES TO ALL ELECTRICAL OUTLETS, SWITCHES AND LIGHT FIXTURES IN THE 1st ROOM FROM EAST AT NORTH LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES AND OUTLETS IN THE ENTIRE APARTMENT LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 551: 551 - REMOVE ACCUMULATION OF RUBBISH, WATER & DISINFECT

- Category (dictionary): CLEANING; cited section (most common in samples): § 27-2010, 2011, 2012 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 3 | 0 | 2000-02-28 | 2001-06-23 | 0 | HOUSEHOLD TRASH AT PUBLIC; THE HOUSEHOLD TRASH AT; PUBLIC HALL 5TH STORY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 6213 | 1335 | 1967-07-12 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 3407 | 726 | 1973-11-26 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2010, 2011, 2012 ADM CODE CLEANSE AND DISINFECT TO THE SATISFACTION OF THIS DEPARTMENT AFTER REMOVING THE HOUSEHOLD TRASH AT PUBLIC HALL, 5th STORY
- B: § 27-2010, 2011, 2012 ADM CODE CLEANSE AND DISINFECT TO THE SATISFACTION OF THIS DEPARTMENT AFTER REMOVING THE 1ST STORY AT FIRE PASSAGE WAY, 1st STORY
- C: § 27-2010, 2011, 2012 ADM CODE CLEANSE AND DISINFECT TO THE SATISFACTION OF THIS DEPARTMENT AFTER REMOVING THE 1 FOOT DEEP STAGNANT WATER AT BASEMENT (BOILER ROOM)

## Order 898: 898 - REPAIR BROKEN, LOOSE CONNECTION

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 277 | 38 | 2000-06-15 | 2026-10-27 | 0 |  | 40 most recent (server-ordered) |
| B | 7429 | 917 | 1999-12-26 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| C | 1157 | 144 | 1999-12-30 | 2026-11-15 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADMIN. CODE: REPAIR THE BROKEN OR DEFECTIVE CONNECTION WASTE LINE AT WASHBASIN IN THE BATHROOM LOCATED AT APT 1, 1st STORY, 2nd APARTMENT FROM EAST AT SOUTH
- B: § 27-2026 ADMIN. CODE: REPAIR THE BROKEN OR DEFECTIVE CONNECTION AT WASTE LINE UNDER SINK IN THE KITCHENETTE LOCATED AT APT B, 2nd STORY, 2nd APARTMENT FROM WEST AT NORTH
- C: § 27-2026 ADMIN. CODE: REPAIR THE BROKEN OR DEFECTIVE CONNECTION AT DRAINLINE AT SINK IN THE KITCHEN LOCATED AT APT 1STFLO, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 877: 877 - INADEQUATE HOT WATER SUPPLY (VOLUME)

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2024 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 3238 | 397 | 1999-12-01 | 2026-11-14 | 0 | IN THE KITCHEN; SINK IN THE KITCHEN; AT SINK IN THE | 40 most recent (server-ordered) |
| C | 5448 | 1054 | 2001-10-24 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2024 ADMIN. CODE: PROVIDE ADEQUATE SUPPLY OF HOT WATER FOR THE FIXTURES AT SINK IN THE KITCHEN LOCATED AT APT 400, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2024 ADMIN. CODE: PROVIDE ADEQUATE SUPPLY OF HOT WATER FOR THE FIXTURES , IN THE ENTIRE APARTMENT LOCATED AT APT 1F, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 658: 658 - REPAIR BROKEN PAYING

- Category (dictionary): PAVING AND GRADING; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1640 | 46 | 1909-11-12 | 2026-11-11 | 0 | AT WEST; COURT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 6194 | 496 | 1974-03-08 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 836 | 203 | 1976-01-18 | 2026-11-16 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING AT 2ND COURT FROM SOUTH AT WEST
- B: § 27-2005 ADM CODE PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING 3RD, 4TH, AND 5TH CONCRETE TREADS UP FROM BOTTOM AT BUILDING FRONT LEADING TO DOORWAY
- C: § 27-2005 ADM CODE PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING 100 SQUARE FEET THROUGH-OUT CONCRETE FLOOR AT CELLAR

## Order 852: 852 - REMOVE ACCUMULATION OR RUBBISH

- Category (dictionary): CLEANING; cited section (most common in samples): § 27-2010, 2011, 2012 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 652 | 111 | 2000-05-19 | 2026-11-16 | 0 |  | 40 most recent (server-ordered) |
| B | 7136 | 688 | 2000-01-11 | 2026-11-15 | 0 |  | 40 most recent (server-ordered) |
| C | 814 | 58 | 1999-11-29 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2010, 2011, 2012 ADMIN. CODE: REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE NORTH AND SOUTH YARD YARD
- B: § 27-2010, 2011, 2012 ADMIN. CODE: REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE CONSISTING OF CARDBOARD BOXES, MATTRESSES, HOUSEHOLD FURNITURE, GARBAGE, AND ETC... YARD
- C: § 27-2010, 2011, 2012 ADMIN. CODE: REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE REAR YARD YARD

## Order 949: 949 - REMOVE OBSTRUCTIONS

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 6615 | 1131 | 1999-12-17 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| C | 1816 | 238 | 1999-12-06 | 2026-11-14 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2026 ADMIN. CODE: REMOVE ALL OBSTRUCTIONS AND REPAIR ALL DEFECTS IN WASTE LINE AT SINK IN THE KITCHEN LOCATED AT APT 1F, 1st STORY, 1st APARTMENT FROM WEST AT NORTH
- C: § 27-2026 ADMIN. CODE: REMOVE ALL OBSTRUCTIONS AND REPAIR ALL DEFECTS IN BATHTUB WASTELINE IN THE BATHROOM LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 578: 578 - REPAIR LEAKY PIPES

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2026 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 471 | 83 | 1967-03-30 | 2026-11-08 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 5694 | 1190 | 1974-09-24 | 2026-11-19 | 0 | LINE AT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1946 | 407 | 1973-11-13 | 2026-11-10 | 0 | ROOM; ROOM CELLAR. | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADM CODE REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE AT BATHTUB IN THE BATHROOM LOCATED AT APT 2C, 2nd STORY, 2nd APARTMENT FROM WEST AT NORTH
- B: § 27-2026 ADM CODE REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE A COLD LINE AT WASHBASIN IN THE BATHROOM LOCATED AT APT 51B, 5th STORY, 1st APARTMENT FROM WEST AT NORTH , SECTION AT WEST
- C: § 27-2026 ADM CODE REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE ACTIVE LEAK AT LOWER CABINET AT WASHBASIN IN THE BATHROOM LOCATED AT APT 1D, 2nd STORY, 2nd APARTMENT FROM EAST AT SOUTH

## Order 703: 703 - FILE CERTIFICATION SMOKE DETECTOR - DO NOT USE, RULE REVISED

- Category (dictionary): RETIRED; cited section (most common in samples): § 27-2045, 2046 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 7786 | 1 | 1982-01-20 | 2024-08-12 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 58 | 13 | 2017-11-13 | 2026-08-12 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 7 | 1 | 2019-08-07 | 2025-09-10 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2045, 2046 ADM CODE FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF SMOKE DETECTING DEVICE IN ACCORDANCE WITH H.P.D. RULES AND REGULATIONS.
- B: § 27-2045, 2046 ADM CODE FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF SMOKE DETECTING DEVICE IN ACCORDANCE WITH H.P.D. RULES AND REGULATIONS. AT PUBLIC HALL, 1st STORY
- C: § 27-2045, 2046 ADM CODE FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF SMOKE DETECTING DEVICE IN ACCORDANCE WITH H.P.D. RULES AND REGULATIONS. IN THE ENTIRE APARTMENT LOCATED AT APT 6D, 6th STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 690: 690 - NO PEEP HOLE

- Category (dictionary): PROTECTIVE DEVICES AND FIRE PROTECTION; cited section (most common in samples): § 27-2041 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 6629 | 628 | 1967-11-28 | 2026-11-18 | 0 | MISSING IN THE ENTRANCE; THAT IS MISSING IN; IS MISSING IN THE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 2 | 0 | 1974-01-04 | 1988-09-02 | 0 | ALL; ENTRANCE DOORS ALL STYS.; ALL ENTRANCE DOORS ALL | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2041 ADM CODE PROVIDE A PEEP HOLE IN ENTRANCE DOOR OF THE DWELLING UNIT SO LOCATED SO AS TO PERMIT A PERSON INSIDE THE DWELLING TO VIEW ANY PERSON OUTSIDE ENTRANCE DOOR ..
- B: D26-20.01 ADM CODE PROVIDE A PEEP HOLE IN ENTRANCE DOOR OF THE DWELLING UNIT SO LOCATED SO AS TO PERMIT A PERSON INSIDE THE DWELLING TO VIEW ANY PERSON OUTSIDE ENTRANCE DOOR 1 & 2 STY ALL APTS.

## Order 495: 495 - FILE PLANS & OBTAIN CERTIFICATE OF OCCUPANCY OR RESTORE

- Category (dictionary): HOTEL AND CERTAIN OTHER CLASS A & CLASS B DWELLINGS; cited section (most common in samples): § 300, 301, 302, M/D LAW
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 6 | 0 | 1975-05-14 | 1981-04-28 | 0 | USED; USED AS | 6 most recent (server-ordered) |
| B | 6344 | 357 | 1959-10-04 | 2026-11-18 | 0 | APARTMENT; CLASS; ILLEGAL | 40 most recent (server-ordered) |
| C | 3 | 0 | 1984-06-15 | 1989-06-23 | 0 | STY FRONT; PARTITIONS ERECTED; ROOMS | 3 most recent (server-ordered) |

One sample per class:

- A: § 300, 301, 302, M/D LAW FILE PLANS AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE THE FOLLOWING ALTERATION OR RESTORE PREMISES TO PRIOR LEGAL CONDITION CELLAR AT SOUTHWEST ALTERED TO BUSINESS USE IN CONJUNCTION WITH 1 STY STORE.
- B: § 300, 301, 302, M/D LAW FILE PLANS AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE THE FOLLOWING ALTERATION OR RESTORE PREMISES TO PRIOR LEGAL CONDITION 5 STORY 24 FAMILY MULTIPLE DWELLING, ILLEGALLY CONVERTED TO 25 FAMILY WHEN INCLUDING ILLEGAL CLASS-A APARTMENT AT CELLAR
- C: § 300, 301, 302, M/D LAW FILE PLANS AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE THE FOLLOWING ALTERATION OR RESTORE PREMISES TO PRIOR LEGAL CONDITION CELLAR PARTITIONS ERECTED CREATING 7 ROOMS PLUMBING FIXTURES INSTALLED.

## Order 514: 514 - F/E DEFECTIVE: PROPERLY SECURE

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 1834 | 221 | 1970-04-22 | 2026-09-12 | 0 | BALCONY AT; 2ND STORY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 4464 | 312 | 1973-10-18 | 2026-11-09 | 0 | STACK | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. PROPERLY SECURE 12TH TREAD UP FROM BALCONY AT NORTH WALL AT FIRE ESCAPE, 2nd STORY
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. PROPERLY SECURE 10TH AND 11TH TREADS FROM BOTTOM AT EAST AT FIRE ESCAPE, 3rd STORY

## Order 876: 876 - INADEQUATE COLD WATER

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2024 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 63 | 8 | 2001-02-02 | 2026-10-15 | 0 |  | 40 most recent (server-ordered) |
| B | 2299 | 316 | 2000-01-19 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| C | 3710 | 695 | 1999-12-19 | 2026-11-12 | 0 | WATER | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2024 ADMIN. CODE: PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES .. IN THE BATHROOM LOCATED AT BSMT-APT PH, 1st BSMT-APT FROM WEST AT NORTH
- B: § 27-2024 ADMIN. CODE: PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES NO SUPPLY OF COLD WATER AT BATHTUB AT UPPER LEVEL IN THE BATHROOM LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM NORTH AT EAST
- C: § 27-2024 ADMIN. CODE: PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES AT KITCHEN AND BATHROOM IN THE ENTIRE APARTMENT LOCATED AT APT 3, 3rd STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 721: 721 - PROVIDE A JANITOR

- Category (dictionary): JANITORIAL SERVICES; cited section (most common in samples): § 27-2053 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 4516 | 792 | 1970-05-04 | 2026-11-19 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1088 | 35 | 1974-01-11 | 2026-08-07 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2053 ADM CODE PROVIDE DWELLING WITH A JANITOR OR RESPONSIBLE PERSON OR JANITORIAL SERVICE.
- C: § 27-2053 ADM CODE PROVIDE DWELLING WITH A JANITOR OR RESPONSIBLE PERSON OR JANITORIAL SERVICE.

## Order 687: 687 - INADEQUATE LIGHTING IN YARD OR COURT

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2040 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 761 | 3 | 1967-11-28 | 2024-12-01 | 0 | AT EAST | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 4809 | 69 | 1974-01-14 | 2026-10-29 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2040 ADM CODE INSTALL AND MAINTAIN SUFFICIENT LIGHT OR LIGHTS OF AT LEAST 100 WATTS INCANDESCENT OR EQUIVALENT EACH, TO LIGHT ADEQUATELY FROM SUNSET TO SUNRISE THE AT COURTYARD
- B: § 27-2040 ADM CODE INSTALL AND MAINTAIN SUFFICIENT LIGHT OR LIGHTS OF AT LEAST 100 WATTS INCANDESCENT OR EQUIVALENT EACH, TO LIGHT ADEQUATELY FROM SUNSET TO SUNRISE THE ...

## Order 761: 761 - DISCONTINUE ROOMS AT CELLAR

- Category (dictionary): ILLEGAL OCCUPANCY OF BASEMENT AND CELLARS; cited section (most common in samples): § 27-2081 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 5513 | 556 | 1971-12-27 | 2026-11-18 | 0 | PLASTERBOARD CREATING ROOMS CELLAR; STUDS PLASTERBOARD CREATING ROOMS; WOOD STUDS PLASTERBOARD CREATING | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1 | 0 | 1984-06-15 | 1984-06-15 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- B: § 27-2081 ADM CODE DISCONTINUE USE OF ROOMS FOR LIVING, DISCONNECT PLUMBING FIXTURES AND PROPERLY SEAL PIPE CONNECTIONS ..
- C: D26-34.01 ADM CODE DISCONTINUE USE OF ROOMS FOR LIVING, DISCONNECT PLUMBING FIXTURES AND PROPERLY SEAL PIPE CONNECTIONS CELLAR USED FOR SLEEPING.

## Order 693: 693 - SELF-CLOSING DOORS

- Category (dictionary): PROTECTIVE DEVICES AND FIRE PROTECTION; cited section (most common in samples): § 27-2044 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 1852 | 0 | 1967-11-09 | 2019-06-10 | 0 | STY; ENTRANCE 2 STY NORTH; WEST ENTRANCE 2 STY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 3242 | 1342 | 2019-06-14 | 2026-11-19 | 0 | 1ST STORY; DOOR; DEFECTIVE SECONDARY ENTRANCE DOOR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- B: § 27-2044 ADM CODE ARRANGE AND MAKE SELF-CLOSING THE DOORS 1 STY APT 2
- C: § 27-2044, 2041.1 HMC: §238 MDL and 28 RCNY §25-171: REPLACE OR REPAIR THE SELF-CLOSING THE DOORS THAT IS MISSING OR DEFECTIVE .. , 1st STORY

## Order 989: 989 - REPAIR/ABATE UNSAFE WIRES

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2005, 2006, 2037 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 137 | 36 | 2012-07-23 | 2026-11-14 | 0 |  | 40 most recent (server-ordered) |
| B | 3786 | 720 | 2012-07-11 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| C | 860 | 177 | 2012-07-26 | 2026-11-14 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF EXPOSED ELECTRICAL WIRING AT NORTH WALL IN THE 4th ROOM FROM NORTH LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF EXPOSED ELECTRICAL WIRING AT CEILING AT CELLAR LEVEL AT BOILER ROOM
- C: § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF EXPOSED ELECTRICAL WIRING AT CEILING IN THE 3rd ROOM FROM NORTH LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 1051: 1051 - DISCONTINUE ROOMING UNIT

- Category (dictionary): MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS; cited section (most common in samples): § 27-2077 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 137 | 11 | 2000-01-24 | 2026-07-21 | 0 |  | 40 most recent (server-ordered) |
| B | 4509 | 403 | 2000-01-10 | 2026-11-16 | 0 | DISCONTINUE THE ROOMING UNIT | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2077 ADM CODE - DISCONTINUE THE ROOMING UNIT ILLEGAL B-ROOM (NORTH 3) CREATED , 1st STORY
- B: § 27-2077 ADM CODE - DISCONTINUE THE ROOMING UNIT OCCUPIED BY ONE ADULT IN THE 5th ROOM FROM EAST AT NORTH LOCATED AT APT 2, 2nd STORY

## Order 893: 893 - REPAIR FLUSHING APPARATUS OF WATER CLOSET

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 290 | 49 | 2000-06-20 | 2026-11-13 | 0 |  | 40 most recent (server-ordered) |
| B | 3558 | 364 | 1999-12-02 | 2026-11-14 | 0 |  | 40 most recent (server-ordered) |
| C | 360 | 53 | 1999-11-21 | 2026-10-28 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADMIN. CODE: REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET IN THE BATHROOM LOCATED AT APT 2NDFLO, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2026 ADMIN. CODE: REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET IN THE BATHROOM LOCATED AT APT 400, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2026 ADMIN. CODE: REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET .. IN THE BATHROOM LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 804: 804 - PROVIDE

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 218 | 16 | 2000-07-31 | 2026-10-16 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 961 | 85 | 2000-01-10 | 2026-10-21 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 2707 | 34 | 1999-12-16 | 2026-07-15 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: PROVIDE APPROVED TYPE MESH AT SKYLIGHT AT PUBLIC HALL, 2nd STORY
- B: § 27-2005 ADMIN. CODE: PROVIDE ACCEPTABLE MECHANICAL HEAVY DUTY LOCK AND LATCH SET AT FRONT ENTRANCE DOOR TO BUILDING , 1st STORY
- C: § 27-2005 ADMIN. CODE: PROVIDE CAP (GAS VAVLE/LINE) AT EAST WALL (BASEMENT AT BASEMENT

## Order 1492: 1492 - FILE PLANS & OBTAIN C/O TO LEGALIZE CONVERSION FROM PD TO MD

- Category (dictionary): CONVERSIONS; cited section (most common in samples): § 9, 170, 171, 300, 301, 302 M.D.LAW
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 372 | 33 | 2000-01-12 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| B | 3077 | 356 | 1999-12-22 | 2026-11-09 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 9, 170, 171, 300, 301, 302 M.D.LAW-FILE PLANS AND APPLICATION AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE THE CONVERSION FROM A PRIVATE DWELLING TO MULTIPLE DWELLING USE IF LAWFULLY FEASIBLE OR RESTORE TO LAWFUL OCCUPANCY
- B: § 9, 170, 171, 300, 301, 302 M.D.LAW-FILE PLANS AND APPLICATION AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE THE CONVERSION FROM A PRIVATE DWELLING TO MULTIPLE DWELLING USE IF LAWFULLY FEASIBLE OR RESTORE TO LAWFUL OCCUPANCY

## Order 684: 684 - PROVIDE Adequate LIGHT

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): D26-19.01 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2 | 0 | 1979-07-18 | 1989-07-25 | 0 | PROOF PASSAGE AT NORTH.; FIRE PROOF PASSAGE AT; CELLAR THROUGHOUT. | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 3099 | 552 | 1966-01-31 | 2026-11-18 | 0 | FIRE PASSAGEWAY; WEST | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-19.01 ADM CODE PROVIDE ADEQUATE LIGHTING CELLAR THROUGHOUT.
- B: § 27-2037 ADM CODE PROVIDE ADEQUATE LIGHTING 10TH STORY COMPACTOR CLOSET

## Order 503: 503 - STRUCTURAL DEFECT

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 516 | 91 | 1970-03-22 | 2026-10-28 | 0 |  | 40 most recent (all-rows-client-sorted) |
| C | 2485 | 424 | 1973-06-06 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE MAKE SAFE BY PROPERLY REPAIRING THE STRUCTURAL DEFECT VERTICAL CRACKS FROM 3RD STORY WINDOW TO PARAPET WALL AT EAST EXTERIOR WALL
- C: § 27-2005 ADM CODE MAKE SAFE BY PROPERLY REPAIRING THE STRUCTURAL DEFECT NORTH EXTERIOR WALL FROM 5TH STORY UP TO PARAPIT WALL

## Order 896: 896 - REPLACE DEFECTIVE SINK, WATER CLOSET, WASH TUB

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 159 | 14 | 2000-07-28 | 2026-11-15 | 0 |  | 40 most recent (server-ordered) |
| B | 2195 | 283 | 2000-01-20 | 2026-11-17 | 0 |  | 40 most recent (server-ordered) |
| C | 441 | 84 | 2000-05-22 | 2026-10-14 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADMIN. CODE: REPLACE THE BROKEN OR DEFECTIVE WASH BASIN IN THE BATHROOM LOCATED AT APT 3, 3rd STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2026 ADMIN. CODE: REPLACE THE BROKEN OR DEFECTIVE BATHTUB IN THE BATHROOM LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- C: § 27-2026 ADMIN. CODE: REPLACE THE BROKEN OR DEFECTIVE BATHTUB IN THE BATHROOM LOCATED AT APT 83A UPPER LEVEL, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 226: 226 - PROVIDE ENCLOSURE AT

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): SECTION 65 M/D LAW
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 7 | 0 | 1973-11-28 | 1988-08-29 | 0 | REAR. | 7 most recent (server-ordered) |
| B | 2751 | 26 | 1919-06-06 | 2026-09-09 | 0 | CELLAR; AT CELLAR | 40 most recent (server-ordered) |
| C | 1 | 0 | 1984-05-24 | 1984-05-24 | 0 |  | 1 most recent (server-ordered) |

One sample per class:

- A: SECTION 65 M/D LAW PROVIDE UNDER COMPLETED PERMIT, A PROPER ENCLOSURE FOR THE CENTRAL HEATING PLANT, CELLAR FRONT.
- B: § 65 M/D LAW PROVIDE UNDER COMPLETED PERMIT, A PROPER ENCLOSURE FOR THE CENTRAL HEATING PLANT, BOILER ROOM AT CELLAR
- C: § 65 M/D LAW PROVIDE UNDER COMPLETED PERMIT, A PROPER ENCLOSURE FOR THE CENTRAL HEATING PLANT, CELLAR REAR.

## Order 851: 851 - REMOVE ACCUMULATION OF RUBBISH, WATER & DISINFECT

- Category (dictionary): CLEANING; cited section (most common in samples): § 27-2010,2011,2012 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 843 | 52 | 2000-01-06 | 2026-10-20 | 0 |  | 40 most recent (server-ordered) |
| C | 1390 | 77 | 1999-12-13 | 2026-11-05 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2010,2011,2012 ADMIN. CODE: CLEANSE AND DISINFECT TO THE SATISFACTION OF THIS DEPARTMENT AFTER REMOVING THE STAGNANT WATER AT CELLAR FLOOR
- C: § 27-2010,2011,2012 ADMIN. CODE: CLEANSE AND DISINFECT TO THE SATISFACTION OF THIS DEPARTMENT AFTER REMOVING THE STAGNANT WATER AT CELLAR

## Order 599: 599 - MAKE GAS TIGHT

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 238 | 0 | 1971-01-07 | 2023-07-26 | 0 | BASE/SINK IN THE BATHROOM; WATER SUPLAY VALVE COLD; SUPLAY VALVE COLD WATER | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1848 | 16 | 1974-03-15 | 2026-06-22 | 0 | LINE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1 | 0 | 1975-05-01 | 1975-05-01 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2026 ADM CODE REPAIR BY CLOSING SO AS TO BE GAS TIGHT ALL OPENINGS IN THE AT SINK WASTE PIPE IN THE KITCHEN LOCATED AT APT 1P, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH
- B: § 27-2026 ADM CODE REPAIR BY CLOSING SO AS TO BE GAS TIGHT ALL OPENINGS IN THE AT DRAINLINE AT SINK IN THE KITCHEN LOCATED AT APT 4, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: D26-16.01 ADM CODE REPAIR BY CLOSING SO AS TO BE GAS-TIGHT ALL OPENINGS IN THE WASTE PIPE OF BATHTUB BASEMENT APT BATHROOM.

## Order 549: 549 - REMOVE EXCESSIVE STORAGE

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005, 2012 HMC & § 309 MDL
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 1337 | 443 | 2015-04-01 | 2026-11-18 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 705 | 156 | 2015-03-31 | 2026-11-16 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005, 2012 HMC & § 309 MDL: ABATE THE NUISANCE CONSISTING OF EXCESSIVE STORAGE OF MATERIAL ACCUMULATION OF HOUSE HOLD ITEMS. FROM FLOOR TO CEILING IN THE ENTIRE APARTMENT LOCATED AT APT 2O, 2nd STORY, 3rd APARTMENT FROM SOUTH AT WEST
- C: § 27-2005, 2012 HMC & § 309 MDL: ABATE THE NUISANCE CONSISTING OF EXCESSIVE STORAGE OF MATERIAL ACCUMULATION OF BAGS AND HOUSEHOLD ARTICLES OBSTRUCTING ELDERLY TENANT FROM GETTING TO FIRE ESCAPE IN THE ENTIRE APARTMENT LOCATED AT APT 3RN, 3rd STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 753: 753 - DISCONTINUE SINGLE ROOM OCCUPANCY

- Category (dictionary): MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS; cited section (most common in samples): § 27-2077, 2078 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 1919 | 339 | 1974-12-30 | 2026-09-25 | 0 | IN THE; IN THE ENTIRE APARTMENT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1 | 0 | 1974-05-16 | 1974-05-16 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- B: § 27-2077, 2078 ADM CODE DISCONTINUE UNLAWFUL USE FOR SINGLE ROOM OCCUPANCY PURPOSES 1 ADULT IN THE 1st ROOM FROM EAST AT NORTH LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH
- C: D26-33.07 & 33.09 ADM CODE DISCONTINUE UNLAWFUL USE FOR SINGLE ROOM OCCUPANCY PURPOSES 3 STY AND 2 STY RENTING OUT IN ROOMS COMMUNITY BATHROOM & KITCHEN.

## Order 535: 535 - REMOVE FLOOR COVERING

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 524 | 37 | 1967-12-12 | 2026-11-17 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1263 | 244 | 1973-11-14 | 2026-11-15 | 0 | FLOOR; FLOOR IN THE; COVERING | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADM CODE REMOVE THE TORN AND/OR LOOSE FLOOR COVERING AT ELEVATOR
- B: § 27-2005 ADM CODE REMOVE THE TORN AND/OR LOOSE FLOOR COVERING 10 SQ FT AT FLOOR IN THE 3rd ROOM FROM EAST LOCATED AT APT 5H, 5th STORY, 3rd APARTMENT FROM WEST AT NORTH

## Order 573: 573 - POST A SIGN

- Category (dictionary): POSTING/SIGNAGE; cited section (most common in samples): § 27-2022 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1768 | 1068 | 1975-08-25 | 2026-11-16 | 0 | YARD; YARD 1ST STORY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1 | 0 | 1990-03-02 | 1990-03-02 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2022 ADM CODE POST A SIGN INDICATING HOURS OF COLLECTION AND METHOD OF COLLECTION OF WASTE MATERIAL WHERE DUMBWAITER SERVICE IS NOT PROVIDED.
- B: D26-14.05 ADM CODE POST A SIGN INDICATING HOURS OF COLLECTION AND METHOD OF COLLECTION OF WASTE MATERIAL WHERE DUMBWAITER SERVICE IS NOT PROVIDED.

## Order 713: 713 - PROVIDE HOSE AND PAIL

- Category (dictionary): SPRINKLER SYSTEM; cited section (most common in samples): D26-21.07 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1979-03-02 | 1979-03-02 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1739 | 116 | 1968-09-13 | 2026-11-04 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-21.07 ADM CODE PROVIDE A PIECE OF GARDEN HOSE 10 FEET IN LENGTH WITH FEMALE COUPLING AND A 10 QUART PAIL ON PREMISES TO TEST SPRINKLER SYSTEM.
- B: § 27-2050 ADM CODE PROVIDE A PIECE OF GARDEN HOSE 10 FEET IN LENGTH WITH FEMALE COUPLING AND A 10 QUART PAIL ON PREMISES TO TEST SPRINKLER SYSTEM.

## Order 620: 620 - FAILURE TO PROVIDE TO THE DEPT. WITHIN 45 DAYS

- Category (dictionary): LEAD-BASED PAINT; cited section (most common in samples): § 27-2056.4(H) AND 27-2056.17 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 1 | 0 | 2019-05-09 | 2019-05-09 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1649 | 551 | 2019-05-17 | 2026-08-12 | 0 | INSPECTIONS AND REMEDIATION/ABATEMENT ACTIVITIES.; NOTICES INSPECTIONS AND REMEDIATION/ABATEMENT; LEAD-BASED PAINT NOTICES INSPECTIONS | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- B: § 27-2056.4(H) AND 27-2056.17 ADM CODE -CORRECT FAILURE TO PROVIDE TO THE DEPARTMENT WITHIN 45 DAYS OF DEMAND ALL RECORDS REQUIRED TO BE MAINTAINED BY OWNER PURSUANT TO LOCAL LAW 1 OF 2004 RELATED TO LEAD-BASED PAINT NOTICES, INSPECTIONS AND REMEDIATION/ABATEMENT ACTIVITIES.
- C: § 27-2056.4(H) AND 27-2056.17 ADM CODE -CORRECT FAILURE TO PROVIDE TO THE DEPARTMENT WITHIN 45 DAYS OF DEMAND ALL RECORDS REQUIRED TO BE MAINTAINED BY OWNER PURSUANT TO LOCAL LAW 1 OF 2004 RELATED TO LEAD-BASED PAINT NOTICES, INSPECTIONS AND REMEDIATION/ABATEMENT ACTIVITIES.

## Order 751: 751 - DISCONTINUE ROOMING UNIT

- Category (dictionary): MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS; cited section (most common in samples): § 27-2077 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 37 | 1 | 1986-06-13 | 2026-04-18 | 0 | APARTMENT CONVERTED FROM CLASS; IN CONJUNCTION WITH APARTMENT; ILLEGALLY USE IN CONJUNCTION | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1519 | 188 | 1985-01-03 | 2026-10-10 | 0 | AT SOUTH; EAST | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2077 ADM CODE DISCONTINUE THE ROOMING UNIT CREATED AT CELLAR ILLEGALLY USE IN CONJUNCTION WITH APARTMENT LOCATED AT APT 1R, 1st STORY, 1st APARTMENT FROM NORTH AT EAST
- B: § 27-2077 ADM CODE DISCONTINUE THE ROOMING UNIT 1 ADULT IN 1ST ROOM FROM EAST AT SOUTH AT CELLAR, SECTION ''FRONT''

## Order 714: 714 - O.S.Y. VALVE NOT SEALED IN OPEN POSITION

- Category (dictionary): SPRINKLER SYSTEM; cited section (most common in samples): D26-21.07 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2 | 0 | 1974-08-08 | 1979-03-02 | 0 | AT FRONT SOUTH.; CENTER. | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1386 | 102 | 1968-04-16 | 2026-11-04 | 0 | AT CELLAR; SPRINKLER SYSTEM IN ACCORDANCE; REGULATIONS OF THIS DEPARTMENT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-21.07 ADM CODE SEAL IN OPEN POSITION THE O.S.Y. VALVE OF THE SPRINKLER SYSTEM IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT CELLAR AT FRONT SOUTH.
- B: § 27-2050 ADM CODE SEAL IN OPEN POSITION THE O.S.Y. VALVE OF THE SPRINKLER SYSTEM IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT

## Order 878: 878 - REPAIR LEAKY PIPES

- Category (dictionary): WATER SUPPLY; cited section (most common in samples): § 27-2026 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 49 | 8 | 2000-07-06 | 2026-07-29 | 0 |  | 40 most recent (server-ordered) |
| B | 847 | 81 | 2000-03-16 | 2026-11-14 | 0 |  | 40 most recent (server-ordered) |
| C | 485 | 73 | 1999-11-23 | 2026-10-15 | 0 | AND/OR DEFECTIVE WATER SUPPLY; LEAKY AND/OR DEFECTIVE WATER; DEFECTIVE WATER SUPPLY PIPE | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2026 ADMIN. CODE: REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE AT WATER CLOSET IN THE BATHROOM LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2026 ADMIN. CODE: REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE UNDER SINK IN THE KITCHEN LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM NORTH AT EAST
- C: § 27-2026 ADMIN. CODE: REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE UNDER SINK IN THE KITCHEN LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH

## Order 675: 675 - ILLEGAL HEATER

- Category (dictionary): GAS APPLIANCES; cited section (most common in samples): D26-17.09, 18.01 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 3 | 0 | 1976-06-22 | 1990-06-25 | 0 | SPACE HEATER FRONT ROOM; STY WEST APT KITCHEN.; HEATER FRONT ROOM 1 | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 896 | 69 | 1971-07-22 | 2026-11-16 | 0 | WALL MOUNTED ELECTRICAL HEATING; MOUNTED ELECTRICAL HEATING UNIT; ELECTRICAL HEATING UNIT AT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 3 | 0 | 1988-09-15 | 1989-08-02 | 0 | SPARE HEATER S. SECTION; ROOM GAS SPARE HEATER; REAR ROOM GAS SPARE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-17.09, 18.01 ADM CODE DISCONTINUE USE OF ILLEGAL SPACE AND/OR HOT WATER HEATER AND PROVIDE EITHER APPROVED HEATER WHICH OBTAINS COMBUSTION AIR DIRECTLY FROM OUTSIDE THE BUILDING OR APPROVED CENTRAL SYSTEM 3RD STY WEST APT KITCHEN.
- B: § 27-2032, 2034 ADM CODE DISCONTINUE USE OF ILLEGAL SPACE AND/OR HOT WATER HEATER AND PROVIDE FILED FOR & APPROVED HEATER WHICH OBTAINS COMBUSTION AIR DIRECTLY FROM OUTSIDE THE BUILDING OR APPROVED CENTRAL SYSTEM ...
- C: D26-17.09, 18.01 ADM CODE DISCONTINUE USE OF ILLEGAL SPACE AND/OR HOT WATER HEATER AND PROVIDE EITHER APPROVED HEATER WHICH OBTAINS COMBUSTION AIR DIRECTLY FROM OUTSIDE THE BUILDING OR APPROVED CENTRAL SYSTEM 2ND STY REAR APT 2 REAR ROOM GAS SPARE HEATER S. , SECTION '' ''

## Order 176: 176 - PROVIDE FIREPROOF PASSAGE OR GATE IN FENCE

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): § 53,187,231 M/D LAW
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2 | 0 | 1978-12-04 | 1984-11-09 | 0 |  | 2 most recent (server-ordered) |
| B | 871 | 92 | 1972-11-29 | 2026-11-12 | 0 |  | 40 most recent (server-ordered) |
| C | 1 | 0 | 1987-11-18 | 1987-11-18 | 0 |  | 1 most recent (server-ordered) |

One sample per class:

- A: § 53,187,231 M/D LAW & DEPT RULES & REG. PROVIDE MEANS OF EGRESS FROM YARD TO STREET BY FIREPROOF PASSAGEWAY FOR WHICH APPLICATION MUST BE FILED FOR APPROVAL,OR BY UNLOCKED DOOR OR GATE IN FENCE TO ADJOINING PREMISES WITH CONSENT OF ADJACENT OWNER.
- B: § 53,187,231 M/D LAW & DEPT RULES & REG. PROVIDE MEANS OF EGRESS FROM YARD TO STREET BY FIREPROOF PASSAGEWAY FOR WHICH APPLICATION MUST BE FILED FOR APPROVAL,OR BY UNLOCKED DOOR OR GATE IN FENCE TO ADJOINING PREMISES WITH CONSENT OF ADJACENT OWNER.
- C: SECTION 53,187,231 M/D LAW & DEPT RULES & REG. PROVIDE MEANS OF EGRESS FROM YARD TO STREET BY FIREPROOF PASSAGEWAY FOR WHICH APPLICATION MUST BE FILED FOR APPROVAL,OR BY UNLOCKED DOOR OR GATE IN FENCE TO ADJOINING PREMISES WITH CONSENT OF ADJACENT OWNER.

## Order 51: 51 - DISCONTINUE STORAGE OF COMBUSTIBLES

- Category (dictionary): UNLAWFUL USE; cited section (most common in samples): § 12 M/D LAW
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 517 | 65 | 1970-04-20 | 2026-10-26 | 0 | REAR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 334 | 103 | 1975-02-04 | 2026-11-11 | 0 | CELLAR; ROOM AT CELLAR; STORAGE OF COMBUSTIBLE MATERIAL | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 12 M/D LAW DISCONTINUE THE STORAGE OF COMBUSTIBLE MATERIAL , AT BOILER ROOM
- C: § 12 M/D LAW DISCONTINUE THE STORAGE OF COMBUSTIBLE MATERIAL 100 CUBIC YARDS AT GASMETER ROOM AT CELLAR, SECTION AT WEST

## Order 899: 899 - MAKE GAS TIGHT

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADMIN. CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 88 | 0 | 2000-01-31 | 2023-05-26 | 0 | PIPE; APT.; KITCHEN SINK | 40 most recent (server-ordered) |
| B | 687 | 5 | 1999-12-09 | 2026-09-09 | 0 | THE SINK; IN THE SINK WASTE | 40 most recent (server-ordered) |

One sample per class:

- A: § 27-2026 ADMIN. CODE: REPAIR BY CLOSING SO AS TO BE GAS TIGHT ALL OPENINGS IN THE CONNECTION AT WASTE LINE AT SINK IN THE KITCHEN LOCATED AT APT 2, 2nd STORY, 2nd APARTMENT FROM NORTH AT EAST
- B: § 27-2026 ADMIN. CODE: REPAIR BY CLOSING SO AS TO BE GAS TIGHT ALL OPENINGS IN THE UNCAPPED GAS LINE IN THE KITCHEN LOCATED AT APT 2, 2nd STORY, 2nd APARTMENT FROM EAST AT SOUTH

## Order 958: 958 - REPAIR BROKEN PAYING

- Category (dictionary): PAVING AND GRADING; cited section (most common in samples): § 27-2027 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 107 | 10 | 2000-01-14 | 2026-11-05 | 0 |  | 40 most recent (server-ordered) |
| B | 556 | 35 | 1999-12-07 | 2026-11-07 | 0 |  | 40 most recent (server-ordered) |
| C | 67 | 7 | 2002-07-02 | 2026-11-04 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2027 ADMIN. CODE: PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING AT FRONT YARD BUILDING ENTRACE EAST/SOUTH SECTION YARD
- B: § 27-2027 ADMIN. CODE: PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING AT SOUTH AT FIRE PASSAGE WAY
- C: § 27-2027 ADMIN. CODE: PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING CONSISTING OF CONCRETE UPPER LANDING AT BUILDING FRONT STAIRS

## Order 589: 589 - HAND HOLD COVER MISSING

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): D26-16.01 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1985-06-19 | 1985-06-19 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 719 | 22 | 1972-09-13 | 2026-10-15 | 0 | CELLAR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-16.01 ADM CODE PROVIDE SUITABLE TIGHT COVER FOR THE HANDHOLE OPENING OF TRAP AT TRAP PIT CELLAR FRONT.
- B: § 27-2026 ADM CODE PROVIDE SUITABLE TIGHT COVER FOR THE HANDHOLE OPENING OF TRAP AT, BATHTUB ,SOUTH WALL , IN THE BATHROOM LOCATED AT APT 302, 3rd STORY, 2nd APARTMENT FROM SOUTH AT WEST , SECTION ''EAST''

## Order 698: 698 - OLT, RATED DOOR, NOT MAIN ENTRANCE DOOR

- Category (dictionary): PROTECTIVE DEVICES AND FIRE PROTECTION; cited section (most common in samples): § 27-2044 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 335 | 0 | 1977-08-31 | 2018-10-02 | 0 | WASTELINE SINK KITCHEN 2; STORY PUBLIC HALL TO; PUBLIC HALL TO ROOF | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 373 | 189 | 2022-06-15 | 2026-11-18 | 0 | PUBLIC HALL 1ST STORY; AT PUBLIC HALL 1ST; DOOR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2044 ADM CODE PROVIDE APPROVED ONE-HOUR FIRE RESISTANCE RATED SELF-CLOSING DOOR AT ALL OPENINGS TO PUBLIC HALL OTHER THAN APT MAIN ENTRANCE DOOR FROM 4 STORY PUBLIC HALL TO ROOF
- C: § 27-2005, 2044 HMC:PROVIDE APPROVED ONE-HOUR FIRE RESISTANCE RATED SELF-CLOSING DOOR AT ALL OPENINGS TO PUBLIC HALL, OTHER THAN APARTMENT MAIN ENTRANCE DOOR 1ST AND 2ND FIRE DOOR FROM SOUTH AT WEST AT PUBLIC HALL, 1st STORY

## Order 697: 697 - OLT, RATED APARTMENT DOOR

- Category (dictionary): PROTECTIVE DEVICES AND FIRE PROTECTION; cited section (most common in samples): § 27-2005, 2044 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 533 | 0 | 1977-08-16 | 2021-11-01 | 0 | TO MAIN ENTRANCE DOOR; MAIN ENTRANCE DOOR TO; 1ST STORY PUBLIC HALL | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 122 | 67 | 2022-06-15 | 2026-10-19 | 0 | IN THE; IN THE FOYER | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2005, 2044 ADM CODE PROVIDE APPROVED ONE-HOUR FIRE RESISTANCE RATED SELF-CLOSING DOOR WITH KEY-OPERATED DEAD BOLT & LATCH SET, PEEP HOLE & CHAIN GUARD AT MAIN ENTRANCE TO 1ST STORY PUBLIC HALL LOCATED AT APT 1D, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH , SECTION AT WEST
- C: § 27-2005, 2044 HMC: PROVIDE APPROVED ONE-HOUR FIRE RESISTANCE RATED SELF-CLOSING DOOR WITH KEY-OPERATED DEAD BOLT & LATCH SET PEEPHOLE & CHAIN GUARD AT MAIN ENTRANCE 2ND FROM EAST AT SOUTH , IN THE ENTRANCE LOCATED AT APT 3, 4th STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 803: 803 - STRUCTURAL DEFECT

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 92 | 1 | 2001-11-28 | 2025-07-18 | 0 | ROTTED LOLLY COLUMMS CELLAR; LOLLY COLUMMS CELLAR FRONT; COLUMMS CELLAR FRONT AND | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 415 | 16 | 2000-01-10 | 2026-09-16 | 0 | NORTH | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADMIN. CODE: MAKE SAFE BY PROPERLY REPAIRING THE STRUCTURAL DEFECT. DEFECTIVE LINTEL AT 1ST WINDOW FROM WEST AT SOUTH, AT BASEMENT
- C: § 27-2005 ADMIN. CODE: MAKE SAFE BY PROPERLY REPAIRING THE STRUCTURAL DEFECT. 2ND STORY BALCONY, BULGING AND CRACKED, SOFFIT, BUILDING FRONT IN DANGER OF COLLASPING

## Order 768: 768 - VACANT BUILDING NOW OCCUPIED

- Category (dictionary): VACANT MULTIPLE DWELLINGS; cited section (most common in samples): § 27-2089 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 452 | 9 | 1970-05-06 | 2025-08-08 | 0 | IN THE ENTIRE APARTMENT; THRU-OUT IN THE ENTIRE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1 | 0 | 1987-02-26 | 1987-02-26 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- B: § 27-2089 ADM CODE THE PREMISES FORMERLY A VACANT BUILDING ARE NOW OCCUPIED BY OTHER THAN A CARETAKER WITHOUT OBTAINING A CERTIFICATE OF OCCUPANCY
- C: D26-35.01 ADM CODE THE PREMISES FORMERLY A VACANT BUILDING ARE NOW OCCUPIED BY OTHER THAN A CARETAKER WITHOUT OBTAINING A CERTIFICATE OF OCCUPANCY BLDG CONVERTED TO 1 FAMILY DWELLING.

## Order 734: 734 - NO WATER CLOSET FOR CLASS "B" ROOMS.

- Category (dictionary): SANITARY FACILITIES; cited section (most common in samples): § 27-2067 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 449 | 1 | 1964-03-16 | 2025-07-27 | 0 | COMMUNITY; PUBLIC HALL COMMUNITY BATHROOM.; MISSING AT COMMUNITY BATHROOM | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1 | 0 | 1974-05-16 | 1974-05-16 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2067 ADM CODE PROVIDE AT LEAST ONE WATER CLOSET ON THE SAME FLOOR FOR THE ROOMS USED FOR CLASS B OCCUPANCY. WORK MUST BE COMPLETED UNDER PERMIT MISSING AT COMMUNITY BATHROOM, 2nd STORY
- C: D26-31.09 ADM CODE PROVIDE AT LEAST ONE WATER CLOSET ON THE SAME FLOOR FOR THE ROOMS USED FOR CLASS B OCCUPANCY. WORK MUST BE COMPLETED UNDER PERMIT 2 STY APT NO WATER CLOSET AND NO KITCHEN.

## Order 222: 222 - PROVIDE CELLAR STAIR ENCLOSURE

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): SECTION 242 M/D LAW
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1979-03-19 | 1979-03-19 | 0 |  | 1 most recent (server-ordered) |
| B | 355 | 0 | 1967-05-05 | 2017-10-10 | 0 | CELLAR | 40 most recent (server-ordered) |

One sample per class:

- A: SECTION 242 M/D LAW PROVIDE UNDER COMPLETED PERMIT,A PROPER ENCLOSURE WITH FIREPROOF SELFCLOSING DOORS AND ASSEMBLIES,AT THE TOP AND THE BOTTOM OF THE CELLAR STAIRS, 1ST STY PUBLIC HALL CENTER TO CELLAR.
- B: § 242 M/D LAW PROVIDE UNDER COMPLETED PERMIT,A PROPER ENCLOSURE WITH FIREPROOF SELFCLOSING DOORS AND ASSEMBLIES,AT THE TOP AND THE BOTTOM OF THE CELLAR STAIRS, MISSING WALL ENCLOSURE AND BOTTOM DOOR , AT CELLAR

## Order 771: 771 - REGISTRATION STATEMENT IS FALSE

- Category (dictionary): ANNUAL PROPERTY REGISTRATION; cited section (most common in samples): § 27-2096 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 172 | 5 | 1979-02-09 | 2026-04-07 | 0 | OR INCOMPLETE INFORMATION RELATED; INCOMPLETE INFORMATION RELATED TO; TRUE REGISTRATION STATEMENT FOR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| I | 139 | 139 | 2026-05-06 | 2026-10-29 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2096 ADM CODE FILE WITH THIS DEPARTMENT A TRUE REGISTRATION STATEMENT FOR BUILDING.
- I: § 27-2096 HMC: PROPERTY REGISTRATION WAS FILED WITH FALSE OR INCOMPLETE INFORMATION RELATED TO THE PROPERTY CONTACTS. FILE WITH THIS DEPARTMENT A TRUE REGISTRATION STATEMENT FOR THE BUILDING.

## Order 835: 835 - REMOVE THE TORN AND/OR LOOSE FLOOR COVERING

- Category (dictionary): MAINTENANCE; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 61 | 2 | 2000-01-12 | 2024-11-02 | 0 |  | 40 most recent (server-ordered) |
| B | 214 | 10 | 2000-04-12 | 2026-10-17 | 0 | FLOOR; AT FLOOR IN; CARPET AT | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2005 ADMIN. CODE: REMOVE THE TORN AND/OR LOOSE FLOOR COVERING , IN THE PRIVATE HALLWAY LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM NORTH AT EAST
- B: § 27-2005 ADMIN. CODE: REMOVE THE TORN AND/OR LOOSE FLOOR COVERING .. IN THE KITCHEN LOCATED AT APT 2, 2nd STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 775: 775 - CHANGE IN REGISTRATION

- Category (dictionary): ANNUAL PROPERTY REGISTRATION; cited section (most common in samples): D26-41.05 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1978-08-25 | 1978-08-25 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 265 | 2 | 1969-03-04 | 2024-02-12 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-41.05 ADM CODE FILE WITH THIS DEPARTMENT REGISTRATION STATEMENT FOR CHANGE OF OWNERSHIP OF BUILDING.
- B: § 27-2099 ADM CODE FILE WITH THIS DEPARTMENT REGISTRATION STATEMENT FOR CHANGE OF OWNERSHIP OF BUILDING.

## Order 654: 654 - REPAIR GUTTER

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2027 ADM CODE
- Pattern: **rare exception**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 254 | 40 | 1970-04-21 | 2026-10-12 | 0 | AT NORTH; SOUTH; YARD | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 1 | 0 | 1974-09-20 | 1974-09-20 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2027 ADM CODE REPAIR THE BROKEN OR DEFECTIVE GUTTER AND DOWNSPOUT AT NORTH FACADE
- C: D26-16.03 ADM CODE REPAIR THE BROKEN OR DEFECTIVE GUTTER RAIN LEADER TOP SECTION AT SOUTH COURT.

## Order 717: 717 - PROVIDE AN ADEQUATE SUPPLY OF WATER FOR SPRINKLER

- Category (dictionary): SPRINKLER SYSTEM; cited section (most common in samples): § 27-2005, 2050 HMC
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 14 | 3 | 2012-07-11 | 2026-09-23 | 0 | AT PUBLIC HALL; 3RD STORY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 229 | 72 | 2012-12-11 | 2026-11-10 | 0 | SPRINKLER SYSTEM | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005, 2050 HMC: PROVIDE AN ADEQUATE SUPPLY OF WATER FOR THE WET SPRINKLER AND/OR STANDPIPE SYSTEM AT .. AT PUBLIC HALL, 1st STORY
- C: § 27-2005, 2050 HMC: PROVIDE AN ADEQUATE SUPPLY OF WATER FOR THE WET SPRINKLER AND/OR STANDPIPE SYSTEM AT ...

## Order 752: 752 - DISCONTINUE SINGLE ROOM OCCUPANCY

- Category (dictionary): MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS; cited section (most common in samples): § 27-2078 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 8 | 3 | 1991-05-02 | 2025-04-25 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 196 | 32 | 1982-02-17 | 2026-06-03 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2078 ADM CODE DISCONTINUE USE FOR SINGLE ROOM OCCUPANCY PURPOSES THE APARTMENTS WHICH ARE OCCUPIED BY MORE THAN 2 BOARDERS, ROOMERS OR LODGERS ... IN THE 1st ROOM FROM EAST AT NORTH LOCATED AT APT 24, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2078 ADM CODE DISCONTINUE USE FOR SINGLE ROOM OCCUPANCY PURPOSES THE APARTMENTS WHICH ARE OCCUPIED BY MORE THAN 2 BOARDERS, ROOMERS OR LODGERS 1 ADULT IN THE 1st ROOM FROM NORTH AT CENTER LOCATED AT APT 5A, 5th STORY, 1st APARTMENT FROM WEST AT NORTH , SECTION ''EAST''

## Order 812: 812 - FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 80 | 2 | 2001-03-27 | 2024-09-03 | 0 | SHOE | 40 most recent (server-ordered) |
| C | 124 | 8 | 2000-02-09 | 2026-11-12 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN, DEFECTIVE AND/OR MISSING FRONT OF BUILDING HOUSEHOLD ITEM AT GARAGE
- C: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN, DEFECTIVE AND/OR MISSING METAL TREAD 5TH FROM BOTTOM AT REAR YARD AT FIRE ESCAPE, 2nd STORY

## Order 515: 515- F/E DEFECTIVE. FILL IN HOLES IN WALL AROUND BRACKETS AND/OR RAILS

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 107 | 16 | 1972-07-20 | 2026-09-16 | 0 | FIRE ESCAPE FROM; NETAL KITCHEN SINK CABINET; ROTTED NETAL KITCHEN SINK | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 52 | 7 | 1986-06-16 | 2026-04-06 | 0 | BALCONY AT; BALCONY AT BUILDING FRONT; STORY BALCONY AT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. FILL IN HOLES IN WALL AROUND BRACKETS AND/OR RAILS 1ST FIRE ESCAPE FROM WEST AT SOUTH, AT (BUILDING FRONT) , 2nd STORY
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. FILL IN HOLES IN WALL AROUND BRACKETS AND/OR RAILS AT 3RD BALCONY AT BUILDING FRONT

## Order 813: 813 - F/E ADJUST THE DROP LADDER

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 94 | 7 | 2001-03-16 | 2026-03-07 | 0 |  | 40 most recent (server-ordered) |
| C | 31 | 1 | 2000-11-22 | 2024-09-06 | 0 |  | 31 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. ADJUST THE DROPLADDER SO THAT IT WILL SLIDE EASILY IN THE GUIDE RODS AT REAR OF BUILDING AT FIRE ESCAPE, 1st STORY
- C: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. ADJUST THE DROPLADDER SO THAT IT WILL SLIDE EASILY IN THE GUIDE RODS STACK AT REAR YARD AT FIRE ESCAPE

## Order 849: 849 - REMOVE EXCESSIVE STORAGE

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005, 2012 HMC & § 309 MDL
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 77 | 16 | 2015-04-04 | 2026-04-25 | 0 |  | 40 most recent (server-ordered) |
| C | 41 | 14 | 2015-03-20 | 2026-11-10 | 0 |  | 40 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005, 2012 HMC & § 309 MDL: ABATE THE NUISANCE CONSISTING OF EXCESSIVE STORAGE OF MATERIAL .. IN THE 1st ROOM FROM NORTH LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM EAST AT SOUTH
- C: § 27-2005, 2012 HMC & § 309 MDL: ABATE THE NUISANCE CONSISTING OF EXCESSIVE STORAGE OF MATERIAL CLOTHING, BOXES, PAPER PRODUCTS, FURNITURE, SHOE BOXES, AND ETC... IN THE ENTIRE APARTMENT LOCATED AT APT 1STFL, 1st APARTMENT FROM EAST AT SOUTH

## Order 81: 81 - NO SPRINKLER OR FIRE ESCAPE

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): SECTION 194 M/D LAW
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 19 | 0 | 1964-05-13 | 1998-05-21 | 0 | ALL; BASEMENT | 19 most recent (server-ordered) |
| C | 91 | 9 | 1972-02-09 | 2026-11-04 | 0 |  | 40 most recent (server-ordered) |

One sample per class:

- B: SECTION 194 M/D LAW PROVIDE SPRINKLER HEADS IN ALL CLASS B ROOMS AND FILE APPLICATION FOR APPROVAL BEFORE DOING THIS WORK 1 STY FRONT AND REAR ROOM.
- C: § 187 M/D LAW PROVIDE A SPRINKLER SYSTEM OR A LEGAL SECOND MEANS OF EGRESS AND FILE APPLICATION FOR APPROVAL BEFORE DOING THIS WORK PARTIAL SPRINKLER SYSTEM AT THE CEILING IN THE PUBLIC HALLWAY , AT BASEMENT

## Order 750: 750 - UNLAWFUL OCCUPANCY OF CHILD OR CHILDREN UNDER 16

- Category (dictionary): MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS; cited section (most common in samples): § 27-2076 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 96 | 2 | 1969-04-17 | 2026-06-17 | 0 | EAST; FROM NORTH AT EAST; 1ST SECTION FROM | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1 | 0 | 1976-01-07 | 1976-01-07 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2076 ADM CODE DISCONTINUE UNLAWFUL OCCUPANCY FOR LIVING PURPOSES BY CHILD OR CHILDREN UNDER 16 YEARS OF AGE AT CELLAR , 1st SECTION FROM NORTH AT EAST
- B: D26-33.05 ADM CODE DISCONTINUE UNLAWFUL OCCUPANCY FOR LIVING PURPOSES BY CHILD OR CHILDREN UNDER 16 YEARS OF AGE 3 STORY FRONT WEST ROOM 7 ONE ROOM.

## Order 776: 776 - ADDRESS OF OWNER INCORRECT

- Category (dictionary): ANNUAL PROPERTY REGISTRATION; cited section (most common in samples): § 27-2100 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 86 | 5 | 1974-07-31 | 2026-03-30 | 0 | PUBLIC HALL 1ST STORY; AT PUBLIC HALL 1ST | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1 | 0 | 1987-10-22 | 1987-10-22 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2100 ADM CODE FILE WITH THIS DEPARTMENT A REGISTRATION STATEMENT WITH A PROPER ADDRESS FOR REGISTERED PARTY.
- B: D26-41.07 ADM CODE FILE WITH THIS DEPARTMENT A REGISTRATION STATEMENT WITH A PROPER ADDRESS FOR REGISTERED PARTY.

## Order 681: 681 - NO LIGHT FOR WATER CLOSET

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2037 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 8 | 3 | 1976-05-06 | 2025-03-23 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 78 | 21 | 1984-09-26 | 2026-05-06 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2037 ADM CODE PROVIDE A PROPER MEANS OF LIGHTING FOR WATER CLOSET COMPARTMENT AT CEILING IN THE BATHROOM LOCATED AT APT 10, 3rd STORY, 1st APARTMENT FROM WEST AT NORTH
- B: § 27-2037 ADM CODE PROVIDE A PROPER MEANS OF LIGHTING FOR WATER CLOSET COMPARTMENT AT ALL ELECTRICAL OUTLETS AT ALL WALLS AND CEILING IN THE BATHROOM LOCATED AT APT 4D, 4th STORY, 2nd APARTMENT FROM WEST AT NORTH

## Order 69: 69 - MANUFACTURING BUSINESS, ETC.

- Category (dictionary): UNLAWFUL USE; cited section (most common in samples): § 61 M/D LAW
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 25 | 0 | 1972-09-07 | 2019-09-30 | 0 | STY; COMMERCIAL SPACE AT 1; APT DBA BRAUN CORSET. | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 53 | 0 | 1983-01-04 | 2023-04-12 | 0 | OBTAINED; OBTAINED TO REALTY BROKER; TO REALTY BROKER OFFICE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 61 M/D LAW DISCONTINUE USE UNLESS AND UNTIL AN APPROVED APPLICATION IS FILED AND A CERTIFICATE OF OCCUPANCY IS OBTAINED ''1ST. STY CLASS 'A' APT USED FOR DAY CARE' IN THE ENTIRE APARTMENT LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 61 M/D LAW DISCONTINUE USE UNLESS AND UNTIL AN APPROVED APPLICATION IS FILED AND A CERTIFICATE OF OCCUPANCY IS OBTAINED, 1st STORY

## Order 516: 516 - FIRE ESCAPE DEFECTIVE. RESET THE BRACES OF THE BRACKETS

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 33 | 2 | 1972-01-25 | 2026-06-06 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 39 | 8 | 1984-03-16 | 2024-12-31 | 0 | FRONT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. RESET THE BRACES OF THE BRACKETS SO THAT THEY SHALL BEAR AGAINST WALL FIRST STACK FROM WEST AT NORTH AT FIRE ESCAPE
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. RESET THE BRACES OF THE BRACKETS SO THAT THEY SHALL BEAR AGAINST WALL 3RD STORY BALCONY AT BUILDING FRONT

## Order 665: 665 - INSTALL CENTRAL HEATING SYSTEM

- Category (dictionary): HEAT AND HOT WATER; cited section (most common in samples): D26-17.01 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 1 | 0 | 1990-06-25 | 1990-06-25 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 71 | 0 | 1971-07-22 | 2022-11-17 | 0 | IN THE ENTIRE APARTMENT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: D26-17.01 ADM CODE INSTALL CENTRAL HEATING SYSTEM OR, IF LAWFULLY FEASIBLE, INDIVIDUAL SPACE HEATERS, AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING WORK FOR ALL APTS ALL STYS.
- C: § 27-2028 ADM CODE INSTALL CENTRAL HEATING SYSTEM OR, IF LAWFULLY FEASIBLE, INDIVIDUAL SPACE HEATERS, AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING WORK ..

## Order 814: 814 - F/E DEFECTIVE: PROPERLY SECURE

- Category (dictionary): EGRESS; cited section (most common in samples): SECTION 27-2005 ADMIN. CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 37 | 0 | 2000-10-13 | 2021-07-02 | 0 |  | 37 most recent (server-ordered) |
| C | 35 | 2 | 2003-06-12 | 2026-08-14 | 0 | FROM BOTTOM; METAL; TREAD | 35 most recent (server-ordered) |

One sample per class:

- B: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. PROPERLY SECURE SCUTTLE LADDER TO THE NORTH WALL AT PUBLIC HALL, 3rd STORY
- C: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. PROPERLY SECURE 1ST, 11TH AND 14TH TREAD FROM BOTTOM AT REAR FIRE ESCAPE , 2nd STORY

## Order 518: 518 - F/E REPLACE WITH 2" X 1/2" IRON BAR EXTENDING ACROSS

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 22 | 0 | 1977-02-07 | 2022-03-02 | 0 | SECTION OF ROOF GOOSENECK; OF ROOF GOOSENECK LADDERS; AND EAST SOUTH SECTION | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 36 | 8 | 1975-05-28 | 2026-10-19 | 0 | AT FIRE ESCAPE; ROOF AT; ROOF AT FIRE ESCAPE | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REPLACE WITH 2 X 1/2 INCH IRON BAR EXTENDING ACROSS AND SECURED TO 2 BRACKETS, THE BROKEN OR DEFECTIVE ANGLE IRON OR BAR AT FOOT OF GOOSENECK LADDER AT EAST NORTH AND EAST SOUTH SECTION OF ROOF GOOSENECK LADDERS
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REPLACE WITH 2 X 1/2 INCH IRON BAR EXTENDING ACROSS AND SECURED TO 2 BRACKETS, THE BROKEN OR DEFECTIVE ANGLE IRON OR BAR AT FOOT OF GOOSENECK LADDER

## Order 517: 517 - F/E. REMOVE AND REPLACE WITH NEW THE BRACKET

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 20 | 5 | 1991-04-17 | 2026-07-11 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 34 | 2 | 1982-11-08 | 2024-11-23 | 0 | AT FRONT; YARD AT; AT EAST | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REMOVE AND REPLACE WITH NEW THE BROKEN AND DEFECTIVE BRACKET AND LEAVE ALL ANCHORAGES UNCOVERED FOR INSPECTION AT 2ND STORY FIRE ESCAPE BALCONY AT 1ST STACK FROM NORTH AT BUILDING FRONT AT FIRE ESCAPE
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REMOVE AND REPLACE WITH NEW THE BROKEN AND DEFECTIVE BRACKET AND LEAVE ALL ANCHORAGES UNCOVERED FOR INSPECTION AT 1ST FIRE ESCAPE FROM FROM SOUTH AT EAST AT BUILDING FRONT AT FIRE ESCAPE, 5th STORY

## Order 118: 118 - BRACE

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): SECTION 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 7 | 0 | 1986-03-20 | 2019-05-07 | 0 |  | 7 most recent (server-ordered) |
| B | 38 | 2 | 1983-09-29 | 2026-06-28 | 0 |  | 38 most recent (server-ordered) |

One sample per class:

- A: § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS. PROPERLY BRACE THE GOOSENECK LADDER AT THE ROOF
- B: § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS. PROPERLY BRACE TOP RETURN RAIL AT EAST WALL AT WEST SIDE OF BUILDING AT FIRE ESCAPE, 3rd STORY, SECTION ''WEST''

## Order 519: 519 - F/E. REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 14 | 1 | 1982-08-19 | 2025-07-23 | 0 | HOUSEHOLD ITEMS CLOTHES/PAINTING AT; ITEMS CLOTHES/PAINTING AT 4TH; CLOTHES/PAINTING AT 4TH STORY | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 21 | 15 | 1986-01-27 | 2026-10-14 | 0 | WALL; BALCONY INSTALLED; EXTERIOR WALL AT | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES HOUSEHOLD ITEMS (CLOTHES/PAINTING) AT 4TH STORY FIRE BALCONY (BUILDING FRONT)
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES ADDITIONAL BALCONY INSTALLED AT 5TH STORY; SPANNING ACROSS FROM 1ST TO 3RD WINDOW FROM SOUTH AT EAST EXTERIOR WALL AT INNER COURTYARD. BUILDING SECTION A-B AT FIRE ESCAPE, 5th STORY

## Order 648: 648 - PROPERLY REAM OUT, TAP AND PLUG

- Category (dictionary): SEWERS AND DRAINAGE; cited section (most common in samples): § 27-2026 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 33 | 2 | 1973-03-22 | 2025-01-07 | 0 | WASTE LINE; IN THE; CELLAR | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1 | 0 | 1975-09-24 | 1975-09-24 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2026 ADM CODE PROPERLY REAM OUT, TAP AND PLUG, WITH SCREW PLUGS, THE HOLES IN RADIATOR RISER AT FLOOR AT PUBLIC HALL, 1st STORY
- B: D26-16.01 ADM CODE PROPERLY REAM OUT, TAP AND PLUG, WITH SCREW PLUGS, THE HOLES IN SOIL LINE CELLAR AT CENTER WEST WALL.

## Order 213: 213 - SEAL UP OR PROVIDE FIREPROOF SELF-CLOSING DOOR

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): SECTION 61 M/D LAW
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 18 | 0 | 1977-05-11 | 2014-07-01 | 0 | STY; 1 STY; STORE | 18 most recent (server-ordered) |
| C | 3 | 3 | 2024-03-15 | 2025-09-02 | 0 | AT PUBLIC HALL; LEADING FROM COMMERCIAL SPACE; WALL LEADING FROM COMMERCIAL | 3 most recent (server-ordered) |

One sample per class:

- B: SECTION 61 M/D LAW SEAL WITH FIRE RETARDING MATERIAL OR PROVIDE WITH FIREPROOF SELF-CLOSING DOOR AND ASSEMBLY THE OPENING LEADING FROM STORE TO PUBLIC HALL -NORTH AND SOUTH OFFICE / STORE INSTALLED GLASS ENTRANCE DOORS AT 1ST STORY VESTIBULE
- C: § 61 MDL: SEAL WITH FIRE RETARDING MATERIAL OR PROVIDE WITH FIREPROOF SELF-CLOSING DOOR AND ASSEMBLY THE OPENING LEADING FROM STORE TO PUBLIC HALL ... IN THE ENTRANCE LOCATED AT APT 10, 3rd STORY, 3rd APARTMENT FROM NORTH AT EAST

## Order 520: 520 - F/E DEFECTIVE REMOVE THE ADDITIONAL, DANGER

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADM CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 15 | 2 | 1972-07-20 | 2025-03-06 | 0 | NORTH | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| C | 6 | 1 | 1997-05-16 | 2025-12-11 | 0 | AT ALL; EXCEEDING THE MAXIMUM TEMPERATURE; WATER EXCEEDING THE MAXIMUM | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- B: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REMOVE THE ADDITIONAL, DANGEROUS, INADEQUATE FIRE ESCAPE DOORS AT NORTH & SOUTH CLOSET IN THE FOYER LOCATED AT APT 2B, 2nd STORY, 1st APARTMENT FROM WEST AT NORTH , SECTION ''SOUTH''
- C: § 27-2005 ADM CODE FIRE ESCAPE DEFECTIVE. REMOVE THE ADDITIONAL, DANGEROUS, INADEQUATE FIRE ESCAPE HOT WATER EXCEEDING THE MAXIMUM TEMPERATURE OF 130 DEGREES AT ALL HOT WATER FIXTURE IN THE ENTIRE APARTMENT LOCATED AT APT 3F, 3rd STORY, 1st APARTMENT FROM NORTH AT EAST

## Order 678: 678 - NO SELF INSPECTION REPORT

- Category (dictionary): GAS APPLIANCES; cited section (most common in samples): § 27-2036 ADM CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 19 | 1 | 1975-01-02 | 2025-09-07 | 0 | PUBLIC HALL 1ST STORY; AT PUBLIC HALL 1ST | lexicographic min/max of all rows and of rows since 2024 (aggregate) |
| B | 1 | 0 | 1989-04-10 | 1989-04-10 | 0 |  | lexicographic min/max of all rows and of rows since 2024 (aggregate) |

One sample per class:

- A: § 27-2036 ADM CODE MAINTAIN ON THE REEMISES A SELF INSPECTION REPORT OF EACH GAS FUELED SPACE HEATER AND EACH GAS APPLIANCE FOR THE CURRENT YEAR. SUCH REPORT SHALL BE SUBMITTED TO THE DEPARTMENT UPON REQUEST.
- B: D26-18.05 ADM CODE MAINTAIN ON THE PREMISES A SELF INSPECTION REPORT OF EACH GAS FUELED SPACE HEATER AND EACH GAS APPLIANCE FOR THE CURRENT YEAR. SUCH REPORT SHALL BE SUBMITTED TO THE DEPARTMENT UPON REQUEST.

## Order 981: 981 - NO LIGHT FOR WATER CLOSET

- Category (dictionary): ARTIFICIAL LIGHTING; cited section (most common in samples): § 27-2037 ADMIN. CODE
- Pattern: **concurrent**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 2 | 1 | 2005-07-15 | 2025-01-14 | 0 | WATTS FOR SINGLE FIXTURE.; PUBLIC HALL AND VESTIBULE; VESTIBULE 60 WATTS FOR | 2 most recent (server-ordered) |
| B | 16 | 3 | 2001-07-25 | 2026-08-21 | 0 | IN THE BATHROOM | 16 most recent (server-ordered) |

Note: the sampled descriptions don't show what sets the class for this order (unsettled from this data).

One sample per class:

- A: § 27-2037 ADMIN. CODE: PROVIDE PROPER MEANS OF LIGHTING FOR WATER CLOSET COMPARTMENT AT CEILING IN THE 2nd BATHROOM FROM EAST LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST
- B: § 27-2037 ADMIN. CODE: PROVIDE PROPER MEANS OF LIGHTING FOR WATER CLOSET COMPARTMENT TO THE FIXTURES AND OUTLETS IN THE 1st BATHROOM FROM NORTH LOCATED AT APT 1, 1st STORY, 1st APARTMENT FROM SOUTH AT WEST

## Order 1504: 1504 - FILE CERTIFICATION FOR CO DETECTOR

- Category (dictionary): RETIRED; cited section (most common in samples): § 27-2046.1, 2046.2 HMC
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| A | 9 | 0 | 2004-11-02 | 2023-04-19 | 0 |  | 9 most recent (server-ordered) |
| B | 6 | 0 | 2004-11-06 | 2018-05-23 | 0 |  | 6 most recent (server-ordered) |

One sample per class:

- A: § 27-2046.1, 2046.2 HMC: FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF CARBON MONOXIDE DETECTING DEVICE(S) IN ACCORDANCE WITH HPD RULE. AT PUBLIC HALL, 1st STORY
- B: § 27-2046.1, 2046.2 HMC: FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF CARBON MONOXIDE DETECTING DEVICE(S) IN ACCORDANCE WITH HPD RULE. IN THE ENTIRE APARTMENT LOCATED AT APT 8F, 8th STORY, 1st APARTMENT FROM EAST AT SOUTH

## Order 1017: 1017 - PROVIDE AN ADEQUATE SUPPLY OF WATER FOR SPRINKLER

- Category (dictionary): MISCELLANEOUS SERVICES AND FACILITIES; cited section (most common in samples): § 27-2005, 2050 HMC
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 2 | 0 | 2019-03-08 | 2022-05-20 | 0 | IN THE ENTIRE APARTMENT; AT IN THE ENTIRE; AT AT CELLAR | 2 most recent (server-ordered) |
| C | 8 | 3 | 2014-12-18 | 2026-03-03 | 0 | ENTIRE BUILDING; AT ENTIRE BUILDING; AT ALL STORIES | 8 most recent (server-ordered) |

One sample per class:

- B: § 27-2005, 2050 HMC: PROVIDE AN ADEQUATE SUPPLY OF WATER FOR THE WET SPRINKLER AND/OR STANDPIPE SYSTEM AT , AT CELLAR
- C: § 27-2005, 2050 HMC: PROVIDE AN ADEQUATE SUPPLY OF WATER FOR THE WET SPRINKLER AND/OR STANDPIPE SYSTEM AT AT ALL STORIES AT PUBLIC HALL

## Order 142: 142 - BRACE BALCONY WITH TIE RODS

- Category (dictionary): FIRE EGRESS AND PROTECTION; cited section (most common in samples): § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 4 | 0 | 2013-06-27 | 2016-07-08 | 0 |  | 4 most recent (server-ordered) |
| C | 5 | 0 | 1987-06-22 | 2020-07-27 | 0 | AT FIRE ESCAPE; 2 STY; ER1. | 5 most recent (server-ordered) |

One sample per class:

- B: SECTION 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS. BRACE AND SUPPORT BALCONY WITH SUITABLE TIE RODS OR SUSPENSION RODS REAR FIRE ESCAPE , 4th STORY
- C: § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS. BRACE AND SUPPORT BALCONY WITH SUITABLE TIE RODS OR SUSPENSION RODS AT 1ST 2ND AND 3RD STORIES BALCONY AT REAR OF BLDG. AT FIRE ESCAPE

## Order 819: 819 - F/E. REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES

- Category (dictionary): EGRESS; cited section (most common in samples): § 27-2005 ADMIN. CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 2 | 0 | 2017-08-23 | 2017-08-23 | 0 | EXTERIOR WALL; AT SOUTH EXTERIOR WALL; AT WEST EXTERIOR WALL | 2 most recent (server-ordered) |
| C | 2 | 0 | 2002-08-16 | 2023-05-20 | 0 | ROOF; FIRE; EGRESS DEFECTIVE. MAKE SAFE. | 2 most recent (server-ordered) |

One sample per class:

- B: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES AT WEST EXTERIOR WALL
- C: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES § 27-2005, 2007 ADM CODE FIRE EGRESS DEFECTIVE. MAKE SAFE. MAKE STATIONARY THE IRON LADDER LEADING TO SCUTTLE OPENING IN ROOF AT PUBLIC HALL STAIRS, 2nd STORY

## Order 817: 817 - F/E. REMOVE AND REPLACE WITH NEW THE BRACKET

- Category (dictionary): EGRESS; cited section (most common in samples): SECTION 27-2005 ADMIN. CODE
- Pattern: **time shift**

| Class | Count | Since 2024 | First inspection | Last inspection | Upgraded rows | Auto distinguishing phrases | Samples |
|---|---|---|---|---|---|---|---|
| B | 2 | 0 | 2000-09-20 | 2005-06-02 | 0 | FIRE ESCAPE; STORY BLACONY WEST BRACKET; FIRE ESCAPE ALL BRACKETS | 2 most recent (server-ordered) |
| C | 1 | 0 | 2003-07-14 | 2003-07-14 | 0 |  | 1 most recent (server-ordered) |

One sample per class:

- B: SECTION 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. REMOVE AND REPLACE WITH NEW THE BROKEN AND DEFECTIVE BRACKET AND LEAVE ALL ANCHORAGES UNCOVERED FOR INSPECTION AT FRONT FIRE ESCAPE ALL BRACKETS OF 2ND STORY BLACONY WEST BRACKET OF 3RD STORY BLACONIES.
- C: § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE. REMOVE AND REPLACE WITH NEW THE BROKEN AND DEFECTIVE BRACKET AND LEAVE ALL ANCHORAGES UNCOVERED FOR INSPECTION ALL STORIES OF REAR FIRE ESCAPES.
