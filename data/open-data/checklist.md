# Workstream 4 checklist (open-data)

Status: `done`, `partial` or `gap` (see `gaps.md`). Updated 2026-11-21 (New York time).

## Do first

| Item | Status | Files |
|---|---|---|
| HPD violation types CSV (order number x class) | done: 612 rows (400 orders; 11,422,299 violations); order-to-class map 400 rows; class notes for the 143 multi-class orders `text/od-hpd-violation-types-class-notes.md` | `text/od-hpd-violation-types.csv`, `text/od-hpd-order-class-map.csv`, raw `raw/od-hpd-violation-types-*.json*` |
| HPD complaint categories and subcategories CSV | done: 62 category/subcategory rows, 182 problem-code rows (Jan 2024 to Nov 2026, 2,541,996 problems; the 2025 total matches an independent count) | `text/od-hpd-complaint-categories.csv`, `text/od-hpd-complaint-problem-codes.csv`, raw `raw/od-hpd-complaint-categories-by-year/` |
| 311 housing complaint types and descriptors CSV | done: 345 rows (Jan 2020 to Nov 2026, 5,629,617 requests; HPD 105, DOB 104, DOHMH 117, other 19); dictionary hierarchy 6,051 rows | `text/od-311-housing-complaint-types.csv`; dictionary hierarchy `text/od-311-dictionary-hpd-complaint-details.csv` (done) |
| Building lookup endpoint docs: GeoSearch, PLUTO, HPD Registrations, Registration Contacts, DHCR rent-stabilized lists | done | `endpoints/od-geosearch.md`, `endpoints/od-pluto.md`, `endpoints/od-hpd-registrations.md`, `endpoints/od-hpd-registration-contacts.md`, `endpoints/od-dhcr-rs-buildings.md` (+ `local/od-dhcr-rs-buildings-2025.csv`, 51,592 rows) |
| Demo buildings (pre-1960, rent-stabilized, NYCHA, 1-2 family) | done | `text/od-demo-*.md`, `raw/od-demo-*.json` |

### Demo buildings

| Case | Address | BBL | BIN | Summary |
|---|---|---|---|---|
| Built before 1960 | 122 West 167th Street, Bronx (1929, 4 units, C3, not on the DHCR list) | 2025140062 | 2003271 | `text/od-demo-122-w-167-st-bx.md` |
| Rent-stabilized | 39-06 114th Street, Queens (1965, 70 units, D3, on the DHCR 2025 list) | 4017860017 | 4044993 | `text/od-demo-3906-114-st-qn.md` |
| NYCHA development | 466 Columbia Street, Brooklyn (Red Hook West, TDS 79) | 3005330001 | 3326977 | `text/od-demo-466-columbia-st-bk.md` |
| 1-2 family house | 1180 Mace Avenue, Bronx (1940, 2 units, B3) | 2044550037 | 2051991 | `text/od-demo-1180-mace-ave-bx.md` |
| Extra: pre-1960 under a full vacate order | 1048 Washington Avenue, Bronx (1899, 3 units) | 2023700005 | 2001261 | `text/od-demo-1048-washington-ave-bx.md` |

How they were chosen (all from public records, 2026-11-21):
- Pre-1960 and 1-2 family: buildings with HPD order 616 ("presumed lead-based paint") violations inspected since mid-2025, grouped by BBL, then checked against PLUTO (`yearbuilt`, `unitsres`, `bldgclass`) and the DHCR list. 1048 Washington Ave was the first pick, but it has an entire-building vacate order, so 122 W 167 St (no vacate order) became the main pre-1960 case.
- Rent-stabilized: PLUTO lots built 1962-1972 with 40-120 units in rental elevator classes D1/D3/D7, one building per lot and not a co-op, intersected with the DHCR 2025 list, then ranked by HPD problems received since 2026-01-01.
- NYCHA: development with the most HPD Housing Court-requested violations in im9z-53hg (Red Hook West, 496), then its building with the most (466 Columbia St, 89).

## Then

| Item | Status | Files |
|---|---|---|
| HPD Housing Litigations | done | `endpoints/od-hpd-litigations.md` |
| HPD Buildings | done | `endpoints/od-hpd-buildings.md` |
| HPD vacate orders | done | `endpoints/od-hpd-vacate-orders.md` |
| Bedbug annual filings | done | `endpoints/od-hpd-bedbug-reporting.md` |
| DOB Complaints | done | `endpoints/od-dob-complaints.md` |
| DOB Violations, DOB Safety Violations, ECB violations | done | `endpoints/od-dob-violations.md`, `endpoints/od-dob-safety-violations.md`, `endpoints/od-dob-ecb-violations.md` |
| OATH hearings | done | `endpoints/od-oath-hearings.md` |
| DOB permits (BIS and DOB NOW) | done | `endpoints/od-dob-permits.md`, `endpoints/od-dob-now-permits.md` |
| DOB Certificates of Occupancy (BIS and DOB NOW) | done | `endpoints/od-dob-cofo.md`, `endpoints/od-dob-now-cofo.md` |
| 311 Service Requests | done | `endpoints/od-311-service-requests.md` |
| ACRIS (legals, master, parties) | done | `endpoints/od-acris-legals.md`, `endpoints/od-acris.md` |
| NYCHA development list with addresses or BBLs | done | `endpoints/od-nycha-residential-addresses.md` (+ full list `raw/od-nycha-residential-addresses-full.csv`), `endpoints/od-nycha-developments.md` |
| Extra found: HPD violations in NYCHA buildings (im9z-53hg), AEP, CONH pilot, Heat Sensor Program | done | `endpoints/od-hpd-violations-nycha.md`, `endpoints/od-hpd-aep.md`, `endpoints/od-hpd-conh-pilot.md`, `endpoints/od-hpd-heat-sensor.md` |
| Weather: NOAA CDO, NCEI, api.weather.gov KNYC, Open-Meteo | done | `endpoints/od-weather-*.md`; 2026 hourly Central Park temperatures `text/od-ncei-ghcnh-knyc-2026-hourly-temperature.csv` |
| HUD Fair Market Rents, NYC, 2020-2027 | done | `endpoints/od-hud-fmr.md`, `text/od-hud-fmr-nyc.csv` |

## Live fetch

Response times measured from this machine on 2026-11-21 with `curl -w '%{time_total}'`, three runs each, on a typical single-building (or single-day) query. NYC Open Data times are from a quiet-period pass (see the note under the table); times during heavy load were much worse.

| Source and endpoint | Access | Typical response time | Rate limits | Update frequency | Terms allow programmatic use | Verdict |
|---|---|---|---|---|---|---|
| NYC GeoSearch `/v2/search`, `/v2/autocomplete` (address to BBL/BIN) | open API, no key | search 0.27-0.59 s; autocomplete 0.09-0.19 s | none published | PAD release (`26c` in responses) | No terms published; it is the city's public geocoder that its own apps use (home page). The `/attribution` page is 404 | good |
| HUD USER FMR API `fmr/data/{entity}` | free key (Bearer) | 0.29-0.63 s | "60 queries a min" (terms) | yearly FMR release; `year` param back to at least 2020 | yes: terms allow apps to "search, display, analyze, retrieve"; required notice "This product uses the HUD User Data API but is not endorsed or certified by HUD User." | good |
| NWS API `stations/KNYC/observations` (`/latest`, `?start&end`) | open API, no key; User-Agent required | latest 0.06-0.13 s; one day 0.07-0.24 s | not public ("generous"); retry after about 5 s if exceeded | about hourly (:51 reports); history about 7 days only | yes: "open data, free to use for any purpose" | good for the last 7 days, no for older clips |
| Open-Meteo archive `archive-api.open-meteo.com/v1/archive` | open API, no key | 0.42-0.45 s | 600/min, 5,000/hour, 10,000/day (free tier) | modelled, includes current and future hours; back to 1940 | non-commercial use only, CC BY 4.0 credit | possible (modelled grid data, non-commercial) |
| NCEI GHCNh station file `GHCNh_USW00094728_2026.psv` | plain file download, no key | HEAD 0.11-0.12 s; full 38 MB download 10.3 s | not stated | 2026 file ended 2026-11-17 (3-4 day lag); `Last-Modified` 2026-11-19 | US government data (no licence statement found) | possible (cache daily; not per request) |
| NCEI Access Data Service `dataset=global-hourly` | open API, no key | 0.17-0.41 s | not stated in docs fetched | no Central Park data after mid-2025 | US government data | no (no 2026 data) |
| NOAA CDO API v2 | free key (`token` header) | 0.23 s | not stated on docs page fetched | GHCND daily to 2026-11-15 | US government data | no (no hourly temperature) |
| DHCR rent-stabilized building PDFs (RGB site) | plain fetch | HEAD 0.06-0.11 s; PDFs 0.1-3 MB | n/a | yearly (2025 registration file, posted 2026-11) | No terms found; government building lists | possible (ship `local/od-dhcr-rs-buildings-2025.csv`, refresh yearly) |
