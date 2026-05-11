"""
RestockWatch Configuration
All confirmed Scarlet & Violet era + Mega Evolution era products
across Pokémon Center CA, Walmart CA, and EB Games CA.

Last updated: May 2026
"""

# ── Settings ──────────────────────────────────────────────────────────────────
CHECK_INTERVAL = 45        # seconds between checks
HISTORY_LIMIT  = 100       # max alert history entries per product
NTFY_TOPIC     = ""        # optional: ntfy.sh topic for phone push alerts
SERVER_PORT    = 5000

# ── Retailer Definitions ──────────────────────────────────────────────────────
RETAILER_CONFIGS = {
    "pokemon_center_ca": {
        "label": "Pokémon Center CA", "short": "PCC", "color": "#e3350d",
        "add_to_cart_selector": "button[data-testid='add-to-cart-button']",
        "oos_text": ["out of stock", "notify me", "sold out"],
        "in_stock_text": ["add to cart", "add to bag"],
        "instore_support": False,
    },
    "walmart_ca": {
        "label": "Walmart CA", "short": "WMT", "color": "#0071ce",
        "add_to_cart_selector": "button[data-automation='add-to-cart-button']",
        "oos_text": ["out of stock", "check store availability only"],
        "in_stock_text": ["add to cart", "add to bag"],
        "instore_support": True,
    },
    "ebgames_ca": {
        "label": "EB Games CA", "short": "EBG", "color": "#ff6a00",
        "add_to_cart_selector": "button.add-to-cart, button[data-action='add-to-cart'], a.add-to-cart-btn",
        "oos_text": ["out of stock", "not available"],
        "in_stock_text": ["add to cart", "buy now", "add to bag"],
        "instore_support": True,
    },
    "amazon_ca": {
        "label": "Amazon CA", "short": "AMZ", "color": "#ff9900",
        "add_to_cart_selector": "#add-to-cart-button",
        "oos_text": ["currently unavailable", "out of stock"],
        "in_stock_text": ["add to cart", "in stock"],
        "instore_support": False,
    },
    "costco_ca": {
        "label": "Costco CA", "short": "CST", "color": "#005daa",
        "add_to_cart_selector": "button.add-to-cart-btn",
        "oos_text": ["out of stock", "sold out", "currently unavailable"],
        "in_stock_text": ["add to cart"],
        "instore_support": False,
    },
    "bestbuy_ca": {
        "label": "Best Buy CA", "short": "BBY", "color": "#1f49a0",
        "add_to_cart_selector": "button.addToCartButton",
        "oos_text": ["sold out", "coming soon"],
        "in_stock_text": ["add to cart"],
        "instore_support": False,
    },
}

# ═════════════════════════════════════════════════════════════════════════════
# WATCHLIST — All confirmed product URLs
# Fields: id (unique), name, retailer, url, track_instore, active
# ═════════════════════════════════════════════════════════════════════════════

WATCHLIST = [

    # ══════════════════════════════════════════════════════════════════════════
    # MEGA EVOLUTION — CHAOS RISING (May 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "cr_etb_pcc",
        "name": "ME: Chaos Rising — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10399-112/pokemon-tcg-mega-evolution-chaos-rising-pokemon-center-elite-trainer-box",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MEGA EVOLUTION — PERFECT ORDER (Apr 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "po_etb_pcc",
        "name": "ME: Perfect Order — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10372-109/pokemon-tcg-mega-evolution-perfect-order-pokemon-center-elite-trainer-box",
    },
    {
        "id": "po_etb_ebg",
        "name": "ME: Perfect Order — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962109",
    },
    {
        "id": "po_etb_ebg_fr",
        "name": "ME: Perfect Order — Elite Trainer Box (FR)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962115",
    },
    {
        "id": "po_bundle_pcc",
        "name": "ME: Perfect Order — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10377-109/pokemon-tcg-mega-evolution-perfect-order-booster-bundle-6-packs",
    },
    {
        "id": "po_bundle_ebg",
        "name": "ME: Perfect Order — Booster Bundle (6pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962106",
    },
    {
        "id": "po_display_pcc",
        "name": "ME: Perfect Order — Booster Display Box (36pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10380-119/pokemon-tcg-mega-evolution-perfect-order-booster-display-box-36-packs",
    },
    {
        "id": "po_display_ebg",
        "name": "ME: Perfect Order — Booster Display Box (36pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962105",
    },
    {
        "id": "po_booster_ebg",
        "name": "ME: Perfect Order — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962104",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FIRST PARTNER ILLUSTRATION COLLECTION S1 (Apr 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "fpic_s1_pcc",
        "name": "First Partner Illustration Collection S1",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85175/pokemon-tcg-first-partner-illustration-collection",
    },
    {
        "id": "fpic_s1_wmt",
        "name": "First Partner Illustration Collection S1",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-First-Partner-Illustration-Collection-Series-1/3VOW28YCVGNC",
    },
    {
        "id": "fpic_s1_ebg_en",
        "name": "First Partner Illustration Collection S1 (EN)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962108",
    },
    {
        "id": "fpic_s1_ebg_fr",
        "name": "First Partner Illustration Collection S1 (FR)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962112",
    },
    {
        "id": "fpic_s1_amz",
        "name": "First Partner Illustration Collection S1",
        "retailer": "amazon_ca", "track_instore": False, "active": True,
        "url": "https://www.amazon.ca/Pok%C3%A9mon-TCG-Partner-Illustration-Collection/dp/B0GG2BM9YQ",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MEGA EVOLUTION — ASCENDED HEROES (Jan 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "ah_bundle_pcc",
        "name": "ME: Ascended Heroes — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10311-114/pokemon-tcg-mega-evolution-ascended-heroes-booster-bundle-6-packs",
    },
    {
        "id": "ah_etb_ebg",
        "name": "ME: Ascended Heroes — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/939890",
    },
    {
        "id": "ah_etb_ebg_fr",
        "name": "ME: Ascended Heroes — Elite Trainer Box (FR)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/960543",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 10.5 — WHITE FLARE / BLACK BOLT (Feb 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "wf_etb_pcc",
        "name": "SV10.5 White Flare — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10037-117/pokemon-tcg-scarlet-and-violet-white-flare-pokemon-center-elite-trainer-box",
    },
    {
        "id": "bb_etb_pcc",
        "name": "SV10.5 Black Bolt — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10037-118/pokemon-tcg-scarlet-and-violet-black-bolt-pokemon-center-elite-trainer-box",
    },
    {
        "id": "wf_bundle_pcc",
        "name": "SV10.5 White Flare — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10115-113/pokemon-tcg-scarlet-and-violet-white-flare-booster-bundle-6-packs",
    },
    {
        "id": "bb_bundle_pcc",
        "name": "SV10.5 Black Bolt — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10115-113/pokemon-tcg-scarlet-and-violet-black-bolt-booster-bundle-6-packs",
    },
    {
        "id": "wf_bundle_wmt",
        "name": "SV10.5 White Flare — Booster Bundle (6pk)",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-White-Flare-Booster-Bundle/5XB0SFI5NSO6",
    },
    {
        "id": "bb_bundle_wmt",
        "name": "SV10.5 Black Bolt — Booster Bundle (6pk)",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-Black-Bolt-Booster-Bundle/15IO4V3GG944",
    },
    {
        "id": "bb_binder_wmt",
        "name": "SV10.5 Black Bolt — Binder Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-Black-Bolt-Binder-Collection/",
    },
    {
        "id": "wf_sticker_pcc",
        "name": "SV10.5 White Flare — Tech Sticker Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10116-114/pokemon-tcg-scarlet-and-violet-white-flare-tech-sticker-collection",
    },
    {
        "id": "bb_sticker_pcc",
        "name": "SV10.5 Black Bolt — Tech Sticker Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10128-114/pokemon-tcg-scarlet-and-violet-black-bolt-tech-sticker-collection",
    },
    {
        "id": "bb_binder_pcc",
        "name": "SV10.5 Black Bolt — Binder Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10039-120/pokemon-tcg-scarlet-and-violet-black-bolt-binder-collection",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 10 — DESTINED RIVALS (May 2025)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "dr_etb_pcc",
        "name": "SV10 Destined Rivals — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10653/pokemon-tcg-scarlet-and-violet-destined-rivals-pokemon-center-elite-trainer-box",
    },
    {
        "id": "dr_etb_wmt",
        "name": "SV10 Destined Rivals — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Destined-Rivals-Elite-Trainer-Box/4ON9AB781V0W",
    },
    {
        "id": "dr_etb_ebg",
        "name": "SV10 Destined Rivals — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/936671",
    },
    {
        "id": "dr_bundle_pcc",
        "name": "SV10 Destined Rivals — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10638/pokemon-tcg-scarlet-and-violet-destined-rivals-booster-bundle-6-packs",
    },
    {
        "id": "dr_bundle_wmt",
        "name": "SV10 Destined Rivals — Booster Bundle (6pk)",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Destined-Rivals-Booster-Bundle/6ZA5591IEHFQ",
    },
    {
        "id": "dr_bundle_ebg",
        "name": "SV10 Destined Rivals — Booster Bundle (6pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/936670",
    },
    {
        "id": "dr_display_pcc",
        "name": "SV10 Destined Rivals — Display Box (36pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10157-101/pokemon-tcg-scarlet-and-violet-destined-rivals-booster-display-box-36-packs",
    },
    {
        "id": "dr_bb_pcc",
        "name": "SV10 Destined Rivals — Build & Battle Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10656/pokemon-tcg-scarlet-and-violet-destined-rivals-build-and-battle-box",
    },
    {
        "id": "dr_blister_wmt",
        "name": "SV10 Destined Rivals — 3-Booster Blister",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Destined-Rivals-Three-Booster-Blister-Receive-1-at-Random/3FXR8LQLKGK0",
    },
    {
        "id": "dr_booster_ebg",
        "name": "SV10 Destined Rivals — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/936668",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 9 — JOURNEY TOGETHER (Mar 2025)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "jt_etb_pcc",
        "name": "SV9 Journey Together — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10356/pokemon-tcg-scarlet-and-violet-journey-together-pokemon-center-elite-trainer-box",
    },
    {
        "id": "jt_etb_wmt",
        "name": "SV9 Journey Together — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/POKEMON-SV9-JOURNEY-TOGETHER-ETB-BL/3EV8QX68MTK6",
    },
    {
        "id": "jt_etb_ebg",
        "name": "SV9 Journey Together — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/932366",
    },
    {
        "id": "jt_bundle_pcc",
        "name": "SV9 Journey Together — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10341/pokemon-tcg-scarlet-and-violet-journey-together-booster-bundle-6-packs",
    },
    {
        "id": "jt_display_pcc",
        "name": "SV9 Journey Together — Enhanced Display (36pk + promo)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10125-102/pokemon-tcg-scarlet-and-violet-journey-together-enhanced-booster-display-box-36-packs-and-1-promo-card",
    },
    {
        "id": "jt_booster_ebg",
        "name": "SV9 Journey Together — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/932364",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 8.5 — PRISMATIC EVOLUTIONS (Jan 2025)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "pe_etb_pcc",
        "name": "SV8.5 Prismatic Evolutions — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10019/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-pokemon-center-elite-trainer-box",
    },
    {
        "id": "pe_etb_ebg",
        "name": "SV8.5 Prismatic Evolutions — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/930025",
    },
    {
        "id": "pe_bundle_pcc",
        "name": "SV8.5 Prismatic Evolutions — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10025-101/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-booster-bundle-6-packs",
    },
    {
        "id": "pe_bundle_ebg",
        "name": "SV8.5 Prismatic Evolutions — Booster Bundle (6pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/930392",
    },
    {
        "id": "pe_spc_pcc",
        "name": "SV8.5 Prismatic Evolutions — Super-Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10027-101/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-super-premium-collection",
    },
    {
        "id": "pe_spc_ebg",
        "name": "SV8.5 Prismatic Evolutions — Super-Premium Collection",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/936673",
    },
    {
        "id": "pe_surprise_pcc",
        "name": "SV8.5 Prismatic Evolutions — Surprise Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10096/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-surprise-box",
    },
    {
        "id": "pe_figure_pcc",
        "name": "SV8.5 Prismatic Evolutions — Premium Figure Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10030-101/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-premium-figure-collection",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 8 — SURGING SPARKS (Nov 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "ss_etb_pcc",
        "name": "SV8 Surging Sparks — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/191-85953/pokemon-tcg-scarlet-and-violet-surging-sparks-pokemon-center-elite-trainer-box",
    },
    {
        "id": "ss_etb_ebg",
        "name": "SV8 Surging Sparks — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/926780",
    },
    {
        "id": "ss_bb_pcc",
        "name": "SV8 Surging Sparks — Build & Battle Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/191-85957/pokemon-tcg-scarlet-and-violet-surging-sparks-build-and-battle-box",
    },
    {
        "id": "ss_booster_ebg",
        "name": "SV8 Surging Sparks — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/926778",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 7 — STELLAR CROWN (Sep 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "sc_etb_pcc",
        "name": "SV7 Stellar Crown — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/190-85923/pokemon-tcg-scarlet-and-violet-stellar-crown-pokemon-center-elite-trainer-box",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 6.5 — SHROUDED FABLE (Aug 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "sf_etb_pcc",
        "name": "SV6.5 Shrouded Fable — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85854/pokemon-tcg-scarlet-and-violet-shrouded-fable-pokemon-center-elite-trainer-box",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 6 — TWILIGHT MASQUERADE (May 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "tm_etb_pcc",
        "name": "SV6 Twilight Masquerade — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/189-85799/pokemon-tcg-scarlet-and-violet-twilight-masquerade-pokemon-center-elite-trainer-box",
    },
    {
        "id": "tm_bundle_pcc",
        "name": "SV6 Twilight Masquerade — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/189-85398/pokemon-tcg-scarlet-and-violet-twilight-masquerade-booster-bundle-6-packs",
    },
    {
        "id": "tm_promo_pcc",
        "name": "SV6 Twilight Masquerade — 3pk + Snorlax Promo",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/699-85786/pokemon-tcg-scarlet-and-violet-twilight-masquerade-3-booster-packs-and-snorlax-promo-card",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 5 — TEMPORAL FORCES (Mar 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "tf_etb_pcc",
        "name": "SV5 Temporal Forces — PC ETB (Walking Wake)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/188-85717/pokemon-tcg-scarlet-and-violet-temporal-forces-pokemon-center-elite-trainer-box-walking-wake",
    },
    {
        "id": "tf_etb_ebg",
        "name": "SV5 Temporal Forces — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/917147",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 4.5 — PALDEAN FATES (Jan 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "pf_bundle_pcc",
        "name": "SV4.5 Paldean Fates — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/699-85739/pokemon-tcg-scarlet-and-violet-paldean-fates-booster-bundle",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 4 — PARADOX RIFT (Nov 2023)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "pr_etb_pcc",
        "name": "SV4 Paradox Rift — PC ETB (Iron Valiant)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/187-85415/pokemon-tcg-scarlet-and-violet-paradox-rift-pokemon-center-elite-trainer-box-iron-valiant",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 3.5 — 151 (Sep 2023)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "151_bundle_pcc",
        "name": "SV3.5 151 — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/699-85322/pokemon-tcg-scarlet-and-violet-151-booster-bundle",
    },
    {
        "id": "151_upc_pcc",
        "name": "SV3.5 151 — Ultra-Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85541/pokemon-tcg-scarlet-and-violet-151-ultra-premium-collection",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 1 — SCARLET & VIOLET BASE (Mar 2023)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "sv1_etb_pcc",
        "name": "SV1 Scarlet & Violet — PC ETB (Koraidon)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/184-85342/pokemon-tcg-scarlet-and-violet-pokemon-center-elite-trainer-box-koraidon",
    },
    {
        "id": "sv1_bundle_pcc",
        "name": "SV1 Scarlet & Violet — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/184-85337/pokemon-tcg-scarlet-and-violet-booster-bundle-6-packs",
    },
    {
        "id": "sv1_promo_pcc",
        "name": "SV1 Scarlet & Violet — 3pk + Arcanine Promo",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/699-85329/pokemon-tcg-scarlet-and-violet-3-booster-packs-and-arcanine-promo-card",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPECIAL COLLECTIONS & PREMIUM PRODUCTS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "charizard_spc_pcc",
        "name": "Charizard ex — Super-Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85819/pokemon-tcg-charizard-ex-super-premium-collection",
    },
    {
        "id": "megacharizardx_upc_pcc",
        "name": "Mega Charizard X ex — Ultra-Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10065-109/pokemon-tcg-mega-charizard-x-ex-ultra-premium-collection",
    },
    {
        "id": "combined_powers_pcc",
        "name": "Combined Powers — Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85595/pokemon-tcg-combined-powers-premium-collection",
    },
    {
        "id": "pokemon_day_2026_ebg",
        "name": "Pokémon Day 2026 Collection",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/960093",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # COSTCO CA — No confirmed online listing as of May 2026.
    # Set active: True and update URL if a listing appears on costco.ca
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "costco_pokemon_browse",
        "name": "Costco CA — Pokémon TCG Browse",
        "retailer": "costco_ca", "track_instore": False, "active": False,
        "url": "https://www.costco.ca/pokemon-cards.html",
    },

]
