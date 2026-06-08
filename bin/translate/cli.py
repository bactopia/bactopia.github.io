"""CLI for Bactopia documentation translation.

Usage:
    python -m bin.translate sync --locale pt          # incremental sync
    python -m bin.translate sync --locale pt --full    # full retranslation
    python -m bin.translate sync --locale pt --dry-run # preview without API calls
    python -m bin.translate file --locale pt --path docs/quick-start.md
    python -m bin.translate verify --locale pt
"""

import argparse
import asyncio
import re
import sys
import time
from pathlib import Path

import anthropic
from tqdm import tqdm

from .api import TranslationResult, call_claude_async
from .config import (
    DEFAULT_PARALLEL,
    MODEL,
    PRICING,
    PROMPTS_DIR,
    REPO_ROOT,
    TranslationError,
    validate_api_key,
)
from .glossary import load_glossary, postprocess
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

_FENCE_RE = re.compile(r"^(`{3,})\w*\s*\n(.*)\n\1\s*$", re.DOTALL)


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
        prompt = f"{general}\n\n---\n\n{locale_prompt}"
    else:
        prompt = general

    glossary = load_glossary(locale)
    never = glossary.get("never_translate", [])
    if never:
        terms = ", ".join(never)
        prompt += (
            f"\n\n---\n\n"
            f"## Terms that must NEVER be translated\n\n"
            f"The following terms must always remain in English exactly as written: {terms}."
        )

    return prompt


def _build_user_prompt(en_text: str) -> str:
    """Build the user prompt with the English source text."""
    return (
        "Translate the following documentation file. "
        "Return ONLY the translated file content, nothing else.\n\n"
        f"```\n{en_text}\n```"
    )


def _format_cost(input_tokens: int, output_tokens: int, model: str) -> str:
    """Format a cost summary line for the given token counts."""
    rates = PRICING.get(model)
    if not rates:
        return f"Tokens: {input_tokens:,} input + {output_tokens:,} output"
    input_cost = input_tokens / 1_000_000 * rates["input"]
    output_cost = output_tokens / 1_000_000 * rates["output"]
    total = input_cost + output_cost
    return (
        f"Tokens: {input_tokens:,} input + {output_tokens:,} output\n"
        f"Cost:   ${total:.2f} (${input_cost:.2f} input + ${output_cost:.2f} output)"
    )


async def _translate_file(
    tf: TranslationFile,
    locale: str,
    system_prompt: str,
    client: anthropic.AsyncAnthropic,
    semaphore: asyncio.Semaphore,
    model: str = MODEL,
) -> tuple[TranslationFile, bool, str, TranslationResult | None]:
    """Translate a single file. Returns (file, success, message, result)."""
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
                model=model,
            )

            translated = result.text.strip()
            m = _FENCE_RE.match(translated)
            if m:
                translated = m.group(2).strip()

            translated = postprocess(translated, locale)

            tf.lang_path.parent.mkdir(parents=True, exist_ok=True)
            tf.lang_path.write_text(translated + "\n")

            tokens = result.input_tokens + result.output_tokens
            return (tf, True, f"OK ({tokens:,} tokens)", result)
        except TranslationError as e:
            return (tf, False, str(e), None)
        except Exception as e:
            return (tf, False, f"Unexpected error: {e}", None)


async def _run_sync(
    locale: str,
    full: bool,
    parallel: int,
    include: str | None,
    exclude: str | None,
    dry_run: bool,
    model: str,
    do_verify: bool,
) -> int:
    """Run the sync operation. Returns exit code."""
    print(f"Discovering files for locale '{locale}'...")
    all_files = discover_files(locale)
    print(f"  Found {len(all_files)} English source files")

    if include:
        all_files = [f for f in all_files if include in f.relative or include in f.plugin_id]
        print(f"  Filtered to {len(all_files)} files matching '{include}'")

    if exclude:
        before = len(all_files)
        all_files = [f for f in all_files if exclude not in f.relative and exclude not in f.plugin_id]
        print(f"  Excluded {before - len(all_files)} files matching '{exclude}'")

    orphaned = remove_orphaned(locale, all_files)
    if orphaned:
        if dry_run:
            print(f"  Would remove {len(orphaned)} orphaned translations")
        else:
            print(f"  Removing {len(orphaned)} orphaned translations")
            for p in orphaned:
                p.unlink()

    valid_keys = {f"{f.plugin_id}/{f.relative}" for f in all_files}
    old_hashes = load_hashes(locale)
    stale = {k for k in old_hashes if k not in valid_keys}
    if stale and not dry_run:
        for k in stale:
            del old_hashes[k]
        save_hashes(locale, old_hashes)
        print(f"  Pruned {len(stale)} stale hash entries")

    changed = find_changed_files(locale, all_files, force=full)
    if not changed:
        print("  No files need translation. Everything is up to date.")
        return 0

    mode = "full retranslation" if full else "incremental"
    print(f"  {len(changed)} files need translation ({mode})")

    if dry_run:
        for tf in changed:
            status = "new" if not tf.lang_path.exists() else "changed"
            print(f"    {tf.plugin_id}/{tf.relative} ({status})")
        return 0

    api_key = validate_api_key()
    system_prompt = _build_system_prompt(locale)
    client = anthropic.AsyncAnthropic(api_key=api_key)
    semaphore = asyncio.Semaphore(parallel)

    try:
        start = time.monotonic()
        tasks = [
            _translate_file(tf, locale, system_prompt, client, semaphore, model)
            for tf in changed
        ]

        succeeded = 0
        failed = 0
        failed_files: list[TranslationFile] = []
        total_input = 0
        total_output = 0
        hashes = load_hashes(locale)

        with tqdm(total=len(changed), desc="Translating", unit="file") as pbar:
            for coro in asyncio.as_completed(tasks):
                tf, ok, msg, result = await coro
                label = f"{tf.plugin_id}/{tf.relative}"
                if ok:
                    succeeded += 1
                    hashes[f"{tf.plugin_id}/{tf.relative}"] = get_hash(tf.en_path)
                    if result:
                        total_input += result.input_tokens
                        total_output += result.output_tokens
                    pbar.set_postfix_str(label[-50:])
                else:
                    failed += 1
                    failed_files.append(tf)
                    tqdm.write(f"  FAILED {label}: {msg}")
                pbar.update(1)

        # Auto-retry failed files once
        if failed_files:
            print(f"\nRetrying {len(failed_files)} failed files...")
            retry_tasks = [
                _translate_file(tf, locale, system_prompt, client, semaphore, model)
                for tf in failed_files
            ]
            with tqdm(total=len(failed_files), desc="Retrying", unit="file") as pbar:
                for coro in asyncio.as_completed(retry_tasks):
                    tf, ok, msg, result = await coro
                    label = f"{tf.plugin_id}/{tf.relative}"
                    if ok:
                        succeeded += 1
                        failed -= 1
                        hashes[f"{tf.plugin_id}/{tf.relative}"] = get_hash(tf.en_path)
                        if result:
                            total_input += result.input_tokens
                            total_output += result.output_tokens
                        pbar.set_postfix_str(label[-50:])
                    else:
                        tqdm.write(f"  RETRY FAILED {label}: {msg}")
                    pbar.update(1)

        save_hashes(locale, hashes)
        elapsed = time.monotonic() - start
        print(f"\nDone in {elapsed:.1f}s: {succeeded} translated, {failed} failed")
        print(_format_cost(total_input, total_output, model))

        if do_verify and succeeded > 0:
            print("\nVerifying translated files...")
            translated_files = [tf for tf in changed if tf.lang_path.exists()]
            issues_count = 0
            for tf in translated_files:
                vr = verify_file(tf.en_path, tf.lang_path, locale)
                if not vr.ok:
                    issues_count += 1
                    label = f"{tf.plugin_id}/{tf.relative}"
                    for issue in vr.issues:
                        print(f"  {label}: {issue}")
            ok_count = len(translated_files) - issues_count
            print(f"  Verified {len(translated_files)} files: {ok_count} ok, {issues_count} with issues")

        return 1 if failed > 0 else 0
    finally:
        await client.close()


async def _run_file(locale: str, path: str, model: str) -> int:
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
        _, ok, msg, result = await _translate_file(
            tf, locale, system_prompt, client, semaphore, model
        )
        label = f"{tf.plugin_id}/{tf.relative}"
        if ok:
            hashes = load_hashes(locale)
            hashes[f"{tf.plugin_id}/{tf.relative}"] = get_hash(tf.en_path)
            save_hashes(locale, hashes)
            print(f"  {label}: {msg}")
            print(f"  Written to: {tf.lang_path}")
            if result:
                print(f"  {_format_cost(result.input_tokens, result.output_tokens, model)}")
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
        result = verify_file(tf.en_path, tf.lang_path, locale)
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
    sync_p.add_argument("--parallel", type=int, default=DEFAULT_PARALLEL, help="Max parallel API calls")
    sync_p.add_argument("--include", help="Only translate files matching this string")
    sync_p.add_argument("--exclude", help="Skip files matching this string")
    sync_p.add_argument("--dry-run", action="store_true", help="Preview what would be translated")
    sync_p.add_argument("--model", default=MODEL, help=f"Claude model to use (default: {MODEL})")
    sync_p.add_argument("--verify", action="store_true", help="Verify files after translation")

    file_p = sub.add_parser("file", help="Translate a single file")
    file_p.add_argument("--locale", required=True, help="Target locale (e.g., pt)")
    file_p.add_argument("--path", required=True, help="Relative path to English source file")
    file_p.add_argument("--model", default=MODEL, help=f"Claude model to use (default: {MODEL})")

    verify_p = sub.add_parser("verify", help="Verify translated files")
    verify_p.add_argument("--locale", required=True, help="Target locale (e.g., pt)")

    args = parser.parse_args()

    if args.command == "sync":
        code = asyncio.run(
            _run_sync(
                args.locale,
                args.full,
                args.parallel,
                args.include,
                args.exclude,
                args.dry_run,
                args.model,
                args.verify,
            )
        )
    elif args.command == "file":
        code = asyncio.run(_run_file(args.locale, args.path, args.model))
    elif args.command == "verify":
        code = _run_verify(args.locale)
    else:
        parser.print_help()
        code = 1

    sys.exit(code)
