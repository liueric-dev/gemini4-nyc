# Housing Litigations

## Dataset name

Housing Litigations (Department of Housing Preservation and Development (HPD)).

The Department of Housing Preservation and Development (HPD) Housing Litigation Division (HLD) initiates' actions in the Housing Court against owners of privately-owned buildings to enforce compliance with the housing quality standards contained in the New York State Multiple Dwelling Law and the New York City Housing Maintenance Code. HLD attorneys also represent HPD when tenants initiate actions against private owners. HPD is automatically named as party to such actions. The goal of these court proceedings is to obtain enforceable Orders to Correct, Civil Penalties (fines) and Contempt Sanctions, compelling owners to comply with the Housing Code.

## Dataset ID

`59kj-x8nc`. Portal page: https://data.cityofnewyork.us/d/59kj-x8nc

## API URL

`https://data.cityofnewyork.us/resource/59kj-x8nc.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-01 16:14.
- Metadata saved: `raw/od-hpd-litigations-metadata.json`.
- Data dictionary: `raw/od-hpd-litigations-dict-housing-litigations-data-dictionary.pdf` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `litigationid` | number | Unique number identifying the case |
| `buildingid` | number | Unique identifier of building |
| `bbl` | text |  |
| `bin` | text |  |
| `casetype` | text | The purpose of the litigation |
| `caseopendate` | calendar_date | Date the case was opened |
| `casestatus` | text | The status of the case |
| `casejudgement` | text | The final judgment if any for this case |
| `findingofharassment` | text |  |
| `findingdate` | text |  |
| `penalty` | text |  |
| `respondent` | text |  |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/59kj-x8nc.json?%24where=bbl%3D%272023700005%27&%24limit=50000"
```

Decoded: `$where=bbl='2023700005'&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 11 rows, 0.433 s.

## Example response row

```json
{
 "litigationid": "444738",
 "buildingid": "119624",
 "boroid": "2",
 "housenumber": "1048",
 "streetname": "WASHINGTON AVENUE",
 "zip": "10456",
 "block": "2370",
 "lot": "5",
 "casetype": "Access Warrant - Non-Lead",
 "caseopendate": "2024-02-26T00:00:00.000",
 "casestatus": "CLOSED",
 "casejudgement": "NO",
 "respondent": "1048 WASHINGTON LLC,MARK SCHIK",
 "latitude": "40.8273360",
 "longitude": "-73.909083",
 "community_district": "3",
 "council_district": "16",
 "census_tract": "18501",
 "bin": "2001261",
 "bbl": "2023700005",
 "nta": "Morrisania"
}
```

## Caveats

- Cases HPD's Housing Litigation Division brings, or is named in when tenants start an HP action (dataset description). Useful for finding a prior HP action or a harassment finding.
- `respondent` can name individual owners.
- Updated monthly (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
