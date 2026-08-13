"""Renders People and Contact page generated-component markers into HTML
at build time, from data/people.yml and data/partners.yml.
"""
from __future__ import annotations

import re

from hooks.data_store import get_data
from hooks.reuse_resolver import page_language, resolve_page_markers, resolve_reuse_markers

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


def _glossary_term(term_id: str, term: dict, lang: str, files, current_file) -> str:
    label = resolve_reuse_markers(term["label"][lang], lang)
    label = resolve_page_markers(label, lang, files, current_file)
    definition = resolve_reuse_markers(term["definition"][lang], lang)
    definition = resolve_page_markers(definition, lang, files, current_file)
    return f'<dt id="term-{term_id}">{label}</dt>\n<dd>{definition}</dd>'


def _glossary_terms(lang: str, files, current_file) -> str:
    terms = get_data()["terms"]
    items = sorted(terms.items(), key=lambda kv: kv[1]["label"][lang].lower())
    body = "\n".join(_glossary_term(term_id, term, lang, files, current_file) for term_id, term in items)
    return f'<dl class="glossary-list">\n{body}\n</dl>'


_COMPONENT_RENDERERS = {
    "repository-management-contact-card": _repository_management_card,
    "contact-search-input": _contact_search_input,
    "partner-contact-cards": _partner_contact_cards,
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
