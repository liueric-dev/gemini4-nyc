# Data collection instructions

Instructions for the sessions and agents that gather the data for the tenant advocate app. Context: [../docs/plan.md](../docs/plan.md), [../docs/REQUIREMENTS.md](../docs/REQUIREMENTS.md).

## Why this data matters

The app takes a tenant's video or photo, works out what's wrong, maps it to the specific NYC, NY State or federal rule it breaks, and tells the tenant their rights and next steps (refer them to an agency, or draft a letter or complaint). That needs five things, which this folder holds:

1. **The law:** the text of every rule a tenant problem can break.
2. **The process:** what a tenant does next, who to contact, and the official forms they file.
3. **Building data:** the facts that decide which laws apply (year built, unit count, owner, rent stabilization, NYCHA), plus the records the app checks.
4. **Test media:** real photos and videos of apartment problems, plus ones with no problem, to evaluate the app against a baseline.
5. **The problem map:** a draft that links each problem type to its rules, violation classes, deadlines and escalation paths, built from 1 to 3.

## How to run

All workstreams run in parallel, one agent per workstream, so each `manifest.jsonl` has one writer. Workstream 6 (problem map) starts once workstreams 1, 2 and 4 have finished their **Do first** items.

Within each workstream, do the **Do first** items before the rest. That way a run cut short by the time box still covers the demo.

Do not commit anything. Do not reformat data for the app; the app's format is decided later in system design. Collect originals plus extracted text.

### Time box (Sat Nov 21, New York time)

| Time | What |
|---|---|
| Start (after midnight) | All workstreams start |
| 07:00 | Every workstream has finished its **Do first** items and updated its `checklist.md`. Verification of those items starts. |
| 09:30 | Stop collecting. Finish manifests, `gaps.md` and `checklist.md`. Write `data/SUMMARY.md`. |
| 10:30 | Hacking begins |

Be comprehensive within the time box. There is no size cap, except the file-size rule below.

## Folder layout

```
data/
  README.md            this file
  SUMMARY.md           written at the end
  law-nyc/             workstream 1
  law-state/           workstream 2 (state and federal)
  process/             workstream 3
  open-data/           workstream 4
  media/               workstream 5
    images/
    videos/
    fallback/          copyrighted items, local evaluation only
  problem-map/         workstream 6
```

Each workstream folder contains:
- `raw/`: original downloaded files (HTML, PDF, JSON, CSV), untouched. Media goes directly in `images/` and `videos/`.
- `text/`: extracted plain text or markdown, one file per law section, article or document where practical.
- `local/`: anything with `committable: no` or `unsure`, and any file over 50 MB. It is git-ignored, so it never reaches the public repo.
- `manifest.jsonl`: one line per item (fields below).
- `gaps.md`: everything looked for but not obtained, and why (blocked, paywall, not found, possibly outdated).
- `checklist.md`: what the workstream set out to collect versus what it got.

### Naming

- **Ids:** a workstream prefix plus a short slug, unique within the folder: `nyc-hmc-27-2005`, `st-rpl-235-b`, `fed-24cfr-35`, `proc-hpd-complaint-process`, `od-hpd-violations`, `med-0042`.
- **Files:** named by id, for example `raw/nyc-hmc-27-2005.html` and `text/nyc-hmc-27-2005.md`. A source covering several sections gets one id, and its manifest line lists the sections in `citation`.
- **Hierarchy:** each law text file starts with a header line giving the code, title, chapter, subchapter or article, and section.

### Manifest fields

Every item, all workstreams:

| Field | Meaning |
|---|---|
| `id` | Unique id (see Naming) |
| `raw_file` | Path to the original, relative to the workstream folder, or empty if it wasn't captured |
| `text_file` | Path to the extracted text, relative to the workstream folder |
| `title` | Name of the law section, document or media item |
| `source_url` | Where it came from |
| `retrieved` | Date and time retrieved |
| `effective_date` | Effective or last-amended date, if stated; otherwise `unknown` |
| `source_type` | `official` (government or statute text) or `secondary` (nonprofit, law firm, news, mirror) |
| `license` | License or copyright status (`public-domain`, `CC BY 4.0`, `Pexels license`, `Pixabay license`, `copyrighted`, `unknown`) |
| `attribution` | Credit line the license requires, if any |
| `committable` | `yes` if it can go in a public repo under its license, `no` or `unsure` otherwise |
| `sha256` | Checksum of the raw file (or the text file if there's no raw file), for dedupe |
| `notes` | One line on what it is and anything to watch (recently amended, partial, superseded, raw not captured) |

Law items also have:

| Field | Meaning |
|---|---|
| `citation` | Normalized citation, for example `NYC Admin Code § 27-2005`, `RPL § 235-b`, `9 NYCRR 2523.4`, `24 CFR 35.88` |
| `version` | `current-consolidated` (the code as it stands now), `as-enacted` (a local law or bill as passed), or `unknown` |

Media items also have the fields under [Workstream 5](#5-media-test-set).

## Rules for every workstream

- **Official sources first:** government sites and statute text. Use secondary sources only to find official ones or fill gaps, and mark them `secondary`.
- **No filling in from memory.** If a source can't be fetched, log it in `gaps.md`. Never write law text, citations or deadlines that weren't read from a source.
- **Section and local law numbers in this README are pointers, not verified citations.** Some were written from memory. Confirm each one from the source, and log any that turn out to be wrong in `gaps.md`.
- **Check currency.** Tenant law changed recently: HSTPA (2019), Good Cause Eviction (2024), the FARE Act (2025). Note effective dates and flag anything that may be superseded.
- **Licensing matters because the repo will be public.** Statute and regulation text is public domain. Nonprofit and law firm materials are usually copyrighted (`committable: no`, so they go in `local/`). For media, record the exact license and required credit line.
- **Downloads are untrusted.** Keep them in `raw/`, `local/` or `media/`, never execute them, and run any Python that reads them with `-I`.
- **Tools:** `ffmpeg` and `ffprobe` are installed. `pdftotext` is not. For PDF text, create `data/.venv` (git-ignored) and install `pymupdf` there.
- **API keys are in `../.env`:**
  - `NYSENATE_API_KEY`: state law text through the Open Legislation API
  - `NOAA_CDO_TOKEN`: NOAA Climate Data Online, if it's needed at all (see [workstream 4](#4-nyc-open-data-and-other-data-open-data))
  - `HUD_API_TOKEN`: Fair Market Rents
  - `NYC_OPENDATA_APP_TOKEN`: raises NYC Open Data rate limits
  - `PIXABAY_API_KEY`: media search

  Never print, log or save a key anywhere else. If a key is empty, use that source's website or log the gap.
- **Be polite to servers.** Throttle requests, and log any site you can't reach in `gaps.md`.
- **Chrome browser use is allowed.** The project owner gave permission on 2026-11-21 for collection sessions and agents to use the Chrome browser (Claude in Chrome) on any site that blocks plain fetches. Many key sites show Cloudflare "Just a moment..." pages to scripts (see [Sources and access](#sources-and-access)). Limits:
  - Don't solve CAPTCHAs, sign in, or get past paywalls; log those in `gaps.md`.
  - Throttle as you would with scripts.
  - Each agent opens its own tab, never touches another agent's tabs, and closes its tabs when done.

- **Be persistent.** This data is the core of the project. When a source fails, try alternatives before logging a gap: other official hosts, the API instead of the website, the browser instead of a plain fetch, a different URL path, a later retry. Keep collecting until the time box ends. Don't stop to wait for the project owner; log open decisions in `gaps.md` and carry on.

### Live-fetch candidates

The app may fetch some data in real time, rather than relying only on what's collected here. For every source you use, add a line to the "Live fetch" section of your `checklist.md` with:
- the source and endpoint
- access: open API, free key, plain fetch, or browser only
- typical response time you saw
- rate limits, if stated
- how often the data updates
- whether its terms allow programmatic use
- a verdict: `good` (open API or a free key, fast, stable), `possible`, or `no` (browser only, slow, or terms forbid it)

## Earlier work: don't use it during collection

Collect everything fresh from the sources. Do not read or copy from the October 2026 projects (`~/hackathons/tenant-advocate`, `~/hackathons/daytona-hackathon-tenant-advocate`) while collecting. The hackathon rules forbid presenting existing projects as new work, and a clean collection avoids that question. Those projects will be compared with this collection afterwards, to find gaps and inconsistencies.

The Nov 20 prep folder `~/hackathons/gemini4-nyc/gemini4-playbook/` was made for this event and may be used:
- `test-sources.md` logs the media sources already searched, with licence notes. Don't repeat those searches.
- `testset/` holds 477 photos found from them. Most are mould, 289 are flagged "test only", and none has been reviewed. They are the [fallback](#fallback-media).
- `testset/videos.json` lists 13 NYC news videos with candidate time ranges. YouTube blocked downloading them.

## Sources and access

Checked on 2026-11-20 and 2026-11-21 from this machine. "Blocked" means a Cloudflare check that stops scripts; the Chrome browser gets through.

| Source | Holds | Access |
|---|---|---|
| NY Senate Open Legislation API (legislation.nysenate.gov/api/3) | State law text. Confirmed law ids: `RPP` Real Property, `RPA` RPAPL, `GOB` General Obligations, `MDW` Multiple Dwelling, `EXC` Executive, `PEN` Penal, `CCA` NYC Civil Court Act, `ETP` Emergency Tenant Protection Act, `ERL` Emergency Housing Rent Control Law, `LEH` Local Emergency Housing Rent Control Act | API, `NYSENATE_API_KEY`. Tested: returns full section text and an active date. Use this first for state law. |
| nysenate.gov/legislation | The same laws as web pages | Blocked: use the API |
| codelibrary.amlegal.com | NYC Admin Code (Housing Maintenance Code, Rent Stabilization Law, Construction Codes), NYC Fire Code, city rules (RCNY) | Blocked: browser. Tested: each page is a whole subchapter or article with full section text, and "Next Doc" steps through. The site says it is "current through Local Law 2026/164". HMC is Title 27, Chapter 2; RCNY Title 28 (HPD) is under NYC Rules. |
| rules.cityofnewyork.us | City rules, including HPD's | Blocked: browser, or use RCNY on amlegal |
| govt.westlaw.com/nycrr | State regulations, including the Rent Stabilization Code (9 NYCRR) | Loads in the browser, but labels itself "Unofficial" and its content shouldn't be copied in bulk. Get the text from a government host first (DHCR on hcr.ny.gov, or the Department of State), and use Westlaw only to confirm section numbers and dates. |
| ecfr.gov | Federal regulations (24 CFR, 40 CFR) | API, no key |
| nycourts.gov, webfiles.nycourts.gov | CourtHelp, court forms, DIY Forms | Blocked for scripts, PDFs included. Forms are at `nycourts.gov/forms?...`, with a `/forms/<slug>` page per form; `/media/NNNN` links redirect to `webfiles.nycourts.gov`. What worked (workstream 3, 2026-11-21): fetch the file from inside a same-site page in Chrome and save it through a download link, one download per fresh tab. The HP Order to Show Cause and Verified Petition aren't online; the clerk hands them out. |
| nyc.gov (HPD, DOHMH, RGB, MOPT) | Agency guides, local law PDFs, fact sheets | Plain fetch is unreliable: it worked with a browser user agent for workstream 3 but returned 403 to workstream 1 at 01:05 and 01:31. Fall back to the browser. MOPT pages are JavaScript shells whose content comes from an open JSON API (`apps.nyc.gov/content-api/v1/...`). The RGB site returned 403 to curl. |
| legistar.council.nyc.gov | Local laws as enacted | Plain fetch works |
| hcr.ny.gov | DHCR fact sheets and forms | Plain fetch works with curl's default user agent; a browser user agent gets Cloudflare. Its robots.txt disallows `/search/`. |
| portal.311.nyc.gov | 311 complaint types | Plain fetch works |
| data.cityofnewyork.us | NYC Open Data | API, `NYC_OPENDATA_APP_TOKEN` |
| Open-Meteo archive, api.weather.gov (station KNYC), NCEI | Hourly weather history | Open-Meteo and NWS need no key (see workstream 4) |
| HUD USER API | Fair Market Rents | API, `HUD_API_TOKEN` |
| Pixabay | Photos and videos | API, `PIXABAY_API_KEY` |
| Pexels | Photos and videos | No new API keys are issued: browser |
| iNaturalist API | CC-licensed phone photos of pests | API, no key |
| nycadmincode.readthedocs.io, intro.nyc | Unofficial mirrors of the Admin Code and Council data | Plain fetch works. `secondary` only; use for gaps or cross-checks |

For pages read through the browser, a raw original may not be savable. Save the page text and the URL, leave `raw_file` empty, and say so in `notes`. That doesn't count as a gap.

A local law PDF from Legistar or nyc.gov is the text as enacted (`version: as-enacted`), not the current code. Prefer amlegal for current text (`version: current-consolidated`).

## Problem types

The labels, the problem map and the evaluation all use these exact names.

**Core types** (collected in depth and scored):

| Name | Covers |
|---|---|
| `leak` | active leaks, water damage, ceiling and wall water stains |
| `mold` | visible mould or mildew on walls, ceilings, windows or fixtures |
| `peeling-paint` | peeling, flaking or chipping paint (lead risk in older buildings) |
| `wall-ceiling-damage` | holes, cracks, broken or fallen plaster |
| `pests` | roaches, mice, rats, bedbugs, or signs of them (droppings, gnaw holes, nests). Record the pest in `draft_facts` |
| `smoke-co-detector` | missing, broken, disconnected or painted-over smoke or carbon monoxide detectors |
| `window` | broken windows, windows that won't close or lock, missing or broken window guards |
| `heat-hot-water` | a thermometer showing a low indoor temperature, or tap water that isn't hot |

**Extended types** (collected for coverage, shallower): `exposed-wiring`, `plumbing-fixture` (toilet, sink, tub, shower), `radiator`, `flooring`, `blocked-exit` (exits, hallways, fire escapes), `door-lock`, `garbage` (common areas), `appliance` (stove, refrigerator), `elevator`, `stairs`, `no-water-sewage`.

## Workstreams

### 1. NYC law (`law-nyc/`)

The city rules a tenant problem breaks. Mostly through amlegal in the browser.

**Do first:**
- NYC Housing Maintenance Code (NYC Admin Code Title 27, Chapter 2), all sections. It includes:
  - repairs and maintenance
  - heat and hot water
  - pests, mold and indoor allergens (Local Law 55 of 2018 is codified here)
  - lead paint (Local Law 1 of 2004 is codified here)
  - window guards
  - smoke and carbon monoxide detectors
  - harassment
  - bedbug history disclosure
  - the tenant's own duties
  - HPD violation classes, correction periods and penalties
- HPD rules in Title 28 of the Rules of the City of New York, all chapters that implement the Housing Maintenance Code. These are separate from Admin Code Title 28 (the Construction Codes).

**Then:**
- NYC Admin Code housing-related provisions outside the Housing Maintenance Code:
  - the FARE Act (2024, broker fees; find its local law number)
  - tenant harassment provisions
  - the Tenant Bill of Rights (not in the Admin Code; it is an HPD guidance document, collected in workstream 3)
  - unlawful eviction and lockouts (§26-521)
  - Right to Counsel (§26-1301 and following)
  - the Rent Stabilization Law (Title 26, Chapter 4) and the rent control law (Title 26, Chapter 3)
  - housing provisions of the NYC Human Rights Law (Title 8): reasonable accommodation, source-of-income discrimination
- NYC Construction Codes (Admin Code Title 28), only the sections that affect tenants:
  - Tenant Protection Plans for construction in occupied buildings (§ 28-104.7.16), and after-hours work
  - egress, exits and fire escapes
  - Local Law 152 of 2016 (gas piping inspections) and the rules on gas shutoffs
- NYC Fire Code sections on blocked exits and fire escapes, and NYC Electrical Code sections on exposed wiring.
- NYC Health Code (DOHMH) sections on window guards, lead and pests.
- City pre-lease disclosures the landlord must give (lead paint, bedbugs, sprinklers and any others found).

### 2. NY State and federal law (`law-state/`)

Mostly through the Senate API, plus eCFR and the browser for Westlaw.

**Do first:**
- Real Property Law:
  - §235-b (warranty of habitability)
  - §223-b (retaliation)
  - every other tenant-protection section in Article 7 (landlord and tenant), including utility shutoffs (§235-a, which cites Public Service Law §§33, 34 and 116), lease terms and illegal clauses
- Multiple Dwelling Law, all articles that apply to NYC apartments (law id `MDW`).
- RPAPL Article 7 (eviction proceedings, including §711 and unlawful eviction under §768) and Article 7-A (administrator for rents, the NYC route). Articles 7-C and 7-D don't apply in NYC (§ 796-a(4), § 797(3)), so collect them only for completeness.
- NYC Civil Court Act §110 (Housing Part, HP actions).
- General Obligations Law §7-108 (security deposits, including the move-in and move-out inspection) and the rest of GOL Article 7, Title 1, on deposits.

**Then:**
- Real Property Law §238-a (limitation on fees) and flood history disclosure.
- Good Cause Eviction (Real Property Law Article 6-A), including its exemptions, plus the yearly rent increase cap if it's published.
- Rent Stabilization Code (9 NYCRR Parts 2520–2531), DHCR's NYC rent control regulations (also in 9 NYCRR), the Emergency Tenant Protection Act (`ETP`), and the rent control laws (`ERL`, `LEH`).
- Housing Stability and Tenant Protection Act of 2019 (HSTPA): the text and which sections it changed.
- The Spiegel Law (Social Services Law §143-b: rent withholding by public assistance for buildings with violations).
- NYC Civil Court Act Small Claims article (security deposit claims).
- NY State Human Rights Law (Executive Law Article 15), housing provisions.
- Penal Law §§250.00 and 250.05 on recording conversations (whether a tenant can record the landlord without consent).
- Federal:
  - lead-based paint disclosure before leasing (Title X §1018, 42 U.S.C. §4852d; 24 CFR Part 35 and 40 CFR Part 745)
  - HUD inspection standards for Section 8 and public housing (NSPIRE, 24 CFR Part 5 Subpart G)
  - Fair Housing Act housing provisions
- Rent Guidelines Board orders for current and recent years (low priority).

### 3. Process and resources (`process/`)

What the tenant does next, who to contact, and the forms. Official city and state pages first. Nonprofit guides are useful context but usually `committable: no` (into `local/`).

**Do first:**
- **HPD:**
  - the complaint and inspection process, and what happens after a 311 complaint
  - violation classes and what they trigger
  - certification of correction
  - the Emergency Repair Program and the Alternative Enforcement Program
  - heat season rules
  - HPD's tenant guides (e.g. "The ABCs of Housing")
- **311:** complaint types for housing and how to file.
- **Housing Court, HP actions:** how to start one, forms and fees. Use CourtHelp, DIY Forms and `nycourts.gov/forms` (see [Sources and access](#sources-and-access) for the PDF caveat). The RPAPL 7-C and 7-D forms on `nycourts.gov/landlord-and-tenant-forms` aren't usable in NYC.
- **DHCR:** tenant complaint forms (rent overcharge, decreased services, rent history request) and fact sheets. Download the actual form PDFs, and take the form numbers from the source.

**Then:**
- **NYCHA and Section 8:** HPD doesn't enforce the Housing Maintenance Code in NYCHA buildings, so these tenants need a different path. Collect:
  - how NYCHA residents report repairs and escalate
  - HP actions against NYCHA
  - the federal monitor
  - the mold settlement
  - Section 8 inspections, for both NYCHA and HPD vouchers
- **Housing Court, other cases:**
  - RPAPL 7-A administrator cases
  - Right to Counsel eligibility and how to get a lawyer
  - answering eviction papers, and what each court paper is (petition, notice of petition, rent demand)
  - nonpayment and holdover forms (low priority)
- **Official forms beyond HP and DHCR:** the eviction answer form and blank court papers, so document reading can be tested; the DHCR rent-stabilized lease rider and renewal lease form, for testing the lease check.
- **Small Claims Court:** suing for a security deposit.
- **Harassment:** HPD and the Mayor's Office to Protect Tenants, and the certification of no harassment.
- **Pre-lease:** what a landlord must disclose before signing, and what a prospective tenant can ask for (rent history, rent-stabilized status, broker fees under the FARE Act).
- **Rent help** (low priority): One Shot Deal, CityFHEPS, SCRIE and DRIE: who qualifies and how to apply.
- **Contacts:** get phone numbers, websites and what each handles for:
  - city: HPD, NYCHA, the NYC Commission on Human Rights, the Mayor's Office to Protect Tenants, HRA's Office of Civil Justice (Right to Counsel)
  - state: DHCR and its Tenant Protection Unit, the NY Attorney General
  - utilities: Con Edison and National Grid (gas and power shutoffs)
  - nonprofits: Housing Court Answers, Met Council on Housing, Legal Aid Society, Legal Services NYC, and tenant unions

### 4. NYC Open Data and other data (`open-data/`)

For each dataset, write `open-data/endpoints/<id>.md` with these headings: dataset name, dataset ID, API URL, key fields with their meanings, an example query, an example response row, and caveats. Save the data dictionary in `raw/`.

**Do first:**
- **The complete list of HPD violation types,** from HPD Housing Maintenance Code Violations (`wvxf-dwi5`), saved as CSV. This is the ground truth for mapping a problem to the law.
  - There is no code-section column. The section is the prefix of `novdescription` (for example "§ 27-2005 ADM CODE ...").
  - Group by order number and class, not by description. Each `novdescription` adds the apartment, room and wall, so nearly every description is unique. On 2026-11-20 there were about 400 order numbers in 612 order-and-class pairs.
  - **Class is not fixed per order:** 143 orders appear under more than one class (order 508 is A about 139k, B about 801k, C about 101k). For each order, record what sets the class where the description shows it (for example the mould area, "LESS THAN 10 SQUARE FEET").
  - For each order-and-class pair, save: the order number, the class (A/B/C/I), the count, the cited section, the shared wording with the location removed, and 3 sample descriptions.
  - A class can be upgraded when a violation goes uncorrected ("HAS BEEN UPGRADED TO CLASS ..."). Flag those rows and leave them out of the order-to-class mapping.
- **The distinct HPD complaint categories and subcategories** (for example "HEAT/HOT WATER", "PLUMBING") from HPD Complaints and Problems (`ygpa-z7cr`), with counts, saved as CSV. The counts also show which problem types are most common.
- **The distinct 311 complaint types and descriptors** for housing, saved as CSV.
- **Building lookup:** endpoint docs for NYC GeoSearch (address to BBL), PLUTO (year built, residential unit count, building class, owner name), HPD Registrations and Registration Contacts (owners and managing agents, the usual way to build a landlord's portfolio), and DHCR rent-stabilized building lists if available.
- **Demo buildings:** a handful of real NYC buildings, by address and BBL, that cover the cases the law branches on: one built before 1960, one rent-stabilized, one NYCHA development, and one 1–2 family house. Choose from public records. For each, save the PLUTO row and a summary of its HPD violations, complaints and registration. Building-level public records only; no tenant names.

**Then:**
- Endpoint docs for: HPD Housing Litigations, HPD Buildings, HPD vacate orders, bedbug annual filings, DOB Complaints, DOB Violations and ECB/OATH violations, DOB permits, DOB Certificates of Occupancy, 311 Service Requests (housing types), ACRIS (deeds and parties), and the NYCHA development list with addresses or BBLs.
- **Weather history:** hourly NYC outdoor temperature by date and time. The daytime heat rule depends on the outdoor temperature, so the app needs the temperature at the hour a clip was taken.
  - The NOAA CDO token API has no hourly temperature dataset, only daily summaries and hourly normals ending 2010.
  - NCEI's hourly data returned Central Park for January 2025 but nothing for 2026.
  - api.weather.gov (station KNYC) and the Open-Meteo archive both returned hourly 2026 data without a key.
  - Document all three: endpoint, fields, example query, how far back and how recent each goes, and license.
- **HUD Fair Market Rents** for New York City, current and recent years. Good Cause Eviction's luxury exemption is measured against them.

### 5. Media test set (`media/`)

Real photos and videos of apartment problems, to evaluate the app against a single-call baseline. Gather from public-domain and openly licensed sources. Copyrighted items are only a [fallback](#fallback-media). No personal or friends' clips. Prefer realistic, messy footage (phone quality, dim, shaky) over polished stock.

Do not edit, splice, or add narration to any clip. Every item must be as published. Anything made by the team would count as examples written to pass. Recording a time range within a published video is fine (the app sends just that stretch), but combining clips or adding anything is not.

**Photos and video have different jobs.** Photos carry the main score, because they are easier to find and are how most tenants document problems. Video is a smaller set, scored separately, plus a stress test on long footage.

**Sources:**
- Pixabay (API; photos and videos)
- Pexels: no API keys are being issued, so search the website in the Chrome browser
- Openverse (api.openverse.org; covers Flickr and other Creative Commons photos)
- Wikimedia Commons (photos and videos; no key)
- Internet Archive (public domain or Creative Commons only; more home footage)
- iNaturalist (CC-licensed phone photos; good for roaches, mice, rats and bedbugs, but check each is indoors)
- US federal agencies, whose works are public domain: EPA (mold, lead), CDC's Public Health Image Library (pests), HUD Healthy Homes, FEMA (water damage)

For YouTube and Vimeo videos under Creative Commons, record the link and metadata in the manifest, but do not download. **Video test items must be downloadable files**, because the Decisions API can't take YouTube links, so link-only videos can't be scored.

**Do first:** core-type photos, no-problem photos and look-alikes.

**Targets** (fallback items don't count toward any of these):
- **Core-type photos:** at least 12 per core type.
- **No-problem photos:** at least a quarter of all photos: clean, ordinary rooms and fixtures.
- **Look-alikes:** at least 3 for each core type where look-alikes exist: shadows or dirt that aren't mold, old repaired stains, deliberate texture that isn't damage, paint that's worn but intact.
- **Extended-type photos:** at least 3 per extended type.
- **Video:** at least 3 downloadable videos per core type where any exist, plus no-problem and look-alike clips, plus a few long walkthroughs as a stress set.
- **Clip length:** prefer clips under 30 seconds. Keep longer videos, but label them by segment: each problem gets a start and end time in `problem_locations`, so one long video can supply several short test items.
- **Narrated videos and paired clips** (the same spot on different dates): collect any that exist, in any language. Expect few.

Walkthroughs, narration and paired clips are rare in public footage. Collect what exists and log the shortfall in `gaps.md`; don't fill it any other way.

#### Dev/test split

The test split is the held-out part of the set. The 5 Sigma track judges the system "on inputs you didn't prepare for", against a baseline.
- **Dev** items are used while building: tuning prompts and setting Decisions API thresholds.
- **Test** items are never looked at while building. They are scored once, at the end, for the reported number.

Without a held-out set, the score measures how well the system was tuned to the same examples, which inflates it.

- **Split by source group, not by item.** Give every item a `group_id` for its origin (one report, one photographer, one video, one dataset). All items in a group go to the same split, so photos from the same report can't land on both sides.
- **Assign the split at random**, with a fixed seed, in a script saved as `media/split.py`. Put about 30% of groups in `test`, and make sure each core type has at least 3 test items and no-problem and look-alike items appear in both splits. Don't choose test items by hand.
- **Labels for test items are reviewed and frozen** by the project owner before building starts. After that, nobody changes them or looks at the test items while building.

#### Fallback media

Use the copyrighted items in `~/hackathons/gemini4-nyc/gemini4-playbook/testset/` only where public sources can't cover a problem type.
- They don't count toward any target.
- They are scored separately from public items. The headline number reports public items only.
- They are for local evaluation only. They're not shown in the demo or the demo video unless the project owner decides otherwise, and they never go in the repo.
- Copy them into `media/fallback/` (git-ignored), keeping the playbook's source folders. Add each to the manifest with `license: copyrighted`, `committable: no`, and the licence flags from the playbook's `manifest.json`.
- Carry over any ground truth the playbook recorded, such as a stated mould area, into `draft_facts`.
- For the news videos, record the links and time ranges; don't download them.
- In `checklist.md`, report for each problem type how many items are public and how many are fallback.

#### Extra manifest fields for media

| Field | Meaning |
|---|---|
| `media_type` | `image` or `video` |
| `duration_s` | Video length in seconds |
| `group_id` | Origin group, for the split |
| `split` | `dev` or `test` |
| `category` | `problem`, `no-problem` or `look-alike` |
| `draft_label` | Problem types present, from [Problem types](#problem-types), or `none` |
| `problem_locations` | For each problem: start and end time in seconds for videos, or a region description for images |
| `draft_facts` | Facts that change the rule or class, where visible or stated: estimated area (mould), which pest, whether it's in an apartment or a common area, the thermometer reading |
| `draft_hpd_orders` | Likely HPD order numbers for each problem, from the violation list. Class comes from the problem map plus `draft_facts`, not from the label. |
| `source_caption` | The caption or description the source gave, verbatim |
| `conditions` | Capture conditions: `dim`, `shaky`, `close-up`, `wide`, `polished-stock`, `phone-quality` |
| `residential` | Whether it's clearly a home or apartment, or possibly somewhere else |
| `narration` | `none`, or the language spoken |
| `pair_id` | Shared id for clips of the same spot on different dates; empty otherwise |
| `label_confidence` | `high`, `medium`, `low` |

Labels are drafts. The project owner reviews every label before it's used in evaluation.
- Never use Gemini to draft labels. Gemini is the system being evaluated, so labels it wrote would inflate its score.
- For video labels, extract frames with `ffmpeg` and look at them before writing timestamps.

### 6. Problem map (`problem-map/`)

A draft linking each [problem type](#problem-types) to the law and to what the tenant can do. It is the expected answer for the "map to the law" and "act" steps, which the media labels alone don't cover. Start once workstreams 1, 2 and 4 have finished their **Do first** items. Cite only files collected in `data/`, by manifest id. Where the sources don't settle something, write `unsettled` and say why.

- **`problem-types.md`:** for each problem type:
  - its definition
  - the HPD order numbers it maps to
  - the code sections they cite
  - the facts that set the class (area, location, building age, child under 6 or under 11, heat season and time of day)
  - the correction deadline for each class
  - which buildings the rule covers (unit count, NYCHA, co-op/condo, year built)
- **`expected-outcomes.csv`:** one row per problem type and set of facts, with the expected section, class, deadline and escalation steps. This is the ground truth for scoring citations, classes and deadlines.
- **`escalation.md`:** for each problem type, the paths by what the tenant wants. Each step gives who to contact, the form or letter, the timeline, and the anti-retaliation protection.
  - get it fixed
  - document it for later
  - get a rent reduction
  - stop harassment
  - recover a deposit
  - leave the apartment

  Different paths for NYCHA and Section 8 tenants where they apply.

It's a draft. The project owner reviews it.

## Done criteria

- Every workstream has its `manifest.jsonl`, `gaps.md` and `checklist.md`.
- **Verification**, done by an agent or session that did not collect the data, such as the reviewer session `gemini-data-fable` or a fresh agent:
  - Spot-check at least 20 law sections: compare the extracted text with the original source, and confirm the section numbers and effective dates.
  - Confirm every section and local law number named in this README against its source, and record the corrections.
  - Confirm the license for every media item from its source page.
  - Confirm that the HPD violation list loads and has the order number, class, cited section and count columns, and that the HPD complaint category and 311 complaint type CSVs load.
  - Count media items by problem type, media type and split. Confirm every core type has at least 3 `test` items, and that no `group_id` appears in both splits.
  - Check that every citation in the problem map points to a collected file.
  - Confirm nothing with `committable: no` or `unsure` sits outside `local/` or `media/fallback/`.
- Verify the **Do first** items as soon as they finish (from 07:00), not only at the end.
- A top-level summary in `data/SUMMARY.md` covering:
  - what was collected per workstream
  - the biggest gaps
  - anything flagged as outdated or uncertain
  - what still needs the project owner (label review, problem map review)

## What's in the repo

The photos and videos (`media/images/`, `media/videos/`), every `local/` folder and `media/fallback/` are not committed. That's for licensing, and because the media alone is 1.2 GB. Each manifest line keeps `source_url`, `license` and `sha256`, so any item can be downloaded again and checked.
