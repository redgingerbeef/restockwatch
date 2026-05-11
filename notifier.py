"""notifier.py — ntfy.sh phone push notifications."""
import requests
from config import NTFY_TOPIC

def notify(name, url, retailer_label, instore_count=0):
    if not NTFY_TOPIC: return
    body = f"{name} is IN STOCK at {retailer_label}!"
    if instore_count: body += f"\n{instore_count} store(s) available nearby."
    try:
        requests.post(f"https://ntfy.sh/{NTFY_TOPIC}", data=body,
            headers={"Title":"🟢 Restock Alert!","Priority":"urgent",
                     "Tags":"rotating_light,pokemon","Click":url}, timeout=10)
        print(f"  ✅ Push sent → {NTFY_TOPIC}")
    except Exception as e:
        print(f"  ⚠️  ntfy failed: {e}")
