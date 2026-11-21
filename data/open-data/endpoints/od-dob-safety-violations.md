# DOB Safety Violations

## Dataset name

DOB Safety Violations (Department of Buildings (DOB)).

This data set includes newer civil penalties (commonly referred to as ‘DOB Violations’) that were issued or payable in DOB NOW. For older civil penalties, see the DOB Violations data set (note: some violations are duplicated in both data sets). Separately, summonses that are issued by DOB but adjudicated by OATH/ECB are in the DOB ECB Violations data set.

## Dataset ID

`855j-jady`. Portal page: https://data.cityofnewyork.us/d/855j-jady

## API URL

`https://data.cityofnewyork.us/resource/855j-jady.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 14:13.
- Metadata saved: `raw/od-dob-safety-violations-metadata.json`.
- Data dictionary: `raw/od-dob-safety-violations-dict-dob-now-safety-violations-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `bin` | text | Building Identification Number assigned by Department of City Planning |
| `bbl` | number | The BBL (Borough, Block, and Lot) is a unique combination of three numeric codes - a 1-digit borough number, a block number (up to 5 digits) and a lot number (up to 4 digits) -- designated and modified by the Department of Finance (DOF). BBLs are used by various city agencies to identify real estate |
| `violation_issue_date` | calendar_date | The date of violation issuance |
| `violation_number` | text | The violation identifier |
| `violation_type` | text | The type of violation issued |
| `violation_remarks` | text | Note recorded about the violation |
| `violation_status` | text | The status of the violation |
| `device_number` | text | The devices identification number |
| `device_type` | text | The specific type of device |

## Example query

Demo building `3906-114-st-qn` (BBL 4017860017, BIN 4044993):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/855j-jady.json?%24where=bin%3D%274044993%27&%24limit=50000"
```

Decoded: `$where=bin='4044993'&$limit=50000`

Result on 2026-11-21T00:59: HTTP 200, 14 rows, 20.719 s.

## Example response row

```json
{
 "bin": "4044993",
 "violation_issue_date": "2024-10-11T00:00:00.000",
 "violation_number": "VIO-FTC-VT-CAT1-202312-0016595",
 "violation_type": "FTC-VT-CAT1-CO",
 "violation_remarks": "Violation Issued-Failure To File 2023 Cat1 Test Affirmation of Correction",
 "violation_status": "Active",
 "device_number": "4P4399",
 "device_type": "Elevators",
 "cycle_end_date": "2023-12-31T00:00:00.000",
 "borough": "Queens",
 "block": "1786",
 "lot": "17",
 "house_number": "39-06",
 "street": "114 STREET",
 "city": "New York",
 "state": "New York",
 "zip": "11368",
 "latitude": "40.753209",
 "longitude": "-73.852941",
 "community_board": "403",
 "council_district": "21",
 "bbl": "4017860017",
 "census_tract_2020_": "39902",
 "neighborhood_tabulation_area_nta_2020_": "North Corona"
}
```

## Caveats

- Newer DOB civil penalties issued or payable in DOB NOW (boilers, elevators, facades and similar), per the dataset description.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
