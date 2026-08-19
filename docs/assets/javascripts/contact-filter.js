/**
 * Contact page filter script
 *
 * Filters the partner institution contact cards on the Contact page
 * (rendered at build time by hooks/generated_components.py) by a
 * case-insensitive substring match against each card's data-search
 * attribute.
 *
 * Page structure produced by the build:
 *   Search input: #contact-search
 *   Cards:        .partner-contact-card[data-search]
 *
 * Behaviour
 * ---------
 * - Runs only if #contact-search exists, so pages without the contact
 *   filter (or a JS-disabled browser) degrade silently: all cards stay
 *   visible via normal markup.
 * - Non-matching cards are hidden by toggling a CSS class rather than
 *   removing them or setting display:none directly, so the underlying
 *   markup (and its links) stays intact.
 */

(function () {
  function initContactFilter() {
    var input = document.getElementById('contact-search')
    if (!input) return

    var cards = document.querySelectorAll('.partner-contact-card[data-search]')

    function applyFilter() {
      var query = input.value.trim().toLowerCase()
      cards.forEach(function (card) {
        var matches = query === '' || card.getAttribute('data-search').indexOf(query) !== -1
        card.classList.toggle('contact-card--hidden', !matches)
      })
    }

    input.addEventListener('input', applyFilter)
    applyFilter()
  }

  // document$ only replays for Material's "instant navigation" feature,
  // which this site doesn't enable — subscribing to it alone silently never
  // fires on an ordinary full page load. Always initialize on normal
  // DOM-ready too; document$ stays as a harmless extra hook in case instant
  // navigation is enabled later. (Same fix as people-filter.js, which this
  // was copied from.)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initContactFilter)
  } else {
    initContactFilter()
  }
  if (typeof document$ !== 'undefined' && document$.subscribe) {
    document$.subscribe(initContactFilter)
  }
})()
