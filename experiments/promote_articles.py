"""Promote the three art-style samples into publishable posts.

Adds the front matter fields the public site needs while preserving the
evidence fields used by validate_article.py.
"""

import pathlib
import re
import sys

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
    "journey-art-style.md": {
        "description": "What is the Journey art style? How colour, minimal shapes and hand-painted shadows carry an emotional arc, according to Jenova Chen and Matt Nava.",
        "summary": "A colour script, a red silhouette, and a blue sky saved for the ending.",
        "tags": ["Journey", "Game art direction", "Colour script", "thatgamecompany"],
        "categories": ["Game history"],
    },
    "firewatch-art-style.md": {
        "description": "What is the Firewatch art style? Bold shapes, distinct colour layers, real-world references and a small set of hand-made trees, explained from Jane Ng's talks and interviews.",
        "summary": "A poster as the goal, a colour script as the structure, and 23 trees for the whole forest.",
        "tags": ["Firewatch", "Game art direction", "Colour script", "Campo Santo"],
        "categories": ["Game history"],
    },
    "gris-art-style.md": {
        "description": "What is the GRIS art style? Nomada Studio on colour scripts, mutable character design, and references from Journey, Shadow of the Colossus, Ghibli and Moebius.",
        "summary": "A story carried by colour, statues and a deliberately simple silhouette.",
        "tags": ["GRIS", "Game art direction", "Nomada Studio", "2D animation"],
        "categories": ["Game history"],
    },
    "tf2-art-style.md": {
        "description": "What is the Team Fortress 2 art style? Valve's 2007 paper on illustrative rendering, early 20th-century illustrators, rim highlights and why it is not cel shading.",
        "summary": "An illustrative rendering system built for class readability, not a stepped-lighting shader.",
        "tags": ["Team Fortress 2", "Game art direction", "Illustrative rendering", "Valve"],
        "categories": ["Game history"],
    },
    "how-gris-tells-story-without-dialogue.md": {
        "description": "How does GRIS tell a story without dialogue? Nomada Studio on colour scripts, statues, camera cues and character simplification as narrative tools.",
        "summary": "Colour tracks progression; statues carry exposition; camera cues keep it readable.",
        "tags": ["GRIS", "Visual storytelling", "Game art direction", "Nomada Studio"],
        "categories": ["Game history"],
    },
    "visual-novel-vs-dating-sim.md": {
        "description": "Visual novel vs dating sim: a narrative form versus a romance simulation genre, with the stat, calendar and love-meter boundary explained.",
        "summary": "One label describes story presentation; the other describes relationship simulation.",
        "tags": ["Visual novel", "Dating sim", "Game genres", "Japanese games"],
        "categories": ["Game design", "Visual novel"],
    },
    "kinetic-novel-meaning.md": {
        "description": "What is a kinetic novel? Key's official definition, the 2004 Planetarian origin, and why it means no choices or very few choices.",
        "summary": "No choices or almost none, one fixed story, and a term that began as a Key label.",
        "tags": ["Kinetic novel", "Visual novel", "Planetarian", "Game genres"],
        "categories": ["Game design", "Visual novel"],
    },
    "nvl-vs-adv.md": {
        "description": "NVL vs ADV: two common visual novel text layouts, what the abbreviations mean, and why a single game can mix both modes.",
        "summary": "ADV advances one dialogue unit in a bottom box; NVL stacks several units.",
        "tags": ["NVL", "ADV", "Visual novel UI", "Ren'Py"],
        "categories": ["Game design", "Visual novel"],
    },
    "lost-museum-object-heads.md": {
        "description": "Why does Lost Museum give its characters object heads? The producer explains Chromageists, the refusal to reveal a human form, and building a museum mystery around paintings.",
        "summary": "A museum mystery where the paintings have object-headed spirits, and a deliberate refusal to turn them back into humans.",
        "tags": ["Lost Museum", "Visual novel", "Character design", "Game art direction"],
        "categories": ["Game culture", "Visual novel"],
    },
    "labyrinthos-bad-endings.md": {
        "description": "Developer Astronauts' own survey: over 60% of its players expect bad endings, about 40% hope for pure love stories. Why the studio refuses to drop either.",
        "summary": "A studio asked its own players about bad endings, then refused to choose between them. What the answers actually say.",
        "tags": ["LABYRINTHOS", "Visual novel", "Narrative design", "Astronauts"],
        "categories": ["Game culture", "Visual novel"],
    },
    "schrodingers-call-three-people.md": {
        "description": "How a three-person team built Schrödinger's Call over four years: a custom scripting language, 15-minute music drafts, 10-minute rough visuals, and one scene made together.",
        "summary": "Three people, four years, and a homemade script that times text, effects and sound as one scene.",
        "tags": ["Schrodinger's Call", "Visual novel", "Game development", "Narrative design"],
        "categories": ["Game culture", "Visual novel"],
    },
    "pragmata-fake-ai-new-york.md": {
        "description": "Why does Pragmata have a New York that looks AI-generated? Capcom's developers explain how humans hand-built the taxis-in-the-floor mistakes to make a fake AI city feel uncanny.",
        "summary": "A city that looks like AI slop, painstakingly made by human developers — on purpose.",
        "tags": ["Pragmata", "Capcom", "Game art direction", "AI in games"],
        "categories": ["Game culture", "Game design"],
    },
    "dragon-quest-ai-slimey-friend.md": {
        "description": "Dragon Quest creator Yuji Horii on why DQ10 is getting a Gemini-powered AI Slimey: not an NPC replacement, but a game character players might treat as a friend.",
        "summary": "Horii wants an AI companion that lowers the barrier to talking — and the comments show how split players are.",
        "tags": ["Dragon Quest", "AI in games", "Yuji Horii", "Game design"],
        "categories": ["Game culture", "Game design"],
    },
    "watamari-debanking.md": {
        "description": "How a yuri visual novel was indefinitely delayed when a bank blocked transfers of its Steam revenue over adult-content patches — and why the developer says the paperwork was pointless.",
        "summary": "A sale triggered a money-laundering flag, and a game lost months. A story about payment pipelines, not patches.",
        "tags": ["Watamari", "Visual novel", "Game industry", "Indie development"],
        "categories": ["Game culture", "Game industry"],
    },
    "big-walk-ai-bug-backlash.md": {
        "description": "Big Walk got 400+ negative reviews after disclosing a 10-line AI-assisted bug fix. A story about a tricky IGF edge case, day-by-day Steam review data, and whether honesty gets punished.",
        "summary": "A beloved indie game disclosed minimal AI use — and became the AI debate's most awkward test case.",
        "tags": ["Big Walk", "House House", "AI in games", "Game industry"],
        "categories": ["Game culture", "Game industry"],
    },
    "valkyrie-tune-japanese-aesthetics.md": {
        "description": "Former Idolmaster director Akihiro Ishihara on Valkyrie Tune: a cute visual novel with a philosophical turn, and why he refused to water down its Japanese aesthetics for overseas players.",
        "summary": "Cute girls, dark questions — and a director who thinks overseas players are being underestimated.",
        "tags": ["Valkyrie Tune", "Visual novel", "Idolmaster", "Game design"],
        "categories": ["Game culture", "Visual novel"],
    },
}

FIELDS = [
    "draft: false",
    'author: "Pixel Dango"',
    "lastmod: 2026-11-21T09:00:00+08:00",
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


if __name__ == "__main__":
    names = sys.argv[1:] or list(SPECS)
    for filename in names:
        promote(filename, SPECS[filename])
