"""checker.py — Playwright-based stock checker with in-store support."""

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
from config import RETAILER_CONFIGS
import re

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
]
_ua_idx = 0

def _ua():
    global _ua_idx
    u = USER_AGENTS[_ua_idx % len(USER_AGENTS)]
    _ua_idx += 1
    return u

def check_online(product: dict) -> dict:
    rk  = product["retailer"]
    url = product["url"]
    cfg = RETAILER_CONFIGS.get(rk, {})

    result = {
        "online_status": "unknown",
        "online_message": "",
        "instore_locations": [],
        "error": None,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent=_ua(),
            viewport={"width": 1280, "height": 900},
            locale="en-CA",
            timezone_id="America/Edmonton",
        )
        page = ctx.new_page()
        page.route("**/*.{png,jpg,jpeg,gif,webp,svg,woff,woff2,ttf,mp4}", lambda r: r.abort())

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=25000)
            page.wait_for_timeout(2500)
            text = page.inner_text("body").lower()

            oos   = next((t for t in cfg.get("oos_text", [])      if t.lower() in text), None)
            instk = next((t for t in cfg.get("in_stock_text", []) if t.lower() in text), None)
            btn   = page.query_selector(cfg.get("add_to_cart_selector", ""))
            btn_disabled = (btn is None) or (btn.get_attribute("disabled") is not None)

            if instk and not btn_disabled:
                result["online_status"]  = "in_stock"
                result["online_message"] = "Add to cart active"
            elif oos or btn_disabled:
                result["online_status"]  = "out_of_stock"
                result["online_message"] = "Out of stock"
            else:
                result["online_status"]  = "unknown"
                result["online_message"] = "Status unclear"

            if product.get("track_instore"):
                if rk == "walmart_ca":
                    result["instore_locations"] = _walmart_instore(page, text)
                elif rk == "ebgames_ca":
                    result["instore_locations"] = _ebgames_instore(page, text)

        except PWTimeout:
            result["online_status"] = "error"
            result["error"] = "Page timed out"
        except Exception as e:
            result["online_status"] = "error"
            result["error"] = str(e)
        finally:
            browser.close()

    return result


def _walmart_instore(page, text: str) -> list:
    locs = []
    try:
        items = page.query_selector_all("[data-automation='store-availability-item'], .store-list-item")
        for item in items[:12]:
            lines = [l.strip() for l in item.inner_text().split("\n") if l.strip()]
            if lines:
                sl = " ".join(lines[1:]).lower()
                locs.append({
                    "store": lines[0],
                    "status": "in_stock" if ("in stock" in sl or "available" in sl) else
                              "limited"  if "limited" in sl else "out_of_stock",
                    "raw": " | ".join(lines),
                })
        if not locs:
            for store, status in re.findall(
                r'(walmart[\w\s]+?)\s+(in stock|limited stock|out of stock)',
                text, re.I)[:8]:
                locs.append({
                    "store": store.strip().title(),
                    "status": "in_stock" if "in stock" in status.lower() else "out_of_stock",
                    "raw": f"{store} — {status}",
                })
    except Exception:
        pass
    return locs


def _ebgames_instore(page, text: str) -> list:
    locs = []
    try:
        items = page.query_selector_all(".store-availability-row, .pickup-store-item, [class*='store-item']")
        for item in items[:12]:
            lines = [l.strip() for l in item.inner_text().split("\n") if l.strip()]
            if lines:
                sl = " ".join(lines[1:]).lower()
                locs.append({
                    "store": lines[0],
                    "status": "in_stock" if ("available" in sl or "in stock" in sl) else
                              "limited"  if "limited" in sl else "out_of_stock",
                    "raw": " | ".join(lines),
                })
    except Exception:
        pass
    return locs
