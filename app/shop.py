"""Fix-it-yourself kits: what to buy, from Shopify stores, when a problem is the tenant's own job.

Each kit (app/diy_kits.json) lists the items and the steps for one tenant-duty rule. Every item gets one
product from Shopify's catalog (Shop MCP, shop.dev), chosen by rule, so the tenant sees one answer per item
and not a list to compare. Search needs no key.
"""
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from statistics import median

import httpx

SHOP_MCP = "https://mcp.shop.com/"
MCP_VERSION = "2026-07-28"
KITS: dict = json.loads((Path(__file__).parent / "diy_kits.json").read_text())


def _product(p: dict) -> dict:
    """One search result, cut down to what a card shows. Merchant text is untrusted; nothing here is run."""
    v = p["variants"][0]
    media = v.get("media") or p.get("media") or [{}]
    rating = p.get("rating") or {}
    return {
        "title": p.get("title", ""),
        "image": media[0].get("url"),
        "price": v["price"]["amount"] / 100,  # amounts arrive in minor units
        "currency": v["price"]["currency"],
        "seller": (v.get("seller") or {}).get("name", "").strip(),
        "rating": rating.get("value"),
        "rating_count": rating.get("count") or 0,
        "url": v.get("url"),
        "checkout_url": v.get("checkout_url"),
        "available": bool((v.get("availability") or {}).get("available")),
    }


def search(query: str, limit: int = 6) -> list[dict]:
    """Products matching a query, for a shopper in the US paying in dollars."""
    r = httpx.post(
        SHOP_MCP,
        timeout=10,
        headers={"Accept": "application/json, text/event-stream", "MCP-Protocol-Version": MCP_VERSION,
                 "Mcp-Method": "tools/call", "Mcp-Name": "search_catalog"},
        json={"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {
            "name": "search_catalog",
            "arguments": {"catalog": {"query": query, "context": {"address_country": "US", "currency": "USD"},
                                      "pagination": {"limit": limit}}},
            "_meta": {"io.modelcontextprotocol/protocolVersion": MCP_VERSION,
                      "io.modelcontextprotocol/clientCapabilities": {},
                      "io.modelcontextprotocol/clientInfo": {"name": "tenant-advocate", "version": "0.1"}},
        }},
    )
    r.raise_for_status()
    result = r.json().get("result") or {}
    if result.get("isError") or "structuredContent" not in result:
        raise RuntimeError("Shop search returned an error")
    return [_product(p) for p in result["structuredContent"].get("products", []) if p.get("variants")]


def pick(candidates: list[dict]) -> dict | None:
    """The one product to show for an item.

    The top search hit is not a safe choice: on Nov 21 a $30.79 imported mould spray ranked above a $2.49 one.
    So: in stock, not above the median price of what came back, rated 4 or more where any are, then the most
    reviews (the cheaper one on a tie).
    """
    stock = [c for c in candidates if c["available"]]
    if not stock:
        return None
    cap = median(c["price"] for c in stock)
    pool = [c for c in stock if c["price"] <= cap]
    rated = [c for c in pool if (c["rating"] or 0) >= 4]
    best = max(rated or pool, key=lambda c: (c["rating_count"], -c["price"]))
    return {k: v for k, v in best.items() if k != "available"}


def kit(rule_id: str) -> dict:
    """The items (each with one product, or None if the search failed) and the steps for a tenant-duty rule."""
    k = KITS[rule_id]

    def one(item: dict) -> dict:
        try:
            product = pick(search(item["query"]))
        except Exception:  # noqa: BLE001  a failed search must not lose the item or the steps
            product = None
        return {"name": item["name"], "kind": item["kind"], "product": product}

    with ThreadPoolExecutor(max_workers=len(k["items"])) as pool:
        items = list(pool.map(one, k["items"]))
    return {"title": k["title"], "items": items, "steps": k["steps"]}
