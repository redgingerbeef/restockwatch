"""
watch.py — Stock watcher loop.
Can run standalone (python watch.py) or as a thread from server.py.
"""

import sys
import time
from datetime import datetime
from checker import check_online
from notifier import notify
from state import load, save, update_product
from config import WATCHLIST, CHECK_INTERVAL, RETAILER_CONFIGS


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def run(once=False):
    active = [p for p in WATCHLIST if p.get("active", True)]
    if not active:
        print("No active products. Edit config.py.")
        return

    print(f"\n{'='*52}")
    print(f"  RestockWatch  |  {len(active)} products  |  {CHECK_INTERVAL}s interval")
    print(f"{'='*52}\n", flush=True)

    while True:
        state = load()
        for product in active:
            rl = RETAILER_CONFIGS.get(product["retailer"], {}).get("label", product["retailer"])
            log(f"[{rl}] {product['name'][:45]}...")
            try:
                result    = check_online(product)
                restocked = update_product(state, product, result)
                icon = {
                    "in_stock":     "🟢",
                    "out_of_stock": "🔴",
                    "error":        "⚠️ ",
                    "unknown":      "❓",
                }.get(result["online_status"], "❓")
                log(f"  {icon} {result['online_message'] or result.get('error', '')}")
                locs = result.get("instore_locations", [])
                if locs:
                    avail = sum(1 for s in locs if s["status"] == "in_stock")
                    log(f"  🏪 {avail}/{len(locs)} stores in stock")
                if restocked:
                    notify(
                        product["name"],
                        product["url"],
                        rl,
                        sum(1 for s in locs if s["status"] == "in_stock"),
                    )
            except Exception as e:
                log(f"  ⚠️  Error checking {product['name']}: {e}")

        save(state)
        log("Saved.\n")

        if once:
            break

        log(f"Next check in {CHECK_INTERVAL}s\n")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--test" in args:
        from notifier import notify
        notify("TEST — Prismatic Evolutions ETB", "https://pokemoncenter.com/en-ca", "Pokémon Center", 2)
    elif "--once" in args:
        run(once=True)
    else:
        try:
            run()
        except KeyboardInterrupt:
            print("\nStopped.")
