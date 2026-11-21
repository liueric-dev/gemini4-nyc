# 311 Service Requests from 2020 to Present

## Dataset name

311 Service Requests from 2020 to Present (311).

NOTE: Learn more about the latest changes to this dataset: https://opendata.cityofnewyork.us/311-service-requests-from-2010-to-present-updates/ 311 responds to thousands of inquiries, comments and requests from customers every single day. This dataset represents only service requests that can be directed to specific agencies. This dataset is updated daily and expected values for many fields will change over time. The lists of expected values associated with each column are not exhaustive. Each row of data contains information about the service request, including complaint type, responding agency, and geographic location. However the data does not reveal any personally identifying information about the customer who made the request. For data from 2010-2019 see: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-2019/76ig-c548/about_data

## Dataset ID

`erm2-nwe9`. Portal page: https://data.cityofnewyork.us/d/erm2-nwe9

## API URL

`https://data.cityofnewyork.us/resource/erm2-nwe9.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 22:11.
- Metadata saved: `raw/od-311-service-requests-metadata.json`.
- Data dictionary: `raw/od-311-service-requests-dict-311-servicerequest-2020-present-datadictionary-updated-2025.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `unique_key` | text | Unique identifier of a Service Request (SR) in the open data set |
| `created_date` | calendar_date | Date SR was created |
| `closed_date` | calendar_date | Date SR was closed by responding agency |
| `agency` | text | Acronym of responding City Government Agency |
| `complaint_type` | text | This is the first level of a hierarchy identifying the topic of the incident or condition. Problem (formerly Complaint Type) broadly describes the topic of the incident or condition and are defined by the responding agencies. New Problems may be added in response to changes in customer demand. |
| `descriptor` | text | This is associated to the Problem (formerly Complaint Type), and provides further detail on the incident or condition. Problem Detail (formerly Descriptor) values are dependent on the Problem, and are not always required in the service request. |
| `descriptor_2` | text | A third level of detail about the Problem (formerly Complaint Type) beyond the Problem Detail (formerly Descriptor). This is not used by every category of issue. |
| `location_type` | text | Describes the type of location used in the address information |
| `incident_address` | text | House number of incident address provided by submitter. |
| `bbl` | text | Borough Block and Lot, provided by geovalidation. Parcel number to identify the location of location of buildings and properties in NYC. |
| `borough` | text | Provided by the submitter and confirmed by geovalidation. |
| `status` | text | Status of SR submitted |
| `resolution_description` | text | Describes the last action taken on the SR by the responding agency. May describe next or future steps. |
| `open_data_channel_type` | text | Indicates how the SR was submitted to 311. i.e. By Phone, Online, Mobile, Other or Unknown. |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/erm2-nwe9.json?%24where=bbl%3D%272023700005%27&%24limit=50000&%24order=created_date+DESC&%24select=unique_key%2Ccreated_date%2Cclosed_date%2Cagency%2Ccomplaint_type%2Cdescriptor%2Cdescriptor_2%2Clocation_type%2Cstatus%2Cresolution_description%2Cbbl%2Cborough"
```

Decoded: `$where=bbl='2023700005'&$limit=50000&$order=created_date DESC&$select=unique_key,created_date,closed_date,agency,complaint_type,descriptor,descriptor_2,location_type,status,resolution_description,bbl,borough`

Result on 2026-11-21T00:57: HTTP 200, 275 rows, 18.82 s.

## Example response row

```json
{
 "unique_key": "70225496",
 "created_date": "2026-08-28T18:03:15.000",
 "closed_date": "2026-09-01T00:00:00.000",
 "agency": "DOB",
 "complaint_type": "Real Time Enforcement",
 "descriptor": "Work Without A Permit - Occupied Multiple Dwelling",
 "status": "Closed",
 "resolution_description": "The Department of Buildings attempted to investigate this complaint twice but could not gain access to the location. If the problem still exists, please call 311 and file a new complaint with additional access information. If you are outside of New York City, please call (212) NEW-YORK (212-639-9675).",
 "bbl": "2023700005",
 "borough": "BRONX"
}
```

## Caveats

- 2020 to present only; 2010 to 2019 is a separate dataset, 76ig-c548 (dataset description).
- The column labels were renamed on the portal (Problem = `complaint_type`, Problem Detail = `descriptor`) but the API field names are unchanged (column descriptions).
- "The data does not reveal any personally identifying information about the customer" (dataset description).
- NYCHA does not use the 311 system, so NYCHA repair requests are not here (311 data dictionary, Agency field note).
- Single-building queries are among the slowest (about 19 s for the first demo building); add a date filter.
- HPD complaint types and descriptors: see `text/od-311-hpd-complaint-types.csv` (counts) and `text/od-311-dictionary-hpd-complaint-details.csv` (the full hierarchy from the data dictionary).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
