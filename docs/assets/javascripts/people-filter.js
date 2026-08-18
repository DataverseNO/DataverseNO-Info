/**
 * People page filter script.
 *
 * Filters the person cards rendered into #people-cards (by hooks/
 * generated_components.py) using the free-text search input, the
 * institution <select multiple>, and the role toggle buttons rendered
 * alongside it by the same hook. Everything stays in the DOM at all times
 * (spec §6.2.6: "All person cards shall remain visible if JavaScript is
 * unavailable") — this script only ever adds/removes the `hidden`
 * attribute on top of what the build already rendered.
 */
(function () {
  function initPeopleFilter() {
    const search = document.querySelector('[data-people-search]')
    const grid = document.getElementById('people-cards')
    if (!search || !grid) return

    const institutionSelect = document.querySelector('[data-institution-filter]')
    const roleButtons = Array.from(document.querySelectorAll('[data-role-filter]'))
    const countEl = document.querySelector('[data-people-count]')
    const emptyState = document.querySelector('[data-people-empty-state]')
    const cards = Array.from(grid.querySelectorAll('[data-person-card]'))

    function selectedInstitutions() {
      if (!institutionSelect) return []
      return Array.from(institutionSelect.selectedOptions).map((o) => o.value)
    }

    function activeRoles() {
      return roleButtons.filter((b) => b.getAttribute('aria-pressed') === 'true').map((b) => b.dataset.role)
    }

    function apply() {
      const query = search.value.trim().toLowerCase()
      const institutions = selectedInstitutions()
      const roles = activeRoles()
      let visibleCount = 0

      cards.forEach((card) => {
        const matchesQuery = !query || card.dataset.search.includes(query)
        const matchesInstitution = institutions.length === 0 || institutions.includes(card.dataset.institution)
        const cardRoles = card.dataset.roles ? card.dataset.roles.split(' ') : []
        const matchesRole = roles.length === 0 || roles.some((r) => cardRoles.includes(r))
        const visible = matchesQuery && matchesInstitution && matchesRole
        card.hidden = !visible
        if (visible) visibleCount += 1
      })

      if (countEl) countEl.textContent = String(visibleCount)
      if (emptyState) emptyState.hidden = visibleCount !== 0
    }

    search.addEventListener('input', apply)
    if (institutionSelect) institutionSelect.addEventListener('change', apply)
    roleButtons.forEach((button) => {
      button.addEventListener('click', () => {
        const pressed = button.getAttribute('aria-pressed') === 'true'
        button.setAttribute('aria-pressed', String(!pressed))
        apply()
      })
    })

    apply()
  }

  if (typeof document$ !== 'undefined' && document$.subscribe) {
    document$.subscribe(initPeopleFilter)
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPeopleFilter)
  } else {
    initPeopleFilter()
  }
})()
