"""Resolves [REUSE: links/<id>], [REUSE: values/<id>], [REUSE: terms/<id>],
and [REUSE: partners/<path>] markers in page Markdown at build time.

A marker may optionally end in `| alias text` (e.g.
`[REUSE: terms/fair | FAIR principles]`) to override the rendered display
text with author-chosen wording while still resolving the reference (link
href, term lookup, etc.) from the underlying data.
"""
from __future__ import annotations

import re
from pathlib import PurePosixPath

from hooks.data_store import get_data

_MARKER = re.compile(
    r"\[REUSE:\s*(?P<kind>links|values|terms|partners)/(?P<ref>[^\]|]+?)\s*(?:\|\s*(?P<alias>[^\]]+?)\s*)?\]"
)

# [PAGE: <path>[#anchor] [| <label>]] — cross-page reference (spec §5.4.1).
# <path> is tried, in order: relative to the current page's own directory
# (covers both same-dir siblings like "prepare-your-data" and nested paths
# like "file-formats/index" written by an author already inside deposit/),
# then relative to the current page's language root as a direct file, then
# as a section index (covers bare "deposit" meaning deposit/index.md).
_PAGE_MARKER = re.compile(r"\[PAGE:\s*(?P<ref>[^|\]]+?)(?:\s*\|\s*(?P<label>[^\]]+))?\]")


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


def resolve_target_href(target: str, lang: str, files, current_file) -> str:
    """Resolve a bare page target (e.g. "prepare-your-data", "file-formats/index",
    or "publish-your-data#some-anchor") into a relative href, using the same
    candidate resolution as [PAGE: ...] markers. Shared by [PAGE: ...] and by
    the Target: field of content-component blocks ([BUTTON], [NAVIGATION CARD],
    [RESOURCE BOX], [WORKFLOW] steps).
    """
    path, _, anchor = target.partition("#")
    path, anchor = path.strip(), anchor.strip()
    current_dir = PurePosixPath(current_file.src_uri).parent.as_posix()
    candidates = [f"{current_dir}/{path}.md", f"{lang}/{path}.md", f"{lang}/{path}/index.md"]

    target_file = next((f for f in (files.get_file_from_path(c) for c in candidates) if f), None)
    if target_file is None:
        raise KeyError(f"target '{target}' not found for lang '{lang}' (tried {candidates})")

    href = target_file.url_relative_to(current_file)
    if anchor:
        href += f"#{anchor}"
    return href


def resolve_page_markers(markdown: str, lang: str, files, current_file) -> str:
    """Resolve [PAGE: ...] markers into real <a> links using mkdocs' own
    Files collection, so hrefs match the relative-URL convention the rest of
    the built site already uses (theme nav, footer, etc).

    `files` is the mkdocs Files collection for the current build; `current_file`
    is the File the markers are being resolved for (used both to compute a
    same-directory fallback for slash-less <path> and to make the href
    relative to it).
    """

    def _replace(match: re.Match) -> str:
        ref = match.group("ref").strip()
        label = (match.group("label") or ref).strip()
        try:
            href = resolve_target_href(ref, lang, files, current_file)
        except KeyError as e:
            raise KeyError(f"[PAGE: {ref}] {e}") from e
        return f'<a href="{href}">{label}</a>'

    return _PAGE_MARKER.sub(_replace, markdown)


def on_page_markdown(markdown, page, config, files, **kwargs):
    lang = page_language(page)
    markdown = resolve_reuse_markers(markdown, lang, page_path=page.file.src_uri)
    markdown = resolve_page_markers(markdown, lang, files, page.file)
    return markdown
