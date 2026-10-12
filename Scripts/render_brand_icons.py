#!/usr/bin/env python3
"""Renders TRINKA's interim app icons from the vector logo mark.

The geometry matches `TrinkaMark` in Packages/TrinkaKit/Sources/TrinkaUI/TrinkaMark.swift.
Once the original logo artwork is committed (see Design/Brand/README.md), prefer
`extract_brand_assets.py`, which crops the official PNGs instead.

Usage: python3 Scripts/render_brand_icons.py [--preview out.png]
Requires Pillow.
"""
import sys, os
from PIL import Image, ImageDraw, ImageFilter

INK = (16, 20, 24)
IVORY = (242, 238, 230)
MINT = (168, 224, 203)
LAGOON = (79, 169, 174)
FJORD = (23, 96, 127)
DEEP = (14, 63, 92)

# Cubic Bézier paths in unit coordinates: (start, [(c1, c2, end), ...])
MINT_PATH = ((0.45, 0.66), [
    ((0.52, 0.45), (0.50, 0.20), (0.62, 0.17)),
    ((0.70, 0.16), (0.74, 0.26), (0.80, 0.27)),
    ((0.92, 0.28), (1.00, 0.38), (0.99, 0.48)),
    ((0.98, 0.60), (0.90, 0.68), (0.80, 0.66)),
    ((0.72, 0.65), (0.68, 0.58), (0.62, 0.60)),
    ((0.55, 0.62), (0.50, 0.64), (0.45, 0.66)),
])
BLUE_PATH = ((0.61, 0.61), [
    ((0.57, 0.63), (0.55, 0.66), (0.55, 0.70)),
    ((0.56, 0.90), (0.46, 1.00), (0.34, 1.00)),
    ((0.22, 1.00), (0.14, 0.91), (0.14, 0.80)),
    ((0.14, 0.69), (0.22, 0.64), (0.34, 0.61)),
    ((0.45, 0.58), (0.55, 0.57), (0.61, 0.61)),
])
IVORY_CIRCLE = (0.33, 0.33, 0.32)  # cx, cy, r


def bezier(path, ox, oy, s, steps=48):
    (x0, y0), segs = path
    pts = [(ox + x0 * s, oy + y0 * s)]
    px, py = x0, y0
    for (c1, c2, e) in segs:
        for i in range(1, steps + 1):
            t = i / steps
            mt = 1 - t
            x = mt**3 * px + 3 * mt * mt * t * c1[0] + 3 * mt * t * t * c2[0] + t**3 * e[0]
            y = mt**3 * py + 3 * mt * mt * t * c1[1] + 3 * mt * t * t * c2[1] + t**3 * e[1]
            pts.append((ox + x * s, oy + y * s))
        px, py = e
    return pts


def gradient(size, c1, c2, vertical=True):
    w, h = size
    g = Image.new("RGB", size)
    d = ImageDraw.Draw(g)
    n = h if vertical else w
    for i in range(n):
        t = i / max(1, n - 1)
        c = tuple(int(c1[k] + (c2[k] - c1[k]) * t) for k in range(3))
        if vertical:
            d.line([(0, i), (w, i)], fill=c)
        else:
            d.line([(i, 0), (i, h)], fill=c)
    return g


def fill_path(img, pts, c1, c2, vertical, alpha):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    x0, y0, x1, y1 = int(min(xs)), int(min(ys)), int(max(xs)) + 1, int(max(ys)) + 1
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).polygon(pts, fill=alpha)
    tint = Image.new("RGBA", img.size, (0, 0, 0, 0))
    tint.paste(gradient((x1 - x0, y1 - y0), c1, c2, vertical).convert("RGBA"), (x0, y0))
    tint.putalpha(mask)
    img.alpha_composite(tint)


def draw_mark(img, ox, oy, s, ivory_fill=IVORY):
    W, H = img.size
    # Ivory sphere
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    cx, cy, r = IVORY_CIRCLE
    ImageDraw.Draw(layer).ellipse([ox + (cx - r) * s, oy + (cy - r) * s, ox + (cx + r) * s, oy + (cy + r) * s], fill=ivory_fill + (255,))
    img.alpha_composite(layer)
    # Mint wave is drawn last and slightly translucent, so it glazes over the sphere.
    # Fjord droplet, tucked under the mint wave
    fill_path(img, bezier(BLUE_PATH, ox, oy, s), (42, 127, 154), FJORD, True, 255)
    fill_path(img, bezier(MINT_PATH, ox, oy, s), LAGOON, MINT, False, 215)


def icon(size, background=INK, supersample=4):
    S = size * supersample
    img = Image.new("RGBA", (S, S), background + (255,))
    mark = S * 0.64
    draw_mark(img, (S - mark) / 2 - S * 0.01, (S - mark) / 2, mark)
    return img.resize((size, size), Image.LANCZOS).convert("RGB")


def mark_only(size, supersample=4):
    S = size * supersample
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    draw_mark(img, 0, 0, S)
    return img.resize((size, size), Image.LANCZOS)


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--preview" in sys.argv:
        out = sys.argv[sys.argv.index("--preview") + 1]
        sheet = Image.new("RGB", (1100, 560), (250, 249, 246))
        sheet.paste(icon(512), (20, 20))
        m = mark_only(512)
        sheet.paste(m, (560, 20), m)
        sheet.save(out)
        return
    targets = {
        "Trinka/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png": icon(1024),
        "TrinkaWatch/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png": icon(1024),
    }
    for rel, image in targets.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        image.save(path)
        print("wrote", rel)


if __name__ == "__main__":
    main()
