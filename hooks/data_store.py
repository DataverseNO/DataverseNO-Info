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
