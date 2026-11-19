"""Generate 1080x606 WebP covers.

The original geometric series is kept for the first six articles. New batches
use an editorial block layout with a large title and one concrete motif.
"""

import pathlib
import sys
from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path(r"D:\web\our-dream-preview\static\img\covers")
OUT.mkdir(parents=True, exist_ok=True)
DIAGRAM_OUT = pathlib.Path(r"D:\web\our-dream-preview\static\img\diagrams")
DIAGRAM_OUT.mkdir(parents=True, exist_ok=True)

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

EDITORIAL = [
    {
        "file": "tf2-art-style.webp",
        "eyebrow": "ART DIRECTION / 07",
        "big": "TF2",
        "title": "Team Fortress 2",
        "sub": "Early 20th-century illustration, not cel shading",
        "bg": (238, 231, 214),
        "ink": (39, 35, 34),
        "accent": (185, 73, 48),
        "motif": "bars",
        "blocks": [(37, 86, 122), (196, 84, 48), (232, 184, 84)],
    },
    {
        "file": "how-gris-tells-story-without-dialogue.webp",
        "eyebrow": "VISUAL STORYTELLING / 08",
        "big": "GRIS",
        "title": "Story without dialogue",
        "sub": "Colour, statues and camera cues",
        "bg": (236, 231, 222),
        "ink": (47, 39, 49),
        "accent": (148, 88, 122),
        "motif": "swatches",
        "blocks": [(206, 190, 172), (184, 139, 136), (148, 88, 122), (91, 63, 103)],
    },
    {
        "file": "what-is-cel-shading.webp",
        "eyebrow": "TECHNIQUE GUIDE / 09",
        "big": "CEL",
        "title": "Cel shading",
        "sub": "A rendering technique, not an art style",
        "bg": (24, 28, 34),
        "ink": (242, 242, 238),
        "accent": (104, 190, 208),
        "motif": "steps",
        "blocks": [(52, 70, 82), (76, 118, 138), (104, 190, 208)],
    },
    {
        "file": "visual-novel-vs-dating-sim.webp",
        "eyebrow": "GENRE GUIDE / 10",
        "big": "VN/DS",
        "title": "Visual novel vs dating sim",
        "sub": "Story form or relationship sim?",
        "bg": (31, 35, 46),
        "ink": (245, 244, 239),
        "accent": (236, 184, 84),
        "motif": "dialogue",
        "blocks": [(45, 52, 68), (74, 90, 116), (236, 184, 84)],
    },
    {
        "file": "kinetic-novel-meaning.webp",
        "eyebrow": "TERM GUIDE / 11",
        "big": "KN",
        "title": "Kinetic novel",
        "sub": "One story, no branches",
        "bg": (236, 232, 222),
        "ink": (42, 58, 52),
        "accent": (57, 104, 92),
        "motif": "dialogue",
        "blocks": [(196, 214, 205), (126, 171, 151), (57, 104, 92)],
    },
    {
        "file": "nvl-vs-adv.webp",
        "eyebrow": "UI GUIDE / 12",
        "big": "NVL",
        "title": "NVL vs ADV",
        "sub": "Two ways to put text on screen",
        "bg": (30, 28, 38),
        "ink": (244, 240, 248),
        "accent": (190, 138, 214),
        "motif": "dialogue",
        "blocks": [(58, 52, 72), (112, 86, 134), (190, 138, 214)],
    },
    {
        "file": "lost-museum-object-heads.webp",
        "eyebrow": "GAL CULTURE / 13",
        "big": "HEADS",
        "title": "Lost Museum",
        "sub": "Why the object heads stay that way",
        "bg": (28, 34, 40),
        "ink": (244, 240, 230),
        "accent": (222, 176, 92),
        "motif": "swatches",
        "blocks": [(70, 96, 112), (120, 150, 160), (196, 156, 92), (222, 176, 92)],
    },
    {
        "file": "labyrinthos-bad-endings.webp",
        "eyebrow": "GAL CULTURE / 14",
        "big": "ENDS",
        "title": "Labyrinthos",
        "sub": "Why one studio keeps the bad ending",
        "bg": (30, 26, 36),
        "ink": (244, 240, 246),
        "accent": (198, 132, 172),
        "motif": "bars",
        "blocks": [(74, 58, 90), (136, 92, 128), (198, 132, 172)],
    },
    {
        "file": "schrodingers-call-three-people.webp",
        "eyebrow": "GAL CULTURE / 15",
        "big": "x3",
        "title": "Schrodinger's Call",
        "sub": "Three people, four years, one scene",
        "bg": (22, 28, 34),
        "ink": (238, 244, 246),
        "accent": (104, 192, 206),
        "motif": "dialogue",
        "blocks": [(42, 56, 66), (60, 96, 112), (104, 192, 206)],
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


def wrap(d, text, fnt, max_width):
    lines = []
    current = ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if current and d.textbbox((0, 0), trial, font=fnt)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


def draw_motif(d, spec):
    kind = spec["motif"]
    blocks = spec["blocks"]
    if kind == "bars":
        for i, col in enumerate(blocks):
            x = 710 + i * 95
            d.rectangle([x, 110, x + 70, 430], fill=col)
            d.ellipse([x - 8, 80, x + 78, 166], fill=col)
            d.rectangle([x, 470, x + 70, 482], fill=spec["accent"])
    elif kind == "swatches":
        for i, col in enumerate(blocks):
            x = 690 + i * 92
            top = 120 + i * 45
            d.rectangle([x, top, x + 72, 480], fill=col)
    elif kind == "steps":
        for i, col in enumerate(blocks):
            x = 690 + i * 35
            y = 160 + i * 105
            d.rectangle([x, y, 1010, y + 78], fill=col)
    elif kind == "dialogue":
        for i, col in enumerate(blocks):
            y = 92 + i * 132
            d.rounded_rectangle([680, y, 1020, y + 96], radius=18, fill=col)
            d.rounded_rectangle([704, y + 20, 820, y + 38], radius=8, fill=spec["bg"])
            d.rectangle([704, y + 52, 980, y + 60], fill=spec["bg"])
            d.rectangle([704, y + 70, 920, y + 78], fill=spec["bg"])


def draw_editorial_cover(spec):
    im = Image.new("RGB", (W, H), spec["bg"])
    d = ImageDraw.Draw(im)

    d.rectangle([0, 0, W, 14], fill=spec["accent"])
    d.text((70, 78), spec["eyebrow"], font=font(24), fill=spec["accent"])
    d.text((60, 126), spec["big"], font=font(132), fill=spec["ink"])

    y = 292
    for line in wrap(d, spec["title"], font(40), 560):
        d.text((70, y), line, font=font(40), fill=spec["ink"])
        y += 50

    y += 16
    for line in wrap(d, spec["sub"], font(26), 560):
        d.text((70, y), line, font=font(26), fill=spec["ink"])
        y += 36

    d.line([70, H - 70, 520, H - 70], fill=spec["accent"], width=3)
    d.text((70, H - 54), "PIXEL DANGO", font=font(20), fill=spec["ink"])

    draw_motif(d, spec)

    target = OUT / spec["file"]
    im.save(target, "WEBP", quality=88)
    print(target.name, target.stat().st_size)


def draw_layout_diagrams():
    adv = Image.new("RGB", (W, H), (28, 30, 38))
    d = ImageDraw.Draw(adv)
    d.text((70, 52), "ADV-style", font=font(52), fill=(245, 244, 239))
    d.rounded_rectangle([390, 110, 690, 398], radius=24, fill=(66, 72, 90))
    d.ellipse([505, 160, 575, 230], fill=(200, 205, 220))
    d.rounded_rectangle([80, 418, 1000, 562], radius=18, fill=(238, 236, 230))
    d.rounded_rectangle([110, 438, 280, 470], radius=8, fill=(42, 46, 60))
    d.text((124, 445), "Speaker", font=font(20), fill=(238, 236, 230))
    d.text((110, 486), "One dialogue / narration unit", font=font(28), fill=(35, 38, 48))
    d.text((110, 524), "(may wrap across physical lines)", font=font(20), fill=(90, 95, 105))
    d.text((70, H - 28), "Schematic diagram - not a game screenshot", font=font(18), fill=(180, 185, 195))
    adv.save(DIAGRAM_OUT / "adv-layout-schematic.png")
    print("adv-layout-schematic.png")

    nvl = Image.new("RGB", (W, H), (236, 232, 224))
    d = ImageDraw.Draw(nvl)
    d.text((70, 46), "NVL-style", font=font(52), fill=(45, 40, 50))
    d.rounded_rectangle([80, 118, 1000, 510], radius=18, fill=(250, 248, 242), outline=(190, 185, 175), width=2)
    lines = [
        "Narration unit 1",
        "Dialogue unit 2",
        "Narration unit 3",
        "Dialogue unit 4",
        "Narration unit 5",
    ]
    for i, line in enumerate(lines):
        d.text((120, 145 + i * 64), line, font=font(28), fill=(60, 55, 65))
    d.text((120, 466), "Multiple units stacked on screen", font=font(20), fill=(130, 125, 135))
    d.text((70, H - 28), "Schematic diagram - not a game screenshot", font=font(18), fill=(110, 105, 115))
    nvl.save(DIAGRAM_OUT / "nvl-layout-schematic.png")
    print("nvl-layout-schematic.png")


if __name__ == "__main__":
    wanted = set(sys.argv[1:])
    for spec in EDITORIAL:
        if not wanted or spec["file"] in wanted:
            draw_editorial_cover(spec)
    draw_layout_diagrams()
