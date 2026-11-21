# NCEI Access Data Service: global-hourly (Integrated Surface Data), Central Park

## Dataset name

NCEI Access Data Service v1, dataset `global-hourly`.

## Dataset ID

Station `72505394728` (the response's `NAME` field reads "NY CITY CENTRAL PARK, NY US" and `CALL_SIGN` is `KNYC`).

## API URL

- `https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-hourly&stations=72505394728&dataTypes=TMP&format=json&includeStationName=true&units=metric&startDate=...&endDate=...`
- Docs: https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation (`text/od-ncei-access-data-service-docs.md`)

No key.

## Key fields

- `DATE` (UTC), `REPORT_TYPE` (`FM-15` routine), `QUALITY_CONTROL`, `STATION`, `CALL_SIGN`, `NAME`
- `TMP`: `"-0017,5"` means -1.7 °C (tenths of a degree), then a quality flag after the comma

## Example query

```
curl "https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-hourly&stations=72505394728&dataTypes=TMP&format=json&includeStationName=true&units=metric&startDate=2025-01-15T00:00:00&endDate=2025-01-15T23:59:59"
```

Saved: `raw/od-ncei-global-hourly-knyc-2025-01-15.json` (data), `raw/od-ncei-global-hourly-knyc-2026-01-15.json` and `raw/od-ncei-global-hourly-knyc-2026-11-10.json` (both `[]`).

## Example response row

```json
{"DATE":"2025-01-15T00:51:00","REPORT_TYPE":"FM-15","QUALITY_CONTROL":"V020","STATION":"72505394728","TMP":"-0017,5","SOURCE":"7","CALL_SIGN":"KNYC ","NAME":"NY CITY CENTRAL PARK, NY US"}
```

## How far back and how recent

- January 2025 and 2025-06-01 return data. 2025-10-01, December 2025, January 2026 and November 2026 return an empty list. The dataset stops somewhere between June and October 2025 for this station.

## License

US government work (NOAA/NCEI); no licence statement in the docs page fetched.

## Caveats

- Not usable for 2026. Use GHCNh (`od-weather-ncei-ghcnh.md`), which does have 2026.
- Response time about 0.1 to 0.4 s.
