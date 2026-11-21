# DOB Permit Issuance

## Dataset name

DOB Permit Issuance (Department of Buildings (DOB)).

The Department of Buildings (DOB) issues permits for construction and demolition activities in the City of New York. The construction industry must submit an application to DOB with details of the construction job they would like to complete. The primary types of application, aka job type, are: New Building, Demolition, and Alterations Type 1, 2, and 3. Each job type can have multiple work types, such as general construction, boiler, elevator, and plumbing. Each work type will receive a separate permit. (See the DOB Job Application Filings dataset for information about each job application.) Each row/record in this dataset represents the life cycle of one permit for one work type. The dataset is updated daily with new records, and each existing record will be updated as the permit application moves through the approval process to reflect the latest status of the application. Note: This dataset only includes permits issued in the Buildings Information System (BIS), most current permits are now issued in DOB NOW -- see the DOB NOW: Build – Approved Permits dataset.

## Dataset ID

`ipu4-2q9a`. Portal page: https://data.cityofnewyork.us/d/ipu4-2q9a

## API URL

`https://data.cityofnewyork.us/resource/ipu4-2q9a.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-19 21:10.
- Metadata saved: `raw/od-dob-permits-metadata.json`.
- Data dictionary: `raw/od-dob-permits-dict-dd-dob-permit-issuance-2019-07-29.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `bin__` | text | Number assigned by City Planning to a specific building |
| `job__` | text | Number assigned by DOB to Job Filing |
| `job_type` | text | Job Type, based on DOB Job Code (NB-New Building, A1, A2, A3- Alterations 1-3, SG-Sign, etc.) |
| `work_type` | text | DOB Designated Work Types (PL-Plumbing, BL-Boiler, MH-Mechanical, OT-Other Constuction Equipment, etc.) |
| `permit_status` | text | Permit Status |
| `filing_status` | text | Filing Status |
| `permit_type` | text | Permit Type (DM-Demolition, EW-Equipment Work, PL-Plumbing, etc.) Complete List - http://www.nyc.gov/html/dob/downloads/pdf/bisjobstatus.pdf |
| `filing_date` | text | Filing Date |
| `issuance_date` | text | Issuance Date |
| `expiration_date` | text | Expiration Date |
| `residential` | text | Residential |
| `bldg_type` | text | 1-2-3 Family or Other |

## Example query

Demo building `3906-114-st-qn` (BBL 4017860017, BIN 4044993):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/ipu4-2q9a.json?%24where=bin__%3D%274044993%27&%24limit=50000&%24select=bin__%2Cjob__%2Cjob_type%2Cwork_type%2Cpermit_status%2Cfiling_status%2Cpermit_type%2Cfiling_date%2Cissuance_date%2Cexpiration_date%2Cresidential%2Cbldg_type"
```

Decoded: `$where=bin__='4044993'&$limit=50000&$select=bin__,job__,job_type,work_type,permit_status,filing_status,permit_type,filing_date,issuance_date,expiration_date,residential,bldg_type`

Result on 2026-11-21T00:59: HTTP 200, 27 rows, 138.633 s.

## Example response row

```json
{
 "bin__": "4044993",
 "job__": "400382652",
 "job_type": "A2",
 "work_type": "OT",
 "permit_status": "ISSUED",
 "filing_status": "INITIAL",
 "permit_type": "EW",
 "filing_date": "1993-07-01",
 "issuance_date": "1993-07-01",
 "expiration_date": "1994-03-20",
 "residential": "YES",
 "bldg_type": "2"
}
```

## Caveats

- BIS permits only; "most current permits are now issued in DOB NOW" (dataset description). Query both.
- Field names have trailing underscores (`bin__`, `job__`). Permittee and owner name and phone fields exist; the demo query selected none of them.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
