"""Verification checks for translated content.

Adapted from the Nextflow Training project's translation system:
https://github.com/nextflow-io/training/tree/master/_scripts/translate
"""

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from .glossary import _CODE_REGION_RE, load_glossary


def _normalize(text: str) -> str:
    """Strip accents and lowercase for fuzzy comparison."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


@dataclass
class VerifyResult:
    path: Path
    issues: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return len(self.issues) == 0


def _strip_code_regions(text: str) -> str:
    """Remove fenced code blocks and inline code spans from text."""
    return _CODE_REGION_RE.sub("", text)


def verify_file(en_path: Path, lang_path: Path, locale: str = "") -> VerifyResult:
    """Run structural checks on a translated file."""
    result = VerifyResult(path=lang_path)

    if not lang_path.exists():
        result.issues.append("translated file missing")
        return result

    en_text = en_path.read_text()
    lang_text = lang_path.read_text()

    if not lang_text.strip():
        result.issues.append("translated file is empty")
        return result

    _check_frontmatter(en_text, lang_text, result)
    _check_code_blocks(en_text, lang_text, result)
    _check_headers(en_text, lang_text, result)
    _check_admonitions(en_text, lang_text, result)
    _check_length_ratio(en_text, lang_text, result)
    _check_jsx_components(en_text, lang_text, result)
    if locale:
        _check_never_translate(en_text, lang_text, locale, result)
        _check_glossary_terms(en_text, lang_text, locale, result)

    return result


def _check_frontmatter(en_text: str, lang_text: str, result: VerifyResult) -> None:
    """Verify frontmatter is present in both files."""
    en_has = en_text.startswith("---")
    lang_has = lang_text.startswith("---")
    if en_has and not lang_has:
        result.issues.append("frontmatter missing in translation")


def _check_code_blocks(en_text: str, lang_text: str, result: VerifyResult) -> None:
    """Verify code block counts match."""
    en_count = en_text.count("```")
    lang_count = lang_text.count("```")
    if en_count != lang_count:
        result.issues.append(f"code block count mismatch: en={en_count} lang={lang_count}")


def _check_headers(en_text: str, lang_text: str, result: VerifyResult) -> None:
    """Verify header counts match (outside code blocks)."""
    header_re = re.compile(r"^#{1,6}\s", re.MULTILINE)
    en_prose = _strip_code_regions(en_text)
    lang_prose = _strip_code_regions(lang_text)
    en_count = len(header_re.findall(en_prose))
    lang_count = len(header_re.findall(lang_prose))
    if en_count != lang_count:
        result.issues.append(f"header count mismatch: en={en_count} lang={lang_count}")


def _check_admonitions(en_text: str, lang_text: str, result: VerifyResult) -> None:
    """Verify admonition counts match and keywords are in English (outside code blocks)."""
    admonition_re = re.compile(r"^:::(\w+)", re.MULTILINE)
    en_prose = _strip_code_regions(en_text)
    lang_prose = _strip_code_regions(lang_text)

    en_matches = admonition_re.findall(en_prose)
    lang_matches = admonition_re.findall(lang_prose)

    if len(en_matches) != len(lang_matches):
        result.issues.append(
            f"admonition count mismatch: en={len(en_matches)} lang={len(lang_matches)}"
        )

    valid_keywords = {"note", "tip", "info", "warning", "danger", "caution"}
    for kw in lang_matches:
        if kw.lower() not in valid_keywords:
            result.issues.append(f"admonition keyword may be translated: '{kw}'")


def _check_length_ratio(en_text: str, lang_text: str, result: VerifyResult) -> None:
    """Flag if translation is suspiciously short or long."""
    en_len = len(en_text.strip())
    lang_len = len(lang_text.strip())
    if en_len == 0:
        return
    ratio = lang_len / en_len
    if ratio < 0.5:
        result.issues.append(f"translation is very short ({ratio:.0%} of English)")
    elif ratio > 2.0:
        result.issues.append(f"translation is very long ({ratio:.0%} of English)")


def _check_jsx_components(en_text: str, lang_text: str, result: VerifyResult) -> None:
    """Verify JSX import statements are preserved."""
    import_re = re.compile(r"^import\s+.*from\s+['\"]", re.MULTILINE)
    en_imports = set(import_re.findall(en_text))
    lang_imports = set(import_re.findall(lang_text))
    missing = en_imports - lang_imports
    if missing:
        result.issues.append(f"missing JSX imports: {missing}")


def _check_never_translate(
    en_text: str, lang_text: str, locale: str, result: VerifyResult
) -> None:
    """Verify never_translate terms appear in translation at similar frequency."""
    glossary = load_glossary(locale)
    never = glossary.get("never_translate", [])
    if not never:
        return

    en_prose = _strip_code_regions(en_text)
    lang_prose = _strip_code_regions(lang_text)

    for term in never:
        pattern = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
        en_count = len(pattern.findall(en_prose))
        if en_count == 0:
            continue
        lang_count = len(pattern.findall(lang_prose))
        if lang_count == 0:
            result.issues.append(f"never_translate term '{term}' missing from translation (en={en_count})")


def _check_glossary_terms(
    en_text: str, lang_text: str, locale: str, result: VerifyResult
) -> None:
    """Verify glossary target terms appear where source terms were used."""
    glossary = load_glossary(locale)
    terms = glossary.get("terms", [])
    if not terms:
        return

    lang_prose_norm = " ".join(_normalize(_strip_code_regions(lang_text)).split())
    en_prose_lower = " ".join(_strip_code_regions(en_text).lower().split())

    for entry in terms:
        source = entry.get("source", "")
        target = entry.get("target", "")
        if not source or not target:
            continue
        if en_prose_lower.count(source.lower()) == 0:
            continue
        if _normalize(target) not in lang_prose_norm:
            result.issues.append(
                f"glossary term '{source}' -> '{target}' not found in translation"
            )
