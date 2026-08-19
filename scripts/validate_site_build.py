"""Fails if the built site still contains unresolved content markers, or has
internal links (nav, footer, glossary, [SECTION: ...]/[PAGE: ...] output,
prose links, ...) that don't resolve to a real page/file/anchor within the
built site. Run after `mkdocs build`.
"""
from __future__ import annotations

import posixpath
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

MARKER_PATTERNS = [
    re.compile(r"\[REUSE:"),
    re.compile(r"\[GENERATED COMPONENT\]"),
    re.compile(r"<!-- PEOPLE_(SEARCH_AND_FILTER|CARDS): "),
    re.compile(r"<!-- GLOSSARY_TERMS: "),
    re.compile(r"\[PAGE:"),
    re.compile(r"\[SECTION:"),
    re.compile(r"\[GENERATED VALUE"),
    re.compile(r"\[ADMONITION\]"),
    re.compile(r"\[BUTTON\]"),
    re.compile(r"\[NAVIGATION CARD\]"),
    re.compile(r"\[RESOURCE BOX"),
    re.compile(r"\[CARD GRID\]"),
    re.compile(r"\[WORKFLOW\]"),
    re.compile(r"\[CHECKLIST\]"),
    re.compile(r"^\[ \] ", re.MULTILINE),
]

_SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "javascript:", "data:")


def check_markers(site_dir: Path) -> list[str]:
    failures = []
    for html_file in site_dir.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8")
        for pattern in MARKER_PATTERNS:
            if pattern.search(text):
                failures.append(f"{html_file}: unresolved marker matching {pattern.pattern!r}")
    return failures


class _LinkCollector(HTMLParser):
    """Collects every element id= (anchor target) and every <a href=>."""

    def __init__(self):
        super().__init__()
        self.ids: set[str] = set()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])


def _site_url_base_path() -> str:
    """The path component of mkdocs.yml's site_url (e.g. "/DataverseNO-Info"
    when deployed as a GitHub Pages project site, "" for a domain root).
    mkdocs-static-i18n's language-switch links (and other absolute-path
    output) are built with exactly this prefix, so absolute hrefs in the
    built site carry it too — strip it back off before resolving against
    site/'s own on-disk paths, which never include it themselves.
    Regex, not yaml.safe_load: mkdocs.yml uses `!!python/...` tags that
    aren't safe-loadable, and a single top-level scalar isn't worth a
    hand-rolled tag constructor.
    """
    match = re.search(r"^site_url:\s*(\S+)", Path("mkdocs.yml").read_text(encoding="utf-8"), re.MULTILINE)
    return urlsplit(match.group(1)).path.rstrip("/") if match else ""


def _resolve_target_path(href: str, page_url: str, base_path: str = "") -> str:
    """Resolve an href (relative or site-root-absolute) against the URL of
    the page it appears on, into a site-relative file path — matching how
    MkDocs' "pretty" directory URLs actually lay out files on disk (a link
    to "foo/" or "foo" means the file foo/index.html).
    """
    if base_path and href.startswith(base_path + "/"):
        href = href[len(base_path):]
    path = href if href.startswith("/") else posixpath.join(posixpath.dirname(page_url), href)
    path = posixpath.normpath(path).strip("/")
    if not path or path == ".":
        return "index.html"
    if "." in posixpath.basename(path):
        return path  # already a concrete file (index.html, foo.png, foo.pdf, ...)
    return f"{path}/index.html"


def check_internal_links(site_dir: Path) -> list[str]:
    base_path = _site_url_base_path()
    html_files = sorted(site_dir.rglob("*.html"))
    all_paths = {p.relative_to(site_dir).as_posix() for p in site_dir.rglob("*") if p.is_file()}

    ids_by_page: dict[str, set[str]] = {}
    hrefs_by_page: dict[str, list[str]] = {}
    for html_file in html_files:
        page_url = html_file.relative_to(site_dir).as_posix()
        collector = _LinkCollector()
        collector.feed(html_file.read_text(encoding="utf-8"))
        ids_by_page[page_url] = collector.ids
        hrefs_by_page[page_url] = collector.hrefs

    errors = []
    for page_url, hrefs in hrefs_by_page.items():
        for href in hrefs:
            if not href or href.startswith(_SKIP_SCHEMES):
                continue
            path, _, fragment = href.partition("#")
            if not path:
                # Same-page anchor, e.g. output of [SECTION: ...].
                if fragment and fragment not in ids_by_page[page_url]:
                    errors.append(f"{page_url}: broken same-page anchor '#{fragment}' in link '{href}'")
                continue
            target = _resolve_target_path(path, page_url, base_path)
            if target in ids_by_page:
                if fragment and fragment not in ids_by_page[target]:
                    errors.append(f"{page_url}: link '{href}' -> {target} has no element with id '{fragment}'")
            elif target not in all_paths:
                errors.append(f"{page_url}: broken internal link '{href}' (resolved to '{target}')")
    return errors


def main() -> int:
    site_dir = Path("site")
    if not site_dir.exists():
        print("site/ not found — run `mkdocs build` first", file=sys.stderr)
        return 1
    failures = check_markers(site_dir) + check_internal_links(site_dir)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        print(f"\n{len(failures)} unresolved marker(s)/broken link(s) found", file=sys.stderr)
        return 1
    print("No unresolved content markers or broken internal links found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
