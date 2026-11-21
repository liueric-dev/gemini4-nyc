# Housing Maintenance Code Violations

## Dataset name

Housing Maintenance Code Violations (Department of Housing Preservation and Development (HPD)).

Pursuant to New York City’s Housing Maintenance Code, the Department of Housing Preservation and Development (HPD) issues violations against conditions, in rental dwelling units and buildings, that have been verified to violate the New York City Housing Maintenance Code (HMC) or the New York State Multiple Dwelling Law (MDL). Each row in this dataset contains discrete information about one violation of the New York City Housing Maintenance Code or New York State Multiple Dwelling Law. Each violation is identified using a unique Violation ID. These Laws are in place to provide requirements for the maintenance of residential dwelling units within New York City. Violations are issued by Housing Inspectors after a physical inspection is conducted (except for class I violations which are generally administratively issued). Violations are issued in four classes: Class A (non-hazardous), Class B (hazardous), Class C (immediately hazardous) and Class I (information orders). For more information on violations, see https://www1.nyc.gov/site/hpd/owners/compliance-clear-violations.page The base data for this file is all violations open as of October 1, 2012. Violation data is updated daily. The daily update includes both new violations and updates to the status of previously issued violations. An open violation is a violation which is still active on the Department records. See the status table for determining how to filter for open violations versus closed violations, and within open vi

## Dataset ID

`wvxf-dwi5`. Portal page: https://data.cityofnewyork.us/d/wvxf-dwi5

## API URL

`https://data.cityofnewyork.us/resource/wvxf-dwi5.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 11:12.
- Metadata saved: `raw/od-hpd-violations-metadata.json`.
- Data dictionary: `raw/od-hpd-violations-dict-hpd-code-violations-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `violationid` | number | Unique identifier of Violation |
| `buildingid` | number | Unique identifier of building |
| `registrationid` | number | Unique identifier of valid registration information |
| `bbl` | text | The Borough, Block, Lot (BBL) associated with the provided entity location. It is formatted as a ten-digit numerical identifier, which is unique to each parcel of real property in NYC. |
| `bin` | text | The Building Identification Number (BIN) associated with the provided entity location. It is formatted as a seven-digit numerical identifier, which is unique to each building in NYC. |
| `boroid` | number | unique number to identify borough |
| `block` | number | Tax block for building |
| `lot` | number | Tax lot for building |
| `apartment` | text | Apartment with violation, if applicable |
| `story` | text | Floor of violation |
| `class` | text | Indicator of seriousness of the violations, where A is the least serious and C is the most serious |
| `inspectiondate` | calendar_date | Date when the violation was observed |
| `approveddate` | calendar_date | Date when violation was approved |
| `originalcorrectbydate` | calendar_date | Original date by when the owner was to correct the violation |
| `originalcertifybydate` | calendar_date | Original date by when the owner was to inform HPD that the violation as corrected |
| `newcorrectbydate` | calendar_date | Modified date by when the owner was to correct the violation |
| `certifieddate` | calendar_date | Date when the violation was certified (if it was) |
| `ordernumber` | text | Reference to the abstract description of the violation condition which cites a specific section of the law which is in violation |
| `novid` | number | Unique identifier of the Notice of Violation sent to the owner |
| `novdescription` | text | Description of the violation |
| `novissueddate` | calendar_date | Date when the NOV was sent |
| `currentstatus` | text | Violation status (see below for details) |
| `currentstatusdate` | calendar_date | Date when the current status when into effect |
| `violationstatus` | text | Status of Violation(Open / Close) |
| `rentimpairing` | text | A rent-impairing violation is a condition within a multiple dwelling which constitutes, or if not promptly corrected will constitute, a fire hazard or a serious threat to the life, health or safety of occupants thereof (New York State Multiple Dwelling Law Section 302). |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/wvxf-dwi5.json?%24where=bbl%3D%272023700005%27&%24limit=50000&%24order=inspectiondate+DESC"
```

Decoded: `$where=bbl='2023700005'&$limit=50000&$order=inspectiondate DESC`

Result on 2026-11-21T00:57: HTTP 200, 481 rows, 11.364 s.

## Example response row

```json
{
 "violationid": "18807365",
 "buildingid": "119624",
 "registrationid": "210568",
 "boroid": "2",
 "boro": "BRONX",
 "housenumber": "1048",
 "lowhousenumber": "1048",
 "highhousenumber": "1048",
 "streetname": "WASHINGTON AVENUE",
 "streetcode": "73120",
 "zip": "10456",
 "story": "2",
 "block": "2370",
 "lot": "5",
 "class": "I",
 "inspectiondate": "2026-04-17T00:00:00.000",
 "approveddate": "2026-04-20T00:00:00.000",
 "ordernumber": "765",
 "novdescription": "§ 27-2142 ADM CODE APTS HAVE BEEN VACATED BY THIS DEPARTMENT AND CANNOT BE REOCCUPIED UNTIL SO ORDERED AFTER PROOF OF COMPLIANCE FOR APTS #2 UNDER VACATE ORDER #260643 IN THE ENTIRE APARTMENT LOCATED AT APT, 2nd STORY, 1st APARTMENT FROM EAST AT SOUTH",
 "currentstatusid": "22",
 "currentstatus": "FIRST NO ACCESS TO RE- INSPECT VIOLATION",
 "currentstatusdate": "2026-06-22T00:00:00.000",
 "violationstatus": "Open",
 "rentimpairing": "N",
 "latitude": "40.827336",
 "longitude": "-73.909084",
 "communityboard": "3",
 "councildistrict": "16",
 "censustract": "18501",
 "bin": "2001261",
 "bbl": "2023700005",
 "nta": "Morrisania"
}
```

## Caveats

- No code-section column: the cited section is the start of `novdescription`. See `text/od-hpd-violation-types.csv` and the data dictionary's Order Number sheet (`raw/od-hpd-violations-dict-hpd-code-violations-data-dictionary.xlsx`).
- Class is not fixed per order number. 143 of 400 orders appear under more than one class; see the violation types CSV.
- Order 550 (mould) has 77,332 rows whose description says the violation "HAS BEEN UPGRADED TO CLASS B/C", so for upgraded rows `class` reflects the upgrade, not the original finding.
- "The base data for this file is all violations open as of October 1, 2012" (dataset description), so older closed violations are missing.
- `bbl` is text (quote it); `violationstatus` is `Open` or `Close`.
- Single-building queries took 0.5 to 12 s on 2026-11-21 (slower while heavy aggregates were running on the same token).
- NYCHA buildings are in a separate dataset, `od-hpd-violations-nycha.md` (im9z-53hg).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
