"""Renders spec section 9 content-component markers into HTML/Markdown at
build time: [ADMONITION], [BUTTON], [NAVIGATION CARD], [RESOURCE BOX],
[WORKFLOW], [CHECKLIST] items, [SECTION: ...] same-page links, and
[GENERATED VALUE: ...] inline values.

[CARD GRID] / [RESOURCE BOX GRID] header lines are dropped without a
wrapping element — .navigation-card/.resource-card lay out into a row-
wrapping grid via CSS on the cards themselves, so no container is needed.

ponytail: Icon: fields are dropped, not rendered as graphics — no icon
library is wired up yet (spec only requires the CSS class per component,
not a specific icon set). Add icon rendering here if a set gets chosen.
"""
from __future__ import annotations

import re

from hooks.data_store import get_data
from hooks.html_safety import escape, safe_href
from hooks.reuse_resolver import page_language, resolve_target_href

_FIELD_LINE = r"[A-Za-z][A-Za-z0-9 ]*:.*\n"

_LEAF_BLOCK = re.compile(
    rf"\[(?P<type>ADMONITION|BUTTON|NAVIGATION CARD|RESOURCE BOX)\]\n(?P<fields>(?:{_FIELD_LINE})+)"
)
_WORKFLOW_BLOCK = re.compile(rf"\[WORKFLOW\]\n(?P<fields>(?:{_FIELD_LINE})+)")

_GRID_HEADER = re.compile(r"\[(?:CARD GRID|RESOURCE BOX GRID)\]\n")
# A [CARD GRID] whose body is a bare list of ids (no [NAVIGATION CARD]/[RESOURCE
# BOX] sub-blocks) is a "fallback if not auto-generated" block that migration
# left behind next to a [GENERATED COMPONENT] — once that component renders
# for real, the fallback text is redundant and is dropped here.
_ORPHAN_ID_LIST_GRID = re.compile(r"\[CARD GRID\]\n(?:[a-z0-9-]+\n)+")

_CHECKLIST_HEADER = re.compile(r"\[CHECKLIST\]\n(?:Migration note:.*\n)?")
_CHECKLIST_ITEM = re.compile(r"^\[ \] (.+)$", re.MULTILINE)

_SECTION_MARKER = re.compile(r"\[SECTION:\s*(?P<anchor>[^|\]]+?)\s*\|\s*(?P<label>[^\]]+)\]")

_GENERATED_VALUE_HEADER = re.compile(rf"\[GENERATED VALUE\]\n(?:{_FIELD_LINE})+")
_GENERATED_VALUE_INLINE = re.compile(r"\[GENERATED VALUE:\s*(?P<id>[\w-]+)\]")

_ADMONITION_STYLE = {"primary": "note", "secondary": "tip", "tertiary": "abstract"}


def _parse_fields(fields_text: str) -> dict:
    fields = {}
    for line in fields_text.strip("\n").split("\n"):
        key, _, value = line.partition(":")
        value = value.strip()
        if value.upper() == "NONE":  # migration placeholder for "field intentionally absent"
            value = ""
        fields[key.strip()] = value
    return fields


def _href_or_none(fields: dict, lang: str, files, current_file) -> tuple[str | None, str]:
    """Resolve a block's Target/URL/Open fields to (href, extra_attrs).
    Returns (None, "") for an explicitly unresolved "Target: [pending]"
    placeholder (per PENDING_ITEMS: do not invent a URL for these).
    """
    url = fields.get("URL")
    if url:
        extra = ' target="_blank" rel="noopener"' if fields.get("Open") == "new-tab" else ""
        return escape(safe_href(url)), extra
    target = fields.get("Target")
    if target and target != "[pending]":
        if "/" not in target and "#" not in target:
            # Bare slug with no path separator: try it as another page first
            # (e.g. "prepare-your-data"), falling back to a same-page heading
            # anchor (e.g. "sharing-data-in-dataverseno" on this very page).
            try:
                return escape(resolve_target_href(target, lang, files, current_file)), ""
            except KeyError:
                return f"#{escape(target)}", ""
        return escape(resolve_target_href(target, lang, files, current_file)), ""
    return None, ""


def _render_admonition(fields, lang, files, current_file) -> str:
    style = _ADMONITION_STYLE.get(fields.get("Style"), "note")
    title = fields.get("Title", "").replace('"', "'")  # admonition title is a quoted string literal
    text = fields.get("Text", "")
    return f'!!! {style} "{title}"\n    {text}\n'


def _render_button(fields, lang, files, current_file) -> str:
    href, extra = _href_or_none(fields, lang, files, current_file)
    style = escape(fields.get("Style", "primary"))
    title = escape(fields.get("Title", ""))
    if href is None:
        return f'<span class="dvno-button dvno-button--{style} dvno-button--pending">{title}</span>'
    return f'<a class="dvno-button dvno-button--{style}" href="{href}"{extra}>{title}</a>'


def _render_navigation_card(fields, lang, files, current_file) -> str:
    href, extra = _href_or_none(fields, lang, files, current_file)
    title = escape(fields.get("Title", ""))
    description = escape(fields.get("Description", ""))
    accent = escape(fields.get("Accent Text", ""))
    body = f'<span class="navigation-card__accent">{accent}</span>' if accent else ""
    body += f'<span class="navigation-card__title">{title}</span>'
    if description:
        body += f'<span class="navigation-card__description">{description}</span>'
    if href is None:
        return f'<div class="navigation-card navigation-card--pending">{body}</div>'
    return f'<a class="navigation-card" href="{href}"{extra}>{body}</a>'


def _render_resource_box(fields, lang, files, current_file) -> str:
    href, extra = _href_or_none(fields, lang, files, current_file)
    title = escape(fields.get("Title", ""))
    if href is None:
        return f'<span class="resource-card resource-card--pending">{title}</span>'
    return f'<a class="resource-card" href="{href}"{extra}>{title}</a>'


_LEAF_RENDERERS = {
    "ADMONITION": _render_admonition,
    "BUTTON": _render_button,
    "NAVIGATION CARD": _render_navigation_card,
    "RESOURCE BOX": _render_resource_box,
}


def _render_workflow(fields_text: str, lang, files, current_file) -> str:
    steps = []
    current: dict = {}
    for line in fields_text.strip("\n").split("\n"):
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if key.startswith("Step"):
            if current:
                steps.append(current)
            current = {}
        else:
            current[key] = value
    if current:
        steps.append(current)

    items = []
    for step in steps:
        href, extra = _href_or_none(step, lang, files, current_file)
        style = escape(step.get("Style", "primary"))
        inner = (
            f'<span class="workflow-step__number">{escape(step.get("Number", ""))}</span>'
            f'<span class="workflow-step__title">{escape(step.get("Title", ""))}</span>'
        )
        content = f'<a href="{href}"{extra}>{inner}</a>' if href else f"<span>{inner}</span>"
        items.append(f'<li class="workflow-step workflow-step--{style}">{content}</li>')
    return '<ol class="workflow">\n' + "\n".join(items) + "\n</ol>"


_GENERATED_VALUES = {
    "partner-institution-count": lambda: str(len(get_data()["partners"]["partners"])),
}


def resolve_content_blocks(markdown: str, lang: str, files, current_file) -> str:
    # MkDocs strips the page source's trailing newline before this hook runs.
    # _FIELD_LINE requires each field to end in "\n", so a block whose last
    # field is also the file's last line would otherwise fall outside every
    # regex match here (field silently dropped, block left half-resolved).
    if not markdown.endswith("\n"):
        markdown += "\n"
    markdown = _ORPHAN_ID_LIST_GRID.sub("", markdown)
    markdown = _GRID_HEADER.sub("", markdown)
    markdown = _CHECKLIST_HEADER.sub("", markdown)
    markdown = _CHECKLIST_ITEM.sub(r'<p class="checklist-item"><input type="checkbox" disabled> \1</p>', markdown)
    markdown = _SECTION_MARKER.sub(
        lambda m: f'<a href="#{escape(m.group("anchor").strip())}">{escape(m.group("label").strip())}</a>', markdown
    )
    markdown = _GENERATED_VALUE_HEADER.sub("", markdown)
    markdown = _GENERATED_VALUE_INLINE.sub(lambda m: _GENERATED_VALUES[m.group("id")](), markdown)

    def _replace_leaf(match: re.Match) -> str:
        fields = _parse_fields(match.group("fields"))
        return _LEAF_RENDERERS[match.group("type")](fields, lang, files, current_file)

    markdown = _LEAF_BLOCK.sub(_replace_leaf, markdown)
    markdown = _WORKFLOW_BLOCK.sub(lambda m: _render_workflow(m.group("fields"), lang, files, current_file), markdown)
    return markdown


def on_page_markdown(markdown, page, config, files, **kwargs):
    lang = page_language(page)
    return resolve_content_blocks(markdown, lang, files, page.file)
