# DOB Certificate Of Occupancy

## Dataset name

DOB Certificate Of Occupancy ().

A Certificate of Occupancy (CO) states a building’s legal use and/or type of permitted occupancy. New buildings must have a CO, and existing buildings must have a current or amended CO when there is a change in use, egress or type of occupancy. No one may legally occupy a building until the Department has issued a Certificate of Occupancy or Temporary Certificate of Occupancy. The Department issues a final Certificate of Occupancy when the completed work matches the submitted plans for new buildings or major alterations. It issues a Letter of Completion for minor alterations to properties. These documents confirm the work complies with all applicable laws, all paperwork has been completed, all fees owed to the Department have been paid, all relevant violations have been resolved and all necessary approvals have been received from other City Agencies. This dataset contains all Certificates of Occupancy issued from 7/12/2012 to March 2021. PDFs of the actual COs are viewable in www.nyc.gov/bis. For COs issued since March 2021, see DOB NOW: Certificate of Occupancy dataset.

## Dataset ID

`bs8b-p36w`. Portal page: https://data.cityofnewyork.us/d/bs8b-p36w

## API URL

`https://data.cityofnewyork.us/resource/bs8b-p36w.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 16:32.
- Metadata saved: `raw/od-dob-cofo-metadata.json`.
- Data dictionary: `raw/od-dob-cofo-dict-dd-dob-certificate-of-occupancy-2017-11-22.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `job_number` | text | Number assigned by the Department of Buildings for the Certificate of Occupancy Application and Filing. |
| `job_type` | text | Job Type based on DOB Job Code (NB- New Building, A1,A2,A3 - Alternations 1-3, SG-Sign, etc.) |
| `c_o_issue_date` | calendar_date | Date the Certificate of Occupancy was issued |
| `bin` | text | Number assigned by City Planning for a specific building. |
| `bbl` | text | Borough-Block_Lot |
| `pr_dwelling_unit` | text | Proposed number of Dwelling Units |
| `ex_dwelling_unit` | text | Existing number of Dwelling Units |
| `issue_type` | text | Certificate of Occupancy Issue Type (Temporary, Final) |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/bs8b-p36w.json?%24where=bin%3D%272001261%27&%24limit=50000"
```

Decoded: `$where=bin='2001261'&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 0 rows, 0.376 s.

## Example response row

No rows for any demo building; see the portal page for a sample.

## Caveats

- Certificates of Occupancy issued 2012-07-12 to March 2021 only; after that use DOB NOW: Certificate of Occupancy (pkdm-hqz6). PDFs of older COs are on BIS (dataset description).
- None of the four demo buildings had a CO in either dataset, which is typical for older buildings.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
