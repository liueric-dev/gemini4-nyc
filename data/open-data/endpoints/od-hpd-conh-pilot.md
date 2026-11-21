# Certification of No Harassment (CONH) Pilot Building List

## Dataset name

Certification of No Harassment (CONH) Pilot Building List (Housing Preservation and Development (HPD)).

List of buildings subject to Certification of No Harassment (CONH) Pilot Program. Data is current as of the update date shown below. To see the latest status of a building, visit HPD Online at https://www1.nyc.gov/site/hpd/about/hpdonline.page.

## Dataset ID

`bzxi-2tsw`. Portal page: https://data.cityofnewyork.us/d/bzxi-2tsw

## API URL

`https://data.cityofnewyork.us/resource/bzxi-2tsw.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): As needed; automated: No; rows last updated 2026-09-25 08:43.
- Metadata saved: `raw/od-hpd-conh-pilot-metadata.json`.
- Data dictionary: `raw/od-hpd-conh-pilot-dict-conh-pilot-building-list-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `building_id` | number | Unique identifier of building (HPD) |
| `bbl` | number | Borough, block, lot - the unique identifier for each tax lot in NYC |
| `bin` | number | Unique identifier of building (DOB) |
| `bqi` | text | Building Qualification Index; building meets threshold of calculated BQI |
| `aep_order` | text | Building was discharged from the HPD Alternative Enforcement Program (AEP) |
| `discharged_7a` | text | Building was discharged from the HPD 7A program |
| `hpd_vacate_order` | text | Building was issued HPD Order to Vacate |
| `dob_vacate_order` | text | Building was issued Department of Buildings (DOB) Order to Vacate |
| `harassment_finding` | text | Building was the subject of a finding of harassment by a court or by New York State Homes and Community Renewal |
| `date_added` | calendar_date | Date added to CONH Pilot Program List |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/bzxi-2tsw.json?%24where=bbl%3D2023700005&%24limit=50000"
```

Decoded: `$where=bbl=2023700005&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 0 rows, 5.647 s.

## Example response row

No rows for any demo building; see the portal page for a sample.

## Caveats

- Buildings subject to the Certification of No Harassment pilot; "Data is current as of the update date" (dataset description). Updated as needed.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
