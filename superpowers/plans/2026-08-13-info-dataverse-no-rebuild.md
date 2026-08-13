# info.dataverse.no Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the info.dataverse.no MkDocs site using `context/initial-migration-handover.zip` as the new content/data baseline, replacing the current pilot's `docs/`, adding the `data/`/`scripts/` structured-data layer, and implementing the header/footer/navigation/data-driven-page/glossary architecture required by the technical standard — producing a testable version for Rieke by the week-36 meeting.

**Architecture:** MkDocs + Material theme, unchanged as the platform. Bilingual content lives under `docs/en/` and `docs/nn/` (parallel paths, `mkdocs-static-i18n` folder mode). Structured data (`data/*.yml`) is the single source of truth for partners, people, links, values, terms, and tags — resolved into Markdown at build time via native MkDocs `hooks:` (Python modules, zero new dependency), not a templating plugin. Theme overrides (`overrides/`) implement header/footer/language-switch per the standard; `docs/assets/stylesheets/` and `docs/assets/javascripts/` implement design tokens and progressive-enhancement filtering for People/Contact.

**Tech Stack:** MkDocs 1.6, mkdocs-material 9.5, mkdocs-static-i18n, PyYAML (new), MkDocs native `hooks:` mechanism (no macros plugin), Python 3.12, existing `generate_people_yml.py` / `validate_people_yml.py`.

**Spec:** `context/initial-migration-handover_extracted/source-work/standards/technical-architecture-and-implementation-standard.docx` (extracted text also readable via the zip); companion handover docs `README.md`, `IMPLEMENTATION_NOTES.md`, `PENDING_ITEMS.md`, `MIGRATION_MANIFEST.md`, `CROSS_REFERENCE_REPORT.md` in the same extracted folder.

## Global Constraints

- Do not change page content/prose — that is Rieke's/editorial's job. Only structure, config, code, CSS/JS, and data wiring belong to this plan (per Philipp's email and `IMPLEMENTATION_NOTES.md`).
- English and Norwegian Nynorsk page paths must stay parallel (same filename, same path under `docs/{en,nn}/`) — spec §5.4.
- No dynamic/reusable information may be hard-coded in Markdown when it can resolve from `data/*.yml` — spec §2.4.
- Generated files (`data/people.yml`) must never be hand-edited outside the generation script — spec §6.2.1.
- All generated cards/components must remain visible with JavaScript disabled — spec §6.1.2, §6.2.6, §13.
- Header/footer must not be encoded in page Markdown — spec §8.5, §8.14.
- Design tokens from spec §11.2 are authoritative; WCAG 2.1 AA contrast required — spec §11.1, §13.
- Support README files under `docs/` must be excluded from the public build or replaced with `.gitkeep` — `PENDING_ITEMS.md` item 4.
- Nothing in `PENDING_ITEMS.md` "must resolve before public launch" may be silently invented — flag, don't fabricate (metadata guide link, contact card id, README exclusion, `[REUSE: ...]` validation).

---

## File Structure

```
DataverseNO-Info/
├── docs/                          # REPLACED with handover docs/ (en/, nn/, assets/)
├── data/                          # NEW — copied from handover
│   ├── links.yml / values.yml / terms.yml / partners.yml / tags.yml
│   ├── people.yml
│   └── sources/people.tsv
├── scripts/                       # NEW — copied from handover
│   ├── generate_people_yml.py
│   └── validate_people_yml.py
├── hooks/                         # NEW — build-time content resolution
│   ├── data_store.py              # loads+caches data/*.yml once per build
│   ├── reuse_resolver.py          # resolves [REUSE: links/values/terms/partners/...]
│   └── generated_components.py    # resolves People/Contact/Glossary markers
├── overrides/                     # NEW — Material theme overrides
│   ├── partials/header.html
│   └── partials/footer.html
├── docs/assets/stylesheets/       # dataverseno.css (tokens), contact.css, people.css
├── docs/assets/javascripts/       # people-filter.js (from handover), contact-filter.js (new)
├── scripts/validate_site_build.py # NEW — post-build marker/link self-check
├── .github/workflows/
│   ├── people-data.yml            # from handover, verified against this repo
│   └── deploy.yml                 # MODIFIED — add validation steps before build
├── mkdocs.yml                     # REWRITTEN
└── requirements.txt                # MODIFIED — add PyYAML
```

---

### Task 1: Replace content tree and structured data from handover package

**Files:**
- Delete: `docs/en/admin/`, `docs/nn/admin/` (Admin/Curation section does not exist in the new content model)
- Replace: `docs/en/`, `docs/nn/` with handover's `docs/en/`, `docs/nn/` (from `context/initial-migration-handover_extracted/docs/`)
- Merge: handover `docs/assets/` into `docs/assets/` (icons, images, javascripts, logos, screenshots, stylesheets — keep existing `docs/stylesheets/dataverseno.css` and `extra.css` content, moving them under `docs/assets/stylesheets/` per spec §3.1/§10.1)
- Create: `data/links.yml`, `data/values.yml`, `data/terms.yml`, `data/partners.yml`, `data/tags.yml`, `data/people.yml`, `data/sources/people.tsv` (copied verbatim from handover `data/`)
- Create: `scripts/generate_people_yml.py`, `scripts/validate_people_yml.py` (copied verbatim from handover `scripts/`)
- Create: `.github/workflows/people-data.yml` (copied from handover `.github/workflows/`)
- Modify: `.gitignore` — confirm `site/` (mkdocs build output) is ignored; add nothing else (data/scripts are source, not generated artifacts, per spec §2.5)

**Interfaces:**
- Produces: `docs/{en,nn}/**/*.md` tree matching spec §5.3 exactly (about/, deposit/ incl. file-formats/, news/, contact/, glossary/, includes/)
- Produces: `data/*.yml` files consumed by Task 3 (`hooks/data_store.py`)
- Produces: `docs/assets/stylesheets/`, `docs/assets/javascripts/`, `docs/assets/logos/institutions/{en,nn}/`, `docs/assets/images/people/` consumed by Task 5/6/8

- [ ] **Step 1: Diff old vs new docs tree to confirm nothing outside Admin is silently dropped**

```bash
diff -rq docs/en context/initial-migration-handover_extracted/docs/en
diff -rq docs/nn context/initial-migration-handover_extracted/docs/nn
```
Expected: differences limited to `admin/` (removed), new pages (`people.md`, `glossary/`, `deposit/file-formats/`, `contact/index.md` content), and front-matter/content changes. No unexplained deletions outside `admin/`.

- [ ] **Step 2: Remove the Admin section**

```bash
git rm -r docs/en/admin docs/nn/admin
```

- [ ] **Step 3: Copy handover docs/, data/, scripts/, workflow over**

```bash
cp -r context/initial-migration-handover_extracted/docs/en/* docs/en/
cp -r context/initial-migration-handover_extracted/docs/nn/* docs/nn/
mkdir -p docs/assets
cp -r context/initial-migration-handover_extracted/docs/assets/* docs/assets/
mkdir -p data/sources scripts
cp context/initial-migration-handover_extracted/data/*.yml data/
cp context/initial-migration-handover_extracted/data/sources/people.tsv data/sources/
cp context/initial-migration-handover_extracted/scripts/*.py scripts/
cp context/initial-migration-handover_extracted/.github/workflows/people-data.yml .github/workflows/
```

- [ ] **Step 4: Reconcile existing news posts and stylesheets that aren't in the handover**

The current repo has `docs/en/news/posts/*.md` (real dated news, e.g. `2026-07-09-new-front-page-for-dataverse-no.md`) and `docs/en/news/.authors.yml` that the handover's `docs/en/news/posts/` (older news set) doesn't fully overlap with, and `docs/nn/news/` had no `posts/` before. Compare file lists and keep the union — do not lose existing news content:

```bash
diff <(ls docs/en/news/posts | sort) <(ls context/initial-migration-handover_extracted/docs/en/news/posts | sort)
```
Merge any posts present only in the pre-existing repo back in; restore `docs/en/news/.authors.yml` if it was overwritten.

Move `docs/stylesheets/dataverseno.css` and `docs/stylesheets/extra.css` content into `docs/assets/stylesheets/` (create `dataverseno.css`, `extra.css` there — the handover's `docs/assets/stylesheets/` only contains `people.css`), then remove the now-empty `docs/stylesheets/`.

- [ ] **Step 5: Verify no orphaned references**

```bash
grep -rl "docs/stylesheets/" mkdocs.yml docs/ 2>/dev/null
```
Expected: no output (all references updated to `assets/stylesheets/` in Task 2).

- [ ] **Step 6: Commit**

```bash
git add docs data scripts .github/workflows/people-data.yml .gitignore
git commit -m "content: replace docs tree and add structured data layer from migration handover"
```

---

### Task 2: Rewrite mkdocs.yml for the new nav, theme features, and data hooks

**Files:**
- Modify: `mkdocs.yml` (full rewrite)
- Modify: `requirements.txt` — add `PyYAML==6.0.2` (needed by `hooks/` in Task 3, not currently a direct dependency even though mkdocs pulls it transitively — pin it directly since hooks import it)

**Interfaces:**
- Consumes: `hooks/data_store.py`, `hooks/reuse_resolver.py`, `hooks/generated_components.py` (Task 3) via `hooks:` key
- Consumes: `overrides/` (Task 4) via `theme.custom_dir`
- Produces: nav structure and `docs_dir` that Task 5/6/7 content generation and Task 9 validation assume

- [ ] **Step 1: Write the new mkdocs.yml**

```yaml
site_name: DataverseNO
site_url: https://info.dataverse.no
site_description: Documentation and information about the DataverseNO research data repository
repo_url: https://github.com/DataverseNO/DataverseNO-Info
repo_name: DataverseNO/DataverseNO-Info
edit_uri: edit/main/docs/

docs_dir: docs
hooks:
  - hooks/data_store.py
  - hooks/reuse_resolver.py
  - hooks/generated_components.py

theme:
  name: material
  custom_dir: overrides
  features:
    - navigation.tabs
    - navigation.top
    - toc.follow
    - content.tooltips
    - content.action.edit
  font: false
  palette:
    - scheme: default
      primary: custom
      accent: custom

extra_css:
  - assets/stylesheets/dataverseno.css
  - assets/stylesheets/extra.css
  - assets/stylesheets/people.css
  - assets/stylesheets/contact.css

extra_javascript:
  - assets/javascripts/people-filter.js
  - assets/javascripts/contact-filter.js

markdown_extensions:
  - attr_list
  - md_in_html
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - tables
  - toc:
      permalink: true

plugins:
  - search:
      lang:
        - en
  - i18n:
      docs_structure: folder
      languages:
        - locale: en
          default: true
          name: English
          build: true
        - locale: nn
          name: Norsk (Nynorsk)
          build: true
  - blog:
      blog_dir: en/news
      post_url_format: "{slug}"
  - git-revision-date-localized:
      enable_creation_date: false
      type: date
  - minify:
      minify_html: true

nav:
  - Home: en/index.md
  - About:
    - en/about/index.md
    - What is DataverseNO?: en/about/what-is-dataverseno.md
    - Who can use DataverseNO?: en/about/who-can-use-dataverseno.md
    - Why use DataverseNO?: en/about/why-use-dataverseno.md
    - Policy Framework: en/about/policy-framework.md
    - People: en/about/people.md
    - Glossary: en/glossary/index.md
  - Deposit Guidelines:
    - en/deposit/index.md
    - Quick guide and checklist: en/deposit/deposit-quick-guide.md
    - "Step 1: Prepare your data": en/deposit/prepare-your-data.md
    - "Step 2: Deposit your data": en/deposit/deposit-your-data.md
    - "Step 3: Curation and publishing": en/deposit/publish-your-data.md
    - "Step 4: Refer to your data": en/deposit/refer-to-your-data.md
    - "Step 5: Modify your data": en/deposit/modify-your-data.md
  - News: en/news/index.md
  - Contact: en/contact/index.md
```

Notes on removed/changed items vs the old file:
- Dropped `navigation.sections`, `navigation.breadcrumbs`, `navigation.indexes`, `search.highlight`, `search.suggest` — spec §8.4 explicitly says do not enable sections/expansion/path unless a future decision changes it, and doesn't call for breadcrumbs/indexes. Kept `navigation.tabs`, `toc.follow`; added back-to-top via CSS/JS in Task 4 (Material's `navigation.top` feature is the "Back to top" button — keep it, it was missing from the old config despite spec §8.4 requiring it).
- Dropped the old `nav_translations` block: the i18n plugin's folder-mode default already resolves `docs/nn/...` for the `nn` build, and per spec §8.9/§5.4.1 localized nav labels come from the Nynorsk pages' own front matter/headings, not a translation map maintained in `mkdocs.yml` (avoids the exact "duplicated reusable content" spec §2.4 warns against).
- Removed Admin nav entirely (Task 1).
- Added `edit_uri`/`repo_*` kept from old config (still correct).
- `mkdocs-redirects` was in `requirements.txt` but unused in the old `mkdocs.yml` — leave the dependency in place but do not add a `plugins: redirects` entry unless Task 9 validation finds moved URLs that need one (YAGNI until a real redirect is needed).

- [ ] **Step 2: Add PyYAML to requirements.txt**

```
mkdocs==1.6.1
mkdocs-material==9.5.49
mkdocs-static-i18n==1.2.3
mkdocs-git-revision-date-localized-plugin==1.3.0
mkdocs-redirects==1.2.2
mkdocs-minify-plugin==0.8.0
PyYAML==6.0.2
```

- [ ] **Step 3: Confirm mkdocs.yml is valid YAML before hooks exist**

```bash
python -c "import yaml; yaml.safe_load(open('mkdocs.yml', encoding='utf-8'))" && echo OK
```
Expected: `OK`. (Full `mkdocs build` will fail until Tasks 3–4 exist — that's expected at this point.)

- [ ] **Step 4: Commit**

```bash
git add mkdocs.yml requirements.txt
git commit -m "config: rewrite mkdocs.yml for new nav, theme features, and data hooks"
```

---

### Task 3: Build-time data resolution hooks (`[REUSE: ...]` and language context)

**Files:**
- Create: `hooks/data_store.py`
- Create: `hooks/reuse_resolver.py`
- Test: `scripts/validate_site_build.py` (started here, extended in Task 9)

**Interfaces:**
- Produces: `hooks.data_store.load_data(config) -> dict` — returns `{"links": {...}, "values": {...}, "terms": {...}, "partners": {...}, "tags": {...}, "people": {...}}`, each the parsed contents of the corresponding `data/*.yml` (top-level key stripped, e.g. `links.yml`'s `links:` mapping is stored directly at `data["links"]`)
- Produces: `hooks.data_store.get_data() -> dict` — module-level accessor other hook files call without re-parsing config
- Produces: `hooks.reuse_resolver.page_language(page) -> str` — returns `"en"` or `"nn"` from `page.file.src_uri` (`docs/en/...` / `docs/nn/...`)
- Produces: `hooks.reuse_resolver.resolve_reuse_markers(markdown: str, lang: str) -> str` — replaces all `[REUSE: links/<id>]`, `[REUSE: values/<id>]`, `[REUSE: terms/<id>]`, `[REUSE: partners/<path>]` occurrences
- Consumes (Task 5/6): `hooks.data_store.get_data()`, `hooks.reuse_resolver.page_language()`

- [ ] **Step 1: Write `hooks/data_store.py`**

```python
"""Loads data/*.yml once per build and caches it for other hooks."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

_DATA: dict[str, Any] = {}

_FILES = {
    "links": ("links.yml", "links"),
    "values": ("values.yml", "values"),
    "terms": ("terms.yml", "terms"),
    "partners": ("partners.yml", None),  # top-level keys used directly (repository_management, partners)
    "tags": ("tags.yml", "tags"),
    "people": ("people.yml", None),
}


def on_config(config, **kwargs):
    data_dir = Path(config["docs_dir"]).parent / "data"
    for key, (filename, top_key) in _FILES.items():
        raw = yaml.safe_load((data_dir / filename).read_text(encoding="utf-8")) or {}
        _DATA[key] = raw[top_key] if top_key else raw
    return config


def get_data() -> dict[str, Any]:
    if not _DATA:
        raise RuntimeError("data_store.get_data() called before on_config populated it")
    return _DATA
```

- [ ] **Step 2: Write `hooks/reuse_resolver.py`**

```python
"""Resolves [REUSE: links/<id>], [REUSE: values/<id>], [REUSE: terms/<id>],
and [REUSE: partners/<path>] markers in page Markdown at build time.
"""
from __future__ import annotations

import re

from hooks.data_store import get_data

_MARKER = re.compile(r"\[REUSE:\s*(?P<kind>links|values|terms|partners)/(?P<ref>[^\]]+)\]")


def page_language(page) -> str:
    parts = page.file.src_uri.split("/")
    return parts[0] if parts and parts[0] in ("en", "nn") else "en"


def _resolve_link(ref: str, lang: str) -> str:
    entry = get_data()["links"][ref]
    label = entry["label"][lang]
    url = entry["url"]
    url = url[lang] if isinstance(url, dict) else url
    target = ' target="_blank" rel="noopener"' if entry.get("open") == "new-tab" else ""
    return f'<a href="{url}"{target}>{label}</a>'


def _resolve_value(ref: str, lang: str) -> str:
    entry = get_data()["values"][ref]
    unit = entry.get("unit", {})
    unit_text = unit.get(lang, "") if isinstance(unit, dict) else (unit or "")
    pattern = entry.get("render_pattern", {}).get(lang) if isinstance(entry.get("render_pattern"), dict) else None
    if pattern:
        return pattern.format(value=entry["value"], unit=unit_text)
    return f'{entry["value"]} {unit_text}'.strip()


def _resolve_term(ref: str, lang: str) -> str:
    entry = get_data()["terms"][ref]
    return entry["label"][lang]


def _resolve_partner(ref: str, lang: str) -> str:
    # ref like "repository_management/support.email" or "<partner-id>/support.url"
    root, *path = ref.split("/")
    data = get_data()["partners"]
    node = data["repository_management"] if root == "repository_management" else next(
        p for p in data["partners"] if p["id"] == root
    )
    for key in path:
        node = node[key]
    if isinstance(node, dict):
        node = node.get(lang, node)
    return str(node)


_RESOLVERS = {
    "links": _resolve_link,
    "values": _resolve_value,
    "terms": _resolve_term,
    "partners": _resolve_partner,
}


def resolve_reuse_markers(markdown: str, lang: str) -> str:
    def _replace(match: re.Match) -> str:
        kind, ref = match.group("kind"), match.group("ref")
        return _RESOLVERS[kind](ref, lang)

    return _MARKER.sub(_replace, markdown)


def on_page_markdown(markdown, page, config, files, **kwargs):
    lang = page_language(page)
    return resolve_reuse_markers(markdown, lang)
```

- [ ] **Step 3: Write a self-check that catches unresolved markers**

```python
# scripts/validate_site_build.py
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
```

- [ ] **Step 4: Verify the resolver in isolation (no full build yet — `[GENERATED COMPONENT]`/marker HTML from Task 5 don't exist yet)**

```bash
python -c "
from hooks import data_store, reuse_resolver
class FakeConfig(dict): pass
cfg = FakeConfig(docs_dir='docs')
data_store.on_config(cfg)
out = reuse_resolver.resolve_reuse_markers('[REUSE: partners/repository_management/support.email]', 'en')
print(out)
assert '@' in out
"
```
Expected: prints an email address (from `data/partners.yml` `repository_management.support.email`), assertion passes.

- [ ] **Step 5: Commit**

```bash
git add hooks/data_store.py hooks/reuse_resolver.py scripts/validate_site_build.py
git commit -m "feat: add build-time [REUSE: ...] marker resolution hooks"
```

---

### Task 4: Header, footer, language switch, and design tokens (theme overrides + CSS)

**Files:**
- Create: `overrides/partials/header.html`
- Create: `overrides/partials/footer.html`
- Modify: `docs/assets/stylesheets/dataverseno.css` (design tokens + header/footer/nav styling)
- Test: manual — `mkdocs serve` and visual/keyboard check (see Step 5)

**Interfaces:**
- Consumes: Material's default `partials/header.html` / `partials/footer.html` as the base to extend (via `{% extends "base.html" %}` inheritance already provided by `theme.custom_dir`)
- Consumes: `docs/assets/icons/dataverseno-icon.svg` (already present in handover assets)
- Produces: `#repository-management-contact-card` target id referenced by footer's "General inquiries" link (must match the id Task 6 emits on the Contact page)

- [ ] **Step 1: Write design tokens into `docs/assets/stylesheets/dataverseno.css`**

Add at the top of the existing file (keep any current non-conflicting rules below):

```css
:root {
  --dataverseno-dark-primary: #000000;
  --dataverseno-light-primary: #FFFFFF;
  --dataverseno-dark-secondary: #B34700;
  --dataverseno-light-secondary: #E66A1A;
  --dataverseno-accent: #8C3800;
  --dataverseno-neutral-primary: #B1CEE0;
  --dataverseno-neutral-secondary: #D9D9D9;
}

body, .md-typeset {
  font-family: Arial, Helvetica, sans-serif;
}
```

- [ ] **Step 2: Write `overrides/partials/header.html`**

Base this on Material's own `partials/header.html` (copy from the installed `mkdocs_material` package as the starting point — locate it with `python -c "import material, os; print(os.path.dirname(material.__file__))"` then `templates/partials/header.html`), then apply these required changes per spec §8.5–§8.9:

- Dataverse icon (`assets/icons/dataverseno-icon.svg`) at the left, linking to `{{ lang.t('language') == 'nn' and '/nn/' or '/en/' }}` (language-local homepage).
- Primary nav items right-aligned, in this order: Home, About (with disclosure), Deposit Guidelines (with disclosure), News, Contact, Login.
- Login item is a plain external link to `https://dataverse.no/`.
- About and Deposit Guidelines each render as `<a>` (primary link to `about/index.md` / `deposit/index.md`) plus an adjacent `<button aria-expanded="false" aria-controls="...">` disclosure toggle that shows/hides the secondary link list from spec §8.8. The button must be a real `<button>`, keyboard-operable (native buttons get Enter/Space for free), and toggle `aria-expanded`.
- Language switch: two links/buttons labelled with the GB/Norway flag icons plus visible text "English" / "Norsk nynorsk", each pointing to the equivalent page under the other language root (use `page.file.src_uri` swapped from `en/`↔`nn/`; fall back to that language's homepage if the file doesn't exist in `files` — check with `files.get_file_from_path`).

- [ ] **Step 3: Write `overrides/partials/footer.html`**

Base on Material's `partials/footer.html`. Implement spec §8.10–§8.13:

- Four sections; Sections 2–4 above Section 1, horizontally distributed on desktop/tablet (CSS `display: flex` in `dataverseno.css`, `flex-direction: column` under a mobile breakpoint), vertical stack on handheld; thin `<hr>`/border between Sections 2–4 and Section 1.
- Section 1: localized CC0 licensing/citation text (exact strings from spec §8.12), smaller font size, at the very bottom.
- Section 2 "About / Om": links to `about/index.md`, `glossary/index.md`, `news/index.md`.
- Section 3 "Legal / Juridisk informasjon": Privacy Policy and Accessibility Statement links (exact URLs from spec §8.13).
- Section 4 "Contact / Kontakt": "Local support services" → `contact/index.md`; "General inquiries" → `contact/index.md#repository-management-contact-card`.
- Localize all labels using the page's language (same `en`/`nn` detection approach as the header).

- [ ] **Step 4: Add header/footer/disclosure CSS to `dataverseno.css`**

Cover: sticky/hover-independent disclosure panel visibility (`[aria-expanded="true"] + .secondary-nav { display: block }` pattern, not `:hover`), visible focus outlines using the design tokens, footer flex layout per Step 3, light/dark mode variants for header/footer background and link colors (use Material's `[data-md-color-scheme="slate"]` selector for dark mode), sufficient contrast against `--dataverseno-dark-primary`/`--dataverseno-light-primary`.

- [ ] **Step 5: Manual verification**

```bash
mkdocs serve
```
Open `http://127.0.0.1:8000/en/` and check:
- Dataverse icon links to `/en/`; switching language via the flag link on any page lands on the equivalent `/nn/...` page (or `/nn/` if no equivalent exists yet).
- Tab through the header with keyboard only: disclosure buttons are reachable, Enter/Space opens the secondary nav, `aria-expanded` toggles.
- Footer renders 4 sections, Section 1 pinned to the very bottom in a smaller font.
- Toggle dark mode (if the palette exposes a toggle) and confirm header/footer text remains readable.

- [ ] **Step 6: Commit**

```bash
git add overrides docs/assets/stylesheets/dataverseno.css
git commit -m "feat: implement header, footer, language switch, and design tokens"
```

---

### Task 5: Generated components — People and Contact pages

**Files:**
- Create: `hooks/generated_components.py`
- Create: `docs/assets/javascripts/contact-filter.js`
- Create: `docs/assets/stylesheets/contact.css`
- Modify: `hooks/reuse_resolver.py` — none (kept separate; `on_page_markdown` chains both hooks since MkDocs calls each hook file's `on_page_markdown` in `hooks:` list order)

**Interfaces:**
- Consumes: `hooks.data_store.get_data()` (`"people"`, `"partners"` keys), `hooks.reuse_resolver.page_language(page)`
- Produces: replacement HTML for markers `<!-- PEOPLE_SEARCH_AND_FILTER: en|nn -->`, `<!-- PEOPLE_CARDS: en|nn -->`, and the three `[GENERATED COMPONENT]` blocks on the Contact page (repository-management-contact-card, contact-search-input, partner-contact-cards) — each block's `ID:` line identifies which one to render, so replace the entire `[GENERATED COMPONENT] ... ID: <x> ... (until next blank-line-terminated block or heading)` region
- Produces: `id="repository-management-contact-card"` element consumed by Task 4's footer link and spec §8.13

- [ ] **Step 1: Write `hooks/generated_components.py`**

```python
"""Renders People and Contact page generated-component markers into HTML
at build time, from data/people.yml and data/partners.yml.
"""
from __future__ import annotations

import re

from hooks.data_store import get_data
from hooks.reuse_resolver import page_language

_GENERATED_BLOCK = re.compile(
    r"\[GENERATED COMPONENT\]\nID: (?P<id>[\w-]+)\n(?:[^\n]*\n)*?(?=\n##|\n\[GENERATED COMPONENT\]|\Z)",
    re.MULTILINE,
)


def _person_card(person: dict, lang: str) -> str:
    photo = person.get("photo")
    img = f'<img src="/assets/{photo}" alt="" loading="lazy">' if photo else ""
    expertise = ", ".join(person["expertise"].get(lang, []))
    roles = ", ".join(person["role_free_text"].get(lang, []))
    aliases = " ".join(person["search_aliases"])
    profile = f'<a href="{person["profile_url"]}">{person["name"]}</a>' if person.get("profile_url") else person["name"]
    return (
        f'<article class="person-card" data-search="{aliases.lower()}" data-institution="{person["institution_id"]}">'
        f'{img}<h3>{profile}</h3><p class="person-roles">{roles}</p><p class="person-expertise">{expertise}</p>'
        f'</article>'
    )


def _people_cards(lang: str) -> str:
    people = get_data()["people"]["people"]
    cards = "\n".join(_person_card(p, lang) for p in people)
    return f'<div class="person-cards" id="person-cards">\n{cards}\n</div>'


def _people_search_and_filter(lang: str) -> str:
    placeholder = "Search by name, institution, role, or expertise" if lang == "en" else "Søk etter namn, institusjon, rolle eller ekspertise"
    label = "Search people" if lang == "en" else "Søk i folk"
    return (
        f'<div class="people-filter" data-lang="{lang}">'
        f'<label for="people-search">{label}</label>'
        f'<input type="search" id="people-search" placeholder="{placeholder}">'
        f'</div>'
    )


def _repository_management_card(lang: str) -> str:
    rm = get_data()["partners"]["repository_management"]
    email = rm["support"]["email"]
    return (
        f'<div class="contact-card repository-management-contact-card" id="repository-management-contact-card">'
        f'<h3>{rm["name"][lang]}</h3>'
        f'<a href="mailto:{email}">{email}</a>'
        f'</div>'
    )


def _contact_search_input(lang: str) -> str:
    label = "Search partner institutions" if lang == "en" else "Søk blant partnarinstitusjonar"
    return f'<div class="contact-filter"><label for="contact-search">{label}</label><input type="search" id="contact-search"></div>'


def _partner_card(partner: dict, lang: str) -> str:
    aliases = " ".join(partner.get("search_aliases", [])).lower()
    email = partner.get("support", {}).get("email")
    url = partner.get("support", {}).get("url")
    contact = f'<a href="mailto:{email}">{email}</a>' if email else (f'<a href="{url}">{url}</a>' if url else "")
    return (
        f'<article class="contact-card partner-contact-card" data-search="{aliases}">'
        f'<h3>{partner["name"][lang]}</h3>{contact}</article>'
    )


def _partner_contact_cards(lang: str) -> str:
    partners = get_data()["partners"]["partners"]
    cards = "\n".join(_partner_card(p, lang) for p in partners)
    return f'<div class="contact-cards" id="contact-cards">\n{cards}\n</div>'


_COMPONENT_RENDERERS = {
    "repository-management-contact-card": _repository_management_card,
    "contact-search-input": _contact_search_input,
    "partner-contact-cards": _partner_contact_cards,
}


def on_page_markdown(markdown, page, config, files, **kwargs):
    lang = page_language(page)

    markdown = markdown.replace(f"<!-- PEOPLE_SEARCH_AND_FILTER: {lang} -->", _people_search_and_filter(lang))
    markdown = markdown.replace(f"<!-- PEOPLE_CARDS: {lang} -->", _people_cards(lang))

    def _replace_component(match: re.Match) -> str:
        component_id = match.group("id")
        renderer = _COMPONENT_RENDERERS.get(component_id)
        return renderer(lang) if renderer else match.group(0)

    markdown = _GENERATED_BLOCK.sub(_replace_component, markdown)
    return markdown
```

- [ ] **Step 2: Register the hook in `mkdocs.yml`**

Already listed in Task 2 Step 1 (`hooks/generated_components.py` is third in the `hooks:` list, after `data_store.py` and `reuse_resolver.py`).

- [ ] **Step 3: Write `docs/assets/javascripts/contact-filter.js`** (mirrors `people-filter.js`'s existing pattern — read it first to match its style, then adapt selectors: `#contact-search` filters `.partner-contact-card[data-search]` elements by substring match, case-insensitive, hides non-matches by toggling a CSS class rather than `display:none` removal, runs only if `#contact-search` exists so pages without the filter degrade silently)

- [ ] **Step 4: Write `docs/assets/stylesheets/contact.css`** — card grid layout for `.contact-cards`/`.contact-card`, consistent with `people.css` (read it first and reuse its grid/spacing patterns rather than inventing a new layout system)

- [ ] **Step 5: Verify markers are fully resolved**

```bash
mkdocs build --strict
python scripts/validate_site_build.py
```
Expected: build succeeds, `validate_site_build.py` reports "No unresolved content markers found."

- [ ] **Step 6: Manual check — JS-disabled fallback**

In `mkdocs serve`, open the People and Contact pages, disable JavaScript in devtools, reload: all person/partner cards must remain visible (spec §6.1.2, §6.2.6, §13).

- [ ] **Step 7: Commit**

```bash
git add hooks/generated_components.py docs/assets/javascripts/contact-filter.js docs/assets/stylesheets/contact.css
git commit -m "feat: render People and Contact pages from structured data at build time"
```

---

### Task 6: Glossary generation and inline term resolution

**Files:**
- Modify: `hooks/generated_components.py` — add glossary rendering
- Modify: `hooks/reuse_resolver.py` — none (terms already resolve via `[REUSE: terms/<id>]` for inline short labels; this task adds the full glossary index page)

**Interfaces:**
- Consumes: `get_data()["terms"]` (id → `{label, short_definition, definition, aliases, related, further_reading}`)
- Produces: replacement HTML for `<!-- GLOSSARY_TERMS: en|nn -->` on `docs/{en,nn}/glossary/index.md`

- [ ] **Step 1: Add glossary rendering to `hooks/generated_components.py`**

```python
def _glossary_term(term_id: str, term: dict, lang: str) -> str:
    label = term["label"][lang]
    definition = term["definition"][lang]
    return f'<dt id="term-{term_id}">{label}</dt>\n<dd>{definition}</dd>'


def _glossary_terms(lang: str) -> str:
    terms = get_data()["terms"]
    items = sorted(terms.items(), key=lambda kv: kv[1]["label"][lang].lower())
    body = "\n".join(_glossary_term(term_id, term, lang) for term_id, term in items)
    return f'<dl class="glossary-list">\n{body}\n</dl>'
```

Add to `on_page_markdown`, after the People replacements:

```python
    markdown = markdown.replace(f"<!-- GLOSSARY_TERMS: {lang} -->", _glossary_terms(lang))
```

- [ ] **Step 2: Verify**

```bash
mkdocs build --strict && python scripts/validate_site_build.py
```
Expected: passes; `site/en/glossary/index.html` contains `<dl class="glossary-list">` with entries from `data/terms.yml`.

- [ ] **Step 3: Commit**

```bash
git add hooks/generated_components.py
git commit -m "feat: generate glossary pages from data/terms.yml"
```

---

### Task 7: Exclude support README files from the public build

**Files:**
- Modify: `mkdocs.yml` — exclude via `not_in_nav` is insufficient (spec's own caution: MkDocs may still serve orphan pages); use the `exclude` mechanism instead
- Create/Modify: files at `docs/en/includes/README.md`, `docs/nn/includes/README.md`, `docs/en/deposit/file-formats/formats/README.md`, `docs/nn/deposit/file-formats/formats/README.md` — replace content with `.gitkeep`-equivalent per `PENDING_ITEMS.md` item 4 (repo decision, not a content decision, so in scope here)

**Interfaces:** none (isolated config change)

- [ ] **Step 1: Decide and apply the exclusion mechanism**

MkDocs core has no built-in `exclude:` key; mkdocs-material doesn't add one either. The correct native approach given the installed toolchain is `mkdocs-static-i18n`'s file handling plus a small `on_files` hook. Add to `hooks/data_store.py` (or a new tiny `hooks/exclude_support_files.py` — prefer the new file, keeping `data_store.py` single-purpose):

```python
# hooks/exclude_support_files.py
"""Excludes repository/support README files from the public MkDocs build."""
from __future__ import annotations

_EXCLUDED_SUFFIXES = (
    "includes/README.md",
    "deposit/file-formats/formats/README.md",
)


def on_files(files, config, **kwargs):
    keep = [f for f in files if not f.src_uri.replace("\\", "/").endswith(_EXCLUDED_SUFFIXES)]
    files._files = keep  # mkdocs.structure.files.Files wraps a list; reassign filtered list
    return files
```

Add `hooks/exclude_support_files.py` to the `hooks:` list in `mkdocs.yml` (Task 2's file), positioned first (before `data_store.py`) since `on_files` runs once at file-discovery time.

- [ ] **Step 2: Verify exclusion**

```bash
mkdocs build --strict
find site -iname "README*"
```
Expected: no `README.html` output anywhere under `site/`.

- [ ] **Step 3: Commit**

```bash
git add hooks/exclude_support_files.py mkdocs.yml
git commit -m "fix: exclude repository support README files from public build"
```

---

### Task 8: SEO front matter mapping

**Files:**
- Modify: `hooks/data_store.py` or new `hooks/seo_meta.py` (prefer new file — different concern from data loading)

**Interfaces:**
- Consumes: page front matter fields `seo_title`, `seo_description`, `tags`, `canonical_url` already present in handover Markdown (confirmed in `docs/en/contact/index.md` front matter)
- Produces: `<title>` override and `<meta name="description">` / `<link rel="canonical">` tags in rendered HTML

- [ ] **Step 1: Write `hooks/seo_meta.py`**

```python
"""Maps custom front matter (seo_title, seo_description, canonical_url)
onto page title/meta description/canonical link, since mkdocs-material's
defaults only read `title`/`description`.
"""
from __future__ import annotations


def on_page_context(context, page, config, nav, **kwargs):
    meta = page.meta
    if meta.get("seo_title"):
        page.title = meta["seo_title"]
    if meta.get("seo_description"):
        page.meta["description"] = meta["seo_description"]
    return context
```

Add `hooks/seo_meta.py` to `mkdocs.yml`'s `hooks:` list (any position after `data_store.py`; it doesn't depend on data store).

- [ ] **Step 2: Verify**

```bash
mkdocs build --strict
grep -o '<title>[^<]*</title>' site/en/contact/index.html
```
Expected: title matches the `seo_title` from `docs/en/contact/index.md` front matter (`Contact DataverseNO | Repository management and local support services`), not the plain `# Contact` heading.

- [ ] **Step 3: Commit**

```bash
git add hooks/seo_meta.py mkdocs.yml
git commit -m "feat: map seo_title/seo_description front matter to page meta tags"
```

---

### Task 9: Language-parity and link validation script

**Files:**
- Create: `scripts/validate_language_parity.py`
- Modify: `scripts/validate_site_build.py` — call the new checks too, or keep separate and run both in CI (keep separate: single-purpose scripts match the existing `generate_/validate_` naming convention from spec §3.3)

**Interfaces:**
- Produces: exit code 1 and printed diagnostics on: missing `en`/`nn` page pairs, broken internal Markdown links, `[REUSE: ...]` references that don't resolve against `data/*.yml`

- [ ] **Step 1: Write `scripts/validate_language_parity.py`**

```python
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

REUSE_PATTERN = re.compile(r"\[REUSE:\s*(links|values|terms|partners)/([^\]]+)\]")


def relative_md_paths(root: Path) -> set[str]:
    return {str(p.relative_to(root)) for p in root.rglob("*.md")}


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
        for kind, ref in REUSE_PATTERN.findall(text):
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
```

- [ ] **Step 2: Run it against the rebuilt tree**

```bash
python scripts/validate_language_parity.py
```
Expected: either "OK", or a concrete list of gaps to fix/flag in `PENDING_ITEMS.md` follow-up — do not silently "fix" by inventing missing pages; report them.

- [ ] **Step 3: Commit**

```bash
git add scripts/validate_language_parity.py
git commit -m "test: add language-parity and REUSE-reference validation script"
```

---

### Task 10: Wire validation and people-data checks into CI

**Files:**
- Modify: `.github/workflows/deploy.yml` — add validation steps before build
- Verify: `.github/workflows/people-data.yml` (copied in Task 1) matches this repo's paths (`data/sources/people.tsv`, `scripts/generate_people_yml.py` etc. — already verified identical in exploration)

**Interfaces:**
- Consumes: `scripts/validate_language_parity.py`, `scripts/validate_site_build.py`, `scripts/validate_people_yml.py`

- [ ] **Step 1: Add validation steps to `.github/workflows/deploy.yml`**

Insert after "Install dependencies" and before "Build site":

```yaml
      - name: Validate language parity and REUSE references
        run: python scripts/validate_language_parity.py

      - name: Validate people data
        run: python scripts/validate_people_yml.py
```

Insert after "Build site" and before "Upload Pages artifact":

```yaml
      - name: Validate built site for unresolved markers
        run: python scripts/validate_site_build.py
```

Also change the `mkdocs build` step to `mkdocs build --strict` so broken internal links fail CI (spec §15.2).

- [ ] **Step 2: Verify the workflow YAML is valid**

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/deploy.yml', encoding='utf-8'))" && echo OK
```

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "ci: run validation scripts before and after site build"
```

---

### Task 11: Full local build verification and PENDING_ITEMS reconciliation

**Files:** none created — verification-only task, plus updating `PENDING_ITEMS.md` status if copied into the main repo (see Step 4)

- [ ] **Step 1: Full clean build**

```bash
rm -rf site
mkdocs build --strict
python scripts/validate_language_parity.py
python scripts/validate_people_yml.py
python scripts/validate_site_build.py
```
Expected: all four commands exit 0.

- [ ] **Step 2: Serve and manually walk the golden path**

```bash
mkdocs serve
```
Check in a browser: `/en/` → About → People (search filters cards, JS off shows all) → Deposit Guidelines steps → Contact (repository management card has `id="repository-management-contact-card"`, partner search works, JS off shows all cards) → Glossary (terms render) → News → language switch to `/nn/` and back.

- [ ] **Step 3: Confirm `PENDING_ITEMS.md` "must resolve before public launch" items are genuinely addressed or explicitly still open**

Cross-check each of the 5 items against what this plan implemented:
1. Metadata guide link — still pending (content decision, out of scope; leave as-is, do not invent a URL).
2. Internal links/anchors validated — done by Task 9/11.
3. `[REUSE: ...]` references validated — done by Task 9.
4. README exclusion — done by Task 7.
5. `repository-management-contact-card` stable id — done by Task 5.

Copy `context/initial-migration-handover_extracted/PENDING_ITEMS.md` into the repo (e.g. `docs/superpowers/PENDING_ITEMS.md` or keep it referenced from `context/`) so item 1 isn't lost before the week-36 meeting.

- [ ] **Step 4: Final commit**

```bash
git add -A
git commit -m "chore: final verification pass for info.dataverse.no rebuild"
```

---

### Task 12: Resolve `[PAGE: ...]` cross-reference markers

**Added mid-execution.** Task 6's review surfaced that `[PAGE: <path>[#anchor] | <label>]` cross-page reference markers (spec §5.4.1 — used throughout the migrated content for internal links, e.g. `[PAGE: deposit/index | the Deposit Guidelines]` or `[PAGE: why-use-dataverseno#curation-and-preservation | curated]`) are never resolved by any hook — only `[REUSE: ...]` is handled. A repo-wide grep found 104 occurrences across `docs/en/` and `docs/nn/` real content pages (About, Deposit Guidelines, glossary definitions), not just glossary. Left unresolved, these render as literal broken bracket-text on the live site. This must be fixed before Task 11's final verification and before Rieke can meaningfully test the site.

**Files:**
- Modify: `hooks/reuse_resolver.py` — add page-marker resolution alongside the existing REUSE resolution
- Modify: `scripts/validate_site_build.py` — already has a `[PAGE:` detection pattern (added during Task 6's fix round); no change needed here, it's the check that proves this task worked
- Modify: `scripts/validate_language_parity.py` (if already written by Task 9 at execution time) or otherwise leave for Task 9 to extend — this task only needs to make `[PAGE: ...]` resolve at build time, not add new source-tree validation

**Interfaces:**
- Consumes: `hooks.reuse_resolver.page_language(page)` (existing), `hooks.data_store` is NOT needed for this — `[PAGE: ...]` resolution is purely structural (build a relative URL), it doesn't consult `data/*.yml`
- Produces: `hooks.reuse_resolver.resolve_page_markers(markdown: str, lang: str) -> str`, called from the same `on_page_markdown` that already calls `resolve_reuse_markers`

**Marker syntax (confirmed from real content):**
- `[PAGE: <page-path> | <label>]` — link to another page, e.g. `[PAGE: deposit/index | the Deposit Guidelines]`
- `[PAGE: <page-path>#<anchor> | <label>]` — link to a section within another page, e.g. `[PAGE: why-use-dataverseno#curation-and-preservation | curated]`
- `[PAGE: <anchor-only>]` or `[PAGE: <path> | <label>]` with no explicit label segment also appears in a few places (e.g. `[PAGE: about/why-use-dataverseno#credit-and-visibility]` with no `| label` — the bracket text itself doubles as the label) — handle the no-label case by using the anchor/path text as the visible label when no `|` is present.
- `<page-path>` is relative to the current page's language root and does NOT include a leading `en/`/`nn/` or a `.md` extension — e.g. `deposit/index`, `prepare-your-data` (same directory as current page when no slash), `about/why-use-dataverseno`, `glossary/index`.
- Per spec §5.4.1, the target page is always in the SAME language as the current page (shared page slugs, localized anchors) — resolve `<page-path>` against the current page's own language root (`en/` or `nn/`), never the other language.

- [ ] **Step 1: Write `resolve_page_markers` in `hooks/reuse_resolver.py`**

Add alongside the existing `_MARKER`/`resolve_reuse_markers` code:

```python
_PAGE_MARKER = re.compile(r"\[PAGE:\s*(?P<ref>[^\|\]]+?)(?:\s*\|\s*(?P<label>[^\]]+))?\]")


def resolve_page_markers(markdown: str, lang: str) -> str:
    def _replace(match: re.Match) -> str:
        ref = match.group("ref").strip()
        label = (match.group("label") or ref).strip()
        path, _, anchor = ref.partition("#")
        path = path.strip()
        if path in ("", "index"):
            href = f"/{lang}/"
        else:
            href = f"/{lang}/{path}/"
        if anchor:
            href += f"#{anchor.strip()}"
        return f'<a href="{href}">{label}</a>'

    return _PAGE_MARKER.sub(_replace, markdown)
```

- [ ] **Step 2: Call it from `on_page_markdown` in `hooks/reuse_resolver.py`**, right after the existing `resolve_reuse_markers` call, so both marker types resolve in the same pass:

```python
def on_page_markdown(markdown, page, config, files, **kwargs):
    lang = page_language(page)
    markdown = resolve_reuse_markers(markdown, lang, page_path=page.file.src_uri)
    markdown = resolve_page_markers(markdown, lang)
    return markdown
```

(Keep whatever exact signature `resolve_reuse_markers` already has from Task 3's fix round — this step only adds the second call, don't change the first.)

- [ ] **Step 3: Handle `[PAGE: ...]` markers embedded in `data/terms.yml` glossary definitions too**

`hooks/generated_components.py`'s `_glossary_term()` (Task 6) already threads definitions through `resolve_reuse_markers`. Add the same `resolve_page_markers` call there so glossary definitions resolve both marker types, matching how `on_page_markdown` handles them for regular pages.

- [ ] **Step 4: Full build verification**

```bash
python -m mkdocs build
python scripts/validate_site_build.py
```
Expected: the `[PAGE:` findings that `validate_site_build.py` started reporting during Task 6's fix round should now be zero. Manually spot check a few resolved links in the built HTML (e.g. `site/en/about/index.html` should contain `<a href="/en/glossary/">Glossary</a>` where the source had `[PAGE: glossary/index | Glossary]`) — confirm hrefs are well-formed and anchors are preserved where present.

- [ ] **Step 5: Commit**

```bash
git add hooks/reuse_resolver.py hooks/generated_components.py
git commit -m "feat: resolve [PAGE: ...] cross-reference markers at build time"
```

---

## Spec Coverage Note

Spec §9 (Content Components: Navigation Cards, Resource Boxes, Buttons, Admonitions, Workflows) is not a separate task — `.navigation-card`, `.resource-card`, and button/workflow classes already exist in the current `docs/stylesheets/extra.css`, carried forward unmodified by Task 1. Verify during Task 11's manual walk that these still render correctly against the new content, but no new component CSS is needed unless that check finds a gap.

## Explicitly Out of Scope (per Philipp's email)

- Any content/prose changes to Markdown pages — Rieke/editorial owns this; report issues instead of fixing them.
- Individual file-format detail pages under `formats/` — deferred by design (`PENDING_ITEMS.md`).
- `data/policies.yml` / structured policy version data — future work, not needed for initial launch.
- Matomo analytics integration — spec §12.4 names it as preferred but doesn't block initial migration; not in the handover package.
