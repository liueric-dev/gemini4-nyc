# Data collection summary

Collected Nov 21, 2026, from 00:35 to about 06:15 New York time. The account usage limit stopped the run from about 02:20 to 06:00. The spec is [README.md](README.md). Each workstream folder has its own `manifest.jsonl`, `checklist.md` and `gaps.md`, which hold the detail. Nothing is committed.

## What was collected

| Workstream | Items | What's in it |
|---|---|---|
| `law-nyc/` | 967 | The whole Housing Maintenance Code (§§ 27-2001 to 27-2154). HPD rules in RCNY Title 28: the 23 chapters that implement the code, plus 7 more. Admin Code Title 26: rent stabilization, rent control, unlawful eviction (§ 26-521), Right to Counsel. The FARE Act (Local Law 119 of 2024), the NYC Human Rights Law, the Health Code (window guards, pests, lead), the tenant parts of the Construction Codes, Fire Code Ch. 10, and § 23-502 (open data). All read from amlegal through the browser and checked against it by hash. |
| `law-state/` | 763 | 463 state law sections from the Senate API: MDL (all), RPL Art. 7 and 6-A (Good Cause), RPAPL 7, 7-A, 7-C and 7-D, CCA § 110 and small claims, GOL Art. 7, ETPA, both rent control laws, Exec Law Art. 15, Penal Law Art. 250, and others. HSTPA, Good Cause as enacted, DHCR notices, RGB Order #58. 63 federal items: lead disclosure, NSPIRE, Fair Housing. 225 secondary items in `local/`. |
| `process/` | 468 | The HPD complaint, inspection, certification and repair programs. 64 articles from 311. The court's HP pages plus 20 landlord-tenant form PDFs and 3 affidavit-of-service forms. 23 DHCR form PDFs and 40 DHCR fact sheets. NYCHA, MOPT, HRA, CCHR, the FARE Act, and contacts. Everything is in `local/` (see decisions). |
| `open-data/` | 276 | **The HPD violation types list: 612 order-and-class rows across 400 orders and 11.4 million violations** (`text/od-hpd-violation-types.csv`), with the order-to-class map and notes. HPD complaint categories: 62 rows covering 2024–2026. 345 housing complaint types from 311. 37 endpoint docs. 5 demo buildings. Weather and HUD FMR. |
| `media/` | 1,319 | 829 public items (739 photos, 90 videos) and 490 copyrighted fallback items. Split by source group: 474 test and 845 dev, with no group on both sides. Selecting the review set later moved 8 dev groups to test, giving 487 test and 832 dev. The frozen review set (203 items) is in `media/review/`. The pre-split manifest is backed up in `media/local/`. |
| `problem-map/` | 5 files | **DRAFT.** `problem-types.md` covers the 8 core and 11 extended types: orders, sections, facts that set the class, deadlines and coverage. `expected-outcomes.csv` has 92 rows: 41 settled, 18 with a class from HPD data only, 20 with the class unsettled, 13 unsettled. `escalation.md` covers six tenant goals, with NYCHA and Section 8 variants. Line 1 of the CSV is a `#` comment. |

**Demo buildings** (in `open-data/text/od-demo-*.md`):

| Address | What it covers |
|---|---|
| 122 W 167th St, Bronx | built 1929 |
| 39-06 114th St, Queens | rent-stabilized |
| 466 Columbia St, Brooklyn | Red Hook West, NYCHA |
| 1180 Mace Ave, Bronx | two-family house |
| 1048 Washington Ave, Bronx | under a vacate order |

## Biggest gaps

- **HPD's violation classification list isn't online.** HMC § 27-2115(d) had it published in the City Record in 1972, with later amendments. Without it, the class for most repair orders (leaks, plaster, windows, wiring) is "unsettled" or comes from HPD's issued data. Next places to look: City Record Online and a860-gpp.nyc.gov.
- **HP action papers:** the Order to Show Cause and the Verified Petition aren't online, because the clerk hands them out. CIV-LT-25 wasn't found. The HP fee is $45 in court sources from 2007 to 2016 but isn't confirmed current.
- **Rent Stabilization Code:** no official full copy exists online. The full text is Cornell LII only (`law-state/local/`, secondary).
- **Media, thin spots:**
  - Heat and hot water: 20 public items.
  - Window photos clearly in a home: very few.
  - Narration: almost none.
  - 183 public items still have unchecked licences.
  - Many items aren't clearly residential; see `media/checklist.md`, which reports residential and committable-only counts.
- **Missing source documents:** RGB orders before 2026, a few image-only PDFs (no OCR), and the national electrical code base text.

## Flagged as outdated or uncertain

- Hot water from midnight to 6 a.m.: HMC § 27-2031 says 6 a.m. to midnight, while HPD and DHCR say 24 hours.
- Smoke and CO detectors in 1–2 family houses: HPD issues orders there, but § 27-2045(b)(1)(a) excludes them from the owner's duty.
- Lead in buildings from 1960 to 1977: unclear whether HPD presumes lead (order 616) or needs a test (617).
- HPD's own data cites a section that doesn't exist (§ 27-2021.4) and repealed sections.
- HPD's heat page gives lower penalties than the statute: $250–500 a day against $350–1,250.
- § 27-2115(o)(5) is cut off on amlegal.
- Amendments already passed but not in force: § 27-2093.1 (April 2027), Title 26 Ch. 39 (January 2027), and §§ 28-304.6.6.2 and 28-304.8 (January 2027).
- RPAPL 7-C and 7-D don't apply in NYC (§ 796-a(4), § 797(3)).
- 261 state law sections have effective_date `unknown`. The API holds versions only from 2014-09-22.
- The full list of 19 is in `problem-map/problem-types.md` Part 4.

## Live-fetch candidates

| Source | Access | Measured | Verdict |
|---|---|---|---|
| NY Senate Open Legislation API | free key | 0.06–0.10 s per section; 10 requests a second | good |
| eCFR, Federal Register | open | 0.2–4 s | good |
| NYC GeoSearch (address to BBL) | open | 0.3–0.6 s | good |
| HPD violations by BBL (`wvxf-dwi5`) | app token | 0.65–1.1 s (481 rows) | good |
| HPD complaints by BBL (`ygpa-z7cr`) | app token | 1.3–3.8 s (368 rows) | good, cache it |
| HPD registrations (`tesw-yqqr`), PLUTO (`64uk-42ks`) by BBL | app token | 0.2–0.5 s | good |
| HUD FMR API | free key | 0.3–0.6 s; 60 a minute; needs a notice line | good |
| NWS KNYC observations | open, User-Agent required | under 0.25 s; **last 7 days only** | good for recent clips |
| Open-Meteo archive | open | 0.4 s; back to 1940 | possible (non-commercial, CC BY credit) |
| NYC content API (MOPT, Tenant Resource Portal) | open | fast | good |
| amlegal, nycourts.gov, Westlaw | browser only | — | no; use the collected copies |

NYC Open Data is free to use under Admin Code § 23-502(d). The city may require reusers to name the source and version and describe any changes, so the app should credit its datasets.

## Decisions for the project owner

1. **Test set:** done. 203 items reviewed and frozen at 08:03 (`media/review/`), plus `freeze-addendum.json` (08:20).
2. **What can go in the public repo:**
   - nyc.gov's terms say all rights reserved, so all of `process/` is in `local/`.
   - Pexels, Pixabay and the NC/ND-licensed media are `unsure`.
   - Recommendation: commit the manifests, labels, split and problem map, and not the media files (1.2 GB) or the process files.
3. **The problem map is a draft.** Review the settled rows first; they're the ground truth for scoring citations, classes and deadlines.
4. **Copyrighted fallback media** stays out of the demo and its numbers. Report public items only.
5. **Optional:** collect RGB orders before 2026 through the browser. A plain download was denied by the session's permission check.
6. **The October projects** weren't used during collection. They can now be compared against this collection to find gaps.

## Format for the app

This is decided in system design, on the day. The law text is about 6 million characters, roughly 1.5 million tokens, so it won't all fit in a prompt. The problem map links each problem type to its sections. So look up those sections by id, put only them in the prompt, and reject any citation outside that set.
