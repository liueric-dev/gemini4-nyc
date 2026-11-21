# NYCHA Residential Addresses

## Dataset name

NYCHA Residential Addresses (NYC Housing Authority (NYCHA)).

List of NYCHA residential addresses.

## Dataset ID

`3ub5-4ph8`. Portal page: https://data.cityofnewyork.us/d/3ub5-4ph8

## API URL

`https://data.cityofnewyork.us/resource/3ub5-4ph8.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): As needed; automated: No; rows last updated 2026-05-19 14:58.
- Metadata saved: `raw/od-nycha-residential-addresses-metadata.json`.
- Data dictionary: `raw/od-nycha-residential-addresses-dict-nycha-residential-addresses-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `development` | text | Development name |
| `tds` | number | Tenant Data System number |
| `building` | text | NYCHA building number |
| `stairhall_` | text | NYCHA stairhall number |
| `address` | text | Address |
| `zip_code` | number | Zip Code |
| `bin` | number | Building Identification Center |
| `block` | number | Tax Block |
| `lot` | number | Tax Lot |
| `borough_block_lot` | number | Combination of borough code, tax block, and tax lot |
| `privately_managed` | text | A "Yes" indicates developments managed by a private management company. |

## Example query

Demo building `466-columbia-st-bk` (BBL 3005330001, BIN 3326977):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/3ub5-4ph8.json?%24where=bin%3D3326977&%24limit=50000"
```

Decoded: `$where=bin=3326977&$limit=50000`

Result on 2026-11-21T01:05: HTTP 200, 3 rows, 8.786 s.

## Example response row

```json
{
 "development": "RED HOOK WEST",
 "tds": "79",
 "building": "22",
 "stairhall_": "074",
 "borough": "BROOKLYN",
 "house": "472",
 "street": "COLUMBIA STREET",
 "address": "472 COLUMBIA STREET",
 "city": "BROOKLYN",
 "state": "NY",
 "zip_code": "11231",
 "bin": "3326977",
 "block": "533",
 "lot": "1",
 "borough_block_lot": "3005330001",
 "census_tract_2010": "85",
 "neighborhood_tabulation_area": "BK0601",
 "neighborhood_tabulation_area_1": "Carroll Gardens-Cobble Hill-Gowanus-Red Hook",
 "community_district": "6",
 "city_council_district": "38",
 "state_assembly_district": "51",
 "state_senate_district": "26",
 "us_congressional_district": "10",
 "latitude": "40.675834",
 "longitude": "-74.00775"
}
```

## Caveats

- 2,955 rows (one per stairhall address); the full list is saved as `raw/od-nycha-residential-addresses-full.csv`. Use it to tell whether an address is NYCHA.
- `privately_managed = Yes` flags privately managed (e.g. PACT/RAD) developments, per the column description.
- Updated "as needed"; last updated 2026-05-19 (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
