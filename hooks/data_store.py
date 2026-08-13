"""Loads data/*.yml once per build and caches it for other hooks."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

# mkdocs loads this file as a hook module under the literal name given in
# mkdocs.yml's `hooks:` list (e.g. "hooks/data_store.py"), while the other
# hook files import it normally via `from hooks.data_store import get_data`.
# Those are two different import paths, so without this line Python creates
# two separate module instances: the one mkdocs calls on_config() on, and a
# second one (under the "hooks.data_store" dotted name) whose _DATA is never
# populated. Registering this module under its dotted name up front makes
# both import paths resolve to the same instance.
sys.modules.setdefault("hooks.data_store", sys.modules[__name__])

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
