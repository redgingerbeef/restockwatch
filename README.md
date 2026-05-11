# RestockWatch 🎴
Personal Canadian Pokémon TCG restock alert site.
Modelled after PokeToolz — restock feed, in-store availability, live ticker, and retailer dashboard.

## Project Layout
```
RestockWatch/
├── config.py           ← Your watchlist + settings (edit this)
├── watch.py            ← Stock checker (keep running in background)
├── server.py           ← Web server for the dashboard
├── checker.py          ← Playwright scraper engine
├── notifier.py         ← Optional phone push (ntfy.sh)
├── state.py            ← JSON state manager
├── data/stock.json     ← Live data file (auto-created)
└── templates/
    └── index.html      ← The full website
```

## Setup

### 1. Install
```bash
pip install playwright requests flask
playwright install chromium
```

### 2. Edit config.py
- Add your product URLs to `WATCHLIST`
- Set `active: True` for products you want to watch
- Optionally set `NTFY_TOPIC` for phone push alerts

### 3. Run
Open two terminals:

**Terminal 1 — Watcher:**
```bash
python watch.py
```

**Terminal 2 — Web server:**
```bash
python server.py
```

Open **http://localhost:5000** — that's your dashboard.

## Commands

| Command | Description |
|---|---|
| `python watch.py` | Start watching (runs forever) |
| `python watch.py --once` | Single check pass, then exit |
| `python watch.py --test` | Send a test push notification |
| `python server.py` | Dashboard on port 5000 |
| `python server.py --port 8080` | Custom port |

## Supported Retailers

| Key | Retailer | In-Store |
|---|---|---|
| `pokemon_center_ca` | Pokémon Center CA | No (queue-based) |
| `walmart_ca` | Walmart CA | ✅ Yes |
| `ebgames_ca` | EB Games CA | ✅ Yes |
| `costco_ca` | Costco CA | No |
| `bestbuy_ca` | Best Buy CA | No |
| `toysrus_ca` | Toys R Us CA | No |
| `amazon_ca` | Amazon CA | No |
| `sport_chek` | Sport Chek | No |

## Hosting on a VPS / Home Server

```bash
# Background watcher (Linux)
nohup python watch.py > watcher.log 2>&1 &

# Run server on port 80 directly (needs sudo) or use nginx proxy
python server.py --port 8080
```

**Nginx reverse proxy (recommended):**
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
    }
}
```

## Phone Push Notifications (optional)
1. Install the **ntfy** app (iOS / Android)
2. Subscribe to a unique topic name (e.g. `myrestocks-4821`)
3. Set `NTFY_TOPIC = "myrestocks-4821"` in config.py
4. Test: `python watch.py --test`
