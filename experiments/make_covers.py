"""Generate simple 1080x606 WebP covers for the three art-style articles."""

import pathlib
from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path(r"D:\web\our-dream-preview\static\img\covers")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1080, 606
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\seguisb.ttf",
    r"C:\Windows\Fonts\calibrib.ttf",
]

COVERS = [
    {
        "file": "cuphead-art-style.webp",
        "bg": (24, 20, 18),
        "accent": (238, 202, 92),
        "eyebrow": "ART STYLE / 01",
        "title": "CUPHEAD",
        "sub": "Hand-drawn cel animation, not cel shading",
    },
    {
        "file": "wind-waker-art-style.webp",
        "bg": (17, 54, 74),
        "accent": (132, 206, 214),
        "eyebrow": "ART STYLE / 02",
        "title": "WIND WAKER",
        "sub": "From realistic demo to toon shading",
    },
    {
        "file": "dishonored-art-style.webp",
        "bg": (26, 28, 26),
        "accent": (188, 166, 112),
        "eyebrow": "ART STYLE / 03",
        "title": "DISHONORED",
        "sub": "How Dunwall's visual identity was built",
    },
    {
        "file": "journey-art-style.webp",
        "bg": (196, 138, 92),
        "accent": (105, 44, 42),
        "eyebrow": "ART STYLE / 04",
        "title": "JOURNEY",
        "sub": "A colour script in red, white and blue",
    },
    {
        "file": "firewatch-art-style.webp",
        "bg": (28, 70, 62),
        "accent": (232, 116, 74),
        "eyebrow": "ART STYLE / 05",
        "title": "FIREWATCH",
        "sub": "Bold shapes, real places, story colours",
    },
    {
        "file": "gris-art-style.webp",
        "bg": (232, 228, 218),
        "accent": (128, 92, 118),
        "eyebrow": "ART STYLE / 06",
        "title": "GRIS",
        "sub": "An illustrated world built through colour",
    },
]


def font(size):
    for path in FONT_CANDIDATES:
        if pathlib.Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_cover(spec):
    im = Image.new("RGB", (W, H), spec["bg"])
    d = ImageDraw.Draw(im)

    # geometric motif on the right
    cx, cy = 860, 300
    for r, alpha in [(220, 22), (160, 34), (100, 50)]:
        col = tuple(int(spec["accent"][i] * alpha // 100 + spec["bg"][i] * (100 - alpha) // 100) for i in range(3))
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=8)

    d.rectangle([70, 70, 120, 76], fill=spec["accent"])
    d.text((70, 100), spec["eyebrow"], font=font(26), fill=spec["accent"])
    d.text((66, 160), spec["title"], font=font(82), fill=(245, 245, 245))
    d.text((70, 270), spec["sub"], font=font(30), fill=(205, 205, 205))

    d.line([70, H - 80, 460, H - 80], fill=spec["accent"], width=4)
    d.text((70, H - 62), "PIXEL DANGO", font=font(22), fill=(160, 160, 160))

    target = OUT / spec["file"]
    im.save(target, "WEBP", quality=88)
    print(target.name, target.stat().st_size)


for spec in COVERS:
    draw_cover(spec)
