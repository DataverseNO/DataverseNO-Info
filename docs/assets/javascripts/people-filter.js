/**
 * People page filter script (stub)
 *
 * Purpose
 * -------
 * This file documents the expected JavaScript contract for the DataverseNO
 * People page. It is intentionally a stub and should be completed during the
 * AI-assisted website migration, once the final generated HTML structure is
 * available.
 *
 * Expected source data
 * --------------------
 * - data/people.yml
 * - data/partner-contacts.yml
 *
 * Expected page structure
 * -----------------------
 * The generated People page should expose the following data attributes:
 *
 * Page root:
 *   [data-people-page]
 *
 * Search input:
 *   [data-people-search]
 *
 * Institution filter:
 *   [data-institution-filter]
 *
 * Role filter buttons:
 *   [data-role-filter]
 *
 * Person cards:
 *   [data-person-card]
 *   data-institution="uit"
 *   data-roles="repository-management curation"
 *   data-search="philipp conzett uit tromsø repository management linguistics"
 *
 * Result count elements:
 *   [data-people-count]
 *   [data-institution-count]
 *   [data-role-count="curation"]
 *   [data-role-count="collection-management"]
 *   [data-role-count="repository-management"]
 *   [data-role-count="board"]
 *
 * Empty-state element:
 *   [data-people-empty-state]
 *
 * Expected behaviour
 * ------------------
 * - Initialize only on pages containing [data-people-page].
 * - Filter cards by free-text search.
 * - Filter cards by one or more selected partner institutions.
 * - Filter cards by one or more selected controlled roles.
 * - Update result counts when filters change.
 * - Show an empty-state message when no person cards match.
 * - Keep all cards visible if JavaScript is unavailable.
 *
 * Accessibility expectations
 * --------------------------
 * - Filter buttons should be real <button> elements.
 * - Toggle filter buttons should use aria-pressed="true|false".
 * - Result count updates should be announced through an aria-live="polite"
 *   region where appropriate.
 * - Filtering must remain usable by keyboard.
 * - Active state must not rely on colour alone.
 *
 * Material for MkDocs note
 * ------------------------
 * If instant loading is enabled, initialization should use Material's
 * document$ observable when available. A fallback DOMContentLoaded listener
 * should be provided for portability.
 */

(function () {
  function initPeopleFilter() {
    const root = document.querySelector('[data-people-page]')
    if (!root) return

    // Stub only: implementation to be finalized during website migration.
    // Suggested implementation outline:
    // 1. Read [data-people-search].
    // 2. Read [data-institution-filter] selected values.
    // 3. Read active [data-role-filter] buttons.
    // 4. Compare filters against [data-person-card] attributes.
    // 5. Toggle card.hidden.
    // 6. Update count and empty-state elements.
  }

  if (typeof document$ !== 'undefined' && document$.subscribe) {
    document$.subscribe(initPeopleFilter)
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPeopleFilter)
  } else {
    initPeopleFilter()
  }
})()
