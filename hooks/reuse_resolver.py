"""Resolves [REUSE: links/<id>], [REUSE: values/<id>], [REUSE: terms/<id>],
and [REUSE: partners/<path>] markers in page Markdown at build time.

A marker may optionally end in `| alias text` (e.g.
`[REUSE: terms/fair | FAIR principles]`) to override the rendered display
text with author-chosen wording while still resolving the reference (link
href, term lookup, etc.) from the underlying data.
"""
from __future__ import annotations

import re

from hooks.data_store import get_data

_MARKER = re.compile(
    r"\[REUSE:\s*(?P<kind>links|values|terms|partners)/(?P<ref>[^\]|]+?)\s*(?:\|\s*(?P<alias>[^\]]+?)\s*)?\]"
)


def page_language(page) -> str:
    parts = page.file.src_uri.split("/")
    return parts[0] if parts and parts[0] in ("en", "nn") else "en"


def _resolve_link(ref: str, lang: str, alias: str | None = None) -> str:
    entry = get_data()["links"][ref]
    label = alias or entry["label"][lang]
    url = entry["url"]
    url = url[lang] if isinstance(url, dict) else url
    target = ' target="_blank" rel="noopener"' if entry.get("open") == "new-tab" else ""
    return f'<a href="{url}"{target}>{label}</a>'


def _resolve_value(ref: str, lang: str, alias: str | None = None) -> str:
    if alias:
        return alias
    entry = get_data()["values"][ref]
    unit = entry.get("unit", {})
    unit_text = unit.get(lang, "") if isinstance(unit, dict) else (unit or "")
    pattern = entry.get("render", {}).get(lang) if isinstance(entry.get("render"), dict) else None
    if pattern:
        return pattern.format(value=entry["value"], unit=unit_text)
    return f'{entry["value"]} {unit_text}'.strip()


def _resolve_term(ref: str, lang: str, alias: str | None = None) -> str:
    entry = get_data()["terms"][ref]
    return alias or entry["label"][lang]


def _resolve_partner(ref: str, lang: str, alias: str | None = None) -> str:
    if alias:
        return alias
    # ref like "repository_management/support.email" or "<partner-id>/support.url"
    root, *path = ref.split("/")
    data = get_data()["partners"]
    if root == "repository_management":
        node = data["repository_management"]
    else:
        try:
            node = next(p for p in data["partners"] if p["id"] == root)
        except StopIteration:
            raise KeyError(root)  # Raise KeyError for consistent error handling
    for key in path:
        # Split dot-separated paths like "support.email"
        for subkey in key.split("."):
            node = node[subkey]
    if isinstance(node, dict):
        node = node.get(lang, node)
    return str(node)


_RESOLVERS = {
    "links": _resolve_link,
    "values": _resolve_value,
    "terms": _resolve_term,
    "partners": _resolve_partner,
}


def resolve_reuse_markers(markdown: str, lang: str, page_path: str = None) -> str:
    def _replace(match: re.Match) -> str:
        kind, ref, alias = match.group("kind"), match.group("ref"), match.group("alias")
        try:
            return _RESOLVERS[kind](ref, lang, alias)
        except KeyError as e:
            ctx = f"[REUSE: {kind}/{ref}] could not be resolved: {e}"
            if page_path:
                ctx = f"{page_path}: {ctx}"
            raise KeyError(ctx) from e

    return _MARKER.sub(_replace, markdown)


def on_page_markdown(markdown, page, config, files, **kwargs):
    lang = page_language(page)
    return resolve_reuse_markers(markdown, lang, page_path=page.file.src_uri)
