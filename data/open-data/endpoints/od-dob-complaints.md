# DOB Complaints Received

## Dataset name

DOB Complaints Received (Department of Buildings (DOB)).

This is the universe of complaints received by Department of Buildings (DOB). It includes complaints that come from 311 or that are entered into the system by DOB staff. A Complaint Categories codes can be found at http://www1.nyc.gov/assets/buildings/pdf/bis_complaint_disposition_codes.pdf

## Dataset ID

`eabe-havv`. Portal page: https://data.cityofnewyork.us/d/eabe-havv

## API URL

`https://data.cityofnewyork.us/resource/eabe-havv.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 12:33.
- Metadata saved: `raw/od-dob-complaints-metadata.json`.
- Data dictionary: `raw/od-dob-complaints-dict-dd-dob-complaints-received-2019-08-21.xlsx`, `raw/od-dob-complaints-dict-dobcomplaints-complaint-category-list.pdf` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `complaint_number` | text | Complaint number starting with borough code: (1= Manhattan, 2= Bronx, 3 = Brooklyn, 4 = Queens, 5 = Staten Island) |
| `status` | text | Status of Complaint |
| `date_entered` | text | Date Complaint was Entered |
| `house_number` | text | House Number of Complaint |
| `house_street` | text | House Street of Complaint |
| `bin` | text | Number assigned by City Planning to a specific building |
| `complaint_category` | text | DOB Complaint Category Codes (01-Accident Construction/Plumbing, etc.) |
| `unit` | text | Unit dispositioning Complaint |
| `disposition_date` | text | Date Complaint was Dispositioned |
| `disposition_code` | text | Disposition Code of Complaint (A1-Building Violations Served, L1-Partial Stop Work Order,etc.) |
| `inspection_date` | text | Inspection Date of Complaint |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/eabe-havv.json?%24where=bin%3D%272001261%27&%24limit=50000"
```

Decoded: `$where=bin='2001261'&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 13 rows, 0.37 s.

## Example response row

```json
{
 "complaint_number": "2433955",
 "status": "CLOSED",
 "date_entered": "02/09/2026",
 "house_number": "1048",
 "house_street": "WASHINGTON AVENUE",
 "zip_code": "10456",
 "bin": "2001261",
 "community_board": "203",
 "complaint_category": "45",
 "unit": "Q-L",
 "disposition_date": "03/26/2026",
 "disposition_code": "C2",
 "inspection_date": "03/24/2026",
 "dobrundate": "20261120000000"
}
```

## Caveats

- Complaint category and disposition codes are listed in `raw/od-dob-complaints-dict-dobcomplaints-complaint-category-list.pdf` (attachment) and the dataset description's link to `bis_complaint_disposition_codes.pdf`.
- Query by `bin` (text). `date_entered` and `disposition_date` are text in MM/DD/YYYY form (e.g. `02/09/2026` for a demo building), so they do not sort as dates.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
