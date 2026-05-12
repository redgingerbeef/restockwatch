"""
checker.py — Stock checker.
- requests: PCC, Walmart, Amazon
- curl_cffi with retry + backoff: EB Games (Cloudflare)
"""

import requests
import time
import random

try:
    from curl_cffi import requests as cf_requests
    CURL_AVAILABLE = True
except ImportError:
    CURL_AVAILABLE = False

from config import RETAILER_CONFIGS

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-CA,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Rotate Chrome versions to avoid fingerprint pattern detection
CF_IMPERSONATE_PROFILES = ["chrome120", "chrome124", "chrome116", "chrome110"]

SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def check_online(product: dict) -> dict:
    retailer_key = product["retailer"]
    url = product["url"]

    result = {
        "online_status": "unknown",
        "online_message": "",
        "instore_locations": [],
        "error": None,
    }

    try:
        if retailer_key == "ebgames_ca":
            result = _fetch_ebgames(url, result)
        else:
            resp = SESSION.get(url, timeout=15, allow_redirects=True)
            if resp.status_code == 404:
                result["online_status"] = "error"
                result["error"] = "Page not found (404)"
                return result
            if resp.status_code != 200:
                result["online_status"] = "error"
                result["error"] = f"HTTP {resp.status_code}"
                return result
            text = resp.text.lower()
            if retailer_key == "walmart_ca":
                result = _check_walmart(text, result)
            elif retailer_key == "pokemon_center_ca":
                result = _check_pcc(text, result)
            elif retailer_key == "amazon_ca":
                result = _check_amazon(text, result)
            else:
                cfg = RETAILER_CONFIGS.get(retailer_key, {})
                oos = next((t for t in cfg.get("oos_text", []) if t in text), None)
                ins = next((t for t in cfg.get("in_stock_text", []) if t in text), None)
                if ins and not oos:
                    result["online_status"] = "in_stock"
                    result["online_message"] = "In stock"
                elif oos:
                    result["online_status"] = "out_of_stock"
                    result["online_message"] = "Out of stock"

    except Exception as e:
        result["online_status"] = "error"
        result["error"] = str(e)[:120]

    return result


def _fetch_ebgames(url: str, result: dict) -> dict:
    """
    Fetch EB Games with curl_cffi + retry logic.
    Rotates Chrome profiles and waits between attempts.
    """
    if not CURL_AVAILABLE:
        result["online_status"] = "error"
        result["error"] = "curl_cffi not available"
        return result

    # Random delay 3–8s before each EB Games request to avoid rate limiting
    time.sleep(random.uniform(3, 8))

    profile = random.choice(CF_IMPERSONATE_PROFILES)

    for attempt in range(2):
        try:
            resp = cf_requests.get(
                url,
                impersonate=profile,
                timeout=25,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                }
            )

            if resp.status_code == 403:
                if attempt == 0:
                    # Wait longer and try a different profile
                    time.sleep(random.uniform(10, 20))
                    profile = random.choice(CF_IMPERSONATE_PROFILES)
                    continue
                result["online_status"] = "error"
                result["error"] = "Blocked by Cloudflare (403)"
                return result

            if resp.status_code == 404:
                result["online_status"] = "error"
                result["error"] = "Page not found (404)"
                return result

            if resp.status_code != 200:
                result["online_status"] = "error"
                result["error"] = f"HTTP {resp.status_code}"
                return result

            return _check_ebgames(resp.text.lower(), result)

        except Exception as e:
            if attempt == 0:
                time.sleep(5)
                continue
            result["online_status"] = "error"
            result["error"] = str(e)[:120]

    return result


def _check_walmart(text: str, result: dict) -> dict:
    if '"availabilityStatus":"IN_STOCK"' in text or \
       ("add to cart" in text and "out of stock" not in text and "unavailable" not in text):
        result["online_status"] = "in_stock"
        result["online_message"] = "In stock online"
    elif "out of stock" in text or '"availabilityStatus":"OUT_OF_STOCK"' in text or \
         "currently unavailable" in text:
        result["online_status"] = "out_of_stock"
        result["online_message"] = "Out of stock"
    else:
        result["online_status"] = "unknown"
        result["online_message"] = "Could not determine status"
    return result


def _check_pcc(text: str, result: dict) -> dict:
    if "add to cart" in text and "sold out" not in text and "notify me" not in text:
        result["online_status"] = "in_stock"
        result["online_message"] = "Add to cart available"
    elif "sold out" in text or "notify me" in text or "out of stock" in text:
        result["online_status"] = "out_of_stock"
        result["online_message"] = "Sold out"
    else:
        result["online_status"] = "unknown"
        result["online_message"] = "Could not determine status"
    return result


def _check_ebgames(text: str, result: dict) -> dict:
    if ("add to cart" in text or "buy now" in text) and \
       "out of stock" not in text and "not available" not in text and \
       "sold out" not in text:
        result["online_status"] = "in_stock"
        result["online_message"] = "Available online"
    elif "out of stock" in text or "not available" in text or "sold out" in text:
        result["online_status"] = "out_of_stock"
        result["online_message"] = "Out of stock"
    else:
        result["online_status"] = "unknown"
        result["online_message"] = "Could not determine status"
    return result


def _check_amazon(text: str, result: dict) -> dict:
    if "add to cart" in text and "currently unavailable" not in text:
        result["online_status"] = "in_stock"
        result["online_message"] = "In stock on Amazon"
    elif "currently unavailable" in text or "out of stock" in text:
        result["online_status"] = "out_of_stock"
        result["online_message"] = "Currently unavailable"
    else:
        result["online_status"] = "unknown"
        result["online_message"] = "Could not determine status"
    return result
