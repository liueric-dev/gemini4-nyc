# Workstream 4 gaps (open-data)

Everything looked for but not fully obtained, plus corrections to the README and decisions made without the project owner. Dates and times are New York time on 2026-11-21 unless stated.

## README corrections

- **"There is no code-section column."** True of the dataset `wvxf-dwi5`. However, its data dictionary (`raw/od-hpd-violations-dict-hpd-code-violations-data-dictionary.xlsx`, sheet "Order Number") lists all 417 order numbers with the official full description (which begins with the cited section), a category, a short description and MD/PD. It is joined into `text/od-hpd-violation-types.csv` as the `dict_*` columns. Order 464 appears in the data but not in the dictionary. In 15 dictionary rows the full description is cut at exactly 255 characters.
- **README counts confirmed** on 2026-11-21 00:35: 612 order-and-class pairs, 400 order numbers, 143 orders under more than one class. Order 508: A 139,019; B 800,630; C 100,891; plus I 2 (the README didn't mention the I).
- **"HAS BEEN UPGRADED TO CLASS ..."** appears only on order 550 (mould): B 65,815 and C 11,517 rows. A broader search for any "UPGRADE" adds 6 rows on orders 491 A (2), 510 B (1), 689 C (2) and 742 C (1). All are flagged in the CSV.
- **NCEI hourly "nothing for 2026"** is true only of the Access Data Service `global-hourly` dataset, whose Central Park data stops between June and October 2025. NCEI's GHCNh product has a Central Park 2026 file running to 2026-11-17 (`endpoints/od-weather-ncei-ghcnh.md`).
- **"api.weather.gov (station KNYC) ... returned hourly 2026 data"** is only partly right: the observations endpoint keeps about the last 7 days (2026-11-14 onward). Queries for 2026-11-10 and earlier, including January and August 2026, returned no observations.
- **Open-Meteo** returns modelled (reanalysis or forecast) values on a grid cell about 4 km from Central Park, including hours that hadn't happened yet. It is not station data.

## Gaps and access problems

- **HPD complaint categories, whole-dataset `$group`:** timed out twice server-side (HTTP 408 after about 10 minutes); a single year (2026) timed out too. Decision: aggregate one month at a time (8 to 50 s each) into `raw/od-hpd-complaint-categories-by-month/` and sum. The 2025 sum matches an independent `count(*)` for 2025 exactly (856,280). The same monthly method is used for 311.
- **Violation-type sampling:** `$order=inspectiondate DESC` with an order-and-class filter was very slow for rare pairs (up to 155 s per query), and the platform was erratic between 01:00 and 01:45 (HTTP 503s; trivial queries taking 4 to 6 s). Decisions:
  - fetch the 40 most recent rows for the largest pairs first;
  - add two aggregate queries (lexicographic min/max description per pair, for all rows and for rows since 2024), which give real sample descriptions for every pair, plus first/last inspection dates;
  - record per row in `sample_source` which method supplied the samples.
  Result: 148 of 612 rows have fewer than 3 distinct samples; 66 of those pairs have fewer than 3 violations in total.
  - 272 pairs (mostly small or no longer issued) still have only min/max samples. A further pass timed out at 120 to 255 s per query even when bounded to the two years before the pair's last inspection, so it was stopped at 02:04 to keep the server free for the 311 and complaint aggregates.
- **What sets the class** is shown in the descriptions for only a few orders (e.g. mould area for 550). For most "concurrent" multi-class orders, the sampled descriptions don't show the driver; `text/od-hpd-violation-types-class-notes.md` marks these "unsettled from this data". Several orders show a clear class change over time (e.g. 568 roaches and 569 mice moved from B to C), recorded as "time shift" without attributing it to a specific law change.
- **Section drift inside one order:** some orders cite different sections over time (e.g. 869 cites § 27-2017.4 and § 27-2018; 550 cites § 27-2005 and § 27-2017.3). `cited_section` is the most common section in the sampled (recent) rows, and `cited_section_variants` lists the others.
- **GeoSearch terms and rate limits:** none published on the docs or about pages; the attribution URL in every response (`/attribution`) returned 404.
- **NYC Open Data license:** the dataset metadata `license` field is empty. The NYC Open Data overview and FAQ pages point to the nyc.gov terms of use, which don't address data reuse. The Open Data Law text (Admin Code § 23-502(d), no restrictions on use) was read from the unofficial mirror nycadmincode.readthedocs.io, because amlegal blocks scripts. Workstream 1 or a verifier should confirm it on amlegal.
- **Socrata paging doc** `https://dev.socrata.com/docs/paging.html` returned 404. The default 1,000-row limit is taken from the NYC Open Data API guide instead.
- **NYC Open Data API guide:** `opendata.cityofnewyork.us/...` redirected to nyc.gov and returned 403 once; `https://www.nyc.gov/opendata/get-started/user-guides/open-data-apis` worked with a browser user agent.
- **HUD FMR effective dates** are not in the API response (only `year`). Take the effective date from HUD's FMR documentation before using it for the Good Cause test.
- **NOAA CDO rate limits** were not stated on the docs page fetched.
- **NYCHA Development Data Book (evjd-dqpz)** has no BBL or address column. Used NYCHA Residential Addresses (3ub5-4ph8) for address, BIN and BBL instead.
- **DHCR rent-stabilized lists** are PDFs only (no API). Converted to CSV by script; see caveats in `endpoints/od-dhcr-rs-buildings.md`.
