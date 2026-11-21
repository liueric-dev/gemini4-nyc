# NYCHA development lists: Development Data Book and Public Housing Developments

## Dataset name

- NYCHA Development Data Book (`evjd-dqpz`): one row per development with IDs, programme, apartments, population, buildings, stories, street boundaries, districts, completion date and RAD/PACT transfer date (dataset description).
- NYCHA Public Housing Developments (`phvi-damg`): development polygons with name, TDS number, borough, programme.
- For addresses, BINs and BBLs use NYCHA Residential Addresses (`3ub5-4ph8`, `od-nycha-residential-addresses.md`).

## Dataset ID

`evjd-dqpz`, `phvi-damg`

## API URL

- `https://data.cityofnewyork.us/resource/evjd-dqpz.json` (update frequency: Annually; automation: No; rows last updated 2025-08-18)
- `https://data.cityofnewyork.us/resource/phvi-damg.json` (update frequency: As needed; rows last updated 2026-10-05). Full download saved: `raw/od-nycha-developments-full.csv` (216 developments).
- Metadata and dictionaries: `raw/od-nycha-development-data-book-metadata.json`, `raw/od-nycha-development-data-book-dict-*.xlsx`, `raw/od-nycha-developments-metadata.json`, `raw/od-nycha-developments-dict-*.xlsx`

## Key fields

Data Book: `development`, `tds_` (development number; zero-padded text, e.g. `079`), `hud_amp_`, `program` (FEDERAL, MIXED FINANCE, ...), `type`, `number_of_current_apartments`, `total_population`, `number_of_residential_bldgs`, `number_of_stories`, `location_street_a`..`d` (boundary streets), `borough`, `completion_date`, `private_management`, `rad_transferred_date`, `data_as_of`.

Developments: `developmen` (name), `tds_num`, `borough`, `program`, `the_geom` (multipolygon).

## Example query

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/evjd-dqpz.json?\$where=development='RED%20HOOK%20WEST'"
```

(10.5 s on 2026-11-21, 1 row.)

## Example response row

```json
{"data_as_of":"1/1/2025","development":"RED HOOK WEST","hud_amp_":"NY005000790","tds_":"079","program":"FEDERAL","method":"CONVENTIONAL","type":"NEW CONST","number_of_current_apartments":"1,471","total_number_of_apartments":"1,480","total_population":"2,698","number_of_residential_bldgs":"14","number_of_stairhalls":"49","number_of_stories":"3–6–14","avg_monthly_gross_rent":"$604","location_street_a":"RICHARDS ST","location_street_b":"LORRAINE ST","location_street_c":"HICKS ST","location_street_d":"WEST 9TH ST","borough":"BROOKLYN","completion_date":"1955-05-31T00:00:00.000"}
```

## Caveats

- The Data Book has no BBL, BIN or street address, and its numbers are text with thousands separators (`"1,471"`).
- `data_as_of` was `1/1/2025` in the row fetched; the dataset is annual and was last updated 2025-08-18.
- TDS numbers are zero-padded text in the Data Book (`079`) but numbers elsewhere (`tds` = 79 in 3ub5-4ph8, `tds_no` = 79 in im9z-53hg).
- PACT/RAD developments may now be privately managed. Check `rad_transferred_date` and `private_management` before routing a tenant to NYCHA's repair process.
- License and rate limits: as for all NYC Open Data datasets (see `od-hpd-violations.md`, Caveats).
