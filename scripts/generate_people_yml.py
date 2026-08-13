#!/usr/bin/env python3
"""Generate data/people.yml from data/sources/people.tsv.

The TSV file is the Git-friendly export of the editorial Excel source.
Person search_aliases are generated from:
- name and name parts;
- institution_id;
- partner search_aliases from data/partners.yml;
- localized role labels;
- expertise_en and expertise_nn.
"""

from __future__ import annotations

import argparse
import csv
import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml

ROLE_LABELS: dict[str, dict[str, str]] = {
    "board": {"en": "Board", "nn": "Styre"},
    "collection-management": {"en": "Collection Management", "nn": "Samlingsforvaltning"},
    "curation": {"en": "Curation", "nn": "Kuratering"},
    "repository-management": {"en": "Repository Management", "nn": "Arkivforvaltning"},
}

DEFAULT_TSV = Path("data/sources/people.tsv")
DEFAULT_PARTNERS = Path("data/partners.yml")
DEFAULT_OUTPUT = Path("data/people.yml")


class IndentedDumper(yaml.SafeDumper):
    """YAML dumper with readable list indentation."""

    def increase_indent(self, flow: bool = False, indentless: bool = False):  # type: ignore[override]
        return super().increase_indent(flow, False)


def norm(value: Any) -> str:
    """Normalize TSV/YAML scalar values for consistent output."""
    if value is None:
        return ""
    value = str(value).replace("\u00a0", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_items(value: Any) -> list[str]:
    """Split semicolon-separated TSV cells into a clean list."""
    value = norm(value)
    if not value:
        return []
    return [norm(part) for part in value.split(";") if norm(part)]


def dedupe(items: list[str]) -> list[str]:
    """Deduplicate exact normalized values while preserving useful case variants."""
    result: list[str] = []
    seen: set[str] = set()
    for item in items:
        item = norm(item)
        if not item:
            continue
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def clean_photo(value: Any) -> str | None:
    """Treat directory-only photo placeholders as missing photos."""
    value = norm(value)
    if not value or value.rstrip("/") == "assets/images/people":
        return None
    if value.endswith("/"):
        return None
    filename = value.split("/")[-1].strip()
    if not filename or "." not in filename:
        return None
    return value


def name_parts(name: str) -> list[str]:
    """Return searchable parts of a person's name."""
    return [part.strip(" ,.;:()[]{}") for part in norm(name).split() if part.strip(" ,.;:()[]{}")]


def role_texts(roles: list[str], lang: str) -> list[str]:
    """Return localized controlled role labels for a list of role IDs."""
    return [ROLE_LABELS[role][lang] for role in roles if role in ROLE_LABELS]


def load_partner_aliases(path: Path) -> dict[str, list[str]]:
    """Load partner search aliases by partner institution ID from partners.yml."""
    if not path.exists():
        raise FileNotFoundError(f"Partner data file not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    aliases: dict[str, list[str]] = {}

    for partner in data.get("partners", []) or []:
        partner_id = norm(partner.get("id"))
        if not partner_id:
            continue
        alias_items: list[str] = []
        alias_items.extend([norm(item) for item in (partner.get("search_aliases", []) or [])])
        for field in ("name", "sort_name"):
            values = partner.get(field, {}) or {}
            alias_items.extend([norm(values.get("en")), norm(values.get("nn"))])
        aliases[partner_id] = dedupe(alias_items)

    repository_management = data.get("repository_management") or {}
    repository_management_id = norm(repository_management.get("id"))
    if repository_management_id:
        alias_items = [norm(item) for item in (repository_management.get("search_aliases", []) or [])]
        for field in ("name", "sort_name"):
            values = repository_management.get(field, {}) or {}
            alias_items.extend([norm(values.get("en")), norm(values.get("nn"))])
        aliases[repository_management_id] = dedupe(alias_items)

    return aliases


def generate_people(tsv_path: Path, partners_path: Path) -> list[dict[str, Any]]:
    """Generate person records from TSV and partner aliases."""
    partner_aliases = load_partner_aliases(partners_path)
    people: list[dict[str, Any]] = []
    unknown_roles: dict[str, list[str]] = {}
    unknown_institutions: dict[str, list[str]] = {}

    with tsv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        expected_columns = [
            "id",
            "name",
            "institution_id",
            "photo",
            "roles",
            "expertise_en",
            "expertise_nn",
            "profile_url",
        ]
        missing_columns = [column for column in expected_columns if column not in (reader.fieldnames or [])]
        if missing_columns:
            raise ValueError(f"Missing required columns in {tsv_path}: {missing_columns}")

        for row_no, row in enumerate(reader, start=2):
            person_id = norm(row.get("id"))
            name = norm(row.get("name"))
            institution_id = norm(row.get("institution_id"))
            roles = split_items(row.get("roles"))
            expertise_en = split_items(row.get("expertise_en"))
            expertise_nn = split_items(row.get("expertise_nn"))
            photo = clean_photo(row.get("photo"))
            profile_url = norm(row.get("profile_url"))

            if not person_id or not name or not institution_id:
                raise ValueError(f"Missing required field in row {row_no}: id/name/institution_id")

            for role in roles:
                if role not in ROLE_LABELS:
                    unknown_roles.setdefault(role, []).append(person_id)

            if institution_id not in partner_aliases:
                unknown_institutions.setdefault(institution_id, []).append(person_id)

            role_free_text_en = role_texts(roles, "en")
            role_free_text_nn = role_texts(roles, "nn")

            search_aliases = dedupe(
                [name]
                + name_parts(name)
                + [institution_id]
                + partner_aliases.get(institution_id, [])
                + role_free_text_en
                + role_free_text_nn
                + expertise_en
                + expertise_nn
            )

            person: dict[str, Any] = {
                "id": person_id,
                "name": name,
                "institution_id": institution_id,
            }
            if photo:
                person["photo"] = photo
            person["roles"] = roles
            person["role_free_text"] = {
                "en": role_free_text_en,
                "nn": role_free_text_nn,
            }
            person["expertise"] = {
                "en": expertise_en,
                "nn": expertise_nn,
            }
            if profile_url:
                person["profile_url"] = profile_url
            person["search_aliases"] = search_aliases
            people.append(person)

    if unknown_roles:
        raise ValueError(f"Unknown roles in TSV: {unknown_roles}")
    if unknown_institutions:
        raise ValueError(f"Unknown institution_id values in TSV: {unknown_institutions}")
    return people


def load_existing_output(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def build_output(people: list[dict[str, Any]], output_path: Path, generated_date: str) -> dict[str, Any]:
    existing = load_existing_output(output_path)
    created = generated_date
    last_updated = generated_date
    if existing:
        created = str(existing.get("created") or generated_date)
        if existing.get("people") == people and existing.get("role_vocabulary") == ROLE_LABELS:
            last_updated = str(existing.get("last_updated") or generated_date)

    return {
        "version": 0.2,
        "created": created,
        "last_updated": last_updated,
        "source": "data/sources/people.tsv",
        "description": "Generated people data for the DataverseNO Information Website.",
        "generation": {
            "script": "scripts/generate_people_yml.py",
            "input": "data/sources/people.tsv",
            "partner_source": "data/partners.yml",
            "note": "Person records are generated from people.tsv and partners.yml. Do not edit generated person records manually unless the generation workflow is updated.",
        },
        "role_vocabulary": ROLE_LABELS,
        "people": people,
    }


def validate_generated_structure(data: dict[str, Any]) -> None:
    people = data.get("people", [])
    ids = [person["id"] for person in people]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate person IDs found")
    for person in people:
        assert person["id"] and person["name"] and person["institution_id"]
        assert isinstance(person["roles"], list)
        assert isinstance(person["role_free_text"]["en"], list)
        assert isinstance(person["role_free_text"]["nn"], list)
        assert isinstance(person["expertise"]["en"], list)
        assert isinstance(person["expertise"]["nn"], list)
        assert isinstance(person["search_aliases"], list)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate data/people.yml from people.tsv and partners.yml")
    parser.add_argument("--input", type=Path, default=DEFAULT_TSV, help="Path to people.tsv")
    parser.add_argument("--partners", type=Path, default=DEFAULT_PARTNERS, help="Path to partners.yml")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Path to generated people.yml")
    parser.add_argument("--date", default=date.today().isoformat(), help="Generated metadata date, format YYYY-MM-DD")
    args = parser.parse_args()

    people = generate_people(args.input, args.partners)
    output = build_output(people, args.output, args.date)
    validate_generated_structure(output)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        yaml.dump(output, Dumper=IndentedDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )

    generated = yaml.safe_load(args.output.read_text(encoding="utf-8"))
    validate_generated_structure(generated)

    print(args.output)
    print(f"people: {len(people)}")
    print("valid yaml")


if __name__ == "__main__":
    main()
