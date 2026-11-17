"""Validate the evidence structure in the art-style sample.
Prototype for the future experiment-site build check.
"""

import pathlib
import re
import sys

BASE = pathlib.Path(__file__).parent
SAMPLE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "cuphead-art-style.md"
TEMPLATE = BASE / "ART-STYLE-TEMPLATE.md"

QUOTE_REQUIRED = {
    "direct_quote",
    "paraphrase",
    "reporter_paraphrase_plus_direct_quote",
    "developer_written_description",
}
SOURCE_TYPES = {
    "developer_document",
    "developer_interview",
    "official_store",
    "contemporary_reporting",
    "retrospective_reporting",
}
HEADINGS = [
    "## Short answer",
    "## What it looks like",
    "## What the developers said",
    "## How it was made",
    "## Sources and evidence limits",
]


def parse_front_matter(text):
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("front matter not found")
    return parts[1], parts[2]


def block_lines(fm, key, next_key=None):
    lines = fm.splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip() == f"{key}:")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^\S", lines[i]):
            end = i
            break
    return lines[start + 1 : end]


def quoted(line, key):
    m = re.search(rf"\b{key}:\s*\"([^\"]+)\"", line)
    return m.group(1) if m else None


errors = []
sample = SAMPLE.read_text(encoding="utf-8")
fm, body = parse_front_matter(sample)

source_lines = block_lines(fm, "primary_sources", "claims")
source_ids = [quoted(l, "id") for l in source_lines if "id:" in l]
published = [quoted(l, "published") for l in source_lines if "published:" in l]
source_types = [quoted(l, "source_type") for l in source_lines if "source_type:" in l]

if not (len(source_ids) == len(published) == len(source_types)):
    errors.append("primary_sources: id/published/source_type counts differ")
if set(source_types) - SOURCE_TYPES:
    errors.append(f"unknown source_type: {set(source_types) - SOURCE_TYPES}")
if published != sorted(published):
    errors.append(f"primary_sources not date-sorted: {published}")

claim_lines = block_lines(fm, "claims", "last_verified")
claim_blocks = []
current = []
for line in claim_lines:
    if re.match(r"^\s+- statement:", line):
        if current:
            claim_blocks.append("\n".join(current))
        current = [line]
    elif current:
        current.append(line)
if current:
    claim_blocks.append("\n".join(current))

for block in claim_blocks:
    statement = quoted(block, "statement")
    usage = quoted(block, "claim_usage")
    if not statement or not usage:
        errors.append("claim missing statement or claim_usage")
        continue
    if usage == "absence_in_reviewed_sources":
        ids_block = re.search(r"reviewed_source_ids:\s*\[([^\]]*)\]", block)
        ids = set(re.findall(r"\"([^\"]+)\"", ids_block.group(1))) if ids_block else set()
        if not ids or ids - set(source_ids):
            errors.append(f"absence claim has invalid reviewed_source_ids: {ids}")
    else:
        source_ref = quoted(block, "source_id")
        if source_ref not in source_ids:
            errors.append(f"claim has invalid source_id: {statement[:40]}")
        if usage in QUOTE_REQUIRED and "supporting_quote:" not in block:
            errors.append(f"claim missing supporting_quote: {statement[:40]}")

for heading in HEADINGS:
    if heading not in body:
        errors.append(f"missing heading: {heading}")

sa = re.search(r"## Short answer\n\n(.*?)\n\n", body, re.S)
if sa:
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", sa.group(1).strip()) if s]
    words = len(sa.group(1).split())
    if not (2 <= len(sentences) <= 4):
        errors.append(f"Short answer has {len(sentences)} sentences (want 2-4)")
    if words > 100:
        errors.append(f"Short answer has {words} words (max 100)")
    print(f"Short answer: {len(sentences)} sentences, {words} words")
else:
    errors.append("Short answer section body not found")

tmpl = TEMPLATE.read_text(encoding="utf-8")
for token in ["supporting_quote", "reviewed_source_ids", "v2.1", "不超过 100"]:
    if token not in tmpl:
        errors.append(f"template missing v2.1 token: {token}")

print(f"sources={len(source_ids)} claims={len(claim_blocks)} errors={len(errors)}")
for e in errors:
    print("ERROR:", e)
raise SystemExit(bool(errors))
