"""Excludes repository/support README files from the public MkDocs build."""
from __future__ import annotations

_EXCLUDED_SUFFIXES = (
    "includes/README.md",
    "deposit/file-formats/formats/README.md",
)


def on_files(files, config, **kwargs):
    keep = [f for f in files if not f.src_uri.replace("\\", "/").endswith(_EXCLUDED_SUFFIXES)]
    files._files = keep  # mkdocs.structure.files.Files wraps a list; reassign filtered list
    return files
