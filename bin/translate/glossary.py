"""Deterministic glossary post-processing for translations.

Applies glossary.yml rules after LLM translation to enforce term consistency.

Adapted from the Nextflow Training project's translation system:
https://github.com/nextflow-io/training/tree/master/_scripts/translate
"""

import re
from functools import lru_cache
from pathlib import Path

import yaml

from .config import TRANSLATIONS_DATA_DIR

_CODE_REGION_RE = re.compile(
    r"(`{3,})[^\n]*\n.*?\1"  # fenced code blocks (``` or longer)
    r"|"
    r"`[^`\n]+`",            # inline code spans
    re.DOTALL,
)

_PLACEHOLDER = "\x00CODE_{}\x00"


@lru_cache(maxsize=8)
def load_glossary(locale: str) -> dict:
    """Load and cache the glossary for a locale."""
    path = TRANSLATIONS_DATA_DIR / locale / "glossary.yml"
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text()) or {}


def _protect_code(text: str) -> tuple[str, list[str]]:
    """Replace code spans/fences with placeholders."""
    regions: list[str] = []

    def _replace(m: re.Match) -> str:
        regions.append(m.group(0))
        return _PLACEHOLDER.format(len(regions) - 1)

    return _CODE_REGION_RE.sub(_replace, text), regions


def _restore_code(text: str, regions: list[str]) -> str:
    """Restore placeholders back to original code."""
    for i, original in enumerate(regions):
        text = text.replace(_PLACEHOLDER.format(i), original)
    return text


def apply_glossary(text: str, locale: str) -> str:
    """Apply glossary term enforcement to translated text (skips code regions)."""
    glossary = load_glossary(locale)
    if not glossary:
        return text

    for entry in glossary.get("terms", []):
        source = entry.get("source", "")
        target = entry.get("target", "")
        if source and target:
            text = re.sub(
                re.escape(source),
                target,
                text,
                flags=re.IGNORECASE,
            )

    return text


def fix_admonitions(text: str, locale: str) -> str:
    """Ensure Docusaurus admonition keywords remain in English.

    Docusaurus uses :::note, :::tip, :::warning etc. The keywords must
    stay in English but the optional title can be translated.
    """
    glossary = load_glossary(locale)
    admonition_titles = glossary.get("admonition_titles", {})

    admonition_re = re.compile(r"^(:::)(\w+)(.*)", re.MULTILINE)

    def _fix_match(m: re.Match) -> str:
        prefix = m.group(1)
        keyword = m.group(2).lower()
        rest = m.group(3)

        valid_keywords = {"note", "tip", "info", "warning", "danger", "caution"}
        if keyword not in valid_keywords:
            return m.group(0)

        if rest.strip() and rest.strip().startswith("["):
            return f"{prefix}{keyword}{rest}"

        if keyword in admonition_titles and not rest.strip():
            title = admonition_titles[keyword]
            return f"{prefix}{keyword}[{title}]"

        return f"{prefix}{keyword}{rest}"

    return admonition_re.sub(_fix_match, text)


def fix_unclosed_fences(text: str) -> str:
    """Append a closing ``` if the translation has an odd number of fences."""
    if text.count("```") % 2 != 0:
        text = text.rstrip() + "\n```\n"
    return text


def postprocess(text: str, locale: str) -> str:
    """Run all post-processing steps on translated text."""
    text, regions = _protect_code(text)
    text = apply_glossary(text, locale)
    text = fix_admonitions(text, locale)
    text = _restore_code(text, regions)
    text = fix_unclosed_fences(text)
    return text
