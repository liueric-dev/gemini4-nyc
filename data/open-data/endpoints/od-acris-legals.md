# ACRIS - Real Property Legals

## Dataset name

ACRIS - Real Property Legals (Department of Finance (DOF)).

Property Details for Real Property Related Documents Recorded in ACRIS

## Dataset ID

`8h5j-fqxa`. Portal page: https://data.cityofnewyork.us/d/8h5j-fqxa

## API URL

`https://data.cityofnewyork.us/resource/8h5j-fqxa.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-10 12:34.
- Metadata saved: `raw/od-acris-legals-metadata.json`.
- Data dictionary: `raw/od-acris-legals-dict-acris-public-opendata-guide.doc`, `raw/od-acris-legals-dict-acris-real-property-legals-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `document_id` | text | Document Identifier |
| `record_type` | text | L for Legals Record |
| `borough` | number | Borough Code: 1 = Manhattan 2 = Bronx 3 = Brooklyn 4 = Queens |
| `block` | number | Block number of instrument |
| `lot` | number | Lot number of instrument |
| `property_type` | text | Code defined in property table |
| `street_number` | text | Street Number for BBL |
| `street_name` | text | Street Name for BBL |
| `unit` | text | Unit Number for BBL |
| `good_through_date` | calendar_date | Date of latest recording or correction included with this extract |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/8h5j-fqxa.json?%24where=borough%3D2+AND+block%3D2370+AND+lot%3D5&%24limit=50000"
```

Decoded: `$where=borough=2 AND block=2370 AND lot=5&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 47 rows, 10.236 s.

## Example response row

```json
{
 "document_id": "2019061700608002",
 "record_type": "L",
 "borough": "2",
 "block": "2370",
 "lot": "5",
 "easement": "N",
 "partial_lot": "E",
 "air_rights": "N",
 "subterranean_rights": "N",
 "property_type": "D3",
 "street_number": "1048",
 "street_name": "WASHINGTON AVENUE",
 "good_through_date": "2019-06-30T00:00:00.000"
}
```

## Caveats

- ACRIS is three linked datasets: Legals (which lot a document is on) -> `document_id` -> Master (`doc_type`, dates, amount; bnx9-e6tj) and Parties (names; 636b-3b5g). Code lists are in separate ACRIS code datasets (e.g. Property Types Codes 94g4-w6xz).
- Updated monthly (metadata). See the ACRIS guides saved in `raw/` (`od-acris-*-dict-*.doc`).
- Parties contain names of individual buyers, sellers and lenders, so they were not saved for the demo buildings.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
