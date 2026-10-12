#!/usr/bin/env python3
"""Crops TRINKA's official logo artwork into the app's asset catalogs.

Put the original PNGs in Design/Brand/ (see Design/Brand/README.md), then run:

    python3 Scripts/extract_brand_assets.py icon Design/Brand/trinka-app-icon.png
        -> App icons for iPhone and Apple Watch (1024×1024, opaque, full-bleed).
           Finds the rounded square on its light background, crops it and fills the
           rounded corners with the icon's own background color (iOS applies its own mask).

    python3 Scripts/extract_brand_assets.py mark Design/Brand/trinka-logo-light.png [--box x0,y0,x1,y1]
        -> `TrinkaMark` image set (transparent PNG) used by the in-app logo instead of the
           vector fallback. Without --box, the mark is taken as the left-most non-background
           blob (works for the horizontal "mark + TRINKA" lockup).

Requires Pillow (`pip install pillow`).
"""
import json
import os
import sys

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def is_background(pixel, threshold=235):
    r, g, b = pixel[:3]
    return r > threshold and g > threshold and b > threshold


def content_bbox(img, threshold=235):
    """Bounding box of everything that isn't near-white."""
    gray = img.convert("L").point(lambda v: 255 if v < threshold else 0)
    return gray.getbbox()


def make_icon(src):
    img = Image.open(src).convert("RGB")
    box = content_bbox(img)
    if not box:
        sys.exit("No artwork found in " + src)
    x0, y0, x1, y1 = box
    side = max(x1 - x0, y1 - y0)
    crop = img.crop((x0, y0, x0 + side, y0 + side))
    # Sample the icon background from the middle of the left edge (inside the rounded square).
    bg = crop.getpixel((max(2, side // 40), side // 2))
    # Flood-fill the four light corners with the background color.
    for corner in [(0, 0), (side - 1, 0), (0, side - 1), (side - 1, side - 1)]:
        if is_background(crop.getpixel(corner)):
            ImageDraw.floodfill(crop, corner, bg, thresh=60)
    icon = crop.resize((1024, 1024), Image.LANCZOS)
    for rel in ("Trinka/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png",
                "TrinkaWatch/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png"):
        path = os.path.join(ROOT, rel)
        icon.save(path)
        print("wrote", rel)


def leftmost_blob_box(img):
    """Left-most connected region of non-background columns (the mark in a horizontal lockup)."""
    w, h = img.size
    px = img.load()
    cols = [any(not is_background(px[x, y]) for y in range(0, h, 2)) for x in range(w)]
    start = next((x for x, filled in enumerate(cols) if filled), None)
    if start is None:
        sys.exit("No artwork found")
    end = start
    gap = 0
    for x in range(start, w):
        if cols[x]:
            end, gap = x, 0
        else:
            gap += 1
            if gap > w * 0.02:  # a clear vertical gap separates the mark from the wordmark
                break
    rows = [y for y in range(h) if any(not is_background(px[x, y]) for x in range(start, end + 1, 2))]
    return start, rows[0], end + 1, rows[-1] + 1


def make_mark(src, box=None):
    img = Image.open(src).convert("RGB")
    box = box or leftmost_blob_box(img)
    crop = img.crop(box)
    # Alpha from distance to white, so soft anti-aliased edges stay smooth.
    rgba = crop.convert("RGBA")
    px = rgba.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, _ = px[x, y]
            distance = 255 - min(r, g, b)
            # Pure background → transparent; a short ramp keeps anti-aliased edges smooth.
            alpha = 0 if distance <= 12 else min(255, (distance - 12) * 255 // 28)
            px[x, y] = (r, g, b, alpha)
    side = max(rgba.size)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(rgba, ((side - rgba.width) // 2, (side - rgba.height) // 2))
    for target in ("Trinka", "TrinkaWatch"):
        folder = os.path.join(ROOT, target, "Assets.xcassets", "TrinkaMark.imageset")
        os.makedirs(folder, exist_ok=True)
        canvas.resize((512, 512), Image.LANCZOS).save(os.path.join(folder, "TrinkaMark.png"))
        json.dump({
            "images": [{"filename": "TrinkaMark.png", "idiom": "universal"}],
            "info": {"author": "xcode", "version": 1},
            "properties": {"preserves-vector-representation": False},
        }, open(os.path.join(folder, "Contents.json"), "w"), indent=2)
        print("wrote", os.path.relpath(folder, ROOT))


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("icon", "mark"):
        sys.exit(__doc__)
    if sys.argv[1] == "icon":
        make_icon(sys.argv[2])
    else:
        box = None
        if "--box" in sys.argv:
            box = tuple(int(v) for v in sys.argv[sys.argv.index("--box") + 1].split(","))
        make_mark(sys.argv[2], box)


if __name__ == "__main__":
    main()
