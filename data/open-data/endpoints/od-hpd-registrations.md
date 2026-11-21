# Multiple Dwelling Registrations

## Dataset name

Multiple Dwelling Registrations (Department of Housing Preservation and Development (HPD)).

Pursuant to New York City’s Housing Maintenance Code, the Department of Housing Preservation and Development (HPD) collects registration information from owners of residential rental units. Owners are required to register if they own residential buildings with three or more units or if they own one- or two-family homes and neither they nor members of their immediate family live there. Registrations are required upon taking ownership of a qualifying building, and once a year thereafter.

## Dataset ID

`tesw-yqqr`. Portal page: https://data.cityofnewyork.us/d/tesw-yqqr

## API URL

`https://data.cityofnewyork.us/resource/tesw-yqqr.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-04 12:16.
- Metadata saved: `raw/od-hpd-registrations-metadata.json`.
- Data dictionary: `raw/od-hpd-registrations-dict-hpd-registration-open-data.pdf` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `registrationid` | number | Unique identifier of Registration |
| `buildingid` | number | Unique identifier of building being registered |
| `boroid` | number | Unique identifier of a borough |
| `block` | number | Tax block for building |
| `lot` | number | Tax lot for building |
| `bin` | number | DCP Building Identification Number for building |
| `housenumber` | text | Address information for the building |
| `streetname` | text | Address information for the building |
| `lastregistrationdate` | calendar_date | Date on which the registration information was processed |
| `registrationenddate` | calendar_date | Expiration date of registration record |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/tesw-yqqr.json?%24where=boroid%3D2+AND+block%3D2370+AND+lot%3D5&%24limit=50000"
```

Decoded: `$where=boroid=2 AND block=2370 AND lot=5&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 1 rows, 0.578 s.

## Example response row

```json
{
 "registrationid": "210568",
 "buildingid": "119624",
 "boroid": "2",
 "boro": "BRONX",
 "housenumber": "1048",
 "lowhousenumber": "1048",
 "highhousenumber": "1048",
 "streetname": "WASHINGTON AVENUE",
 "streetcode": "73120",
 "zip": "10456",
 "block": "2370",
 "lot": "5",
 "bin": "2001261",
 "communityboard": "3",
 "lastregistrationdate": "2026-09-20T00:00:00.000",
 "registrationenddate": "2027-09-01T00:00:00.000"
}
```

## Caveats

- Registration is required for buildings with 3 or more units, and for 1-2 family homes where neither the owner nor immediate family lives there (dataset description). A missing registration for a qualifying building is itself a violation type (order numbers in the ANNUAL PROPERTY REGISTRATION category of the violation types CSV).
- Join to Registration Contacts on `registrationid` to get the owner, head officer and managing agent.
- Updated monthly (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
