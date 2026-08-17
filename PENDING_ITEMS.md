# Pending Items

Copied from `context/initial-migration-handover_extracted/PENDING_ITEMS.md`
(the original migration handover) and annotated with implementation status
as of the info.dataverse.no rebuild. See `superpowers/plans/2026-08-13-info-dataverse-no-rebuild.md`
for the implementation plan and `.superpowers/sdd/2026-08-13-info-dataverse-no-rebuild/progress.md`
for the full build ledger.

## Must resolve before public launch

1. Add the approved target for the full metadata guide.
   - English Deposit landing page: `Full metadata guide (link coming)`.
   - Norwegian Nynorsk Deposit landing page: `Full metadataguide (lenkje kjem)`.
   - English Step 2 page: `DataverseNO metadata guide (link coming)`.
   - Norwegian Nynorsk Step 2 page: `DataverseNO-metadataguiden (lenkje kjem)`.
   - **Status: still open.** Content decision, out of scope for the technical
     rebuild — no URL has been invented. The corresponding resource box
     currently renders as a non-linked "pending" card so it reads clearly as
     unfinished rather than broken.

2. Validate internal links and localized anchors after MkDocs configuration is finalized.
   - **Status: done.** `scripts/validate_language_parity.py` and
     `scripts/validate_site_build.py` run in CI and pass; `[PAGE: ...]` and
     `[SECTION: ...]` cross-reference markers resolve to real hrefs at build time.

3. Validate all `[REUSE: ...]` references against the current root-level `data/` files.
   - **Status: done.** `scripts/validate_language_parity.py` checks this in CI.

4. Confirm that README files under `docs/` are excluded from the public build, or replace them with `.gitkeep` files and move their explanatory text outside the public documentation tree.
   - **Status: done.** Excluded from the build via `hooks/exclude_support_files.py`.

5. Confirm that the repository management contact card receives the stable id `repository-management-contact-card` in both language versions.
   - **Status: done.**

## Deferred by design

1. Glossary generation from `data/terms.yml`.
   - **Status: done.** Glossary pages generate from `data/terms.yml` at build time.

2. Individual file-format pages.
   - **Status: still deferred**, as originally scoped — placeholders only.

3. File-format structured data model.
   - **Status: still deferred**, as originally scoped.

4. Final header, footer, language switch, and secondary navigation implementation.
   - **Status: done.**

5. Final validation scripts and build workflows.
   - **Status: done.** `validate_language_parity.py`, `validate_people_yml.py`,
     and `validate_site_build.py` all run as CI gates before/after `mkdocs build`.

## Newly discovered during the rebuild (not in the original handover)

The migrated content uses several custom bracket-marker component types beyond
`[REUSE: ...]` and `[PAGE: ...]` — `[NAVIGATION CARD]`, `[RESOURCE BOX]` /
`[RESOURCE BOX GRID]`, `[BUTTON]`, `[ADMONITION]`, `[CHECKLIST]`, `[WORKFLOW]`,
`[SECTION: ...]`, and `[GENERATED VALUE: ...]` (spec §9, "Content components
and rendering"). These were flagged in `MIGRATION_REPORT.md` as "preserved for
later implementation" but had no owning task in the rebuild plan and no build
hook resolved them — 144 occurrences across most content pages rendered as
literal broken bracket text. Resolved now via `hooks/content_blocks.py` (new)
plus a fix to `hooks/generated_components.py`'s block-matching regex, which
was accidentally swallowing unrelated prose after `[GENERATED COMPONENT]`
blocks. `scripts/validate_site_build.py` now checks for all of these marker
types so a future regression fails CI instead of shipping silently.

One open design note: icon names (`Icon: pencil-square`, etc.) are not
currently rendered as graphics — no icon library is wired up for them yet.
Cards, buttons, and workflow steps render without icon glyphs. Not blocking
for a first test pass; flag if an icon set (e.g. Bootstrap Icons, to match
the icon names already used in the migrated content) should be added.

## Intentional exceptions

- English Continuity Policy version `1.0` remains plain text unless an approved DOI/link is provided.
- Norwegian Nynorsk Continuity Policy version remains `1.0 (lenkje kjem)` until an approved DOI/link is provided.
- Some prose references to later workflow steps are intentionally not links because nearby buttons provide the actual navigation.
- `Organizational Agreement` is the intentional destination for the organizational documents references in both English and Norwegian Nynorsk About pages.
