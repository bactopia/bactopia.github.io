"""CLI for Bactopia documentation translation.

Usage:
    python -m bin.translate sync --locale pt          # incremental sync
    python -m bin.translate sync --locale pt --full    # full retranslation
    python -m bin.translate file --locale pt --path docs/quick-start.md
    python -m bin.translate verify --locale pt
"""

import argparse
import asyncio
import sys
import time
from pathlib import Path

import anthropic

from .api import call_claude_async
from .config import PROMPTS_DIR, REPO_ROOT, TranslationError, validate_api_key
from .glossary import postprocess
from .sync import (
    TranslationFile,
    discover_files,
    find_changed_files,
    get_hash,
    load_hashes,
    remove_orphaned,
    save_hashes,
)
from .verify import verify_file


def _load_prompt(name: str) -> str:
    """Load a prompt file from the prompts directory."""
    path = PROMPTS_DIR / name
    if not path.exists():
        print(f"ERROR: Prompt file not found: {path}", file=sys.stderr)
        sys.exit(1)
    return path.read_text().strip()


def _build_system_prompt(locale: str) -> str:
    """Build the full system prompt from general + locale-specific prompts."""
    general = _load_prompt("general.md")
    locale_path = PROMPTS_DIR / f"{locale}.md"
    if locale_path.exists():
        locale_prompt = locale_path.read_text().strip()
        return f"{general}\n\n---\n\n{locale_prompt}"
    return general


def _build_user_prompt(en_text: str) -> str:
    """Build the user prompt with the English source text."""
    return (
        "Translate the following documentation file. "
        "Return ONLY the translated file content, nothing else.\n\n"
        f"```\n{en_text}\n```"
    )


async def _translate_file(
    tf: TranslationFile,
    locale: str,
    system_prompt: str,
    client: anthropic.AsyncAnthropic,
    semaphore: asyncio.Semaphore,
) -> tuple[TranslationFile, bool, str]:
    """Translate a single file. Returns (file, success, message)."""
    async with semaphore:
        en_text = tf.en_path.read_text()
        user_prompt = _build_user_prompt(en_text)
        label = f"{tf.plugin_id}/{tf.relative}"

        try:
            result = await call_claude_async(
                prompt=user_prompt,
                system=system_prompt,
                client=client,
                label=label,
            )

            translated = result.text.strip()
            if translated.startswith("```"):
                first_newline = translated.index("\n") + 1
                translated = translated[first_newline:]
            if translated.endswith("```"):
                translated = translated[: -len("```")]
            translated = translated.strip()

            translated = postprocess(translated, locale)

            tf.lang_path.parent.mkdir(parents=True, exist_ok=True)
            tf.lang_path.write_text(translated + "\n")

            tokens = result.input_tokens + result.output_tokens
            return (tf, True, f"OK ({tokens} tokens)")
        except TranslationError as e:
            return (tf, False, str(e))
        except Exception as e:
            return (tf, False, f"Unexpected error: {e}")


async def _run_sync(locale: str, full: bool, parallel: int, include: str | None) -> int:
    """Run the sync operation. Returns exit code."""
    print(f"Discovering files for locale '{locale}'...")
    all_files = discover_files(locale)
    print(f"  Found {len(all_files)} English source files")

    if include:
        all_files = [f for f in all_files if include in f.relative or include in f.plugin_id]
        print(f"  Filtered to {len(all_files)} files matching '{include}'")

    orphaned = remove_orphaned(locale, all_files)
    if orphaned:
        print(f"  Removing {len(orphaned)} orphaned translations")
        for p in orphaned:
            p.unlink()

    changed = find_changed_files(locale, all_files, force=full)
    if not changed:
        print("  No files need translation. Everything is up to date.")
        return 0

    mode = "full retranslation" if full else "incremental"
    print(f"  {len(changed)} files need translation ({mode})")

    api_key = validate_api_key()
    system_prompt = _build_system_prompt(locale)
    client = anthropic.AsyncAnthropic(api_key=api_key)
    semaphore = asyncio.Semaphore(parallel)

    try:
        start = time.monotonic()
        tasks = [_translate_file(tf, locale, system_prompt, client, semaphore) for tf in changed]

        succeeded = 0
        failed = 0
        hashes = load_hashes(locale)

        for coro in asyncio.as_completed(tasks):
            tf, ok, msg = await coro
            label = f"{tf.plugin_id}/{tf.relative}"
            if ok:
                succeeded += 1
                hashes[f"{tf.plugin_id}/{tf.relative}"] = get_hash(tf.en_path)
                print(f"  [{succeeded + failed}/{len(changed)}] {label}: {msg}")
            else:
                failed += 1
                print(f"  [{succeeded + failed}/{len(changed)}] FAILED {label}: {msg}")

        save_hashes(locale, hashes)
        elapsed = time.monotonic() - start
        print(f"\nDone in {elapsed:.1f}s: {succeeded} translated, {failed} failed")
        return 1 if failed > 0 else 0
    finally:
        await client.close()


async def _run_file(locale: str, path: str) -> int:
    """Translate a single file. Returns exit code."""
    source = REPO_ROOT / path
    if not source.exists():
        print(f"ERROR: File not found: {source}", file=sys.stderr)
        return 1

    all_files = discover_files(locale)
    matching = [f for f in all_files if f.en_path == source]
    if not matching:
        print(f"ERROR: File not in any docs plugin: {path}", file=sys.stderr)
        return 1

    tf = matching[0]
    api_key = validate_api_key()
    system_prompt = _build_system_prompt(locale)
    client = anthropic.AsyncAnthropic(api_key=api_key)

    try:
        semaphore = asyncio.Semaphore(1)
        _, ok, msg = await _translate_file(tf, locale, system_prompt, client, semaphore)
        label = f"{tf.plugin_id}/{tf.relative}"
        if ok:
            hashes = load_hashes(locale)
            hashes[f"{tf.plugin_id}/{tf.relative}"] = get_hash(tf.en_path)
            save_hashes(locale, hashes)
            print(f"  {label}: {msg}")
            print(f"  Written to: {tf.lang_path}")
            return 0
        else:
            print(f"  FAILED {label}: {msg}", file=sys.stderr)
            return 1
    finally:
        await client.close()


def _run_verify(locale: str) -> int:
    """Verify translated files. Returns exit code."""
    all_files = discover_files(locale)
    total = 0
    issues_count = 0

    for tf in all_files:
        if not tf.lang_path.exists():
            continue
        total += 1
        result = verify_file(tf.en_path, tf.lang_path)
        if not result.ok:
            issues_count += 1
            label = f"{tf.plugin_id}/{tf.relative}"
            for issue in result.issues:
                print(f"  {label}: {issue}")

    print(f"\nVerified {total} files: {total - issues_count} ok, {issues_count} with issues")
    return 1 if issues_count > 0 else 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bactopia documentation translation tool",
        prog="python -m bin.translate",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sync_p = sub.add_parser("sync", help="Sync translations for a locale")
    sync_p.add_argument("--locale", required=True, help="Target locale (e.g., pt)")
    sync_p.add_argument("--full", action="store_true", help="Force full retranslation")
    sync_p.add_argument("--parallel", type=int, default=10, help="Max parallel API calls")
    sync_p.add_argument("--include", help="Only translate files matching this string")

    file_p = sub.add_parser("file", help="Translate a single file")
    file_p.add_argument("--locale", required=True, help="Target locale (e.g., pt)")
    file_p.add_argument("--path", required=True, help="Relative path to English source file")

    verify_p = sub.add_parser("verify", help="Verify translated files")
    verify_p.add_argument("--locale", required=True, help="Target locale (e.g., pt)")

    args = parser.parse_args()

    if args.command == "sync":
        code = asyncio.run(_run_sync(args.locale, args.full, args.parallel, args.include))
    elif args.command == "file":
        code = asyncio.run(_run_file(args.locale, args.path))
    elif args.command == "verify":
        code = _run_verify(args.locale)
    else:
        parser.print_help()
        code = 1

    sys.exit(code)
