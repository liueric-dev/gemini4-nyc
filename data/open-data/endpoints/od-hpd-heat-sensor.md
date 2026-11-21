# Buildings Selected for the Heat Sensor Program (HSP)

## Dataset name

Buildings Selected for the Heat Sensor Program (HSP) (NYC Department of Housing Preservation and Development (HPD)).

Every two years beginning in July 2020, the Department of Housing Preservation and Development (HPD) designates 50 class "A" multiple dwellings with heat violations and complaints for participation in a program requiring installation of heat sensors.

## Dataset ID

`h4mf-f24e`. Portal page: https://data.cityofnewyork.us/d/h4mf-f24e

## API URL

`https://data.cityofnewyork.us/resource/h4mf-f24e.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-01 14:30.
- Metadata saved: `raw/od-hpd-heat-sensor-metadata.json`.
- Data dictionary: `raw/od-hpd-heat-sensor-dict-heat-sensors-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `building_id` | number |  |
| `bbl` | number |  |
| `bin` | number |  |
| `total_units` | number |  |
| `program_start_date` | calendar_date |  |
| `current_status` | text |  |
| `discharge_date` | calendar_date |  |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/h4mf-f24e.json?%24where=bbl%3D2023700005&%24limit=50000"
```

Decoded: `$where=bbl=2023700005&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 0 rows, 0.719 s.

## Example response row

No rows for any demo building; see the portal page for a sample.

## Caveats

- Every two years since July 2020 HPD designates 50 class A multiple dwellings with heat violations and complaints for heat sensors (dataset description).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
