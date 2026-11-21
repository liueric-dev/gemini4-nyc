"""The outdoor temperature right now, which the heat rules turn on (heat is owed by day only when it is
below 55 °F outside).

    outside_temp_f() -> 63.9, or None if the reading can't be had

Source: the National Weather Service's Central Park station (KNYC), which is the city's reference station.
Free, no key. A reading is kept for ten minutes. A failure returns None and is never an error: the rule
then stays undecided, as it was before this lookup existed.
"""
import threading
import time

import httpx

URL = "https://api.weather.gov/stations/KNYC/observations"
KEEP_SECONDS = 600
_lock = threading.Lock()
_last: tuple[float, float | None] | None = None  # (when fetched, °F)


def _fetch() -> float | None:
    r = httpx.get(URL, params={"limit": 6}, timeout=8,
                  headers={"User-Agent": "tenant-advocate", "Accept": "application/geo+json"})
    r.raise_for_status()
    for obs in r.json().get("features") or []:  # newest first; a reading is sometimes blank
        c = ((obs.get("properties") or {}).get("temperature") or {}).get("value")
        if c is not None:
            return round(c * 9 / 5 + 32, 1)
    return None


def outside_temp_f() -> float | None:
    global _last
    with _lock:  # a video asks once per frame, all at the same moment; one request serves them all
        if _last and time.time() - _last[0] < KEEP_SECONDS:
            return _last[1]
        try:
            value = _fetch()
        except Exception:  # noqa: BLE001 - weather is a convenience; the answer must not fail over it
            value = None
        _last = (time.time(), value)
        return value
