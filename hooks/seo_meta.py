"""Maps custom front matter (seo_title, seo_description, canonical_url)
onto page title/meta description/canonical link, since mkdocs-material's
defaults only read `title`/`description`.
"""
from __future__ import annotations


def on_page_context(context, page, config, nav, **kwargs):
    meta = page.meta
    if meta.get("seo_description"):
        page.meta["description"] = meta["seo_description"]
    return context
