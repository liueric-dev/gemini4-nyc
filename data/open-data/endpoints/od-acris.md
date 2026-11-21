# ACRIS Real Property: Master, Parties (and Legals)

## Dataset name

ACRIS (Automated City Register Information System, NYC Department of Finance): Real Property Master ("Document Details"), Real Property Parties ("Party Names"), Real Property Legals ("Property Details"). Deeds, mortgages, satisfactions and other recorded documents.

## Dataset ID

- Legals: `8h5j-fqxa` (separate doc: `od-acris-legals.md`)
- Master: `bnx9-e6tj`
- Parties: `636b-3b5g`
- Code lists, e.g. Property Types Codes `94g4-w6xz`; document type codes are in the ACRIS guides (`raw/od-acris-*-dict-*.doc`, text in `text/`)

## API URL

- `https://data.cityofnewyork.us/resource/bnx9-e6tj.json`
- `https://data.cityofnewyork.us/resource/636b-3b5g.json`
- Update frequency (metadata): Monthly for all three.
- Metadata: `raw/od-acris-master-metadata.json`, `raw/od-acris-parties-metadata.json`. Data dictionaries: `raw/od-acris-master-dict-acris-real-property-master-data-dictionary.xlsx`, `raw/od-acris-parties-dict-acris-real-property-parties-data-dictionary.xlsx`.

## Key fields

Master: `document_id` (join key), `record_type`, `crfn`, `recorded_borough`, `doc_type` (e.g. DEED, MTGE, SAT, ASST, AGMT), `document_date`, `document_amt`, `recorded_datetime`, `modified_date`, `good_through_date`.

Parties: `document_id`, `party_type` (1 or 2; the guide defines which side each is for each document type), `name`, `address_1`, `address_2`, `city`, `state`, `zip`, `country`.

## Example query

Step 1, documents on a lot (Legals): `$where=borough='2' AND block=2514 AND lot=62` (122 West 167th Street; 50 rows at the limit, 11.9 s; `raw/od-acris-legals-example.json`).

Step 2, details:

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/bnx9-e6tj.json?\$select=document_id,doc_type,document_date,document_amt,recorded_datetime&\$where=document_id%20in('2021122301143001','2022100700704001')"
```

(50 documents in one `in (...)` query took 3.6 s; `raw/od-acris-master-example.json`.)

Step 3, parties: `https://data.cityofnewyork.us/resource/636b-3b5g.json?$where=document_id='2021122301143001'` (6.0 s, 2 rows).

## Example response row

Master:

```json
{"document_id": "2021122301143001", "record_type": "A", "crfn": "2022000002734", "recorded_borough": "1", "doc_type": "DEED", "document_date": "2021-12-21T00:00:00.000", "document_amt": "1575000.00", "recorded_datetime": "2022-01-04T00:00:00.000", "modified_date": "2022-01-04T00:00:00.000", "good_through_date": "2022-01-31T00:00:00.000"}
```

Parties (name and street redacted in this doc):

```json
{"document_id": "2021122301143001", "record_type": "P", "party_type": "1", "name": "[redacted]", "address_1": "[redacted]", "country": "US", "city": "HOLLIS", "state": "NY", "zip": "11423", "good_through_date": "2022-01-31T00:00:00.000"}
```

## Caveats

- Three-step lookup (Legals, then Master, then Parties). Each step took 3 to 12 s on 2026-11-21, so it's better suited to background enrichment than to a live call.
- `recorded_borough` on the master row for a Bronx-lot deed was `1`. A document can cover several lots, so filter on the Legals row, not on Master.
- Parties hold individual names and addresses of buyers, sellers and lenders. No parties data was saved.
- Monthly refresh: recent sales can be missing for weeks.
- License and rate limits: as for all NYC Open Data datasets (see `od-hpd-violations.md`, Caveats).
