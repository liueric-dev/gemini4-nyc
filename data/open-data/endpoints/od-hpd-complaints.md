# Housing Maintenance Code Complaints and Problems

## Dataset name

Housing Maintenance Code Complaints and Problems (Department of Housing Preservation & Development (HPD)).

The Department of Housing Preservation and Development (HPD) records complaints that are made by the public for conditions which violate the New York City Housing Maintenance Code (HMC) or the New York State Multiple Dwelling Law (MDL).

## Dataset ID

`ygpa-z7cr`. Portal page: https://data.cityofnewyork.us/d/ygpa-z7cr

## API URL

`https://data.cityofnewyork.us/resource/ygpa-z7cr.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 10:09.
- Metadata saved: `raw/od-hpd-complaints-metadata.json`.
- Data dictionary: `raw/od-hpd-complaints-dict-housing-maintenance-code-complaints-and-problems-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `problem_id` | number | Unique identifier of this problem |
| `complaint_id` | number | Unique identifier of the complaint this problem is associated with |
| `building_id` | number | Unique identifier given to a building record |
| `bbl` | number |  |
| `bin` | number |  |
| `received_date` | calendar_date | Date when the complaint was received |
| `apartment` | text | Number of the unit or apartment in a building |
| `unit_type` | text | Type of space where the problem was reported |
| `space_type` | text | Type of space where the problem was reported |
| `type` | text | Code indicating the problem type |
| `major_category` | text | The major category of the problem |
| `minor_category` | text | The minor category of the problem |
| `problem_code` | text | The problem code |
| `complaint_status` | text | The status of the complaint |
| `complaint_status_date` | calendar_date | Date when the complaint status was updated |
| `problem_status` | text | The status of the problem |
| `problem_status_date` | calendar_date | Status description |
| `status_description` | text |  |
| `problem_duplicate_flag` | text | Duplicate complaint Indicator |
| `complaint_anonymous_flag` | text | Anonymous complaint Indicator |
| `unique_key` | text | Unique identifier of a Service Request (SR) in the open data set * Ties to 311 |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/ygpa-z7cr.json?%24where=bbl%3D2023700005&%24limit=50000&%24order=received_date+DESC"
```

Decoded: `$where=bbl=2023700005&$limit=50000&$order=received_date DESC`

Result on 2026-11-21T00:57: HTTP 200, 368 rows, 7.917 s.

## Example response row

```json
{
 "received_date": "2026-04-29T10:42:47.000",
 "problem_id": "28634817",
 "complaint_id": "14713179",
 "building_id": "119624",
 "borough": "BRONX",
 "house_number": "1048",
 "street_name": "WASHINGTON AVENUE",
 "post_code": "10456",
 "block": "2370",
 "lot": "5",
 "apartment": "1",
 "community_board": "3",
 "unit_type": "PUBLIC AREA",
 "space_type": "BUILDING ENTRANCE",
 "type": "NON EMERGENCY",
 "major_category": "GENERAL",
 "minor_category": "BELL/BUZZER/INTERCOM",
 "problem_code": "BROKEN OR MISSING",
 "complaint_status": "CLOSE",
 "complaint_status_date": "2026-05-02T05:20:24.000",
 "problem_status": "CLOSE",
 "problem_status_date": "2026-05-01T17:22:50.000",
 "status_description": "HPD attempted to conduct an inspection in response to this complaint, but was unable to complete the inspection. Please submit a new service request with 311 if the condition still exists. For more information on the reason why HPD was unable to inspect, contact HPD at the Tenant Information Messaging Service at 212-863-4951.",
 "problem_duplicate_flag": "N",
 "complaint_anonymous_flag": "N",
 "latitude": "40.827336000000003",
 "longitude": "-73.909083999999993",
 "council_district": "16",
 "census_tract": "18501",
 "bin": "2001261",
 "bbl": "2023700005",
 "nta": "Morrisania"
}
```

## Caveats

- One row per problem; one complaint can have several problems (`complaint_id`).
- `unique_key` ties the problem to the 311 service request.
- `bbl` is a number here (no quotes), unlike `wvxf-dwi5` where it is text.
- `status_description` is HPD's outcome text, e.g. whether an inspection found a violation or could not get access.
- Records go back to 2001-12-16 (earliest `received_date`). A whole-dataset `$group` timed out (HTTP 408 after about 10 minutes), so the category CSV was built from yearly chunks.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
