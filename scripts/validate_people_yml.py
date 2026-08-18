#!/usr/bin/env python3
"""Validate data/people.yml against data/partners.yml and the people data schema."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

ROLE_IDS = {"board", "collection-management", "curation", "repository-management"}
ROLE_LABELS = {
    "board": {"en": "Board", "nn": "Styre"},
    "collection-management": {"en": "Collection Management", "nn": "Samlingsforvaltning"},
    "curation": {"en": "Curation", "nn": "Kuratering"},
    "repository-management": {"en": "Repository Management", "nn": "Arkivforvaltning"},
}

DEFAULT_PEOPLE = Path("data/people.yml")
DEFAULT_PARTNERS = Path("data/partners.yml")


def norm(value: Any) -> str:
    if value is None:
        return ""
    value = str(value).replace("\u00a0", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def partner_aliases(data: dict[str, Any]) -> dict[str, list[str]]:
    aliases: dict[str, list[str]] = {}
    for partner in data.get("partners", []) or []:
        partner_id = norm(partner.get("id"))
        if partner_id:
            aliases[partner_id] = [norm(item) for item in (partner.get("search_aliases") or []) if norm(item)]
    repo = data.get("repository_management") or {}
    repo_id = norm(repo.get("id"))
    if repo_id:
        aliases[repo_id] = [norm(item) for item in (repo.get("search_aliases") or []) if norm(item)]
    return aliases


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate(people_path: Path, partners_path: Path) -> None:
    people_data = load_yaml(people_path)
    partners_data = load_yaml(partners_path)
    institution_aliases = partner_aliases(partners_data)
    institution_ids = set(institution_aliases)

    errors: list[str] = []
    people = people_data.get("people")
    require(isinstance(people, list), "people must be a list", errors)
    if not isinstance(people, list):
        raise ValueError("people must be a list")

    person_ids: set[str] = set()
    for index, person in enumerate(people, start=1):
        context = f"person #{index}"
        person_id = norm(person.get("id"))
        name = norm(person.get("name"))
        institution_id = norm(person.get("institution_id"))
        context = person_id or context

        require(bool(person_id), f"{context}: id is required", errors)
        require(bool(name), f"{context}: name is required", errors)
        require(bool(institution_id), f"{context}: institution_id is required", errors)
        if person_id:
            require(person_id not in person_ids, f"{context}: duplicate id", errors)
            person_ids.add(person_id)

        require(institution_id in institution_ids, f"{context}: unknown institution_id {institution_id!r}", errors)

        roles = person.get("roles")
        require(isinstance(roles, list) and bool(roles), f"{context}: roles must be a non-empty list", errors)
        if isinstance(roles, list):
            for role in roles:
                require(role in ROLE_IDS, f"{context}: unknown role {role!r}", errors)

        role_free_text = person.get("role_free_text") or {}
        for lang in ("en", "nn"):
            require(isinstance(role_free_text.get(lang), list), f"{context}: role_free_text.{lang} must be a list", errors)
        if isinstance(roles, list):
            expected_en = [ROLE_LABELS[role]["en"] for role in roles if role in ROLE_LABELS]
            expected_nn = [ROLE_LABELS[role]["nn"] for role in roles if role in ROLE_LABELS]
            require(role_free_text.get("en") == expected_en, f"{context}: role_free_text.en does not match roles", errors)
            require(role_free_text.get("nn") == expected_nn, f"{context}: role_free_text.nn does not match roles", errors)

        expertise = person.get("expertise") or {}
        for lang in ("en", "nn"):
            require(isinstance(expertise.get(lang), list), f"{context}: expertise.{lang} must be a list", errors)

        profile_url = norm(person.get("profile_url"))
        if profile_url:
            require(profile_url.startswith("https://"), f"{context}: profile_url should start with https://", errors)

        photo = norm(person.get("photo"))
        if photo:
            require(photo.startswith("assets/images/people/"), f"{context}: photo should be under assets/images/people/", errors)
            require(not photo.endswith("/"), f"{context}: photo must point to a file, not a directory", errors)

        search_aliases = person.get("search_aliases")
        require(isinstance(search_aliases, list) and bool(search_aliases), f"{context}: search_aliases must be a non-empty list", errors)
        if isinstance(search_aliases, list):
            require(name in search_aliases, f"{context}: search_aliases must include full name", errors)
            for name_part in [part for part in name.split(" ") if part]:
                require(name_part in search_aliases, f"{context}: search_aliases missing name part {name_part!r}", errors)
            require(institution_id in search_aliases, f"{context}: search_aliases must include institution_id", errors)
            for alias in institution_aliases.get(institution_id, []):
                require(alias in search_aliases, f"{context}: search_aliases missing partner alias {alias!r}", errors)
            for label in (role_free_text.get("en") or []) + (role_free_text.get("nn") or []):
                require(label in search_aliases, f"{context}: search_aliases missing role label {label!r}", errors)
            for item in (expertise.get("en") or []) + (expertise.get("nn") or []):
                require(item in search_aliases, f"{context}: search_aliases missing expertise item {item!r}", errors)

    if errors:
        message = "people.yml validation failed:\n" + "\n".join(f"- {error}" for error in errors)
        raise SystemExit(message)

    print(f"Valid people data: {len(people)} people")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate generated people.yml")
    parser.add_argument("--people", type=Path, default=DEFAULT_PEOPLE, help="Path to people.yml")
    parser.add_argument("--partners", type=Path, default=DEFAULT_PARTNERS, help="Path to partners.yml")
    args = parser.parse_args()
    validate(args.people, args.partners)


if __name__ == "__main__":
    main()
