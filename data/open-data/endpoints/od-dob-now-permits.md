# DOB NOW: Build – Approved Permits

## Dataset name

DOB NOW: Build – Approved Permits (Department of Buildings (DOB)).

List of all approved construction permits in DOB NOW except for Electrical , Elevator , and Limited Alteration Application (LAA) which have their own datasets.

## Dataset ID

`rbx6-tga4`. Portal page: https://data.cityofnewyork.us/d/rbx6-tga4

## API URL

`https://data.cityofnewyork.us/resource/rbx6-tga4.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 14:49.
- Metadata saved: `raw/od-dob-now-permits-metadata.json`.
- Data dictionary: `raw/od-dob-now-permits-dict-dob-now-build-approved-permits-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `job_filing_number` | text |  |
| `work_permit` | text |  |
| `filing_reason` | text |  |
| `work_type` | text |  |
| `approved_date` | calendar_date |  |
| `issued_date` | calendar_date |  |
| `expired_date` | calendar_date |  |
| `job_description` | text |  |
| `permit_status` | text |  |
| `bin` | text |  |
| `bbl` | number |  |

## Example query

Demo building `3906-114-st-qn` (BBL 4017860017, BIN 4044993):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/rbx6-tga4.json?%24where=bin%3D%274044993%27&%24limit=50000&%24select=job_filing_number%2Cwork_permit%2Cfiling_reason%2Cwork_type%2Capproved_date%2Cissued_date%2Cexpired_date%2Cjob_description%2Cpermit_status%2Cbin%2Cbbl"
```

Decoded: `$where=bin='4044993'&$limit=50000&$select=job_filing_number,work_permit,filing_reason,work_type,approved_date,issued_date,expired_date,job_description,permit_status,bin,bbl`

Result on 2026-11-21T00:59: HTTP 200, 8 rows, 2.17 s.

## Example response row

```json
{
 "job_filing_number": "Q01459804-I1",
 "work_permit": "Q01459804-I1-GC-CX",
 "filing_reason": "Initial Permit",
 "work_type": "Mechanical Systems",
 "approved_date": "2026-10-16T00:00:00.000",
 "issued_date": "2026-11-13T00:00:00.000",
 "expired_date": "2026-12-31T00:00:00.000",
 "job_description": "Minor partition work and dryer exhaust duxtwork as required to replace existing washers and dryers.  PL work filed subsequently.  No change is use, occupancy or egress",
 "permit_status": "Permit Issued",
 "bin": "4044993",
 "bbl": "4017860017"
}
```

## Caveats

- All approved DOB NOW construction permits except electrical, elevator and Limited Alteration Applications (dataset description).
- Owner and applicant name fields exist; the demo query selected none of them.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
