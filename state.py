"""state.py — Persistent JSON state for stock data and alert history."""

import json, os
from datetime import datetime
from config import HISTORY_LIMIT

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "stock.json")

def _now(): return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load() -> dict:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"products": {}, "alerts": [], "last_updated": None}

def save(state: dict):
    state["last_updated"] = _now()
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(state, f, indent=2)

def update_product(state: dict, product: dict, result: dict) -> bool:
    pid  = product["id"]
    now  = _now()

    if pid not in state["products"]:
        state["products"][pid] = {
            "id": pid, "name": product["name"],
            "retailer": product["retailer"], "url": product["url"],
            "image": product.get("image", ""),
            "online_status": "unknown", "online_message": "",
            "last_checked": None, "last_changed": None,
            "instore_locations": [], "history": [],
        }

    entry       = state["products"][pid]
    prev_status = entry["online_status"]
    new_status  = result["online_status"]
    restocked   = (prev_status != "in_stock") and (new_status == "in_stock")

    if new_status != prev_status:
        entry["history"].insert(0, {
            "timestamp": now,
            "from_status": prev_status,
            "to_status": new_status,
            "message": result.get("online_message", ""),
        })
        entry["history"] = entry["history"][:HISTORY_LIMIT]
        entry["last_changed"] = now

        # Global alerts feed (for the live ticker)
        if new_status == "in_stock":
            from config import RETAILER_CONFIGS
            rl = RETAILER_CONFIGS.get(product["retailer"], {}).get("label", product["retailer"])
            state.setdefault("alerts", []).insert(0, {
                "timestamp": now,
                "product": product["name"],
                "retailer": rl,
                "retailer_key": product["retailer"],
                "url": product["url"],
            })
            state["alerts"] = state["alerts"][:50]

    entry.update({
        "online_status": new_status,
        "online_message": result.get("online_message", ""),
        "last_checked": now,
        "instore_locations": result.get("instore_locations", []),
    })
    if result.get("error"):
        entry["last_error"] = result["error"]
    else:
        entry.pop("last_error", None)

    return restocked
