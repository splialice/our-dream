"""Promote the three art-style samples into publishable posts.

Adds the front matter fields the public site needs while preserving the
evidence fields used by validate_article.py.
"""

import pathlib
import re

BASE = pathlib.Path(r"D:\web\our-dream-preview")
SRC = BASE / "experiments"
DST = BASE / "content" / "posts"

SPECS = {
    "cuphead-art-style.md": {
        "description": "What is the Cuphead art style? Hand-drawn cel animation inspired by 1930s cartoons, what the developers called it, and why it is not cel shading.",
        "summary": "A specific studio, a specific cartoon tradition, and a specific production shortcut that saved the game.",
        "tags": ["Cuphead", "Cel animation", "Game art direction", "1930s animation"],
        "categories": ["Game history"],
    },
    "wind-waker-art-style.md": {
        "description": "What is the Wind Waker art style? Nintendo's developers explain the move from a realistic demo to toon shading, and why the change helped puzzle readability.",
        "summary": "A realistic demo, a sketch that changed direction, and an interview recorded years later.",
        "tags": ["The Wind Waker", "Toon shading", "Game art direction", "Nintendo"],
        "categories": ["Game history"],
    },
    "dishonored-art-style.md": {
        "description": "What is the Dishonored art style? How Arkane built Dunwall from London, Edinburgh, maritime costume, 1940s illustration and deliberate stylization.",
        "summary": "No single technique name: a city assembled from real research, illustration and anti-photorealistic choices.",
        "tags": ["Dishonored", "Game art direction", "Concept art", "Dunwall"],
        "categories": ["Game history"],
    },
}

FIELDS = [
    "draft: false",
    'author: "Pixel Dango"',
    "lastmod: 2026-11-17T12:00:00+08:00",
]


def yaml_list(items):
    return "[" + ", ".join(f'"{item}"' for item in items) + "]"


def promote(name, spec):
    text = (SRC / name).read_text(encoding="utf-8")
    parts = text.split("---", 2)
    fm, body = parts[1], parts[2]

    fm = re.sub(r'^type:\s*"art-style"\n', "", fm, flags=re.M)
    if not re.search(r"^draft:", fm, flags=re.M):
        fm = re.sub(r"^date:.*\n", lambda m: m.group(0) + FIELDS[0] + "\n", fm, count=1, flags=re.M)
    if not re.search(r"^author:", fm, flags=re.M):
        fm = re.sub(r"^draft:.*\n", lambda m: m.group(0) + FIELDS[1] + "\n", fm, count=1, flags=re.M)
    if not re.search(r"^lastmod:", fm, flags=re.M):
        fm = re.sub(r"^author:.*\n", lambda m: m.group(0) + FIELDS[2] + "\n", fm, count=1, flags=re.M)

    insert = (
        f'description: "{spec["description"]}"\n'
        f'summary: "{spec["summary"]}"\n'
        f"tags: {yaml_list(spec['tags'])}\n"
        f"categories: {yaml_list(spec['categories'])}\n"
        f'cover: "/img/covers/{name.replace(".md", ".webp")}"\n'
        "comments: true\n"
    )
    if "description:" not in fm:
        fm = re.sub(r"^author:.*\n", lambda m: m.group(0) + insert, fm, count=1, flags=re.M)

    out = DST / name
    out.write_text("---" + fm + "---" + body, encoding="utf-8")
    print("wrote", out, out.stat().st_size)


for filename, data in SPECS.items():
    promote(filename, data)
