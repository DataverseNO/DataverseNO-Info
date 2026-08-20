"""Localizes header/sidebar nav titles per language.

mkdocs.yml's `nav:` block gives every entry an explicit English title
("About", "Deposit Guidelines", "What is DataverseNO?", ...). Explicit nav
titles are literal strings, not derived from page content, so
mkdocs-static-i18n's per-locale rebuild swaps in the nn/ source files but
leaves these labels in English — confirmed live (nav bar stays English after
switching to Nynorsk).

Every content page under docs/{en,nn}/ already carries a `nav_label` front
matter field with the correct localized label (added during migration but
never consumed). This hook overwrites each nav item's title with its page's
`nav_label` at build time, once per locale pass, so the fix is data-driven
off content already in the repo instead of a second, easily-drifting
translation table in mkdocs.yml.

Section items (e.g. "About") have no page of their own — their title in
this nav is always taken from their first, implicitly-titled child (the
section's own index.md), which is itself always given an explicit
`nav_label` for exactly this purpose (e.g. docs/en/about/index.md ->
"About", docs/nn/about/index.md -> "Om").
"""
from __future__ import annotations

import re

from mkdocs.structure.nav import Section
from mkdocs.structure.pages import Page

import yaml

_FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?\n)---\s*\n", re.DOTALL)


def _read_nav_label(abs_src_path: str) -> str | None:
    with open(abs_src_path, "r", encoding="utf-8") as fh:
        head = fh.read(4000)
    match = _FRONT_MATTER_RE.match(head)
    if not match:
        return None
    meta = yaml.safe_load(match.group(1)) or {}
    label = meta.get("nav_label")
    return label if isinstance(label, str) else None


def _localize(items) -> None:
    for item in items:
        if isinstance(item, Page) and item.title and item.file is not None:
            label = _read_nav_label(item.file.abs_src_path)
            if label:
                item.title = label
        elif isinstance(item, Section) and item.children:
            first_child = item.children[0]
            if isinstance(first_child, Page) and first_child.file is not None:
                label = _read_nav_label(first_child.file.abs_src_path)
                if label:
                    item.title = label
            _localize(item.children)


def on_nav(nav, config, files, **kwargs):
    _localize(nav.items)
    return nav
