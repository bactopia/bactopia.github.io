"""File discovery, content mapping, and hash-based change detection.

Maps English source directories to their corresponding i18n output
directories based on the Docusaurus plugin configuration.
"""

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from .config import EXCLUDE_FILES, I18N_DIR, PLUGIN_MAP, TRANSLATIONS_DATA_DIR


@dataclass
class TranslationFile:
    """A file that needs translation."""

    en_path: Path
    lang_path: Path
    plugin_id: str
    relative: str


def get_hash(path: Path) -> str:
    """Return MD5 hex digest of a file's contents."""
    return hashlib.md5(path.read_bytes()).hexdigest()


def load_hashes(locale: str) -> dict[str, str]:
    """Load the saved hash file for a locale."""
    hash_file = TRANSLATIONS_DATA_DIR / locale / ".hashes.json"
    if hash_file.exists():
        return json.loads(hash_file.read_text())
    return {}


def save_hashes(locale: str, hashes: dict[str, str]) -> None:
    """Save the hash file for a locale."""
    hash_file = TRANSLATIONS_DATA_DIR / locale / ".hashes.json"
    hash_file.parent.mkdir(parents=True, exist_ok=True)
    hash_file.write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n")


def discover_files(locale: str) -> list[TranslationFile]:
    """Discover all English source files and their i18n target paths."""
    files = []

    for plugin_id, cfg in PLUGIN_MAP.items():
        source_dir = cfg["source"]
        i18n_subdir = cfg["i18n_subdir"]
        extensions = cfg["extensions"]
        target_base = I18N_DIR / locale / i18n_subdir
        if cfg.get("versioned", True):
            target_base = target_base / "current"

        if not source_dir.exists():
            continue

        for ext in extensions:
            for en_path in sorted(source_dir.rglob(f"*{ext}")):
                relative = en_path.relative_to(source_dir)

                if relative.name.lower() in EXCLUDE_FILES:
                    continue

                lang_path = target_base / relative
                files.append(
                    TranslationFile(
                        en_path=en_path,
                        lang_path=lang_path,
                        plugin_id=plugin_id,
                        relative=str(relative),
                    )
                )

    return files


def find_changed_files(
    locale: str,
    files: list[TranslationFile],
    force: bool = False,
) -> list[TranslationFile]:
    """Return only files whose English source has changed since last sync."""
    if force:
        return files

    old_hashes = load_hashes(locale)
    changed = []

    for f in files:
        current_hash = get_hash(f.en_path)
        key = f"{f.plugin_id}/{f.relative}"
        if old_hashes.get(key) != current_hash:
            changed.append(f)

    return changed


def remove_orphaned(locale: str, files: list[TranslationFile]) -> list[Path]:
    """Find translated files that no longer have an English source."""
    en_targets = {f.lang_path for f in files}
    active_plugins = {f.plugin_id for f in files}
    orphaned = []

    for plugin_id, cfg in PLUGIN_MAP.items():
        if plugin_id not in active_plugins:
            continue

        i18n_subdir = cfg["i18n_subdir"]
        target_base = I18N_DIR / locale / i18n_subdir
        if cfg.get("versioned", True):
            target_base = target_base / "current"

        if not target_base.exists():
            continue

        for lang_file in target_base.rglob("*"):
            if lang_file.is_file() and lang_file not in en_targets:
                orphaned.append(lang_file)

    return orphaned
