"""Shared HTML-safety helpers for hooks that build raw HTML fragments from
editor-maintained data (data/*.yml, page front matter, [BUTTON]/[NAVIGATION
CARD]/etc. content blocks) rather than from markdown prose, which the
markdown parser escapes on its own. Plain-text values (names, titles, email
addresses, search-index strings) must not be interpolated into HTML/attributes
unescaped, and href/src values sourced from data must not carry a dangerous
URL scheme (javascript:, data:, ...).
"""
from __future__ import annotations

import html

_SAFE_URL_PREFIXES = ("http://", "https://", "mailto:", "/", "#", "./", "../")


def escape(value) -> str:
    return html.escape(str(value), quote=True)


def safe_href(url: str) -> str:
    """Reject dangerous URL schemes in hrefs/srcs built from editor-maintained
    data. Relative paths and http(s)/mailto links pass through unchanged.
    Raises ValueError (fail loud, like the rest of this build's resolvers)
    rather than silently dropping or neutering the link.
    """
    stripped = url.strip()
    if stripped.lower().startswith(_SAFE_URL_PREFIXES):
        return url
    # A bare relative path/slug (e.g. "prepare-your-data") has no scheme at
    # all — only reject if there's a "scheme:" before the first "/".
    if ":" not in stripped.split("/", 1)[0]:
        return url
    raise ValueError(f"unsafe URL scheme in href/src: {url!r}")
