# The decision matrix

For each problem the app recognises: the situations it can be in, the facts that tell them apart, and what the law says happens in each. This page is generated from `data/problem-map/expected-outcomes.csv` by `scripts/render_decision_matrix.py`; don't edit it by hand.

**This is a draft.** It was assembled overnight from the law text and HPD's records. Nobody with legal training has reviewed it.

## How to read it

- **Situation:** what the tenant has.
- **Deciding facts:** what the app needs to know to land on this row. Some come from the photo, some from the building lookup, some from a question to the tenant.
- **Class:** how serious HPD treats it. A is non-hazardous, B is hazardous, C is immediately hazardous.
- **Landlord's deadline:** how long the landlord has to fix it. The clock starts when HPD issues a violation notice after an inspection, not when the tenant reports it.
- **How sure:**
  - *Settled*: the law states the class and deadline.
  - *From HPD's records*: the law doesn't state the class, but HPD has consistently issued this class.
  - *Class not settled*: it is a violation, but HPD issues it in more than one class and the rule for choosing isn't published. The inspector decides.
  - *Not settled*: we couldn't establish the outcome from the sources collected.

Default deadlines by class: A 90 days, B 30 days, C 24 hours. Some problems have their own: 21 days for Class C mould, pests, lead paint and window guards; no grace period at all for heat and hot water.

## At a glance

| Problem | Situations | Settled or from HPD's records | Main deciding facts |
|---|---|---|---|
| Mould | 11 | 9 | Area in square feet; where it is; whether an earlier violation went unfixed |
| Peeling paint (and lead) | 10 | 8 | Year the building was built; whether a child under 6 lives there |
| Pests | 10 | 9 | Which pest |
| Windows and window guards | 9 | 8 | Whether a child aged 10 or under lives there; type of window |
| Heat and hot water | 12 | 10 | Indoor, outdoor and water temperature; time of day; time of year |
| Smoke and carbon monoxide detectors | 7 | 4 | Which device; why it is missing or not working |
| Leaks | 6 | 0 | Whether water is cascading; where it comes from |
| Wall and ceiling damage | 5 | 0 | Collapse or structural damage, against hairline cracks |

The other 11 problem types (wiring, plumbing, doors and so on) are at the end.

## Mould

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-007 | visible mold under 10 sq ft in a room | multiple dwelling (3+ units) | mold area sqft<10; not on tile or grout | yes | A | 90 days from mailing of notice | Settled |
| EO-008 | visible mold 10 to under 30 sq ft in a room | multiple dwelling (3+ units) | 10≤ mold area sqft<30 | yes | B | 30 days from mailing of notice | Settled |
| EO-009 | visible mold exactly 10 sq ft in a room | multiple dwelling (3+ units) | mold area sqft=10 | yes | B | 30 days from mailing of notice | Settled |
| EO-010 | visible mold 30 sq ft or more in a room | multiple dwelling (3+ units) | mold area sqft≥ 30 | yes | C | 21 days after service | Settled |
| EO-011 | uncorrected class A mold still present in same room after certification period | multiple dwelling (3+ units) | prior class=A; not certified or falsely certified | yes | B | 30 days from mailing of notice | Settled |
| EO-012 | uncorrected class B mold, reinspected within 70 days, still present | multiple dwelling (3+ units) | prior class=B; reinspection within 70 days; or false certification | yes | C | 21 days after service | Settled |
| EO-013 | visible mold in hallway or laundry room, under 30 sq ft per room or hallway level and under 50 sq ft total | multiple dwelling (3+ units) | mold area sqft<30 per room/level and <50 aggregate | yes | A | 90 days from mailing of notice | Settled |
| EO-014 | visible mold in common area, 30 sq ft or more in one room or hallway level, or 50 sq ft total | multiple dwelling (3+ units) | mold area sqft≥ 30 per room/level or ≥ 50 aggregate | yes | B | 30 days from mailing of notice | Settled |
| EO-015 | surface mould only on intact tile, grout or caulk (e.g. bathtub caulk line) | multiple dwelling (3+ units) | surface=tile, grout or caulk; caulk/tile intact; no mould behind; not recurring | no owner mould violation; tenant's cleaning duty | n/a (553 Class A if HPD cites it) | n/a | Settled |
| EO-016 | visible mold in a one- or two-family house | one- or two-family house, tenant-occupied unit | — | unsettled | unsettled | unsettled | Not settled |
| EO-017 | visible mold, NYCHA apartment | NYCHA | — | unsettled | same area rules as private buildings (A <10, B 10-<30, C ≥ 30 sq ft) | unsettled | Not settled |

Notes:
- **EO-007:** certify within 5 days after correction date
- **EO-008:** 10+ unit buildings: NYS-licensed assessor and remediator for >10 sq ft
- **EO-009:** boundary case
- **EO-010:** postponement up to 14 days
- **EO-011:** HPD page adds a 70-day reinspection condition not in the statute text
- **EO-012:** no postponement for a C issued on reinspection of an uncorrected B
- **EO-014:** common-area mold tops out at B
- **EO-015:** Caulk is not named in the statute; grouped with tile and grout per HPD practice (553 cleanse orders name caulking with tiles and grout) and the owner's decision. Damaged caulk or mould behind it is the owner's problem.

## Peeling paint (and lead)

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-018 | peeling paint, building erected before 1960, child under 6 resides | multiple dwelling (3+ units) | year built<1960; child under 6 resides=yes (10+ hours/week) | yes | C | 21 days after service | Settled |
| EO-019 | peeling paint in hallway, building erected before 1960, child under 6 lives in building | multiple dwelling (3+ units) | year built<1960; child under 6 resides=yes | yes | C | 21 days after service | Settled |
| EO-020 | peeling paint, building 1960-1977, child under 6, owner knows of lead paint | multiple dwelling (3+ units) | 1960≤ year built<1978; owner actual knowledge=yes; child under 6 resides=yes | yes if paint is lead-based | C if lead-based paint; else A (556) | 21 days if C; 90 days if 556 A | Not settled |
| EO-021 | peeling paint, no child under 6 in the unit | multiple dwelling (3+ units) | child under 6 resides=no | yes | A | 90 days from mailing of notice | Settled |
| EO-022 | peeling paint, building erected 1978 or later | multiple dwelling (3+ units) | year built≥ 1978 | yes | A | 90 days from mailing of notice | Settled |
| EO-023 | peeling paint, pre-1960 house with tenant, child under 6 resides | one- or two-family house, tenant-occupied unit | year built<1960; child under 6 resides=yes | yes | C | 21 days after service | Settled |
| EO-024 | peeling paint in a one- or two-family house, no child under 6 | one- or two-family house, tenant-occupied unit | child under 6 resides=no | yes | A | 90 days from mailing of notice | Settled |
| EO-025 | peeling paint in unit occupied by the owner or owner's family | any | owner occupied unit=yes | no lead violation (Article 14 does not apply) | n/a | n/a | Settled |
| EO-026 | peeling paint, unit tested negative or exempted from presumption | multiple dwelling (3+ units) | presumption rebutted or exemption granted | no lead violation; 556 possible | A (556) | 90 days from mailing of notice | Settled |
| EO-027 | peeling paint, NYCHA apartment, child under 6 | NYCHA | child under 6 resides=yes | unsettled | C if issued | unsettled | Not settled |

Notes:
- **EO-018:** HPD final inspection within 14 days after correction date; work practices 27-2056.11
- **EO-020:** whether HPD presumes (616) or needs a test (617) is unsettled
- **EO-021:** class from data, not a published rule
- **EO-022:** lead article not triggered by age

## Pests

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-033 | cockroaches in apartment | multiple dwelling (3+ units) | pest=roach | yes | C | 21 days after service | Settled |
| EO-034 | mice or droppings in apartment | multiple dwelling (3+ units) | pest=mouse | yes | C | 21 days after service | Settled |
| EO-035 | rats in apartment or common area | multiple dwelling (3+ units) | pest=rat | yes | C | 21 days after service | Settled |
| EO-036 | roaches or mice in hallway or laundry room | multiple dwelling (3+ units) | pest=roach or mouse | yes | C | 21 days after service | Settled |
| EO-037 | bedbugs | multiple dwelling (3+ units) | pest=bedbug | yes | B | 30 days from mailing of notice | Settled |
| EO-038 | other pests (flies, ants, etc.) | multiple dwelling (3+ units) | pest=other | yes | B | 30 days from mailing of notice | Settled |
| EO-039 | cockroaches in a one- or two-family house | one- or two-family house, tenant-occupied unit | pest=roach | yes | B | 30 days from mailing of notice | From HPD's records |
| EO-040 | mice in a one- or two-family house | one- or two-family house, tenant-occupied unit | pest=mouse | yes | B | 30 days from mailing of notice | From HPD's records |
| EO-041 | rats in a one- or two-family house | one- or two-family house, tenant-occupied unit | pest=rat | yes | C | 21 days after service | Not settled |
| EO-042 | bedbugs in a one- or two-family house | one- or two-family house, tenant-occupied unit | pest=bedbug | yes | B | 30 days from mailing of notice | Settled |

Notes:
- **EO-033:** IPM work practices 27-2017.8 / 28 RCNY 54-04(a); postponement up to 14 days
- **EO-038:** 566 cites a nonexistent "27-2021.4" (data error)
- **EO-041:** deadline pairing unsettled

## Windows and window guards

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-050 | window guard missing or broken, child 10 or under lives in unit | multiple dwelling (3+ units) | child 10 or under=yes; window not to fire escape | yes | C | 21 days after service | Settled |
| EO-051 | window guard missing in public hall, child 10 or under lives in building | multiple dwelling (3+ units) | child 10 or under in building=yes | yes | C | 21 days after service | Settled |
| EO-052 | window guard requested in writing, no child | multiple dwelling (3+ units) | written request=yes; child 10 or under=no | yes | C | 21 days after service | Settled |
| EO-053 | no guard on window to fire escape (or first-floor egress window) | multiple dwelling (3+ units) | window type=fire escape access | no | n/a | n/a | Settled |
| EO-054 | window guard missing, child 10 or under, condo unit | condo unit in a multiple dwelling | child 10 or under=yes | yes | C | 21 days after service | Settled |
| EO-055 | window guard missing, child 10 or under, one- or two-family house | one- or two-family house, tenant-occupied unit | child 10 or under=yes | no (rule covers multiple dwellings) | n/a | n/a | Settled |
| EO-056 | broken or missing glass, broken sash, window will not close or lock | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-057 | bars or gates on a window that is not a fire escape window | multiple dwelling (3+ units) | — | yes | B | 30 days from mailing of notice | From HPD's records |
| EO-058 | bars or gates on a fire escape window | multiple dwelling (3+ units) | — | yes | B | 30 days from mailing of notice | From HPD's records |

Notes:
- **EO-054:** co-op boards bound by Health Code 131.15(a)(1)
- **EO-058:** Section 8: tenant-caused illegal gates are the tenant's responsibility

## Heat and hot water

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-059 | daytime, cold outside, apartment below 68 F | multiple dwelling (3+ units) | date Oct 1-May 31; 06:00-22:00; outside temp f<55; indoor temp f<68 | yes | C | none: penalties run from day notice affixed; first violation satisfied if corrected within 24 hours and $250 paid within 10 days | Settled |
| EO-060 | daytime, 55 F or warmer outside, apartment below 68 F | multiple dwelling (3+ units) | 06:00-22:00; outside temp f≥ 55; indoor temp f<68 | no | n/a | n/a | Settled |
| EO-061 | night, apartment below 62 F | multiple dwelling (3+ units) | date Oct 1-May 31; 22:00-06:00; indoor temp f<62 (any outside temp) | yes | C | none: penalties run from day notice affixed; first violation satisfied if corrected within 24 hours and $250 paid within 10 days | Settled |
| EO-062 | apartment cold outside heat season | multiple dwelling (3+ units) | date Jun 1-Sep 30 | no (no heat requirement) | n/a | n/a | Settled |
| EO-063 | no heating system or no heat at all | multiple dwelling (3+ units) | — | yes | C | none: penalties run from day notice affixed; first violation satisfied if corrected within 24 hours and $250 paid within 10 days | Settled |
| EO-064 | tap water below 120 F, daytime or evening | multiple dwelling (3+ units) | 06:00-24:00; water temp f<120; fixture without anti-scald valve | yes | C | none: penalties run from day notice affixed; first violation satisfied if corrected within 24 hours and $250 paid within 10 days | Settled |
| EO-065 | shower with anti-scald valve at 110-119 F | multiple dwelling (3+ units) | anti scald valve=yes; 110≤ water temp f<120 | no | n/a | n/a | Settled |
| EO-066 | no hot water at all between midnight and 6 a.m. | multiple dwelling (3+ units) | 00:00-06:00; no hot water; building 3+ stories erected on/after 1929-04-18 or any built after 1951 | yes | C | none: penalties run from day notice affixed; first violation satisfied if corrected within 24 hours and $250 paid within 10 days | Settled |
| EO-067 | tap water warm but below 120 F between midnight and 6 a.m. | multiple dwelling (3+ units) | 00:00-06:00; 0<water temp f<120 | unsettled | C if a violation | unsettled | Not settled |
| EO-068 | scalding hot water above 130 F | multiple dwelling (3+ units) | water temp f>130 | yes (data) | C (data samples) | 24 hours | From HPD's records |
| EO-069 | daytime, cold outside, apartment below 68 F | one- or two-family house, tenant-occupied unit | tenant-occupied; same facts as MD row | yes | C | none: penalties run from day notice affixed; first violation satisfied if corrected within 24 hours and $250 paid within 10 days | Settled |
| EO-070 | no heat or hot water, NYCHA | NYCHA | — | unsettled | unsettled | unsettled | Not settled |

Notes:
- **EO-059:** HPD measures in the coldest room other than kitchen or bathroom
- **EO-066:** MDL 75(3) sets no temperature
- **EO-068:** 510 is a catch-all order with mixed classes

## Smoke and carbon monoxide detectors

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-043 | smoke detector missing or not working at start of tenancy or past useful life | multiple dwelling (3+ units) | device=smoke; cause=not tenant | yes | B | 30 days from mailing of notice | From HPD's records |
| EO-044 | carbon monoxide detector missing or not working | multiple dwelling (3+ units) | device=CO; cause=not tenant | yes | B | 30 days from mailing of notice | From HPD's records |
| EO-045 | carbon monoxide detector missing in a one- or two-family rental | one- or two-family house, tenant-occupied unit | device=CO | yes | B | 30 days from mailing of notice | From HPD's records |
| EO-046 | smoke detector missing in a one- or two-family rental | one- or two-family house, tenant-occupied unit | device=smoke | unsettled | unsettled (B in data) | unsettled | Not settled |
| EO-047 | battery-operated detector removed or broken by the occupant during the tenancy | multiple dwelling (3+ units) | cause=occupant | occupant duty, not owner | unsettled | n/a | Not settled |
| EO-048 | detector painted over or disconnected | multiple dwelling (3+ units) | tampering=yes | yes (tampering unlawful for any person) | unsettled | unsettled | Not settled |
| EO-049 | smoke detector, Section 8 unit | Section 8 (private building) | voucher=yes | yes (HMC) plus HQS/NSPIRE failure | B (HMC) | 30 days from mailing of notice (HMC); HQS 24 hours if life-threatening, else 30 days | From HPD's records |

Notes:
- **EO-044:** 1502 cites repealed 27-2046.1/2046.2
- **EO-049:** sealed 10-year battery or hardwired from 2024-12-29

## Leaks

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-001 | active leak or water stain in apartment | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-002 | cascading leak, water soaking electrical fixtures | multiple dwelling (3+ units) | cascading=yes | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-003 | roof leak into top-floor apartment or public hall | multiple dwelling (3+ units) | source=roof | yes | unsettled (B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-004 | leaky water supply pipe | multiple dwelling (3+ units) | source=pipe | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-005 | active leak or water stain | one- or two-family house, tenant-occupied unit | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-006 | active leak, NYCHA apartment | NYCHA | — | unsettled (HPD inspects NYCHA only at Housing Court request) | unsettled (A, B or C, as for private buildings) | unsettled | Not settled |

Notes:
- **EO-001:** 583 is not rent-impairing

## Wall and ceiling damage

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-028 | hole, crack or broken plaster in wall or ceiling | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-029 | fallen or collapsing ceiling or wall | multiple dwelling (3+ units) | collapse=yes | yes | unsettled (503 is B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-030 | structural defect (bowing or cracked exterior wall) | multiple dwelling (3+ units) | structural=yes | yes | unsettled (B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-031 | hairline cracks only | multiple dwelling (3+ units) | hairline=yes | unsettled | unsettled | unsettled | Not settled |
| EO-032 | hole, crack or broken plaster | one- or two-family house, tenant-occupied unit | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |

Notes:
- **EO-028:** 508 not rent-impairing

## Other problem types

### Appliance

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-086 | no gas to the stove | multiple dwelling (3+ units) | — | yes | unsettled (B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-087 | broken refrigerator or stove provided by owner | multiple dwelling (3+ units) | owner-provided appliance | unsettled | unsettled | unsettled | Not settled |
| EO-088 | no stove knob covers, child under 6 | multiple dwelling (3+ units) | child under 6 resides=yes; gas stove | yes | B | 30 days from mailing of notice | From HPD's records |

### Blocked exit

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-078 | hallway, stairs or fire escape blocked by encumbrances | multiple dwelling (3+ units) | — | yes | B | 30 days from mailing of notice | From HPD's records |
| EO-079 | exit door or gate locked with key or illegal fastening | multiple dwelling (3+ units) | — | yes | unsettled (B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |

### Door lock

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-080 | no lock or key for apartment entrance door | multiple dwelling (3+ units) | — | yes | A | 90 days from mailing of notice | From HPD's records |
| EO-081 | double cylinder (key both sides) lock on apartment door | multiple dwelling (3+ units) | — | yes | C | 24 hours | From HPD's records |
| EO-082 | apartment or hallway door not self-closing | multiple dwelling (3+ units) | building required to have self-closing doors | yes | C | 14 days after service | Settled |
| EO-083 | no peephole in apartment door | multiple dwelling (3+ units) | — | yes | A | 90 days from mailing of notice | From HPD's records |

Notes:
- **EO-081:** Section 8: tenant-installed double cylinder locks are tenant responsibility
- **EO-082:** HPD reinspects within 20 days after the correction period

### Elevator

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-089 | elevator out of service | multiple dwelling (3+ units) | — | DOB violation; HPD on DOB referral | unsettled | unsettled | Not settled |

### Exposed wiring

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-071 | exposed or unsafe wiring, extension cords | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-072 | uncovered electrical outlet in public hall | multiple dwelling (3+ units) | — | yes | A | 90 days from mailing of notice | Settled |

Notes:
- **EO-072:** HPD writes this under the general 506 order citing 27-2005

### Flooring

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-077 | broken or lifting floor tiles, torn floor covering | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |

### Garbage

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-084 | garbage or rubbish piled up in common areas or yard | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-085 | no or too few garbage cans | multiple dwelling (3+ units) | — | yes | B | 30 days from mailing of notice | From HPD's records |

### No water sewage

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-091 | no water or low water in apartment | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-092 | sewage backup or raw sewage | multiple dwelling (3+ units) | — | yes | unsettled (B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |

### Plumbing fixture

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-073 | leaky or broken faucet, sink, tub or toilet | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
| EO-074 | toilet clogged or obstructed | multiple dwelling (3+ units) | — | yes | C | 24 hours | From HPD's records |
| EO-075 | loose toilet bowl needs resetting | multiple dwelling (3+ units) | — | yes | A | 90 days from mailing of notice | From HPD's records |

### Radiator

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-076 | broken, leaking or loose radiator | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |

### Stairs

| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |
|---|---|---|---|---|---|---|---|
| EO-090 | loose tread or handrail, broken stairs | multiple dwelling (3+ units) | — | yes | unsettled (A, B or C) | by assigned class: A 90 days, B 30 days, C 24 hours | Class not settled |
