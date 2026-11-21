# Buildings Selected for the Alternative Enforcement Program (AEP)

## Dataset name

Buildings Selected for the Alternative Enforcement Program (AEP) (NYC Department of Housing Preservation and Development (HPD)).

Each year, the Department of Housing Preservation and Development (HPD) designates severely distressed multiple dwellings for participation in the Alternative Enforcement Program (AEP). HPD is required by law to submit and post an annual summary report of all AEP buildings. This dataset includes all buildings selected for participation in the AEP and the current status of the building in the program.

## Dataset ID

`hcir-3275`. Portal page: https://data.cityofnewyork.us/d/hcir-3275

## API URL

`https://data.cityofnewyork.us/resource/hcir-3275.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-01 15:01.
- Metadata saved: `raw/od-hpd-aep-metadata.json`.
- Data dictionary: `raw/od-hpd-aep-dict-20181210-buildings-selected-for-the-alternative-enforcement-program-aep-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `building_id` | number | The Building ID is a unique numeric identifier assigned to each building by HPD. |
| `bbl` | number |  |
| `bin` | number |  |
| `total_units` | number | Total Units reflects the number of units in the building as of the report run date and may vary from the unit count reported when the building was selected for the AEP program. HPD records indicated that all the buildings had at least three dwelling units at the time of selection. |
| `aep_start_date` | calendar_date | The date the building was selected for participation in the AEP. All buildings in a particular round will have the same start date. |
| `of_b_c_violations_at_start` | number | The count of hazardous and immediately hazardous violations open on the date the building was selected for participation in the AEP. |
| `current_status` | text | "Active" buildings are currenty participating in program. "Discharged" buildings have met a statutory requirement for removal from the program. |
| `discharge_date` | calendar_date | The date the building was removed from the program. |
| `aep_round` | text | The round identifies a group of buildings selected for the AEP annually. |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/hcir-3275.json?%24where=bbl%3D2023700005&%24limit=50000"
```

Decoded: `$where=bbl=2023700005&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 2 rows, 0.357 s.

## Example response row

```json
{
 "building_id": "119624",
 "boro": "Bronx",
 "phn": "1048",
 "street_address": "WASHINGTON AVENUE",
 "total_units": "3",
 "aep_start_date": "2025-01-31T00:00:00.000",
 "of_b_c_violations_at_start": "368",
 "current_status": "AEP Discharged",
 "discharge_date": "2025-07-25T00:00:00.000",
 "aep_round": "Aep Round 18",
 "postcode": "10456",
 "latitude": "40.827336",
 "longitude": "-73.909084",
 "community_board": "3",
 "council_district": "16",
 "census_tract": "18501",
 "bin": "2001261",
 "bbl": "2023700005",
 "nta": "Morrisania"
}
```

## Caveats

- Buildings HPD designated as "severely distressed" for the Alternative Enforcement Program, with current status (dataset description).
- Updated monthly (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
