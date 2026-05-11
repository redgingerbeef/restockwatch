"""
server.py — Flask web server + background watcher thread.
On Railway, only this process runs. The watcher runs inside it as a thread.
"""

import sys
import os
import json
import threading
from flask import Flask, render_template, jsonify

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "stock.json")


def load_state():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"products": {}, "alerts": [], "last_updated": None}


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/stock")
def api_stock():
    return jsonify(load_state())


def start_watcher():
    """Launch watch.py logic in a background thread."""
    try:
        from watch import run
        watcher_thread = threading.Thread(target=run, daemon=True)
        watcher_thread.start()
        print("  [Watcher] Background thread started.")
    except Exception as e:
        print(f"  [Watcher] Failed to start: {e}")


if __name__ == "__main__":
    # Start watcher in background
    start_watcher()

    # Get port from Railway env var or argument
    port = int(os.environ.get("PORT", 5000))
    if "--port" in sys.argv:
        idx = sys.argv.index("--port")
        port = int(sys.argv[idx + 1])

    print(f"\n  RestockWatch → http://0.0.0.0:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=False)
