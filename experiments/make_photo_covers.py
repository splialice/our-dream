"""Generate 1080x606 WebP covers from official game art.

Each cover crops an official screenshot/art image to fill the frame, darkens it
with a left-to-right gradient so the title stays readable, then overlays an
eyebrow, a big title and a sub-line. These are edited game images, not the
site's geometric default covers.
"""

import pathlib
from PIL import Image, ImageDraw, ImageFont

BASE = pathlib.Path(r"D:\web\our-dream-preview")
SRC = BASE / "static" / "img" / "editorial"
OUT = BASE / "static" / "img" / "covers"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1080, 606
BOLD = r"C:\Windows\Fonts\arialbd.ttf"
REG = r"C:\Windows\Fonts\arial.ttf"

COVERS = [
    {
        "file": "pragmata-fake-ai-new-york.webp",
        "source": "pragmata-new-york.jpg",
        "eyebrow": "GAL CULTURE / 16",
        "title": ["A Fake New York", "Made by Hand"],
        "sub": "Why Capcom drew AI's mistakes itself",
        "credit": "© CAPCOM Co., Ltd.",
        "focus": (0.58, 0.42),
    },
    {
        "file": "dragon-quest-ai-slimey-friend.webp",
        "source": "dq10-slimey-official.jpg",
        "eyebrow": "GAL CULTURE / 17",
        "title": ["An AI Slime", "You Can Befriend"],
        "sub": "Horii wants a companion, not a tool",
        "credit": "© ARMOR PROJECT / BIRD STUDIO / SQUARE ENIX",
        "focus": (0.30, 0.50),
        "base_dark": 78,
        "grad_width": 1.15,
        "grad_strength": 170,
    },
    {
        "file": "watamari-debanking.webp",
        "source": "watamari-nanna-rebis.jpg",
        "eyebrow": "GAL CULTURE / 18",
        "title": ["When the Bank", "Stopped the Money"],
        "sub": "How a yuri game hit a wall",
        "credit": "© Kuro Irodoru Yomiji / Sekai Project",
        "focus": (0.62, 0.45),
    },
    {
        "file": "big-walk-ai-bug-backlash.webp",
        "source": "big-walk-sunset.jpg",
        "eyebrow": "GAL CULTURE / 19",
        "title": ["10 Lines of AI", "400 Bad Reviews"],
        "sub": "The honesty that backfired",
        "credit": "© House House / Panic",
        "focus": (0.5, 0.45),
    },
    {
        "file": "valkyrie-tune-japanese-aesthetics.webp",
        "source": "valkyrie-tune-cast.jpg",
        "eyebrow": "GAL CULTURE / 20",
        "title": ["Cute Girls,", "Dark Questions"],
        "sub": "A director who won't water it down",
        "credit": "© Frontwing / GOOD SMILE COMPANY",
        "focus": (0.5, 0.42),
        "base_dark": 48,
        "grad_width": 1.05,
        "grad_strength": 180,
    },
]


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_crop(im, focus):
    """Crop the source image to 16:9 around a focal point, then resize to W,H."""
    iw, ih = im.size
    target = W / H
    if iw / ih > target:
        new_w = int(ih * target)
        left = int((iw - new_w) * focus[0])
        left = max(0, min(iw - new_w, left))
        im = im.crop((left, 0, left + new_w, ih))
    else:
        new_h = int(iw / target)
        top = int((ih - new_h) * focus[1])
        top = max(0, min(ih - new_h, top))
        im = im.crop((0, top, iw, top + new_h))
    return im.resize((W, H), Image.LANCZOS)


def gradient_overlay(base=0, width=0.82, strength=205):
    grad = Image.new("L", (W, H), 0)
    px = grad.load()
    for x in range(W):
        left = base + int(strength * max(0.0, 1 - x / (W * width)) ** 1.3)
        for y in range(H):
            bottom_boost = 40 if y > H - 90 else 0
            px[x, y] = min(242, left + bottom_boost)
    return grad


def text_width(d, text, fnt):
    box = d.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def make(spec):
    im = fit_crop(Image.open(SRC / spec["source"]).convert("RGB"), spec["focus"])
    dark = Image.new("RGB", (W, H), (6, 8, 14))
    mask = gradient_overlay(
        base=spec.get("base_dark", 0),
        width=spec.get("grad_width", 0.82),
        strength=spec.get("grad_strength", 205),
    )
    im = Image.composite(dark, im, mask)

    d = ImageDraw.Draw(im)
    accent = (240, 196, 92)

    d.text((62, 54), spec["eyebrow"], font=font(BOLD, 24), fill=accent)
    d.rectangle([62, 92, 132, 97], fill=accent)

    y = 132
    for line in spec["title"]:
        d.text((58, y), line, font=font(BOLD, 66), fill=(250, 250, 248))
        y += 78

    d.text((62, y + 8), spec["sub"], font=font(REG, 27), fill=(214, 216, 220))

    d.line([62, H - 74, 470, H - 74], fill=accent, width=3)
    d.text((62, H - 58), "PIXEL DANGO", font=font(BOLD, 20), fill=(200, 202, 206))

    d.text((W - 20 - text_width(d, spec["credit"], font(REG, 15)), H - 34),
           spec["credit"], font=font(REG, 15), fill=(178, 180, 184))

    target = OUT / spec["file"]
    im.save(target, "WEBP", quality=88)
    print(target.name, target.stat().st_size)


if __name__ == "__main__":
    for s in COVERS:
        make(s)
