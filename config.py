"""
RestockWatch Configuration
Scarlet & Violet era + Mega Evolution era products
Pokémon Center CA, Walmart CA, EB Games CA, Amazon CA
Last updated: May 2026
"""

CHECK_INTERVAL = 45
HISTORY_LIMIT  = 100
NTFY_TOPIC     = ""
SERVER_PORT    = 5000

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
        "add_to_cart_selector": "button.add-to-cart",
        "oos_text": ["out of stock", "not available", "sold out"],
        "in_stock_text": ["add to cart", "buy now"],
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
}

WATCHLIST = [

    # ══════════════════════════════════════════════════════════════════════════
    # MEGA EVOLUTION — CHAOS RISING (May 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "cr_etb_pcc", "name": "ME: Chaos Rising — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10399-112/pokemon-tcg-mega-evolution-chaos-rising-pokemon-center-elite-trainer-box",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MEGA EVOLUTION — PERFECT ORDER (Apr 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "po_etb_pcc", "name": "ME: Perfect Order — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10372-109/pokemon-tcg-mega-evolution-perfect-order-pokemon-center-elite-trainer-box",
    },
    {
        "id": "po_bundle_pcc", "name": "ME: Perfect Order — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10377-109/pokemon-tcg-mega-evolution-perfect-order-booster-bundle-6-packs",
    },
    {
        "id": "po_bundle_wmt", "name": "ME: Perfect Order — Booster Bundle",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Mega-Evolution-Perfect-Order-Booster-Bundle/6LAA72BDBO4P",
    },
    {
        "id": "po_display_pcc", "name": "ME: Perfect Order — Display Box (36pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10380-119/pokemon-tcg-mega-evolution-perfect-order-booster-display-box-36-packs",
    },
    {
        "id": "po_etb_ebg", "name": "ME: Perfect Order — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962109",
    },
    {
        "id": "po_etb_ebg_fr", "name": "ME: Perfect Order — Elite Trainer Box (FR)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962115",
    },
    {
        "id": "po_bundle_ebg", "name": "ME: Perfect Order — Booster Bundle (6pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962106",
    },
    {
        "id": "po_display_ebg", "name": "ME: Perfect Order — Display Box (36pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962105",
    },
    {
        "id": "po_booster_ebg", "name": "ME: Perfect Order — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962104",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FIRST PARTNER ILLUSTRATION COLLECTION S1 (Apr 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "fpic_s1_pcc", "name": "First Partner Illustration Collection S1",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85175/pokemon-tcg-first-partner-illustration-collection",
    },
    {
        "id": "fpic_s1_wmt", "name": "First Partner Illustration Collection S1",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-First-Partner-Illustration-Collection-Series-1/3VOW28YCVGNC",
    },
    {
        "id": "fpic_s1_ebg_en", "name": "First Partner Illustration Collection S1 (EN)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962108",
    },
    {
        "id": "fpic_s1_ebg_fr", "name": "First Partner Illustration Collection S1 (FR)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/962112",
    },
    {
        "id": "fpic_s1_amz", "name": "First Partner Illustration Collection S1",
        "retailer": "amazon_ca", "track_instore": False, "active": True,
        "url": "https://www.amazon.ca/Pok%C3%A9mon-TCG-Partner-Illustration-Collection/dp/B0GG2BM9YQ",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # POKÉMON DAY 2026 COLLECTION
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "pd2026_wmt", "name": "Pokémon Day 2026 Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Pok-mon-Day-2026-Collection/70PH2R4R8A83",
    },
    {
        "id": "pd2026_ebg", "name": "Pokémon Day 2026 Collection",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/960093",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MEGA EVOLUTION — ASCENDED HEROES (Jan 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "ah_bundle_pcc", "name": "ME: Ascended Heroes — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10311-114/pokemon-tcg-mega-evolution-ascended-heroes-booster-bundle-6-packs",
    },
    {
        "id": "ah_etb_ebg", "name": "ME: Ascended Heroes — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/939890",
    },
    {
        "id": "ah_etb_ebg_fr", "name": "ME: Ascended Heroes — Elite Trainer Box (FR)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/960543",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 10.5 — WHITE FLARE / BLACK BOLT (Feb 2026)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "wf_etb_pcc", "name": "SV10.5 White Flare — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10037-117/pokemon-tcg-scarlet-and-violet-white-flare-pokemon-center-elite-trainer-box",
    },
    {
        "id": "bb_etb_pcc", "name": "SV10.5 Black Bolt — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10037-118/pokemon-tcg-scarlet-and-violet-black-bolt-pokemon-center-elite-trainer-box",
    },
    {
        "id": "bb_etb_wmt", "name": "SV10.5 Black Bolt — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-Black-Bolt-Elite-Trainer-Box/6000209337542",
    },
    {
        "id": "wf_bundle_pcc", "name": "SV10.5 White Flare — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10115-113/pokemon-tcg-scarlet-and-violet-white-flare-booster-bundle-6-packs",
    },
    {
        "id": "bb_bundle_pcc", "name": "SV10.5 Black Bolt — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10128-113/pokemon-tcg-scarlet-and-violet-black-bolt-booster-bundle-6-packs",
    },
    {
        "id": "wf_bundle_wmt", "name": "SV10.5 White Flare — Booster Bundle (6pk)",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-White-Flare-Booster-Bundle/5XB0SFI5NSO6",
    },
    {
        "id": "bb_bundle_wmt", "name": "SV10.5 Black Bolt — Booster Bundle (6pk)",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-Black-Bolt-Booster-Bundle/15IO4V3GG944",
    },
    {
        "id": "wf_binder_wmt", "name": "SV10.5 White Flare — Binder Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-White-Flare-Binder-Collection/6000209337540",
    },
    {
        "id": "bb_binder_wmt", "name": "SV10.5 Black Bolt — Binder Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-Black-Bolt-Binder-Collection/6000209337541",
    },
    {
        "id": "wf_sticker_pcc", "name": "SV10.5 White Flare — Tech Sticker Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10116-114/pokemon-tcg-scarlet-and-violet-white-flare-tech-sticker-collection",
    },
    {
        "id": "bb_sticker_pcc", "name": "SV10.5 Black Bolt — Tech Sticker Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10128-114/pokemon-tcg-scarlet-and-violet-black-bolt-tech-sticker-collection",
    },
    {
        "id": "bb_sticker_wmt", "name": "SV10.5 Black Bolt — Tech Sticker Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Scarlet-Violet-Black-Bolt-Tech-Sticker-Collection/6000209337543",
    },
    {
        "id": "bb_binder_pcc", "name": "SV10.5 Black Bolt — Binder Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10039-120/pokemon-tcg-scarlet-and-violet-black-bolt-binder-collection",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 10 — DESTINED RIVALS (May 2025)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "dr_etb_pcc", "name": "SV10 Destined Rivals — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10653/pokemon-tcg-scarlet-and-violet-destined-rivals-pokemon-center-elite-trainer-box",
    },
    {
        "id": "dr_etb_wmt", "name": "SV10 Destined Rivals — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Destined-Rivals-Elite-Trainer-Box/4ON9AB781V0W",
    },
    {
        "id": "dr_etb_ebg", "name": "SV10 Destined Rivals — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/936671",
    },
    {
        "id": "dr_bundle_pcc", "name": "SV10 Destined Rivals — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10638/pokemon-tcg-scarlet-and-violet-destined-rivals-booster-bundle-6-packs",
    },
    {
        "id": "dr_bundle_wmt", "name": "SV10 Destined Rivals — Booster Bundle (6pk)",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Destined-Rivals-Booster-Bundle/6ZA5591IEHFQ",
    },
    {
        "id": "dr_bundle_ebg", "name": "SV10 Destined Rivals — Booster Bundle (6pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/936670",
    },
    {
        "id": "dr_blister_wmt", "name": "SV10 Destined Rivals — 3pk Blister",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Destined-Rivals-Three-Booster-Blister-Receive-1-at-Random/3FXR8LQLKGK0",
    },
    {
        "id": "dr_display_pcc", "name": "SV10 Destined Rivals — Display Box (36pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10157-101/pokemon-tcg-scarlet-and-violet-destined-rivals-booster-display-box-36-packs",
    },
    {
        "id": "dr_bb_pcc", "name": "SV10 Destined Rivals — Build & Battle Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10656/pokemon-tcg-scarlet-and-violet-destined-rivals-build-and-battle-box",
    },
    {
        "id": "dr_booster_ebg", "name": "SV10 Destined Rivals — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/936668",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 9 — JOURNEY TOGETHER (Mar 2025)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "jt_etb_pcc", "name": "SV9 Journey Together — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10356/pokemon-tcg-scarlet-and-violet-journey-together-pokemon-center-elite-trainer-box",
    },
    {
        "id": "jt_etb_wmt", "name": "SV9 Journey Together — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Journey-Together-Elite-Trainer-Box/3GIM8P636RR6",
    },
    {
        "id": "jt_etb_ebg", "name": "SV9 Journey Together — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/932366",
    },
    {
        "id": "jt_bundle_pcc", "name": "SV9 Journey Together — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10341/pokemon-tcg-scarlet-and-violet-journey-together-booster-bundle-6-packs",
    },
    {
        "id": "jt_display_pcc", "name": "SV9 Journey Together — Enhanced Display (36pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10125-102/pokemon-tcg-scarlet-and-violet-journey-together-enhanced-booster-display-box-36-packs-and-1-promo-card",
    },
    {
        "id": "jt_booster_ebg", "name": "SV9 Journey Together — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/932364",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 8.5 — PRISMATIC EVOLUTIONS (Jan 2025)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "pe_etb_pcc", "name": "SV8.5 Prismatic Evolutions — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10019/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-pokemon-center-elite-trainer-box",
    },
    {
        "id": "pe_etb_wmt", "name": "SV8.5 Prismatic Evolutions — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Scarlet-Violet-Prismatic-Evolutions-Elite-Trainer-Box/6000208831664",
    },
    {
        "id": "pe_etb_ebg", "name": "SV8.5 Prismatic Evolutions — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/930025",
    },
    {
        "id": "pe_bundle_pcc", "name": "SV8.5 Prismatic Evolutions — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10025-101/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-booster-bundle-6-packs",
    },
    {
        "id": "pe_bundle_wmt", "name": "SV8.5 Prismatic Evolutions — Booster Bundle",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Prismatic-Evolutions-Booster-Bundle/6000208884941",
    },
    {
        "id": "pe_bundle_ebg", "name": "SV8.5 Prismatic Evolutions — Booster Bundle (6pk)",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/930392",
    },
    {
        "id": "pe_surprise_wmt", "name": "SV8.5 Prismatic Evolutions — Surprise Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Prismatic-Evolutions-Surprise-Box/6000208885051",
    },
    {
        "id": "pe_surprise_pcc", "name": "SV8.5 Prismatic Evolutions — Surprise Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/100-10096/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-surprise-box",
    },
    {
        "id": "pe_spc_pcc", "name": "SV8.5 Prismatic Evolutions — Super-Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10027-101/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-super-premium-collection",
    },
    {
        "id": "pe_spc_ebg", "name": "SV8.5 Prismatic Evolutions — Super-Premium Collection",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/936673",
    },
    {
        "id": "pe_figure_pcc", "name": "SV8.5 Prismatic Evolutions — Premium Figure Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10030-101/pokemon-tcg-scarlet-and-violet-prismatic-evolutions-premium-figure-collection",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 8 — SURGING SPARKS (Nov 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "ss_etb_pcc", "name": "SV8 Surging Sparks — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/191-85953/pokemon-tcg-scarlet-and-violet-surging-sparks-pokemon-center-elite-trainer-box",
    },
    {
        "id": "ss_etb_wmt", "name": "SV8 Surging Sparks — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Surging-Sparks-Elite-Trainer-Box/6000208610306",
    },
    {
        "id": "ss_etb_ebg", "name": "SV8 Surging Sparks — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Trading%20Cards/Games/926780",
    },
    {
        "id": "ss_bb_pcc", "name": "SV8 Surging Sparks — Build & Battle Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/191-85957/pokemon-tcg-scarlet-and-violet-surging-sparks-build-and-battle-box",
    },
    {
        "id": "ss_booster_ebg", "name": "SV8 Surging Sparks — Sleeved Booster",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/926778",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 7 — STELLAR CROWN (Sep 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "sc_etb_pcc", "name": "SV7 Stellar Crown — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/190-85923/pokemon-tcg-scarlet-and-violet-stellar-crown-pokemon-center-elite-trainer-box",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 6.5 — SHROUDED FABLE (Aug 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "sf_etb_pcc", "name": "SV6.5 Shrouded Fable — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85854/pokemon-tcg-scarlet-and-violet-shrouded-fable-pokemon-center-elite-trainer-box",
    },
    {
        "id": "sf_etb_wmt", "name": "SV6.5 Shrouded Fable — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Shrouded-Fable-Elite-Trainer-Box/6000208143199",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 6 — TWILIGHT MASQUERADE (May 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "tm_etb_pcc", "name": "SV6 Twilight Masquerade — PC Elite Trainer Box",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/189-85799/pokemon-tcg-scarlet-and-violet-twilight-masquerade-pokemon-center-elite-trainer-box",
    },
    {
        "id": "tm_bundle_pcc", "name": "SV6 Twilight Masquerade — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/189-85398/pokemon-tcg-scarlet-and-violet-twilight-masquerade-booster-bundle-6-packs",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 5 — TEMPORAL FORCES (Mar 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "tf_etb_pcc", "name": "SV5 Temporal Forces — PC ETB (Walking Wake)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/188-85717/pokemon-tcg-scarlet-and-violet-temporal-forces-pokemon-center-elite-trainer-box-walking-wake",
    },
    {
        "id": "tf_bundle_wmt", "name": "SV5 Temporal Forces — Booster Bundle",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Temporal-Forces-Booster-Bundle/6000207970496",
    },
    {
        "id": "tf_etb_ebg", "name": "SV5 Temporal Forces — Elite Trainer Box",
        "retailer": "ebgames_ca", "track_instore": True, "active": True,
        "url": "https://www.ebgames.ca/Toys-Collectibles/Games/917147",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 4.5 — PALDEAN FATES (Jan 2024)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "pf_etb_wmt", "name": "SV4.5 Paldean Fates — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-Paldean-Fates-Elite-Trainer-Box/6000207556441",
    },
    {
        "id": "pf_bundle_pcc", "name": "SV4.5 Paldean Fates — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/699-85739/pokemon-tcg-scarlet-and-violet-paldean-fates-booster-bundle",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 4 — PARADOX RIFT (Nov 2023)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "pr_etb_pcc", "name": "SV4 Paradox Rift — PC ETB (Iron Valiant)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/187-85415/pokemon-tcg-scarlet-and-violet-paradox-rift-pokemon-center-elite-trainer-box-iron-valiant",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SV 3.5 — 151 (Sep 2023)
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "151_etb_wmt", "name": "SV3.5 151 — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-Trading-Card-Games-Scarlet-Violet-3-5-151-Elite-Trainer-Box/6000207132536",
    },
    {
        "id": "151_upc_wmt", "name": "SV3.5 151 — Ultra-Premium Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Scarlet-Violet-151-Ultra-Premium-Collection/6000207556440",
    },
    {
        "id": "151_bundle_pcc", "name": "SV3.5 151 — Booster Bundle (6pk)",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/699-85322/pokemon-tcg-scarlet-and-violet-151-booster-bundle",
    },
    {
        "id": "151_upc_pcc", "name": "SV3.5 151 — Ultra-Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85541/pokemon-tcg-scarlet-and-violet-151-ultra-premium-collection",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPECIAL COLLECTIONS & TINS
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "lucario_etb_wmt", "name": "ME: Lucario EX — Elite Trainer Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Mega-Evolution-Elite-Trainer-Box-Lucario-EX/6000209337544",
    },
    {
        "id": "charizard_tin_wmt", "name": "Pokémon TCG: Mega Charizard Tin",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pok-mon-TCG-Mega-Charizard-Tin-Receive-1-at-Random/6000208610307",
    },
    {
        "id": "kangaskhan_wmt", "name": "Mega Kangaskhan ex Box",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Mega-Kangaskhan-ex-Box/6000209337545",
    },
    {
        "id": "snorlax_blissey_wmt", "name": "Snorlax ex & Blissey ex Special Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Snorlax-ex-Blissey-ex-Special-Collection/6000209337546",
    },
    {
        "id": "incineroar_torterra_wmt", "name": "Incineroar ex & Torterra ex Special Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Incineroar-ex-Torterra-ex-Special-Collection/6000209337547",
    },
    {
        "id": "greninja_kingdra_wmt", "name": "Greninja ex & Kingdra ex Special Collection",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Greninja-ex-Kingdra-ex-Special-Collection/6000209337548",
    },
    {
        "id": "trainers_toolkit_wmt", "name": "Trainer's Toolkit 2025",
        "retailer": "walmart_ca", "track_instore": True, "active": True,
        "url": "https://www.walmart.ca/en/ip/Pokemon-TCG-Trainers-Toolkit-2025/6000209337549",
    },
    {
        "id": "megacharizardx_upc_pcc", "name": "Mega Charizard X ex — Ultra-Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/10-10065-109/pokemon-tcg-mega-charizard-x-ex-ultra-premium-collection",
    },
    {
        "id": "combined_powers_pcc", "name": "Combined Powers — Premium Collection",
        "retailer": "pokemon_center_ca", "track_instore": False, "active": True,
        "url": "https://www.pokemoncenter.com/en-ca/product/290-85595/pokemon-tcg-combined-powers-premium-collection",
    },
]
