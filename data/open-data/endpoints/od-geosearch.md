# NYC GeoSearch (address to BBL and BIN)

## Dataset name

NYC GeoSearch API v2 (NYC Department of City Planning, Planning Labs). Pelias geocoder over the NYC Property Address Directory (PAD).

## Dataset ID

No dataset ID. The PAD version is returned per result in `properties.addendum.pad.version` (`26c` on 2026-11-21).

## API URL

- Search (full address): `https://geosearch.planninglabs.nyc/v2/search?text=<address>[&size=N]`
- Autocomplete (as the user types): `https://geosearch.planninglabs.nyc/v2/autocomplete?text=<partial>[&focus.point.lat=..&focus.point.lon=..]`
- Docs: https://geosearch.planninglabs.nyc/docs/ (`local/od-geosearch-docs.html`, `local/od-geosearch-docs.md`); about: `local/od-geosearch-home.md`

No key.

## Key fields

GeoJSON `FeatureCollection`. In each `features[].properties`:
- `addendum.pad.bbl`: 10-digit borough-block-lot, the join key for PLUTO, HPD, DOB and ACRIS
- `addendum.pad.bin`: Building Identification Number (DOB datasets, HPD `bin`)
- `label`, `name`, `housenumber`, `street`, `postalcode`, `borough`, `neighbourhood`
- `confidence` (search only), `match_type`, `accuracy`, `layer` (`venue`, `address`, ...)
- `geometry.coordinates`: [lon, lat]

## Example query

```
curl -G "https://geosearch.planninglabs.nyc/v2/search" --data-urlencode "text=100 Gold Street, Manhattan"
```

Saved: `raw/od-geosearch-example-search.json`, `raw/od-geosearch-example-autocomplete.json`.

## Example response row

```json
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-74.00324, 40.710156]}, "properties": {"name": "100 GOLD STREET", "housenumber": "100", "street": "GOLD STREET", "postalcode": "10038", "confidence": 0.8, "match_type": "fallback", "accuracy": "point", "borough": "Manhattan", "neighbourhood": "Financial District", "label": "100 GOLD STREET, New York, NY, USA", "addendum": {"pad": {"bbl": "1000940025", "bin": "1001289", "version": "26c"}}}}
```

## Caveats

- Returns 10 results by default; take `features[0]` only after checking `confidence` and `borough`, and use `size=1` for speed.
- The docs say to throttle autocomplete, and responses may arrive out of order.
- No rate limit or terms of use found on the docs or about pages; the `/attribution` link in the response's `geocoding.attribution` returned 404 (and timed out once).
- A building on a large lot (e.g. NYCHA campuses) shares one BBL across many BINs; use BIN for building-level DOB and HPD lookups.
- Response time 0.07 to 0.18 s (search), 0.07 s (autocomplete).
