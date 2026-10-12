# TRINKA brand assets

Palette (from the logo):

| Token | Hex | Use |
|---|---|---|
| Ink | `#101418` | Dark backgrounds, text on light |
| Ivory | `#F2EEE6` | Sphere, text on dark |
| Mint | `#A8E0CB` | Wave, dark-mode accent |
| Lagoon | `#4FA9AE` | Secondary accent |
| Fjord | `#17607F` | Droplet, light-mode accent |
| Deep fjord | `#0E3F5C` | Gradients |

Semantic light/dark tokens live in `Packages/TrinkaKit/Sources/TrinkaUI/Theme.swift`.

## Using the official artwork

The app currently ships a **vector re-creation** of the mark (`TrinkaMark` in TrinkaUI) and
interim app icons rendered from it (`Scripts/render_brand_icons.py`). To use the original files:

1. Save the originals here, e.g.
   - `trinka-app-icon.png` — the dark rounded-square icon (first logo).
   - `trinka-logo-light.png` — horizontal mark + "TRINKA" on a light background.
2. Run:
   ```sh
   python3 Scripts/extract_brand_assets.py icon Design/Brand/trinka-app-icon.png
   python3 Scripts/extract_brand_assets.py mark Design/Brand/trinka-logo-light.png
   ```
   The first replaces both app icons; the second adds a `TrinkaMark` image set, which the
   in-app logo automatically prefers over the vector version.
