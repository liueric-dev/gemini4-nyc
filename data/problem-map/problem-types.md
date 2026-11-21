# Problem map: problem types

**DRAFT, not reviewed by the project owner.**

Workstream 6. Drafted 2026-11-21 (New York time) from the files collected in `data/`. Every claim cites a collected file by manifest id in square brackets, for example [nyc-hmc-27-2115 (c)]. Where the collected sources don't settle something, the text says `unsettled` and why. Nothing here is filled in from memory.

Companion files: [expected-outcomes.csv](expected-outcomes.csv) (one row per problem type and set of facts) and [escalation.md](escalation.md) (paths by what the tenant wants).

## How to read the citations

| Prefix | Folder | Manifest |
|---|---|---|
| `nyc-` | `law-nyc/` | `law-nyc/manifest.jsonl` |
| `st-`, `fed-` | `law-state/` | `law-state/manifest.jsonl` |
| `proc-` | `process/` (almost all in `process/local/`, `committable: unsure`) | `process/manifest.jsonl` |
| `od-` | `open-data/` | `open-data/manifest.jsonl` (created during drafting; every `od-` id here was checked against it) |

HPD order numbers, classes and row counts come from `od-hpd-violation-types` (612 order x class rows) and `od-hpd-order-class-map` (400 orders), as re-read at the end of drafting (files dated 2026-11-21 01:48; the open-data gaps file says a further sampling pass was stopped at 02:04, so no later refresh was expected; at the final check the file was unchanged, md5 61a87c45b6bfbf0ffcf806bfae9fb2c3). Counts exclude rows HPD marked "HAS BEEN UPGRADED TO CLASS ..." (`count_excluding_upgraded`). "Since 2024" counts are `count_since_2024`. What sets the class for multi-class orders is from `od-hpd-violation-types-class-notes` plus the per-class samples in `open-data/raw/od-hpd-violation-types-samples.jsonl`.

The `MD`/`PD` labels come from the `dict_md_pd` column of `od-hpd-violation-types` (HPD's data dictionary, [od-hpd-violations-dict-hpd-code-violations-data-dictionary]). Orders 801-1079 are labelled `PD` (private dwelling, a one- or two-family house) and mostly mirror the 501-779 `MD` (multiple dwelling) orders; for example 883 mirrors 583 and 966 mirrors 666.

### About expected-outcomes.csv

Line 1 is a `# DRAFT` comment; skip it when parsing. One row per problem type and set of facts. Columns:

| Column | Meaning |
|---|---|
| `row_id` | `EO-001` ... |
| `problem_type` | One of the README's problem type names |
| `scenario`, `building`, `location`, `facts` | The facts that select the row. `facts` uses `key=value` pairs where possible (`mold_area_sqft`, `child_under_6_resides`, `child_10_or_under`, `year_built`, `pest`, `indoor_temp_f`, `outside_temp_f`, `water_temp_f`, times as 24-hour ranges). |
| `expected_violation` | `yes`, `no`, or `unsettled` |
| `hpd_orders` | Likely HPD order numbers |
| `expected_sections` | Code sections the violation would cite |
| `expected_class` | A, B, C, `n/a`, or `unsettled` (with the classes seen in the data) |
| `class_basis` | Whether the class comes from a statute or only from the data |
| `correction_deadline`, `deadline_basis` | Deadline and its source |
| `escalation` | Path codes from [escalation.md](escalation.md) (A1-A8 fix, B1-B5 document, C1-C7 rent reduction, D1-D8 harassment, E1-E6 deposit, F1-F6 leave; Part 0 anti-retaliation) |
| `status` | `settled` (class and deadline from statute or statute plus data), `class-from-data` (only HPD's issued classes support it), `class-unsettled` (several classes issued, rule unknown), `unsettled` (the violation itself or its pairing is unsettled) |
| `notes`, `sources` | Notes, and the manifest ids behind the row |

---

## Part 1. Rules that apply to every problem type

### 1.1 Violation classes

HPD issues violations in four classes: A (non-hazardous), B (hazardous), C (immediately hazardous) and I (information orders, generally issued administratively) [od-hpd-violations-dict-hpd-code-violations-data-dictionary; proc-hpd-clear-violations]. The Housing Maintenance Code itself uses the words non-hazardous, hazardous and immediately hazardous [nyc-hmc-27-2115 (a), (c)]. The A/B/C letters are HPD's labels for those three; the statute uses "class C immediately hazardous" in several places [nyc-hmc-27-2043-1 (e); nyc-hmc-27-2041-1 (b); nyc-hmc-27-2056-6].

The HMC required HPD to classify all violations by hazard and publish the list in the City Record [nyc-hmc-27-2115 (d)]. **That classification list was not collected**, so for most orders the class comes only from what HPD has actually issued (the open data), not from a published rule. This is the single biggest reason for `unsettled` classes below.

### 1.2 Correction periods

| Class | Default period to correct | Source |
|---|---|---|
| A, non-hazardous | 90 days from mailing of the notice | [nyc-hmc-27-2115 (c)(1)] |
| B, hazardous | 30 days from mailing of the notice | [nyc-hmc-27-2115 (c)(2)] |
| C, immediately hazardous | 24 hours (notice served personally or by registered or certified mail) | [nyc-hmc-27-2115 (c)(3)] |

Special periods that override the default:

| Condition | Class | Period | Source |
|---|---|---|---|
| Mold, 30 sq ft or more in a room of a dwelling unit | C | 21 days after service | [nyc-hmc-27-2017-3 (c)(2)] |
| Mold, other classes | A or B | the 27-2115(c) default (90 or 30 days) | [nyc-hmc-27-2017-3 (c)(1)] |
| Cockroaches, mice or rats | C | 21 days after service | [nyc-hmc-27-2017-4 (c)] |
| Lead-based paint (HMC Article 14) | C / B | 21 days / 30 days after service | [nyc-hmc-27-2115 (l)(1)] |
| Window guards missing or not maintained | C | 21 days after service | [nyc-hmc-27-2043-1 (e)] |
| Self-closing doors | C | 14 days after service | [nyc-hmc-27-2041-1 (b)] |
| Heat and hot water (27-2028, 27-2029(a), 27-2031, 27-2032) | C | No correction period: penalties run from the day HPD affixes the notice. A first violation's penalty is satisfied if it is corrected within 24 hours of the notice and $250 is paid within 10 days. | [nyc-hmc-27-2115 (k)(1)(i)-(ii), (k)(2)]; HPD's table says "No time" [proc-hpd-clear-violations] |

HPD's own table matches these: A 90 days, B 30 days, C 21 days for lead, window guards, mold, mice, cockroaches and rats, C 14 days for self-closing doors, C "No time" for heat and hot water, and 24 hours for all other C [proc-hpd-clear-violations]. HPD's mold and pest page gives the same 90/30/21 days [proc-hpd-mold-and-pests].

Postponements: the default periods can be postponed on a showing made within the correction period [nyc-hmc-27-2115 (c)]. Mold C, pests C and lead postponements are capped at 14 days, with one further 14 days for lead once the paint is stabilized [nyc-hmc-27-2017-3 (c)(3); nyc-hmc-27-2017-4 (d); nyc-hmc-27-2115 (l)(1)]. No postponement is allowed for a mold C issued on reinspection of an uncorrected B [nyc-hmc-27-2017-3 (c)(3)].

Certification: the owner certifies correction no later than 14 days after the correction date for A and B, and 5 days after for C [nyc-hmc-27-2115 (f)(1)]; 5 days for lead and for Article 4 (mold, pests) violations [nyc-hmc-27-2115 (l)(2), (o)(2)]. HPD mails the complainant a copy of the certification [nyc-hmc-27-2115 (f)(2)]. A certified violation is deemed corrected 70 days after HPD receives the certification unless HPD reinspects and sets it aside [nyc-hmc-27-2115 (f)(3)(i)]. Failure to certify is prima facie evidence the violation was not corrected [nyc-hmc-27-2115 (f)(7)].

Tenant-facing summary of the process: HPD aims to inspect within 30 days; if the inspector can't get in, the tenant has 10 days to call and reschedule; most class C violations get HPD's "fix this now" notice (within 24 hours) and may go to the Emergency Repair Program; if the owner certifies but didn't fix it, the tenant can challenge as the letter instructs [proc-hpd-code-guide-what-to-expect] (dated "Updated: 2019").

Penalties (for the tenant's information, not a deadline): A $50-$150 plus $25/day; B $75-$500 plus $25-$125/day; C $150-$750 plus $50-$150/day in buildings of 5 or fewer units, or $150-$1,200 plus $150-$1,200/day in buildings of more than 5 units [nyc-hmc-27-2115 (a)].

### 1.3 Which buildings the Housing Maintenance Code covers

| Fact | Rule | Source |
|---|---|---|
| Any dwelling | The HMC applies to all dwellings unless a section says otherwise. | [nyc-hmc-27-2003] |
| Multiple dwelling | Occupied, or rented to be occupied, as the home of three or more families living independently. | [nyc-hmc-27-2004 (a)(7)]; same definition in state law [st-mdl-4 (7)] |
| Private dwelling | Built and occupied for residence by not more than two families. | [nyc-hmc-27-2004 (a)(6)] |
| Owner's duty to repair, multiple dwelling | Keep the premises in good repair. | [nyc-hmc-27-2005 (a)]; state law [st-mdl-78] |
| Owner's duty to repair, one- or two-family house | Keep the premises in good repair, except as otherwise agreed in a written lease. | [nyc-hmc-27-2005 (c)] |
| Vacant units in a multiple dwelling | Must also be kept in good repair. | [nyc-hmc-27-2005 (h)] |
| Co-op or condo, owner-occupied unit | see sources in text | Several provisions carve these out: harassment provisions don't apply where the shareholder or condo owner lives in the unit [nyc-hmc-27-2115 (n)]; lead violations in such units can be reissued on application by the co-op or condo board [nyc-rcny28-11-13]. Window guards expressly bind condo unit owners and co-op boards [nyc-hmc-27-2043-1 (a); nyc-healthcode-131-15 (a)(1)]. For most other sections the collected sources don't say who the "owner" is in a co-op or condo: `unsettled`. |
| NYCHA | HPD inspects NYCHA buildings and issues HMC and MDL violations "at the request of the NYC Housing Court", kept in a separate dataset [od-hpd-violations-nycha; od-hpd-violations-dict-hpd-code-violations-data-dictionary]. HPD and DOB must publish open violations in NYCHA buildings [nyc-hmc-27-2154]. HPD's inspection pamphlet says HPD violations in NYCHA buildings are sent to NYCHA as work tickets [proc-hpd-complaint-pamphlet]. Two HMC exemptions for NYCHA are narrow: Article 13 (janitorial services) [nyc-hmc-27-2056] and Article 2 of Subchapter 4 (registration) [nyc-hmc-27-2108]. The NYCHA dataset uses the same order numbers and A/B/C classes: the NYCHA demo building (466 Columbia St, Red Hook West) has 76 Housing Court-requested violations, A 19, B 47, C 10, including orders 508, 502, 583, 501, 556, 550 and 624 (lead) [od-demo-466-columbia-st-bk; od-hpd-violations-nycha]. So the class rules in this file can be applied to NYCHA findings; whether the correction deadlines and penalties are enforced against NYCHA the same way: `unsettled`; no collected source says so. |
| Private NYCHA buildings (PACT) | 311 says privately managed NYCHA buildings report to the management company first and, if conditions persist, file an ordinary Apartment Maintenance Complaint [proc-311-nycha-maintenance-complaint]. |
| Section 8 voucher units | The building is privately owned, so the HMC applies as usual; separately, the unit must meet federal Housing Quality Standards, inspected by HPD or NYCHA (see [escalation.md](escalation.md)) [proc-hpd-s8-inspections; fed-24cfr-982-i § 982.404]. |

HPD's 311 complaint categories are useful for routing the app's output to the right 311 complaint: `od-hpd-complaint-categories` lists major and minor categories with counts since 2024 (for example HEAT/HOT WATER, UNSANITARY CONDITION/PESTS, UNSANITARY CONDITION/MOLD, PAINT/PLASTER/WALL and CEILING, WATER LEAK/HEAVY FLOW and SLOW LEAK, DOOR/WINDOW/WINDOW FRAME and WINDOW PANE, SAFETY/SMOKE DETECTOR, SAFETY/CARBON MONOXIDE DETECTOR, SAFETY/WINDOW GUARD BROKEN/MISSING). 311's housing complaint types and descriptors [od-311-housing-complaint-types] (re-read at its 2026-11-21 02:15 version) carry the same HPD pairs, plus DOB, DOHMH and DEP types (see [escalation.md](escalation.md) Part 3).

### 1.4 Rent-impairing violations (MDL § 302-a)

If a "rent impairing" violation stays on HPD's record for six months after notice to the owner, no rent can be recovered for the affected premises while it remains uncorrected; a condition in a common area counts against every unit; the tenant must plead it and deposit the rent with the court clerk [st-mdl-302-a (3)]. The list of rent-impairing orders is in [nyc-rcny28-25-191]. Orders on that list that matter for the problem types: 503, 507, 511, 512-514, 516-520, 523, 524, 526, 538, 551, 567, 576-578, 580, 586, 587, 590, 592-596, 599, 600, 646-649, 665, 666, 668-670, 675, 677, 680, 682, 695, 696, 741, 742 [nyc-rcny28-25-191]. Not on the list: 501, 502, 508 (plaster), 550 (mold), 556 (paint), 568/569 (roaches, mice), 583 (water leak), 616/617 (lead), 702/1503 (detectors), 790/791 (window guards). The list cites § 27-2018 for order 567; that section has since been repealed [nyc-hmc-27-2018], so the list may be dated (`unsettled` whether it has been updated; only this version was collected).

---

## Part 2. Core problem types

Each section gives: definition, HPD orders, code sections, the facts that set the class, the deadline for each class, and coverage.

### 2.1 `leak`

**Definition** (README): active leaks, water damage, ceiling and wall water stains.

**HPD orders**

| Order | What | Classes (count, since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 583 | Repair the source and abate the evidence of a water leak | A 30,014 (9,934); B 258,314 (84,163); C 52,781 (11,906); I 17 (0) | MD | § 27-2026, 2027 HMC |
| 883 | Same, private dwelling | A 1,691; B 15,880; C 2,849 | PD | § 27-2026, 2027 HMC |
| 507 | Repair the roof so that it will not leak | A 1 (0); B 89,192 (27,558); C 19,383 (3,288) | MD | § 27-2005 (some rows D26-10.01) |
| 807 | Same, private dwelling | B 15,500; C 3,580 | PD | § 27-2005 |
| 578 | Repair the leaky and/or defective water supply pipe | A 471; B 5,694; C 1,946 | MD | § 27-2026 |
| 878 | Same, private dwelling | A 49; B 847; C 485 | PD | § 27-2026 |

Water stains left after a leak are usually written as plaster and paint orders too (508, 556); see `wall-ceiling-damage` and `peeling-paint`. A leak is also the typical "underlying defect" behind mold [nyc-hmc-27-2017 "Underlying defect"].

**Code sections**: owner must maintain the plumbing and drainage system in good repair [nyc-hmc-27-2026]; drain roofs so storm water doesn't cause dampness in walls and ceilings [nyc-hmc-27-2027 (b)]; general duty to repair [nyc-hmc-27-2005 (a), (c)]; state duty to repair [st-mdl-78].

**Facts that set the class**: `unsettled`. Order 583 is issued in A, B and C at the same time, and the sampled descriptions don't show what separates them [od-hpd-violation-types-class-notes, order 583]. Order 507 class C samples more often mention a public hall [od-hpd-violation-types-class-notes, order 507]. No collected rule sets the class. Indications of severity from process sources (not class rules):
- HPD's Emergency Repair Program follow-up checklist lists "Cascading Water Leaks" [proc-hpd-complaint-pamphlet].
- DHCR treats "water leak (cascading water, soaking electrical fixtures)" as an emergency decreased-services complaint [proc-dhcr-fact-sheet-14].

**Deadline**: whatever class HPD assigns, the default periods apply: A 90 days, B 30 days, C 24 hours [nyc-hmc-27-2115 (c)].

**Coverage**: all dwellings (583 in multiple dwellings, 883 in private dwellings) [nyc-hmc-27-2003; nyc-hmc-27-2026]. Rent-impairing: 507 and 578 are; 583 is not [nyc-rcny28-25-191].

### 2.2 `mold`

**Definition** (README): visible mould or mildew on walls, ceilings, windows or fixtures.

**HPD orders**

| Order | What | Classes (count excl. upgraded; since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 550 | Trace and repair the source and abate the visible mold condition | A 123,953 (52,327); B 145,500 (51,845), plus 65,815 upgraded rows; C 29,409 (10,485), plus 11,517 upgraded rows | MD | § 27-2017.3 HMC |

There is no private-dwelling (8xx) mold order in the data. Mildew is sometimes written under 510 "abate the nuisance" (one class A sample: "MILDEW AT BATHTUB") [od-hpd-violation-types-samples, order 510] and under 553 "cleanse" [od-hpd-violation-types], so a mildew finding may not always be order 550.

**Code sections**: [nyc-hmc-27-2017-3] (violation for visible mold); [nyc-hmc-27-2017] (definitions: visible mold includes mold behind furniture; underlying defect includes water leaks); [nyc-hmc-27-2017-1] (owner must keep premises free of indoor allergen hazards and remediate the underlying defect); mold work practices under [nyc-hmc-27-2017-9] are in [nyc-rcny28-54-04 (b)] (correct the underlying moisture or leak, isolate the area, clean with soap or detergent and water, discard what can't be cleaned).

**Facts that set the class** [nyc-hmc-27-2017-3]:

| Location | Area of visible mold (total, per room) | Class |
|---|---|---|
| Room in a dwelling unit | under 10 sq ft | A, non-hazardous (a)(1) |
| Room in a dwelling unit | 10 to under 30 sq ft ("between ten square feet and thirty square feet") | B, hazardous (a)(2) |
| Room in a dwelling unit | 30 sq ft or more | C, immediately hazardous (a)(4) |
| Room in a dwelling unit | an uncorrected or falsely certified A in the same room, still present | upgraded to B (a)(3) |
| Room in a dwelling unit | an uncorrected B, reinspected within 70 days and still present, or a falsely certified B | upgraded to C (a)(5) |
| Common area, any one room or any one level of a hallway | under 30 sq ft, and under 50 sq ft in aggregate | A, non-hazardous (b) |
| Common area | 30 sq ft or more in one room or hallway level, or 50 sq ft in aggregate | B, hazardous (b) |
| Mold on tile or grout | excluded from the dwelling-unit rule | no Article 4 mold violation (a) |

The data agrees: sampled class A descriptions say "LESS THAN 10 SQ FT", class B "MORE THAN 10" or "GREATER THAN 10 LESS THAN 30", class C "GREATER THAN 30" [od-hpd-violation-types-class-notes, order 550]. HPD's page gives the same table (it writes the B range as "10 to 29 square feet") [proc-hpd-mold-and-pests].

Boundary: the statute puts exactly 10 sq ft in B and exactly 30 sq ft in C [nyc-hmc-27-2017-3 (a)(2), (a)(4)].

Discrepancy: HPD's page says an A is upgraded to B only if HPD has reinspected within 70 days and the condition remains [proc-hpd-mold-and-pests]; the statute's A-to-B rule doesn't mention reinspection (the 70-day reinspection is in the B-to-C rule) [nyc-hmc-27-2017-3 (a)(3), (a)(5)].

**Deadline**: A 90 days, B 30 days [nyc-hmc-27-2017-3 (c)(1); nyc-hmc-27-2115 (c)]; C 21 days after service [nyc-hmc-27-2017-3 (c)(2)]. Certification within 5 days after the correction date [nyc-hmc-27-2115 (o)(2)]. HPD must do a final inspection for mold B and C [nyc-hmc-27-2115 (o)(3)].

**Coverage**: the violation rule applies to "a dwelling unit in a multiple dwelling" and common areas of a multiple dwelling (3+ units) [nyc-hmc-27-2017-3; nyc-hmc-27-2017 "Common area"]. HPD says Local Law 55 of 2018 applies to residential buildings with three or more units [proc-hpd-mold-and-pests]. One- or two-family houses: the general duty in [nyc-hmc-27-2017-1] is written for "an owner of a dwelling", but there is no PD mold order in the data and § 27-2017.3 covers only multiple dwellings: `unsettled`. Building size also changes the work practice (not the class): in buildings with 10 or more units, mold over 10 sq ft must be assessed and remediated by separate NYS-licensed mold assessor and remediator [proc-hpd-mold-and-pests]. NYCHA: see the separate NYCHA path (Ombudsperson Call Center for mold) in [escalation.md](escalation.md) [proc-nycha-nycha-repairs-process].

### 2.3 `peeling-paint`

**Definition** (README): peeling, flaking or chipping paint (lead risk in older buildings).

**HPD orders**

| Order | What | Classes (count; since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 556 | Paint with light colored paint ... all peeling paint surfaces | A 576,235 (129,035); B 14 (0, last 2023); C 7 (7) | MD | § 27-2013 |
| 856 | Paint, private dwelling | A 25,540 | PD | § 27-2013 |
| 616 | Lead-based paint hazard, presumed lead paint | C 88,773 (11,390) | MD/PD | § 27-2056.6 |
| 617 | Lead-based paint hazard, positive (tested) | C 154,574 (32,361) | MD/PD | § 27-2056.6 |
| 624 | Correct the lead-based paint tested inconclusive or ... | C 18,123 (11,321) | MD/PD | § 27-2056.6 |
| 555, 610, 611, 612, 614 | Labelled "REPEALED: LEAD-BASED PAINT" in HPD's dictionary | C | | old sections |

Lead record-keeping and turnover orders (618-623, 625, 626) are about owner duties, not a visible condition, and are left out of this problem type.

**Code sections**: painting [nyc-hmc-27-2013] (paint walls and ceilings; repaint occupied units in multiple dwellings every three years (b)(2); public parts of multiple dwellings and tenant-occupied units of one- and two-family houses (a)); lead [nyc-hmc-27-2056-6] (dwelling unit) and [nyc-hmc-27-2056-6-1] (common area, effective 2024-06-08); presumption [nyc-hmc-27-2056-5]; investigation duty [nyc-hmc-27-2056-4]; owner's duty to remediate [nyc-hmc-27-2056-3]; definitions [nyc-hmc-27-2056-2]; work practices [nyc-hmc-27-2056-11; nyc-rcny28-11-06]; Health Code lead paint [nyc-healthcode-173-13; nyc-healthcode-173-14].

**Facts that set the class**

| Facts | Result | Source |
|---|---|---|
| Peeling paint, building erected before 1960-01-01, multiple dwelling, child under 6 resides in the unit (routinely spends 10+ hours a week) | Lead-based paint presumed; peeling or on a deteriorated subsurface = class C | [nyc-hmc-27-2056-5 (a); nyc-hmc-27-2056-6; nyc-hmc-27-2056-2 (12) "Resides"] |
| Same, but in a common area of such a building | Class C | [nyc-hmc-27-2056-6-1] |
| Building erected 1960-01-01 to 1977-12-31, owner has actual knowledge of lead-based paint, child under 6 resides | Owner must investigate for peeling paint and lead hazards [nyc-hmc-27-2056-4]. The statutory presumption covers only buildings erected before 1960 [nyc-hmc-27-2056-5 (a)], but HPD says owners of 1960-1977 buildings who know there is lead-based paint must also presume it [proc-hpd-lead-based-paint]. Whether HPD writes 616 (presumed) or needs a test (617) in such buildings: `unsettled`. | [nyc-hmc-27-2056-4; nyc-hmc-27-2056-5 (a); proc-hpd-lead-based-paint] |
| Paint tested and found to be lead-based paint (1.0 mg/cm2 or more), peeling, child under 6 resides | Class C (order 617) | [nyc-hmc-27-2056-2 (7)(a); nyc-hmc-27-2056-6] |
| Presumption rebutted by certified testing, or unit exempted | No lead violation | [nyc-hmc-27-2056-5 (a), (b)] |
| No child under 6, or building built 1960 or later with no known lead | Ordinary painting violation, order 556: class A in the data (576,235 A rows vs 14 B and 7 C) | [od-hpd-violation-types, order 556; nyc-hmc-27-2013] |
| Peeling paint in a one- or two-family house | 856, class A | [od-hpd-violation-types, order 856] |

"Child of applicable age" means under six: Health Code § 173.14 ("Applicable age ... under six years of age") [nyc-healthcode-173-14 (b)] and 28 RCNY § 11-01 ("less than six years of age") [nyc-rcny28-11-01]. The HMC text itself says "under seven" for at least one year and lets the Board of Health lower it to "under six, but no lower" [nyc-hmc-27-2056-18]; HPD applies "under six" [proc-hpd-lead-based-paint]. The README's "child under 6" matches.

"Resides" means routinely spends 10 or more hours a week in the unit [nyc-hmc-27-2056-2 (12)]; HPD's inspection-request form for HP actions asks the same question [proc-court-form-hp-inspection-request].

Order 556 B and C: 14 B rows (none since 2024) and 7 C rows (all 2025-2026) exist, but the samples don't show why [od-hpd-violation-types-class-notes, order 556]: `unsettled`, treated as rare exceptions.

**Deadline**: lead class C 21 days after service, class B 30 days [nyc-hmc-27-2115 (l)(1)]; postponement up to 14 days, plus one more 14 days if the paint is stabilized [nyc-hmc-27-2115 (l)(1)]; certification with dust clearance results within 5 days after the correction date [nyc-hmc-27-2115 (l)(2)]; HPD must do a final inspection within 14 days after the correction date and, if not corrected, correct it within 45 days [nyc-hmc-27-2115 (l)(3)]. Ordinary paint (556) class A: 90 days [nyc-hmc-27-2115 (c)(1)].

**Coverage**: lead Article 14 applies to multiple dwellings, and for this article "multiple dwelling" includes a private dwelling where at least one unit is occupied by someone other than the owner or the owner's family; it doesn't apply to a unit occupied by the owner or the owner's family [nyc-hmc-27-2056-1]. HPD summarizes: multiple dwellings (3+ units) built before 1960; those built 1960-1978 if the owner knows of lead paint; tenant-occupied units in 1-2 unit private dwellings built before 1960 [proc-hpd-lead-based-paint]. Co-op or condo units occupied by the shareholder or owner: violations can be reissued on the board's application [nyc-rcny28-11-13]. NYCHA: the amlegal headers place the NYCHA exemption [nyc-hmc-27-2056] in Article 13 (janitorial), not Article 14, which would mean it doesn't exempt NYCHA from the lead article; but 28 RCNY § 11-01 calls the lead article "Article 13" (Part 4, item 8), so whether NYCHA is exempt from Article 14 is `unsettled` in law. In practice HPD has issued order 624 (lead) at a NYCHA building after a Housing Court-requested inspection [od-demo-466-columbia-st-bk]. Federal rules for Section 8 and public housing: [fed-24cfr-35-l] (public housing), [fed-24cfr-35-m] (tenant-based rental assistance); details not mapped in this draft.

### 2.4 `wall-ceiling-damage`

**Definition** (README): holes, cracks, broken or fallen plaster.

**HPD orders**

| Order | What | Classes (count; since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 508 | Repair the broken or defective plastered surfaces and paint in a uniform color | A 139,019 (26,797); B 800,630 (176,074); C 100,891 (20,519); I 2 | MD | § 27-2005 |
| 808 | Same, private dwelling | A 12,109; B 78,425; C 8,794 | PD | § 27-2005 |
| 502 | Properly repair with similar material the broken or defective ... | A 110,335; B 550,989; C 70,419 | MD | § 27-2005 |
| 802 | Same, private dwelling | A 7,402; B 42,983; C 4,674 | PD | § 27-2005 |
| 503 | Make safe by properly repairing the structural defect | B 516 (91); C 2,485 (424) | MD | § 27-2005 |
| 803 | Same, private dwelling | B 92; C 415 | PD | § 27-2005 |
| 509 | Properly secure the loose ... (tiles, fixtures, masonry) | A 16,916; B 73,248; C 7,397 | MD | § 27-2005 |

**Code sections**: [nyc-hmc-27-2005 (a), (c)] (good repair); [nyc-hmc-27-2013] (walls and ceilings painted or covered); [nyc-rcny28-25-231] (surfaces of walls and ceilings in multiple dwellings); state duty to repair [st-mdl-78].

**Facts that set the class**: `unsettled` for 508, 502 and 509. All three are issued in A, B and C at the same time, and the sampled descriptions don't show what separates the classes [od-hpd-violation-types-class-notes, orders 508, 502, 509]. Order 509 class B samples more often mention a public hall [same]. Order 503 (structural defect) is only B or C; its samples are mostly exterior walls, parapets and chimneys, with class C samples including a compromised second means of egress and a bowing exterior wall [od-hpd-violation-types-samples, order 503]. Indications of severity from process sources (not class rules): DHCR treats "collapsed or collapsing ceiling or walls" as an emergency complaint [proc-dhcr-fact-sheet-14].

**Deadline**: default periods by assigned class: A 90 days, B 30 days, C 24 hours [nyc-hmc-27-2115 (c)].

**Coverage**: all dwellings [nyc-hmc-27-2005 (a), (c)]. Rent-impairing: 503 is; 508 and 502 are not [nyc-rcny28-25-191].

### 2.5 `pests`

**Definition** (README): roaches, mice, rats, bedbugs, or signs of them (droppings, gnaw holes, nests). Record the pest in `draft_facts`.

**HPD orders**

| Order | Pest | Classes (count; since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 568 | Roaches | B 69,295 (0, last 2021-11); C 232,595 (102,968, from 2018-11) | MD | § 27-2017.4 |
| 569 | Mice | B 85,946 (0, last 2019-01); C 193,293 (77,738, from 2019-01) | MD | § 27-2017.4 |
| 567 | Rats ("evidence of rats and all underlying causes") | C 23,846 (8,782); A 1 and B 1 (1978, 1999) | MD | § 27-2017, 27-2017.1, 27-2017.4 |
| 570 | Bedbugs | B 25,499 (1,405) | MD | § 27-2017.4 |
| 566 | Vermin (other, e.g. flies) | B 72,670 (5,153); A 15 and C 1 (old) | MD | "27-2021.4 HMC" (see data errors) |
| 868 | Roaches, private dwelling | B 21,943 (5,970) | PD | § 27-2017.4 |
| 869 | Mice, private dwelling | B 24,458 (5,968) | PD | § 27-2017.4 |
| 867 | Rats, private dwelling | C 2,368 (407) | PD | § 27-2017, 27-2017.1, 27-2017.4 |
| 870 | Bedbugs, private dwelling | B 2,740 (85) | PD | § 27-2017.4 |
| 866 | Vermin, private dwelling | B 15,749 (492) | PD | "27-2021.4 HMC" |

**Code sections**: [nyc-hmc-27-2017-4] (violation for pests); [nyc-hmc-27-2017] (definitions: pest, harborage, underlying defect includes holes and entry paths); [nyc-hmc-27-2017-1] (duty to remediate); [nyc-hmc-27-2017-8] (integrated pest management work practices); [nyc-hmc-27-2019] (owner and tenants store materials so as not to give pests harborage or food); [nyc-rcny28-54-04 (a)] (IPM work practices: remove nests and debris, seal holes and gaps, door sweeps); bedbugs: [nyc-hmc-27-2018-1] (bedbug history notice with vacancy leases), [nyc-hmc-27-2018-2] (annual bedbug report), [st-rpl-235-j] (landlord must give written notice of a known bed bug infestation to the units immediately above, below and adjacent, and post notice for a common-area infestation, within 72 hours); Health Code: premises must be kept free of pests and conditions conducive to them [nyc-healthcode-151-02 (a)].

**Facts that set the class** [nyc-hmc-27-2017-4]:

| Facts | Class | Source |
|---|---|---|
| Cockroaches, mice or rats in any room of a dwelling unit in a multiple dwelling, or in a common area | C, immediately hazardous | (b) |
| Any other pest (bedbugs, flies, etc.) found to infest the premises | B, hazardous | (a) |
| Cockroaches or mice in a one- or two-family house | B in the data (868, 869 are B only); § 27-2017.4(b) covers only multiple dwellings and common areas, so the statute doesn't set this class | [od-hpd-violation-types, orders 868, 869]: class from data only |
| Rats in a one- or two-family house | C in the data (867 is C only) | [od-hpd-violation-types, order 867]: class from data only |

The data shows the switch to C when Local Law 55 took effect (2019-01-19 [nyc-hmc-27-2017-4]): roach B rows stop in 2021-11 and C rows start 2018-11; mouse B rows stop in 2019-01 and C rows start 2019-01 [od-hpd-violation-types-class-notes, orders 568, 569]. The roach B rows running to 2021-11, nearly three years after the law took effect, are not explained by the sources: `unsettled`, but irrelevant for new violations (none since 2024).

**Deadline**: C (roaches, mice, rats) 21 days after service, with a postponement of up to 14 days [nyc-hmc-27-2017-4 (c), (d)]. B (other pests, including bedbugs): 30 days, because § 27-2017.4(a) makes it a hazardous violation "pursuant to section 27-2115" [nyc-hmc-27-2017-4 (a); nyc-hmc-27-2115 (c)(2)]. HPD's table agrees (B 30 days for "all other pests besides mice, rats, or cockroaches"; C 21 days) [proc-hpd-mold-and-pests]. Private-dwelling roaches and mice (B in the data): 30 days if the B is accepted. Private-dwelling rats (C in the data): 21 days under § 27-2017.4(c), which isn't limited to multiple dwellings, but this pairing is `unsettled`.

**Coverage**: the C rule is for multiple dwellings (3+ units) and their common areas [nyc-hmc-27-2017-4 (b)]; Local Law 55 duties apply to buildings with three or more units [proc-hpd-mold-and-pests]; private dwellings get the 86x orders [od-hpd-violation-types]. Rent-impairing: 567 (rodents) is; 568, 569, 570 are not [nyc-rcny28-25-191]. Bedbug history disclosure applies to housing accommodations subject to the HMC with a vacancy lease, enforced by DHCR on the tenant's written complaint [nyc-hmc-27-2018-1 (a), (b)]; the DHCR notice form is DBB-N [proc-dhcr-form-dbb-n]. Annual bedbug filing order 1507 (A) [od-hpd-violation-types].

### 2.6 `smoke-co-detector`

**Definition** (README): missing, broken, disconnected or painted-over smoke or carbon monoxide detectors.

**HPD orders**

| Order | What | Classes (count; since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 702 | Repair or replace smoke detector | B 371,713 (80,146) | MD | § 27-2045(B)(1)(A) HMC, § 12-01, § 12-03 RCNY |
| 1503 | Repair or replace CO detector | B 303,909 (88,435); C 1 (2021) | MD/PD | § 27-2045(B)(1)(B) HMC, § 12-06, § 12-07 RCNY |
| 1502 | No CO detector or detector not operational | B 98,228 (285, last 2025-07) | MD/PD | § 27-2046.1, 2046.2 HMC (both repealed) |
| 701 | (labelled "LAW REPEALED") | B 10,443 (94, last 2025-07) | MD | § 27-2045, 2046 |
| 1001 | No smoke detector or smoke detector not operational, private dwelling | B 158 (6) | PD | § 27-2045 |
| 1002 | Repair or replace smoke detector, private dwelling | B 804 (60) | PD | "§ 27-2044" (see data errors) |
| 700 / 1501 | Post smoke detector / CO detector notice | A | MD / MD-PD | § 27-2045(b)(5) |

**Code sections**: [nyc-hmc-27-2045] (owner and occupant duties for smoke, CO and natural gas detectors); [nyc-rcny28-12-01] to [nyc-rcny28-12-14] (HPD rules: smoke 12-01 to 12-04, CO 12-05 to 12-10, natural gas 12-09.1, 12-09.2); useful life and replacement [nyc-adm-28-312-2; nyc-adm-28-312-4]; state law: every multiple dwelling, expressly including units in co-op and condo buildings, must have approved, operational smoke detecting devices in each unit [st-mdl-68 (1), (2)(a)]. Old CO sections 27-2046, 27-2046.1, 27-2046.2 were repealed effective 2019-05-01 [nyc-hmc-27-2046; nyc-hmc-27-2046-1; nyc-hmc-27-2046-2].

**Facts that set the class**: every current detector violation is class B in the data (702 and 1503) [od-hpd-violation-types]. No collected rule sets the class, so B is from data only. Facts that decide whether there is an owner violation at all:

| Fact | Effect | Source |
|---|---|---|
| Smoke detector in a class A multiple dwelling | Owner must install in each unit | [nyc-hmc-27-2045 (b)(1)(a)] |
| Smoke detector in a class B multiple dwelling | Owner installs in each unit or a central zoned system | [nyc-hmc-27-2045 (b)(1)(a)] |
| Smoke detector in a private dwelling (tenant-occupied unit of a 1-2 family house) | Paragraph (b)(1)(a) "shall not apply to private dwellings" | [nyc-hmc-27-2045 (b)(1)(a)]; yet the data has PD orders 1001 and 1002 (B): `unsettled` what they enforce |
| CO detector | Owner must install in each unit of class A, class B and private dwellings | [nyc-hmc-27-2045 (b)(1)(b)] |
| Device stolen, removed, missing or made inoperable during the current occupancy | Occupant must replace it; occupant must maintain battery-operated devices | [nyc-hmc-27-2045 (c)] |
| Device missing or inoperable at the start of a new occupancy | Owner must replace it (class A MD and private dwellings; smoke detectors in private dwellings excepted) | [nyc-hmc-27-2045 (b)(3)] |
| Device fails within 1 year from a manufacturing defect, not the occupant's fault | Owner replaces within 30 days of written notice | [nyc-hmc-27-2045 (b)(4)] |
| Device past its useful life | Owner replaces | [nyc-hmc-27-2045 (b)(2)] |
| Natural gas detectors | Required on or before 2027-01-01 | [nyc-hmc-27-2045 (b)(1)(c)] |
| Tampering ("painted-over", disconnected) | Unlawful for any person, except to change batteries or for maintenance | [nyc-hmc-27-2045 (d)] |

The occupant reimburses the owner up to $25 per smoke or CO device, $50 per combined smoke/CO device, $75 per combined three-way device, for new or replacement battery-operated devices [nyc-hmc-27-2045 (e)].

**Deadline**: class B, 30 days [nyc-hmc-27-2115 (c)(2)], taking B from the data. The repeat-inspection fee doesn't apply to inspections that only find inoperable smoke or CO detectors [nyc-hmc-27-2115 (f)(8)(ii)(D)].

**Coverage**: class A multiple dwellings (which include garden-type maisonettes built before 1954-04-18), class B multiple dwellings and private dwellings (for CO; not smoke) [nyc-hmc-27-2045 (a), (b)]. The section can be enforced by HPD, DOB, FDNY and DOHMH [nyc-hmc-27-2045 (f)]. Section 8: under NSPIRE, from 2024-12-29 every smoke detector must be hardwired or have a sealed 10-year battery; in HPD's Section 8 inspections HPD "generally holds tenants responsible" for non-functioning smoke or CO detectors where the tenant pays for electricity, and for missing smoke detectors that were present at the initial or last annual inspection [proc-hpd-s8-inspections].

### 2.7 `window`

**Definition** (README): broken windows, windows that won't close or lock, missing or broken window guards.

**HPD orders**

| Order | What | Classes (count; since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 790 | Install/replace/repair window guards (apartment) | C 130,153 (17,579) | MD | § 27-2043.1 HMC |
| 791 | Install/replace/repair window guards (public area) | C 9,355 (1,254) | MD | § 27-2043.1 HMC |
| 501 | Properly repair or replace the broken or defective ... (window samples: spring balance, sash, glass pane) | A 99,262; B 522,204; C 110,407 | MD | § 27-2005 |
| 801 | Same, private dwelling | A 9,602; B 55,725; C 5,432 | PD | § 27-2005 |
| 506 | Replace with new the missing ... (glass pane, sash) | A 42,249; B 112,209; C 23,213 | MD | § 27-2005 |
| 806 | Same, private dwelling | A 4,125; B 16,493; C 3,516 | PD | § 27-2005 |
| 522 | Remove bars or gates from non-fire-escape window | B 13,300 | MD | § 27-2005, 2007 |
| 521 | Remove bars or gates from fire escape window | B 37,085 | MD | § 27-2005, 2007 |
| 562 / 862 | Paint window frames and sashes (exterior) | A | MD / PD | § 27-2014 |

Orders 501 and 506 cover many fixtures, not only windows; 15 of 40 sampled B and 19 of 40 sampled C descriptions for 501 mention a window [od-hpd-violation-types-class-notes, order 501].

**Code sections**: window guards [nyc-hmc-27-2043-1]; Health Code [nyc-healthcode-131-15]; DOHMH window guard rules [nyc-rcny24-12-07] (where guards go) and [nyc-rcny24-12-02] to [nyc-rcny24-12-13]; general repair [nyc-hmc-27-2005]; window frames [nyc-hmc-27-2014 (a)]; illegal gates and window bars (522, 521) cite § 27-2007 [nyc-hmc-27-2007].

**Facts that set the class**

| Facts | Class | Source |
|---|---|---|
| Window guard missing, broken or not maintained, in a unit where a child 10 or under resides, or in the public-area windows of a building where such a child resides | C | [nyc-hmc-27-2043-1 (a), (e)] |
| Window guard requested in writing by the tenant (any reason) and not installed | C | [nyc-hmc-27-2043-1 (d), (e)]; HPD: tenants can request guards "for any reason" [proc-hpd-window-guards] |
| Window that opens to a fire escape, or a first-floor window that is a required means of egress | No guard required (and a guard must not be installed there) | [nyc-hmc-27-2043-1 (b), (d); nyc-rcny24-12-07 (a)] |
| More than 4 1/2 inches of open unguarded space in the window | HPD tells tenants to complain | [proc-hpd-window-guards] |
| Broken or missing glass, broken sash, spring balance, window won't close or lock (501, 506) | A, B or C: `unsettled`. The sampled descriptions don't show what separates the classes [od-hpd-violation-types-class-notes, orders 501, 506]. DHCR treats "window-glass broken (not cracked)" and "window to fire escape (does not open)" as emergency decreased-services complaints [proc-dhcr-fact-sheet-14], which is an indication, not a class rule. |
| Bars or gates on a window | B (522, 521 B in the data) | [od-hpd-violation-types] |

**Deadline**: window guards C, 21 days after service [nyc-hmc-27-2043-1 (e)]; HPD agrees [proc-hpd-clear-violations]. Other window orders: default by assigned class, A 90 days, B 30 days, C 24 hours [nyc-hmc-27-2115 (c)]. The repeat-inspection fee doesn't apply to inspections finding only illegal window gates or absent window guards [nyc-hmc-27-2115 (f)(8)(ii)(D)].

**Coverage**: window guards: owners of multiple dwellings, owners of condo units in multiple dwellings [nyc-hmc-27-2043-1 (a)], and co-op boards [nyc-healthcode-131-15 (a)(1)]. Not one- or two-family houses (the rule is limited to multiple dwellings) [nyc-hmc-27-2043-1 (a)]. Owners must find out whether a child 10 or under lives in the unit through DOHMH's annual notice [nyc-healthcode-131-15 (a)(2); proc-doh-window-guard-annual-notice]. DHCR: owners of rent stabilized or rent controlled units may collect a temporary surcharge of at most $10 per window guard [proc-dhcr-fact-sheet-25]. Other window repairs: all dwellings [nyc-hmc-27-2005].

### 2.8 `heat-hot-water`

**Definition** (README): a thermometer showing a low indoor temperature, or tap water that isn't hot.

**HPD orders**

| Order | What | Classes (count; since 2024) | MD/PD | Cited section |
|---|---|---|---|---|
| 666 | Inadequate heat | C 55,734 (21,709) | MD | § 27-2029 |
| 966 | Inadequate heat, private dwelling | C 13,158 (3,349) | PD | § 27-2029 |
| 664 | Provide adequate heat | C 9,839 (1,800) | MD | § 27-2028, 2032 |
| 964 | Same, private dwelling | C 2,702 (210) | PD | § 27-2028, 2032 |
| 670 | Inadequate hot water | C 127,658 (43,122); B 799 (last 2012); A 1 (1974) | MD | § 27-2031 |
| 970 | Inadequate hot water, private dwelling | C 28,394 (4,029); B 476 (last 2011) | PD | § 27-2031 |
| 669 / 969 | Provide hot water (no system) | C | MD / PD | § 27-2031 |
| 577 / 877 | Inadequate hot water supply (volume) | B 12,400 / 3,238; C 11,628 / 5,448 | MD / PD | § 27-2024 |
| 674 | Illegal device (on a heating system) | C 1,020 | MD | § 27-2029 |
| 510 | Abate the nuisance (class C samples: scalding hot water over 130 F) | C 139,599 overall, mixed conditions | MD | § 27-2005 & 309 MDL |

**Code sections**: [nyc-hmc-27-2028] (central heat required in multiple dwellings and tenant-occupied 1-2 family houses); [nyc-hmc-27-2029] (minimum temperatures; no devices that disable heat); [nyc-hmc-27-2031] (hot water); [nyc-hmc-27-2032] (gas or electric heaters); [nyc-hmc-27-2033-1] (heat inspections and temperature-reporting devices); penalties [nyc-hmc-27-2115 (k)]; state: MDL § 79 sets a lower floor (68 F from 6 a.m. to 10 p.m. when it is below 55 F outside; 55 F from 10 p.m. to 6 a.m. when it is below 40 F outside) and requires heat sufficient for the minimums set by local law [st-mdl-79 (1)]; the HMC night minimum (62 F at any outside temperature) is higher.

**Facts that set the violation** (all current heat and hot water violations are class C [od-hpd-violation-types]; heat violations are "immediately hazardous" in [nyc-hmc-27-2115 (k)(1)(iv)]):

| Fact | Rule | Source |
|---|---|---|
| Date | Heat season is October 1 to May 31 | [nyc-hmc-27-2029 (a)] |
| 6 a.m. to 10 p.m. | At least 68 F indoors, but only when the outside temperature is below 55 F | [nyc-hmc-27-2029 (a)(1)] |
| 10 p.m. to 6 a.m. | At least 62 F indoors, regardless of outside temperature | [nyc-hmc-27-2029 (a)(2)] |
| Room | "every portion ... used or occupied for living purposes"; HPD measures in the room the tenant says is coldest, except the kitchen or bathroom, "since heat is not required in these rooms" | [nyc-hmc-27-2029 (a); proc-hpd-abcs-of-housing-tenants] |
| Outside temperature at inspection | HPD can only issue a daytime violation if it is below 55 F outside at the time of inspection | [proc-hpd-abcs-of-housing-tenants] |
| Hot water temperature | At least 120 F constant; 110 F minimum allowed at baths and showers with anti-scald mixing valves | [nyc-hmc-27-2031] |
| Hot water hours | HMC: 120 F "at all times between the hours of six a.m. and midnight" [nyc-hmc-27-2031]; MDL: hot water "during all hours" in covered multiple dwellings, no temperature [st-mdl-75 (3)]; HPD: "24 hours a day, 365 days a year" [proc-hpd-abcs-of-housing-tenants] | partly `unsettled` (see below) |
| Too hot | Class C samples of order 510 cite hot water over 130 F as a nuisance | [od-hpd-violation-types-samples, order 510] |

Partly `unsettled`: hot water between midnight and 6 a.m. The collected HMC § 27-2031 sets the 120 F minimum for 6 a.m. to midnight [nyc-hmc-27-2031]. State law requires hot and cold water "at all times of the year, during all hours" in multiple dwellings of three or more stories erected on or after 1929-04-18 and all dwellings erected after 1951-01-01 (with an exception for pre-1929 buildings that never had it), but sets no temperature [st-mdl-75 (3)]. HPD and DHCR say 120 F 24 hours a day [proc-hpd-abcs-of-housing-tenants; proc-dhcr-form-hhw-1; proc-dhcr-fact-sheet-15]. So: no hot water at all overnight is a violation in buildings covered by MDL § 75(3); water that is warm but under 120 F overnight is `unsettled`. The app's weather data (open-data workstream) is needed for the daytime rule: the outdoor temperature at the hour of the reading.

**Deadline**: no correction period. Penalties run from the day the notice is affixed: $350-$1,250 per day for a first violation, $500-$1,500 per day for a repeat within two consecutive heat seasons; a first violation's penalty is satisfied by correcting within 24 hours of the notice and paying $250 within 10 days [nyc-hmc-27-2115 (k)(1)(i)-(ii), (k)(2)]. HPD: "Class C: Heat and Hot Water ... No time" [proc-hpd-clear-violations]. HPD's heat page still says "$250-$500 dollars per day for each initial heat or hot water violation" [proc-hpd-heat-hot-water], which conflicts with the statute's $350-$1,250 (see data errors). A $200 fee applies to the third and later inspections in a season that find a heat violation [nyc-hmc-27-2115 (k)(1)(iv); proc-hpd-heat-hot-water].

**Coverage**: heat: every multiple dwelling and every tenant-occupied one- or two-family house [nyc-hmc-27-2028]. Hot water: every unit in a multiple dwelling or a tenant-occupied one- or two-family house [nyc-hmc-27-2031]. Rent-impairing: 665, 666, 669, 670 are [nyc-rcny28-25-191]. NYCHA: report to NYCHA's Customer Contact Center, not 311's HPD complaint [proc-311-heat-hot-water-complaint].

---

## Part 3. Extended problem types

(Shallower. Drafted after the core types.)

For every extended type, the class of the main repair orders is **`unsettled`**: the orders below are issued in more than one class at the same time and the sampled descriptions don't show what separates the classes [od-hpd-violation-types-class-notes]. Where an order has only one class in the data, that is noted. The deadline then follows the default periods by whatever class HPD assigns: A 90 days, B 30 days, C 24 hours [nyc-hmc-27-2115 (c)].

### 3.1 `exposed-wiring`

- **Orders**: 689 repair/abate unsafe wires (A 1,205; B 29,277; C 10,860) and private-dwelling 989 (A 137; B 3,786; C 860), citing § 27-2005, 2006, 2037; 688 provide supply of electricity to fixtures (A 1,272; B 22,826; C 13,578) and 988 [od-hpd-violation-types]. One 989 C sample is "EXTENTION CORDS TRAVELING FROM ELECTRIC ..." [od-hpd-violation-types-samples, order 989]. Uncovered outlets in public parts: § 27-2046.3, class A by statute [nyc-hmc-27-2046-3 (b)]; HPD writes these under the general order 506 (class A samples: "MISSING SAFETY CAPS/ COVERS FOR ELECTRICAL OUTLETS AT ... PUBLIC HALL") [od-hpd-violation-types-samples, order 506].
- **Sections**: owner must equip every dwelling for electric lighting and maintain fixtures and required outlets [nyc-hmc-27-2037]; owner responsible for maintenance of electrical installations [nyc-elec-x-81-3-1-owner-responsibility]; good repair [nyc-hmc-27-2005].
- **Class facts**: `unsettled` for 689/688 (class B 689 samples mention "UNSAFE ELECTRIC WIRING CONDITION"; class A samples mention public halls) [od-hpd-violation-types-class-notes, orders 689, 688]. Uncovered public-area outlet: A [nyc-hmc-27-2046-3 (b)].
- **Coverage**: all dwellings [nyc-hmc-27-2037]; outlet covers only multiple dwellings [nyc-hmc-27-2046-3 (a)].

### 3.2 `plumbing-fixture`

- **Orders** (all cite § 27-2026) [od-hpd-violation-types]: 579 leaky or defective faucets (A 13,780; B 121,028; C 9,265; class C samples mention hot water); 593 repair the flushing apparatus of the toilet (A 3,746; B 29,160; C 2,578); 596 replace defective sink, toilet, wash tub (A 3,881; B 20,672; C 4,172); 598 broken or loose connection (A 2,500; B 42,721; C 9,245; class C samples mention active leaks); 595 remove obstruction from toilet (C only, 5,025); 591 reset toilet bowl (A only, 17,611); 592 defective flush pipe (A only); 594 leaky flush pipe connection (A only); 534 seat for toilet (A only, § 27-2005). Private-dwelling mirrors: 879, 893, 895, 896, 898.
- **Sections**: maintain plumbing and drainage, including toilets, sinks and fixtures [nyc-hmc-27-2026]; state plumbing and drainage [st-mdl-77] (not read in detail).
- **Class facts**: `unsettled` for 579, 593, 596, 598 [od-hpd-violation-types-class-notes]. Single-class orders: 595 C (24 hours), 591/592/594/534 A (90 days) [od-hpd-violation-types]. DHCR treats "no operable toilet" as an emergency complaint [proc-dhcr-fact-sheet-14].
- **Coverage**: all dwellings [nyc-hmc-27-2026]. Rent-impairing: 592, 593, 594, 595, 596 [nyc-rcny28-25-191].

### 3.3 `radiator`

- **Orders**: no radiator-specific order. Radiator conditions appear in 501 and 801 repair (for example "RADIATOR RELEASING STEAM AND WATER"), 509/809 secure loose (for example "LOOSE CAST IRON RADIATOR", sampled in A, B and C), 506 replace missing radiator shut-off valve (B, C), 896 replace missing radiator, 554/861 paint metal radiator (A), and 510 C "FREE STANDING RADIATOR" [od-hpd-violation-types-samples]. HPD complaint category PLUMBING/RADIATOR [od-hpd-complaint-categories].
- **Sections**: good repair [nyc-hmc-27-2005]; steam radiator inspections, HMC Article 15: at least every 2 years in a "covered multiple dwelling", meaning one with at least one unit where a child under 6 resides, inspecting each radiator for safe operation and signs such as leaking water or corrosion [nyc-hmc-27-2056-21; nyc-hmc-27-2056-22]; notice to tenants [nyc-hmc-27-2056-24] (not read in detail). Heat itself: see `heat-hot-water`.
- **Class facts**: `unsettled` (same multi-class orders).
- **Coverage**: repair duty all dwellings; Article 15 inspections only multiple dwellings with a child under 6 [nyc-hmc-27-2056-21].

### 3.4 `flooring`

- **Orders**: 502 repair with similar material (samples include "BROKEN OR DEFECTIVE CERAMIC FLOOR TILES") [od-hpd-violation-types-class-notes, order 502]; 535 remove floor covering (A 524; B 1,263) and 835 "remove the torn and/or loose floor covering" (A 61; B 214); 657 broken floor, pave with concrete (A only, 279); 510 A samples "LEFTING [sic] VINYL FLOOR TILES" [od-hpd-violation-types; od-hpd-violation-types-samples].
- **Sections**: good repair [nyc-hmc-27-2005].
- **Class facts**: `unsettled`. Process indications: DHCR treats a "collapsing floor" as an emergency complaint [proc-dhcr-fact-sheet-14]; DHCR treats frayed carpet that is not a tripping hazard as de minimis [proc-dhcr-fact-sheet-37].
- **Coverage**: all dwellings.

### 3.5 `blocked-exit`

- **Orders** [od-hpd-violation-types]: 538 remove encumbrances (B 85,507; A and C only before 1989) and 539 (B 90,221), private-dwelling 838 and 839 (B); 524 fire passageway obstructed (B only); 526 remove illegal fastening (B 18,307; C 52,528; samples include double-cylinder locks at building entrances); 549 remove excessive storage (B 1,337; C 705); 521 remove bars or gates from fire escape window (B); fire escape defects 512-520 (B and C).
- **Sections**: tenants and others must not obstruct fire escapes, public halls or any required means of egress [nyc-hmc-27-2007 (c)]; public halls, stairs, corridors and passageways used as egress must be kept free of encumbrances; doors or gates with key locks on egress passageways are prohibited [nyc-rcny28-25-221 (a), (b)]; Fire Code: all required means of egress kept free of obstructions [nyc-fc-x-1027-3-unobstructed-and-unimpeded-egress-required]; no bicycles, strollers or other personal property stored in residential hallway corridors [nyc-fc-x-1027-4-5-personal-property]; fire escape components maintained, and bars or grilles over fire escape openings kept in good working order [nyc-fc-x-1027-7-1-maintenance; nyc-fc-x-1027-7-2-window-gates]; fire escapes painted [nyc-hmc-27-2014 (b)].
- **Class facts**: encumbrances B (538/539 B in the data; class from data only); illegal fastening and excessive storage `unsettled` (B and C concurrent) [od-hpd-violation-types-class-notes, orders 526, 549].
- **Who to tell**: 311 takes blocked fire escape or secondary exit reports, including locked or sealed exits; call 911 for an emergency [proc-311-blocked-exit-fire-escape].
- **Coverage**: [nyc-rcny28-25-221] applies to multiple dwellings; the Fire Code and § 27-2007 apply to "any person". Rent-impairing: 512-514, 516-520, 523, 524, 526, 538 [nyc-rcny28-25-191] (515 is not on the list).

### 3.6 `door-lock`

- **Orders** [od-hpd-violation-types]: 692 no lock and key to apartment (A only, 10,726) and 992 (A); 546 remove double cylinder lock (C only, 5,510) and 846 (C); 690 no peephole (A) and 990 (A); 530 make doors self-closing (C 338,176 since 2019; B rows end 2024-05) and 536 door not self-closing (C 25,453 since 2022; A rows end 2022); 501 repair "MORTISE LOCK ASSEMBLY" (sampled in C) [od-hpd-violation-types-samples].
- **Sections**: key lock and at least one key for each unit entrance door; in a class A multiple dwelling a heavy duty latch set, a heavy duty dead bolt (key outside, thumb-turn inside) and a chain door guard [nyc-hmc-27-2043]; peephole in every unit entrance door, with exceptions for owner-occupied one- and two-family homes [nyc-hmc-27-2041]; self-closing doors [nyc-hmc-27-2041-1]; building entrance doors and locks [st-mdl-50-a; nyc-rcny28-25-151] (not read in detail).
- **Class facts**: no lock/key A (90 days); double-cylinder lock C (24 hours); self-closing door C, 14 days by statute [nyc-hmc-27-2041-1 (b)], with HPD reinspection no later than 20 days after the correction period [nyc-hmc-27-2041-1 (c)]. Process indication: DHCR treats a "broken or inoperative apartment front door lock" as an emergency complaint [proc-dhcr-fact-sheet-14]. The repeat-inspection fee doesn't apply to inspections finding only double cylinder locks on entry doors [nyc-hmc-27-2115 (f)(8)(ii)(D)].
- **Coverage**: locks all dwellings, extra hardware for class A multiple dwellings [nyc-hmc-27-2043]; self-closing doors in multiple dwellings required to have them under § 28-315.10 or other law [nyc-hmc-27-2041-1 (a); nyc-adm-28-315-10]. Changing or plugging a tenant's lock without giving a key is listed as harassment [nyc-hmc-27-2004 (a)(48)(f)].

### 3.7 `garbage` (common areas)

- **Orders** [od-hpd-violation-types]: 552 remove accumulation of refuse or rubbish (A 5,525; B 45,719; C 4,784) and 852; 551 remove accumulation of rubbish, water and disinfect (B 6,213; C 3,407) and 851 (samples: raw sewage); 553 cleanse (A only); 571 provide garbage cans (B only) and 871 (A only, § 27-2023); 572 storage of garbage cans (A).
- **Sections**: cleaning of roofs, yards and open spaces [nyc-hmc-27-2010], interior shared space [nyc-hmc-27-2011] (titles); receptacles of sufficient size and number for 72 hours of waste, with tight covers [nyc-hmc-27-2021 (a)]; no accumulation outside lawful receptacles and daily collection in multiple dwellings [nyc-hmc-27-2022 (a)-(c)]; one- and two-family houses [nyc-hmc-27-2023] (title); Health Code: garbage in tightly covered, pest-resistant receptacles [nyc-healthcode-151-02 (b)]; HPD rules [nyc-rcny28-25-201] (title).
- **Class facts**: `unsettled` for 552 and 551 (class A and C samples of 552 mention yards) [od-hpd-violation-types-class-notes, orders 552, 551]. Garbage cans B (571 B only; from data).
- **Coverage**: §§ 27-2021, 2022 multiple dwellings and dwellings; 27-2023 one- and two-family. Rent-impairing: 551 [nyc-rcny28-25-191]. Garbage that feeds pests also supports a pest violation [nyc-hmc-27-2019; nyc-hmc-27-2017 "Harborage"].

### 3.8 `appliance` (stove, refrigerator)

- **Orders** [od-hpd-violation-types; od-hpd-violation-types-samples]: 742 no gas, "provide an adequate supply of gas to the fixtures" at the stove or range (B 12,152; C 45,607; § 27-2070) and private-dwelling 1042 (B 4,915; C 8,176; § 27-2073); 744 provide stove knob safety covers (B only, 154; § 27-2046.4); broken refrigerator or stove parts appear under 505 and 801/805 (for example refrigerator door gaskets, sampled in A and B) and 506 (missing refrigerator handle, A).
- **Sections**: owner of a multiple dwelling must provide every kitchen with gas or electricity for cooking and a sink with running water [nyc-hmc-27-2070 (a), (b)]; kitchens in one- and two-family houses [nyc-hmc-27-2073] (title); stove knob covers or locking knobs for units where a child under 6 resides [nyc-hmc-27-2046-4]. The HMC text collected does not require the owner to provide a refrigerator or stove as such: `unsettled`. For rent-regulated units, DHCR says owner-provided equipment such as a refrigerator, stove or air conditioner must be kept in good working order, repaired at the owner's expense or replaced with comparable working equipment [proc-dhcr-fact-sheet-3].
- **Class facts**: no gas `unsettled` (B and C concurrent) [od-hpd-violation-types-class-notes, order 742]; knob covers B (from data).
- **Coverage**: § 27-2070 multiple dwellings; § 27-2073 one- and two-family. Rent-impairing: 741, 742 [nyc-rcny28-25-191]. Gas leak: tenants call 911 first, then the gas utility, before the owner [nyc-hmc-27-2005 (f)].

### 3.9 `elevator`

- **Orders**: HPD has no elevator repair order in the data except 691 no mirror in elevator (A, § 27-2042) [od-hpd-violation-types]. Elevator repair is DOB's: DOB orders the owner to restore service and, after its compliance period, refers the condition to HPD, which may contract the repair itself or go to Housing Court (Local Law 101 of 2015, effective 2016-07-01) [proc-hpd-elevators]. HPD's rule for DOB referrals of immediately hazardous elevator violations in multiple dwellings considers whether units are served by another working elevator [nyc-rcny28-48-01]; HPD reports on referred elevators [nyc-hmc-27-2129-1] (title).
- **Sections**: DOB periodic inspection and testing [nyc-adm-28-304-1; nyc-adm-28-304-5] (titles); elevator safety [nyc-adm-28-315-4]; state [st-mdl-51] (title).
- **Who to tell**: 311 Elevator or Escalator Complaint (not working, defective, not inspected); 911 for someone stuck, an open shaft, or an elevator moving with doors open; NYCHA elevators go to NYCHA [proc-311-elevator-complaint]. DHCR treats "all elevators inoperable" as an emergency complaint [proc-dhcr-fact-sheet-14]; elevator service is a required service under rent regulation [proc-dhcr-fact-sheet-3].
- **Class / deadline**: `unsettled` (DOB's violation classes and deadlines were not mapped in this draft).

### 3.10 `stairs`

- **Orders**: no stairs-specific repair order; stairs conditions appear in 509 secure loose (for example "LOOSE MARBLE TREAD ... AT PUBLIC HALL STAIRS", sampled in C; "LOOSE HANDRAIL" in B), 806 replace missing handrails (C sample), 835 torn floor covering at stair treads (A, B), 538 encumbrances at public hall stairs (B), 219 open treads (A, § 190 MDL), 222 cellar stair enclosure (B, § 242 MDL) [od-hpd-violation-types-samples]. HPD complaint category FLOORING/STAIRS/STAIRS [od-hpd-complaint-categories].
- **Sections**: good repair [nyc-hmc-27-2005]; MDL § 52: in multiple dwellings erected after 1929-04-18 (and exterior stairs altered or erected after 1951-01-01), stairs must have proper balustrades or railings and be kept in good repair and free from encumbrance; stairs wider than 3 ft 8 in need a handrail on each side [st-mdl-52 (1)]; egress kept clear [nyc-rcny28-25-221 (a)].
- **Class facts**: `unsettled`.
- **Coverage**: all dwellings (repair); MDL § 52 by building date as above.

### 3.11 `no-water-sewage`

- **Orders** [od-hpd-violation-types]: 576 inadequate cold water (A 467; B 9,542; C 7,773; § 27-2024) and 876; 577 inadequate hot water supply, volume (B, C); 551 and 851 cleanse and disinfect after removing sewage (B, C); 649 remove obstructions, drains (B 40,862; C 8,296; class B samples mention bathtubs, class C yards) and 949; 595 remove obstruction from toilet (C only); 586 separate house sewer, 587 remove cesspool (A, rare).
- **Sections**: owner must provide pure, wholesome water at sufficient pressure for all fixtures [nyc-hmc-27-2024] and appliances to distribute it to every unit at all hours [nyc-hmc-27-2025]; plumbing and drainage in good repair [nyc-hmc-27-2026]; state water supply [st-mdl-75] (title). Water shut off because the landlord didn't pay: a tenant who lawfully pays the utility or water provider for service the landlord was responsible for can deduct that payment from future rent [st-rpl-235-a (1)]; utility shutoff rules for multiple dwellings [st-psl-116] (title).
- **Class facts**: `unsettled` for 576, 551, 649 [od-hpd-violation-types-class-notes]; 595 C. Process indications: HPD's ERP follow-up list includes "No Water" [proc-hpd-complaint-pamphlet]; DHCR treats "no water apartment wide" and "no operable toilet" as emergencies [proc-dhcr-fact-sheet-14].
- **Who to tell**: 311 "No Water, Low Water Pressure, or Water Temperature Complaint" and "Sewage Leak or Odor Indoors" [proc-311-no-water-pressure-temperature; proc-311-sewage-leak-indoors] (titles).
- **Coverage**: all dwellings. Rent-impairing: 576, 577, 551, 586, 587, 595, 649 [nyc-rcny28-25-191]. RPAPL Article 7-A covers "lack of ... running water ... or adequate sewage disposal facilities" lasting five days [st-rpapl-770 (1)].

---

## Part 4. Errors and inconsistencies found in the collected data

Found while drafting. "Collection" items are problems in how a file was captured; "source" items are problems or conflicts in the official sources themselves; "data" items are in HPD's open data.

| # | Kind | File (id) | What | Effect on this map |
|---|---|---|---|---|
| 1 | Collection | `open-data/` | `manifest.jsonl` did not exist for most of the drafting; it appeared later. | All `od-` ids were re-checked against it and resolve. |
| 2 | Collection | [nyc-hmc-27-2115] | Subdivision (o)(5) is cut off mid-sentence: "... in the rules established pursuant to section" is followed directly by "(i) That the condition ...". The text naming the penalty for Article 4 work-practice failures appears to be missing. | Article 4 work-practice penalty not mapped. Re-capture from amlegal. |
| 3 | Collection or source | [nyc-hmc-27-2056-6-1] | The common-area section repeats the dwelling-unit sentence of § 27-2056.6 after its own sentence, with no space ("subsurface.The existence ..."). | None (both sentences say class C); check against amlegal. |
| 4 | Collection | `process/local/contacts-finding-aid.md` | Not in `process/manifest.jsonl`. | Not cited as a source here. |
| 5 | Source | [nyc-hmc-27-2031] vs [proc-hpd-abcs-of-housing-tenants], [proc-hpd-heat-hot-water], [proc-dhcr-form-hhw-1], [proc-dhcr-fact-sheet-15] | The collected HMC text requires 120 F hot water "at all times between the hours of six a.m. and midnight"; HPD and DHCR say 24 hours a day, 365 days a year (HHW-1 attributes this to "State Law"; MDL § 75(3) [st-mdl-75] requires hot water "during all hours" in covered buildings but sets no temperature). | Overnight hot water marked `unsettled` (EO row for 00:00-06:00). |
| 6 | Source | [proc-hpd-heat-hot-water] vs [nyc-hmc-27-2115 (k)(1)(i)] | HPD's heat page says "$250-$500 dollars per day for each initial heat or hot water violation"; the statute says $350-$1,250 per day (repeat $500-$1,500). The HPD page looks out of date. | Statute used. |
| 7 | Source | [nyc-hmc-27-2056-18] vs [nyc-healthcode-173-14], [nyc-rcny28-11-01] | The HMC still reads "under seven years of age" with power for the Board of Health to lower it; the Health Code and HPD rule say under six. Consistent if the Board of Health acted, but the Board's determination itself wasn't collected. | "Under 6" used, per Health Code and HPD. |
| 8 | Source | [nyc-rcny28-11-01] | Refers to the lead article as "Article 13 of Subchapter 2 of Chapter 2 of Title 27"; the amlegal headers put lead in Article 14 and janitorial services (including the NYCHA exemption, [nyc-hmc-27-2056]) in Article 13, and [nyc-hmc-27-2115 (l)] also says "article fourteen". | Whether the NYCHA exemption in § 27-2056 was ever meant to cover lead is `unsettled`; flagged for the owner. |
| 9 | Source | [nyc-rcny28-25-191] | The rent-impairing list cites § 27-2018 for order 567 (rodents); § 27-2018 was repealed effective 2019-01-19 [nyc-hmc-27-2018]. | The list may be outdated; used as collected. |
| 10 | Source | [proc-hpd-mold-and-pests] vs [nyc-hmc-27-2017-3 (a)(3)] | HPD says a class A mold violation is upgraded to B only after a reinspection within 70 days; the statute's A-to-B rule has no reinspection condition (the 70-day reinspection is in the B-to-C rule). | Statute used. |
| 11 | Source | [proc-hpd-complaint-pamphlet] | ERP follow-up checklist says "No Heat (under 64 degrees)", which matches neither statutory minimum (68 F day, 62 F night). HPD's heat page also uses 64 F as a fee trigger [proc-hpd-heat-hot-water]. | Treated as an HPD operational threshold, not the legal standard. |
| 12 | Source | [proc-court-fees] | The Housing Court fee page has no HP action line; the $45 figure comes only from a 2017 nonprofit sheet [proc-np-hca-infosheet-hp-2017]. | HP fee `unsettled`. |
| 13 | Data (HPD) | `od-hpd-violation-types` orders 566, 866 | Cited section "§ 27-2021.4 HMC" (also in HPD's dictionary `dict_section`). No § 27-2021.4 exists in the collected HMC; § 27-2021 is waste receptacles and pests are §§ 27-2017 to 27-2017.12. | Mapped to § 27-2017.4(a) by subject; the cited section is likely an HPD error. |
| 14 | Data (HPD) | order 1002 | "Repair or replace smoke detector" (private dwelling) cites § 27-2044 (fire protection in old law tenements); the smoke detector section is § 27-2045. | Treated as § 27-2045. |
| 15 | Data (HPD) | orders 1502, 701, one 1503 C row | Cite §§ 27-2046, 27-2046.1, 27-2046.2, repealed effective 2019-05-01, but were issued until 2025-07. | Current orders are 702 and 1503. |
| 16 | Data (HPD) | order 568 | Roach class B rows run to 2021-11, almost three years after § 27-2017.4(b) made roaches class C (effective 2019-01-19). | No effect for new violations (no B since 2024). |
| 17 | Data (HPD) | order 556 | 14 class B and 7 class C rows (C all 2025-2026) of an otherwise class A paint order. | Treated as exceptions. |
| 18 | Source | [proc-hpd-clear-violations] | The "Violation Reissuance" link points to a personal SharePoint/OneDrive URL rather than nyc.gov. | None. |
| 19 | Source vs data | [nyc-hmc-27-2045 (b)(1)(a)] vs orders 1001, 1002 | The statute says the owner's smoke detector duty doesn't apply to private dwellings, but HPD issues private-dwelling smoke detector orders (1001, 1002, class B). | Marked `unsettled`. |

README pointers checked along the way: RPAPL 7-C doesn't apply in NYC [st-rpapl-796-a (4)] and 7-D can't be brought in the five NYC counties [st-rpapl-797 (3)], as the README says. Window guards apply where a child "ten years of age or under" resides [nyc-hmc-27-2043-1 (a)], as the README says. Lead: "child under 6" matches the Health Code and HPD (see item 7); the README's "pre-1960 building" matches the presumption [nyc-hmc-27-2056-5 (a)], but 1960-1977 buildings with known lead paint are also covered [nyc-hmc-27-2056-4].
