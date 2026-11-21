# NCEI Global Historical Climatology Network hourly (GHCNh), Central Park

## Dataset name

NOAA NCEI Global Historical Climatology Network hourly (GHCNh), station USW00094728 "NY CITY CNTRL PARK".

## Dataset ID

Station `USW00094728` (the station file's own `STATION` and `Station_name` columns confirm it; source station ID `ICAO-KNYC`).

## API URL

There is no query API. Static files are published per station:
- By year: `https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/2026/psv/GHCNh_USW00094728_2026.psv` (38 MB, `Last-Modified: Thu, 19 Nov 2026 07:34:26 GMT`)
- Period of record: `https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-station/GHCNh_USW00094728_por.psv` (363 MB; not downloaded)
- Docs: `raw/od-ncei-ghcnh-documentation.pdf` (Version 1.1.0, updated March 10, 2026), text in `text/od-ncei-ghcnh-documentation.md`. Product page: `text/od-ncei-ghcnh-product-page.md`.

## Key fields

Pipe-separated. Per the docs: `DATE` plus `Year`/`Month`/`Day`/`Hour`/`Minute` are in **UTC**; `temperature` is 2 m air temperature in °C to tenths. Each variable has `_Measurement_Code`, `_Quality_Code` (docs Table 3, "code varies by source"), `_Report_Type` (`FM15` routine METAR, `FM16` special), `_Source_Code`, `_Source_Station_ID`.

Derived file: `text/od-ncei-ghcnh-knyc-2026-hourly-temperature.csv` (9,479 temperature rows, 2026-01-01T00:51Z to 2026-11-17T15:51Z) with columns `station, date_utc, date_new_york, temperature_c, temperature_f, quality_code, report_type`. Fahrenheit and New York time were computed by script; everything else is copied from the source.

## Example query

```
curl -O "https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/2026/psv/GHCNh_USW00094728_2026.psv"
```

## Example response row

```
USW00094728|NY CITY CNTRL PARK|2026-11-17T15:51:00|2026|11|17|15|51|40.7789|-73.9692|42.7|10.6|||FM15|413|ICAO-KNYC|1.1|...
```

Derived CSV row: `USW00094728,2026-01-01T00:51:00Z,2025-12-31T19:51-05:00,-1.1,30.0,1,FM15`

## How far back and how recent

- The 2026 file runs to 2026-11-17 15:51 UTC (downloaded 2026-11-21 00:47 New York time), so it lags by about 3 to 4 days.
- The period-of-record file covers the station's full history (it was not downloaded; the size is from a HEAD request).

## License

NOAA/NCEI is a US federal agency, so the data is a US government work. No licence statement was found in the documents fetched; recorded as `public-domain` on that basis. Check the NCEI product page before relying on it.

## Caveats

- This replaces the README's claim that NCEI had "nothing for 2026". That claim is true for the Access Data Service `global-hourly` dataset (`od-weather-ncei-global-hourly.md`), not for GHCNh.
- The product page warns: "Many access portals, interactive maps, and data folders are currently unavailable due to the migration. Expect delayed data archival and slower update cycles for many products."
- Static file, so a live lookup means downloading the 38 MB year file (or caching it daily).
- Quality code `1` appears on the 2026 rows. Table 3 lists `1 = Passed all quality control checks` for legacy sources 313 to 346; this file's source code is 413, so check Table 3 before relying on the flag.
