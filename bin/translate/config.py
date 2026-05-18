"""Configuration for the Bactopia docs translation system."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Claude API settings
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 32_768
REQUEST_TIMEOUT = 600
MAX_RETRIES = 8
BASE_DELAY = 2.0
MAX_CONTINUATIONS = 5
DEFAULT_PARALLEL = 10

# Paths
PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
I18N_DIR = REPO_ROOT / "i18n"
TRANSLATIONS_DATA_DIR = REPO_ROOT / "data" / "translations"

# Docusaurus plugin ID to source directory mapping.
# The default docs plugin (preset-classic) has no explicit ID, so its
# i18n directory is just "docusaurus-plugin-content-docs".
PLUGIN_MAP = {
    "docs": {
        "source": REPO_ROOT / "docs",
        "i18n_subdir": "docusaurus-plugin-content-docs",
        "extensions": [".md", ".mdx"],
    },
    "bactopia-tools": {
        "source": REPO_ROOT / "bactopia-tools",
        "i18n_subdir": "docusaurus-plugin-content-docs-bactopia-tools",
        "extensions": [".md", ".mdx"],
    },
    "bactopia-pipelines": {
        "source": REPO_ROOT / "bactopia-pipelines",
        "i18n_subdir": "docusaurus-plugin-content-docs-bactopia-pipelines",
        "extensions": [".md", ".mdx"],
    },
    "developers": {
        "source": REPO_ROOT / "developers",
        "i18n_subdir": "docusaurus-plugin-content-docs-developers",
        "extensions": [".md", ".mdx"],
    },
    "impact": {
        "source": REPO_ROOT / "impact",
        "i18n_subdir": "docusaurus-plugin-content-docs-impact",
        "extensions": [".md", ".mdx"],
    },
}

# Files to exclude from translation
EXCLUDE_FILES = {
    "changelog.md",
}


class TranslationError(Exception):
    pass


class ConfigError(Exception):
    pass


def validate_api_key() -> str:
    """Return the ANTHROPIC_API_KEY or raise ConfigError."""
    import os

    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        raise ConfigError(
            "ANTHROPIC_API_KEY environment variable is not set. "
            "Get one at https://console.anthropic.com/"
        )
    return key
