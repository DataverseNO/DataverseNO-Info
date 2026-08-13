"""Fails if the built site still contains unresolved content markers.
Run after `mkdocs build`.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

MARKER_PATTERNS = [
    re.compile(r"\[REUSE:"),
    re.compile(r"\[GENERATED COMPONENT\]"),
    re.compile(r"<!-- PEOPLE_(SEARCH_AND_FILTER|CARDS): "),
    re.compile(r"<!-- GLOSSARY_TERMS: "),
]


def main() -> int:
    site_dir = Path("site")
    if not site_dir.exists():
        print("site/ not found — run `mkdocs build` first", file=sys.stderr)
        return 1
    failures = []
    for html_file in site_dir.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8")
        for pattern in MARKER_PATTERNS:
            if pattern.search(text):
                failures.append(f"{html_file}: unresolved marker matching {pattern.pattern!r}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        print(f"\n{len(failures)} unresolved marker(s) found", file=sys.stderr)
        return 1
    print("No unresolved content markers found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
