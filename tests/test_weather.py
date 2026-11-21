from app import weather


class Reply:
    def __init__(self, features):
        self._features = features

    def raise_for_status(self):
        pass

    def json(self):
        return {"features": self._features}


def obs(celsius):
    return {"properties": {"temperature": {"value": celsius}}}


def test_newest_reading_that_has_a_value_is_used_and_kept(monkeypatch):
    calls = []
    monkeypatch.setattr(weather, "_last", None)
    monkeypatch.setattr(weather.httpx, "get", lambda *a, **k: calls.append(1) or Reply([obs(None), obs(10.0), obs(30.0)]))
    assert weather.outside_temp_f() == 50.0
    assert weather.outside_temp_f() == 50.0 and len(calls) == 1  # the second ask is served from the kept reading


def test_no_reading_is_none_and_never_an_error(monkeypatch):
    def down(*a, **k):
        raise OSError("network")

    monkeypatch.setattr(weather, "_last", None)
    monkeypatch.setattr(weather.httpx, "get", down)
    assert weather.outside_temp_f() is None
