"""Fix-it-yourself kits: the product pick rule and the endpoint. No network calls."""
from fastapi.testclient import TestClient

from app import pipeline, shop
from app.main import app


def product(title, price, rating=None, count=0, available=True):
    return {"title": title, "image": "https://cdn.example/x.jpg", "price": price, "currency": "USD",
            "seller": "Store", "rating": rating, "rating_count": count, "url": "https://store.example/p",
            "checkout_url": "https://store.example/buy", "available": available}


def test_kits_cover_exactly_the_tenant_duty_rules():
    assert set(shop.KITS) == pipeline.TENANT_DUTY_RULES
    for kit in shop.KITS.values():
        assert kit["items"] and kit["steps"]
        assert all(i["kind"] in ("tool", "material") and i["query"] for i in kit["items"])


def test_pick_skips_the_expensive_top_hit():
    # The order and prices Shop returned for a mould spray on Nov 21.
    found = [product("Imported spray", 30.79, 4.7, 3), product("Blast spray", 2.49, 4.6, 10),
             product("Unrated cleaner", 29.99), product("Other spray", 5.24),
             product("Foam", 17.55, 3.5, 4), product("Foam 2", 12.99)]
    assert shop.pick(found)["title"] == "Blast spray"


def test_pick_prefers_more_reviews_and_drops_out_of_stock():
    found = [product("Few reviews", 7.69, 4.8, 22), product("Many reviews", 7.99, 4.1, 898),
             product("Gone", 6.00, 5.0, 5000, available=False), product("Pricey", 42.50, 4.8, 181)]
    best = shop.pick(found)
    assert best["title"] == "Many reviews"
    assert "available" not in best


def test_pick_falls_back_to_unrated_and_handles_nothing():
    assert shop.pick([product("Only one", 9.99)])["title"] == "Only one"
    assert shop.pick([]) is None
    assert shop.pick([product("Gone", 5.00, available=False)]) is None


def test_endpoint_returns_items_and_steps(monkeypatch):
    def fake_search(query, limit=6):
        if "brush" in query:
            raise RuntimeError("network down")
        return [product(f"Result for {query}", 4.00, 4.5, 12)]

    monkeypatch.setattr(shop, "search", fake_search)
    r = TestClient(app).get("/api/diy/EO-015")
    assert r.status_code == 200
    body = r.json()
    assert [i["name"] for i in body["items"]] == ["Mould and mildew remover", "Grout scrub brush",
                                                  "Mould-resistant caulk"]
    assert body["items"][0]["product"]["checkout_url"] == "https://store.example/buy"
    assert body["items"][1]["product"] is None  # a failed search keeps the item
    assert len(body["steps"]) == 4


def test_endpoint_refuses_a_landlord_rule():
    assert TestClient(app).get("/api/diy/EO-008").status_code == 404
