"""Verification checks for translated content.

Adapted from the Nextflow Training project's translation system:
https://github.com/nextflow-io/training/tree/master/_scripts/translate
"""

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class VerifyResult:
    path: Path
    issues: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return len(self.issues) == 0


def verify_file(en_path: Path, lang_path: Path) -> VerifyResult:
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
    """Verify header counts match."""
    header_re = re.compile(r"^#{1,6}\s", re.MULTILINE)
    en_count = len(header_re.findall(en_text))
    lang_count = len(header_re.findall(lang_text))
    if en_count != lang_count:
        result.issues.append(f"header count mismatch: en={en_count} lang={lang_count}")


def _check_admonitions(en_text: str, lang_text: str, result: VerifyResult) -> None:
    """Verify admonition counts match and keywords are in English."""
    admonition_re = re.compile(r"^:::(\w+)", re.MULTILINE)

    en_matches = admonition_re.findall(en_text)
    lang_matches = admonition_re.findall(lang_text)

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
