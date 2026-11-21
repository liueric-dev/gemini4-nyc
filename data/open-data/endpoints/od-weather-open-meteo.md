# Open-Meteo Historical Weather API (archive)

## Dataset name

Open-Meteo Historical Weather API (reanalysis: ERA5, ERA5-Land, ECMWF IFS, combined as "Best match" by default).

## Dataset ID

Not station data. A grid point chosen from the `latitude`/`longitude` you pass.

## API URL

- `https://archive-api.open-meteo.com/v1/archive`
- Docs: https://open-meteo.com/en/docs/historical-weather-api (`local/od-open-meteo-historical-docs.html`, `local/od-open-meteo-historical-docs.md`)
- Terms: https://open-meteo.com/en/terms (`local/od-open-meteo-terms.md`); licence: https://open-meteo.com/en/licence (`local/od-open-meteo-licence.md`)

No key for the free tier.

## Key fields

- Parameters: `latitude`, `longitude`, `start_date`, `end_date` (YYYY-MM-DD), `hourly=temperature_2m`, `temperature_unit=fahrenheit`, `timezone=America/New_York`
- Response: `hourly.time` (local times when `timezone` is set), `hourly.temperature_2m`, `hourly_units`, plus the snapped grid `latitude`, `longitude`, `elevation`, `utc_offset_seconds`

## Example query

```
curl "https://archive-api.open-meteo.com/v1/archive?latitude=40.78333&longitude=-73.96667&hourly=temperature_2m&temperature_unit=fahrenheit&timezone=America%2FNew_York&start_date=2026-01-15&end_date=2026-01-15"
```

Saved: `raw/od-open-meteo-archive-2026-01-15.json`, `raw/od-open-meteo-archive-2026-11-10-to-21.json`, `raw/od-open-meteo-archive-1940-01-01.json`.

## Example response row

```json
{"latitude": 40.808434, "longitude": -74.0199, "utc_offset_seconds": -18000, "timezone": "America/New_York", "elevation": 45.0, "hourly_units": {"time": "iso8601", "temperature_2m": "°F"}, "hourly": {"time": ["2026-01-15T00:00", "..."], "temperature_2m": [43.5, "..."]}}
```

## How far back and how recent

- Back to 1940 (1940-01-01 returned values; docs: "past weather data dating back to 1940").
- Recent: the 2026-11-10 to 2026-11-21 query, sent at 00:50 on 2026-11-21, returned no nulls through 2026-11-21T23:00, which is in the future. The newest values are therefore model output (the docs say "Best match" blends IFS HRES with ERA5), not observations.

## License and terms

- Data: CC BY 4.0 (licence page). Credit Open-Meteo with a link to the licence.
- Free API is **non-commercial only**: "Less than 10'000 API calls per day, 5'000 per hour and 600 per minute", applied by IP and application.

## Caveats

- **Grid snapping:** for the KNYC coordinates the API returned the cell at 40.808, -74.020, about 4 km west, across the Hudson. It is modelled, not measured at Central Park.
- The most recent days are modelled or forecast values. Prefer NWS KNYC for the last week and NCEI GHCNh for older dates when a measured value matters.
- Commercial use requires a paid plan.
