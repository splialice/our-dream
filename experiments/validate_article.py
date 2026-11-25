"""Structural validation for art-style research articles.

Scope: this checks STRUCTURE only. It does NOT verify that a quote is real or
that a source actually supports a claim. That remains a manual fact-check step.

Usage:
    python validate_article.py <article.md> [article2.md ...]
    python validate_article.py --all      # validate every *-art-style.md here

Requires PyYAML (pip install pyyaml).
"""

import pathlib
import re
import sys
from urllib.parse import urlparse

import yaml

BASE = pathlib.Path(__file__).parent

# Independent schema. Do NOT read rules out of the Markdown template —
# editing template prose must never silently change validation behaviour.
SOURCE_TYPES = {
    "developer_document",
    "developer_interview",
    "republished_interview",
    "official_store",
    "contemporary_reporting",
    "retrospective_reporting",
}
CLAIM_USAGES = {
    "direct_quote",
    "paraphrase",
    "reporter_paraphrase",
    "reporter_paraphrase_plus_direct_quote",
    "developer_written_description",
    "absence_in_reviewed_sources",
}
QUOTE_REQUIRED = CLAIM_USAGES - {"absence_in_reviewed_sources"}
REQUIRED_TOP_LEVEL = {
    "title",
    "slug",
    "date",
    "type",
    "primary_keyword",
    "primary_question",
    "answer",
    "evidence_status",
    "primary_sources",
    "claims",
    "last_verified",
}
EVIDENCE_STATUSES = {"verified", "partial", "contested"}
BASE_HEADINGS = [
    "## Short answer",
    "## What it looks like",
    "## What the developers said",
]
FINAL_HEADING = "## Sources and evidence limits"
PROCESS_HEADINGS = {
    "## How it was made",
    "## How the look was developed",
    "## How the visual direction was developed",
}
ISO_DATE = re.compile(r"^\d{4}(-\d{2}-\d{2})?$")


def parse_yaml(text):
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        raise ValueError("no front matter block at start of file")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError("front matter is not a mapping")
    return data, parts[2]


def check_url(value, label, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label}: url is missing or not a string")
        return
    parsed = urlparse(value.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        errors.append(f"{label}: invalid url '{value}'")


def validate_front_matter(fm, errors):
    for key in REQUIRED_TOP_LEVEL:
        if key not in fm or fm[key] in (None, "", [], {}):
            errors.append(f"front matter: missing or empty '{key}'")
    if fm.get("evidence_status") not in EVIDENCE_STATUSES:
        errors.append(f"evidence_status invalid: {fm.get('evidence_status')}")
    for key in ("date", "last_verified"):
        value = fm.get(key)
        if value is not None and not ISO_DATE.match(str(value)):
            errors.append(f"{key}: expected ISO date, got '{value}'")
    for key in ("title", "slug", "primary_keyword", "primary_question", "answer"):
        value = fm.get(key)
        if value is not None and not isinstance(value, str):
            errors.append(f"{key}: expected a string")


def validate_sources(sources, errors):
    if not isinstance(sources, list) or not sources:
        errors.append("primary_sources: must be a non-empty list")
        return {}
    by_id = {}
    dates = []
    for i, source in enumerate(sources):
        label = f"source[{i}]"
        if not isinstance(source, dict):
            errors.append(f"{label}: not a mapping")
            continue
        sid = source.get("id")
        if not isinstance(sid, str) or not sid:
            errors.append(f"{label}: missing id")
        elif sid in by_id:
            errors.append(f"{label}: duplicate id '{sid}'")
        else:
            by_id[sid] = source
        for key in ("title", "author", "published", "source_type"):
            if not source.get(key):
                errors.append(f"{label}: missing '{key}'")
        if source.get("source_type") not in SOURCE_TYPES:
            errors.append(f"{label}: unknown source_type '{source.get('source_type')}'")
        published = str(source.get("published", ""))
        if published:
            if not ISO_DATE.match(published):
                errors.append(f"{label}: published not ISO date '{published}'")
            dates.append(published)
        check_url(source.get("url"), label, errors)
    if dates and dates != sorted(dates):
        errors.append(f"primary_sources not date-sorted: {dates}")
    return by_id


def validate_claims(claims, source_ids, errors):
    if not isinstance(claims, list) or not claims:
        errors.append("claims: must be a non-empty list")
        return 0
    seen_statements = set()
    for i, claim in enumerate(claims):
        label = f"claim[{i}]"
        if not isinstance(claim, dict):
            errors.append(f"{label}: not a mapping")
            continue
        statement = claim.get("statement")
        usage = claim.get("claim_usage")
        if not isinstance(statement, str) or not statement.strip():
            errors.append(f"{label}: statement missing or empty")
        else:
            if statement in seen_statements:
                errors.append(f"{label}: duplicate statement")
            seen_statements.add(statement)
        if usage not in CLAIM_USAGES:
            errors.append(f"{label}: unknown claim_usage '{usage}'")
            continue
        if usage == "absence_in_reviewed_sources":
            ids = claim.get("reviewed_source_ids")
            if not isinstance(ids, list) or not ids:
                errors.append(f"{label}: absence claim needs reviewed_source_ids")
            else:
                bad = set(ids) - source_ids
                if bad:
                    errors.append(f"{label}: unknown reviewed_source_ids {bad}")
            if claim.get("source_id"):
                errors.append(f"{label}: absence claim must not use single source_id")
        else:
            sid = claim.get("source_id")
            if sid not in source_ids:
                errors.append(f"{label}: unknown source_id '{sid}'")
            if usage in QUOTE_REQUIRED:
                quote = claim.get("supporting_quote")
                if not isinstance(quote, str) or not quote.strip():
                    errors.append(f"{label}: supporting_quote missing or empty")
                raw = claim.get("quote_raw")
                if raw is not None and not isinstance(raw, str):
                    errors.append(f"{label}: quote_raw must be a string when present")
    return len(claims)


def validate_headings(body, errors):
    headings = re.findall(r"^## .+$", body, flags=re.M)
    for h in BASE_HEADINGS:
        if h not in headings:
            errors.append(f"missing heading: {h}")
    if FINAL_HEADING not in headings:
        errors.append(f"missing heading: {FINAL_HEADING}")
    process = [h for h in headings if h in PROCESS_HEADINGS]
    if len(process) != 1:
        errors.append(f"need exactly one process heading from {sorted(PROCESS_HEADINGS)}, got {process}")
    order = [h for h in headings if h in set(BASE_HEADINGS) | PROCESS_HEADINGS | {FINAL_HEADING}]
    if order and order[0] != "## Short answer":
        errors.append("Short answer must be the first section")

    match = re.search(r"^## Short answer\s*\n\n(.*?)(?=\n## )", body, flags=re.M | re.S)
    if not match:
        errors.append("Short answer section has no body")
        return
    text = match.group(1).strip()
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s]
    words = len(text.split())
    if not (2 <= len(sentences) <= 4):
        errors.append(f"Short answer has {len(sentences)} sentences (want 2-4)")
    if words > 100:
        errors.append(f"Short answer has {words} words (max 100)")
    print(f"  Short answer: {len(sentences)} sentences, {words} words")


def validate_article(path):
    print(f"[{path.name}]")
    errors = []
    try:
        text = path.read_text(encoding="utf-8")
        fm, body = parse_yaml(text)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"  PARSE ERROR: {exc}")
        return 1

    validate_front_matter(fm, errors)
    source_ids_map = validate_sources(fm.get("primary_sources"), errors)
    claim_count = validate_claims(fm.get("claims"), set(source_ids_map), errors)
    validate_headings(body, errors)

    answer = fm.get("answer")
    if isinstance(answer, str):
        answer_words = len(answer.split())
        if answer_words > 100:
            errors.append(f"answer field has {answer_words} words (max 100)")

    print(f"  sources={len(source_ids_map)} claims={claim_count} errors={len(errors)}")
    for err in errors:
        print(f"  ERROR: {err}")
    return 1 if errors else 0


def main():
    args = sys.argv[1:]
    if not args or args == ["--all"]:
        files = sorted(BASE.glob("*-art-style.md"))
    else:
        files = [pathlib.Path(a) for a in args]
    if not files:
        print("no article files found")
        return 1
    return 1 if any(validate_article(f) for f in files) else 0


if __name__ == "__main__":
    raise SystemExit(main())
