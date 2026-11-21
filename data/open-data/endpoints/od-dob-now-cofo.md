# DOB NOW: Certificate of Occupancy

## Dataset name

DOB NOW: Certificate of Occupancy (Department of Buildings (DOB)).

This data set includes certificates of occupancy issued through the New York City Department of Buildings' DOB NOW: Certificate of Occupancy module. This module was released in March of 2021, anbd from that point onward this data set should be utilized instead of the "DOB Certificate of Occupancy" data set. The data is collected because the Department of Buildings tracks Certificates of Occupancies issued. This data include items such as job filing name, job filing label, BIN, Address, and Certificate of Occupancy status, sequence, label, and issuance date. "A Certificate of Occupancy (CO) states a legal use and/or type of permitted occupancy of a building. New buildings must have a CO, and existing buildings must have a current or amended CO when there is a change in use, egress or type of occupancy. No one may legally occupy a building until the Department has issued a CO or Temporary Certificate of Occupancy (TCO). A CO confirms that the completed work complies with all applicable laws, all paperwork has been completed, all fees owed to the Department have been paid, all relevant violations have been resolved, and all necessary approvals have been received from other City Agencies. The Department issues a final CO when the completed work matches the submitted plans for new buildings or major alterations."

## Dataset ID

`pkdm-hqz6`. Portal page: https://data.cityofnewyork.us/d/pkdm-hqz6

## API URL

`https://data.cityofnewyork.us/resource/pkdm-hqz6.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 16:03.
- Metadata saved: `raw/od-dob-now-cofo-metadata.json`.
- Data dictionary: `raw/od-dob-now-cofo-dict-data-dictionary-dob-now-certificate-of-occupancy-final.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `job_filing_name` | text | The filing sequence indicator |
| `job_type` | text | Overall job type for the application |
| `bin` | text | Building Identification Number assigned by Department of City Planning |
| `bbl` | text |  |
| `c_of_o_status` | text | The status of the Certificate of Occupancy |
| `c_of_o_filing_type` | text | The type of Certificate of Occupancy requested |
| `c_of_o_issuance_date` | text | The date the Certificate of Occupancy is issued |
| `number_of_dwelling_units` | text |  |
| `c_of_o_number` | text |  |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/pkdm-hqz6.json?%24where=bin%3D%272001261%27&%24limit=50000"
```

Decoded: `$where=bin='2001261'&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 0 rows, 0.448 s.

## Example response row

No rows for any demo building; see the portal page for a sample.

## Caveats

- COs issued through DOB NOW since March 2021 (dataset description).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
