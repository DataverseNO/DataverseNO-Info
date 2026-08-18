"""Renders People and Contact page generated-component markers into HTML
at build time, from data/people.yml and data/partners.yml.
"""
from __future__ import annotations

import re

from hooks.data_store import get_data
from hooks.reuse_resolver import page_language, resolve_page_markers, resolve_reuse_markers

_GENERATED_BLOCK = re.compile(
    # Stops at the first line that isn't "Key: value" (i.e. the block's own
    # blank-line terminator) instead of scanning ahead to the next heading —
    # scanning ahead swallowed unrelated prose paragraphs following the block.
    r"\[GENERATED COMPONENT\]\nID: (?P<id>[\w-]+)\n(?:[A-Za-z][A-Za-z ]*:.*\n)*"
)


def _person_card(person: dict, lang: str) -> str:
    photo = person.get("photo")
    img = f'<img class="people-card__photo" src="/{photo}" alt="" loading="lazy">' if photo else ""
    expertise = ", ".join(person["expertise"].get(lang, []))
    roles = ", ".join(person["role_free_text"].get(lang, []))
    aliases = " ".join(person["search_aliases"])
    profile = (
        f'<a class="people-card__profile" href="{person["profile_url"]}">{person["name"]}</a>'
        if person.get("profile_url")
        else person["name"]
    )
    return (
        f'<article class="people-card" data-person-card'
        f' data-search="{aliases.lower()}" data-institution="{person["institution_id"]}"'
        f' data-roles="{" ".join(person["roles"])}">'
        f'{img}<div class="people-card__content">'
        f'<p class="people-card__name">{profile}</p>'
        f'<p class="people-card__roles">{roles}</p>'
        f'<p class="people-card__expertise">{expertise}</p>'
        f'</div></article>'
    )


def _people_cards(lang: str) -> str:
    people = get_data()["people"]["people"]
    cards = "\n".join(_person_card(p, lang) for p in people)
    empty_label = "No people match the current filters." if lang == "en" else "Ingen personar samsvarar med filtera."
    return (
        f'<div class="people-card-grid" id="people-cards">\n{cards}\n</div>\n'
        f'<p class="people-empty-state" data-people-empty-state hidden>{empty_label}</p>'
    )


def _people_search_and_filter(lang: str) -> str:
    # ponytail: no shared [data-people-page] wrapper — PEOPLE_SEARCH_AND_FILTER
    # and PEOPLE_CARDS resolve as two separate markers on the page, not nested
    # inside one container, so people-filter.js scopes off [data-people-search]
    # (this component) and #people-cards (the grid) directly instead.
    partners = get_data()["partners"]["partners"]
    roles = get_data()["people"]["role_vocabulary"]
    ordered_partners = sorted(partners, key=lambda p: p["sort_name"][lang])

    search_label = "Search people" if lang == "en" else "Søk i folk"
    search_placeholder = (
        "Search by name, institution, role, or expertise"
        if lang == "en"
        else "Søk etter namn, institusjon, rolle eller ekspertise"
    )
    institution_label = "Filter by institution" if lang == "en" else "Filtrer etter institusjon"
    role_group_label = "Filter by role" if lang == "en" else "Filtrer etter rolle"

    institution_options = "".join(f'<option value="{p["id"]}">{p["name"][lang]}</option>' for p in ordered_partners)
    role_buttons = "".join(
        f'<button type="button" class="people-filter-box" data-role-filter data-role="{role_id}" aria-pressed="false">{label[lang]}</button>'
        for role_id, label in roles.items()
    )

    return (
        '<div class="people-filter">'
        f'<div class="people-filter__search"><label for="people-search">{search_label}</label>'
        f'<input type="search" id="people-search" data-people-search placeholder="{search_placeholder}"></div>'
        '<div class="people-filter__boxes">'
        f'<label for="people-institution-filter">{institution_label}</label>'
        f'<select id="people-institution-filter" class="people-institution-select" data-institution-filter multiple size="1">{institution_options}</select>'
        f'<span class="people-filter__roles" role="group" aria-label="{role_group_label}">{role_buttons}</span>'
        '</div>'
        '<p class="people-results-summary" data-people-count aria-live="polite"></p>'
        '</div>'
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
    name = partner["name"][lang]
    logo = partner.get("logo", {}).get(lang)
    img = f'<img src="/{logo}" alt="{name}" loading="lazy">' if logo else ""
    return (
        f'<article class="contact-card partner-contact-card" data-search="{aliases}">'
        f'{img}<h3>{name}</h3>{contact}</article>'
    )


def _partner_contact_cards(lang: str) -> str:
    partners = get_data()["partners"]["partners"]
    cards = "\n".join(_partner_card(p, lang) for p in partners)
    return f'<div class="contact-cards" id="contact-cards">\n{cards}\n</div>'


def _glossary_term(term_id: str, term: dict, lang: str, files, current_file) -> str:
    label = resolve_reuse_markers(term["label"][lang], lang, files=files, current_file=current_file)
    label = resolve_page_markers(label, lang, files, current_file)
    definition = resolve_reuse_markers(term["definition"][lang], lang, files=files, current_file=current_file)
    definition = resolve_page_markers(definition, lang, files, current_file)
    return f'<dt id="term-{term_id}">{label}</dt>\n<dd>{definition}</dd>'


def _glossary_terms(lang: str, files, current_file) -> str:
    terms = get_data()["terms"]
    items = sorted(terms.items(), key=lambda kv: kv[1]["label"][lang].lower())
    body = "\n".join(_glossary_term(term_id, term, lang, files, current_file) for term_id, term in items)
    return f'<dl class="glossary-list">\n{body}\n</dl>'


def _partner_logo_grid(lang: str) -> str:
    partners = get_data()["partners"]["partners"]
    ordered = sorted(partners, key=lambda p: p["sort_name"][lang])
    items = []
    for partner in ordered:
        logo = partner["logo"][lang]
        name = partner["name"][lang]
        items.append(f'<span class="partner-logo" title="{name}"><img src="/{logo}" alt="{name}" loading="lazy"></span>')
    return f'<div class="partner-logo-grid">\n{"".join(items)}\n</div>'


_COMPONENT_RENDERERS = {
    "repository-management-contact-card": _repository_management_card,
    "contact-search-input": _contact_search_input,
    "partner-contact-cards": _partner_contact_cards,
    "partner-institution-logo-grid": _partner_logo_grid,
}


def on_page_markdown(markdown, page, config, files, **kwargs):
    lang = page_language(page)

    markdown = markdown.replace(f"<!-- PEOPLE_SEARCH_AND_FILTER: {lang} -->", _people_search_and_filter(lang))
    markdown = markdown.replace(f"<!-- PEOPLE_CARDS: {lang} -->", _people_cards(lang))
    markdown = markdown.replace(f"<!-- GLOSSARY_TERMS: {lang} -->", _glossary_terms(lang, files, page.file))

    def _replace_component(match: re.Match) -> str:
        component_id = match.group("id")
        renderer = _COMPONENT_RENDERERS.get(component_id)
        return renderer(lang) if renderer else match.group(0)

    markdown = _GENERATED_BLOCK.sub(_replace_component, markdown)
    return markdown
