#!/usr/bin/env python3
"""Validates that docs/en and docs/nn have parallel page structures,
and that all [REUSE: ...] references resolve against data/*.yml.
Run before `mkdocs build` (source-tree check, not a built-site check).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

# Mirrors hooks/reuse_resolver.py's _MARKER regex: ref stops at "|" so an
# alias suffix like "[REUSE: terms/fair | FAIR principles]" doesn't get
# folded into the id being checked against data/*.yml.
REUSE_PATTERN = re.compile(
    r"\[REUSE:\s*(?P<kind>links|values|terms|partners)/(?P<ref>[^\]|]+?)\s*(?:\|[^\]]*)?\]"
)


def relative_md_paths(root: Path) -> set[str]:
    # as_posix(): rglob paths are backslash-joined on Windows, which would
    # break the "news/posts" prefix check below.
    return {p.relative_to(root).as_posix() for p in root.rglob("*.md")}


def check_language_parity() -> list[str]:
    en_root, nn_root = Path("docs/en"), Path("docs/nn")
    en_paths, nn_paths = relative_md_paths(en_root), relative_md_paths(nn_root)
    # news/ posts are allowed to diverge (dated, independently authored)
    en_paths = {p for p in en_paths if not p.startswith("news/posts")}
    nn_paths = {p for p in nn_paths if not p.startswith("news/posts")}
    missing_in_nn = sorted(en_paths - nn_paths)
    missing_in_en = sorted(nn_paths - en_paths)
    errors = [f"Missing in docs/nn: {p}" for p in missing_in_nn]
    errors += [f"Missing in docs/en: {p}" for p in missing_in_en]
    return errors


def load_data_ids() -> dict[str, set[str]]:
    ids: dict[str, set[str]] = {}
    for kind, filename, top_key in (
        ("links", "links.yml", "links"),
        ("values", "values.yml", "values"),
        ("terms", "terms.yml", "terms"),
    ):
        raw = yaml.safe_load(Path("data", filename).read_text(encoding="utf-8")) or {}
        ids[kind] = set((raw.get(top_key) or {}).keys())
    partners_raw = yaml.safe_load(Path("data/partners.yml").read_text(encoding="utf-8")) or {}
    partner_ids = {p["id"] for p in partners_raw.get("partners", [])}
    partner_ids.add(partners_raw.get("repository_management", {}).get("id", "dataverseno"))
    ids["partners"] = partner_ids
    return ids


def check_reuse_references() -> list[str]:
    ids = load_data_ids()
    errors = []
    for md_file in list(Path("docs/en").rglob("*.md")) + list(Path("docs/nn").rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        for match in REUSE_PATTERN.finditer(text):
            kind, ref = match.group("kind"), match.group("ref").strip()
            root_id = ref.split("/")[0] if kind == "partners" else ref
            if kind == "partners" and root_id == "repository_management":
                root_id = "dataverseno"
            if root_id not in ids[kind]:
                errors.append(f"{md_file}: unresolved [REUSE: {kind}/{ref}]")
    return errors


def main() -> int:
    errors = check_language_parity() + check_reuse_references()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"\n{len(errors)} validation error(s)", file=sys.stderr)
        return 1
    print("Language parity and [REUSE: ...] references OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
