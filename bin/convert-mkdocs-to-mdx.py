#!/usr/bin/env python3
"""Convert mkdocs-material markdown to Docusaurus-compatible markdown."""

import argparse
import difflib
import re
import sys
from pathlib import Path

ADMONITION_TYPE_MAP = {
    "note": "note",
    "tip": "tip",
    "info": "info",
    "warning": "warning",
    "danger": "danger",
    "question": "info",
    "error": "danger",
    "success": "tip",
    "failure": "danger",
    "example": "info",
    "abstract": "info",
}

DEFAULT_EXCLUDES = ["blog", "custom", "data", "assets", "impact-and-outreach"]


def convert_code_fences(content: str) -> str:
    """Convert ```{lang} and ``` { .lang .attr } to ```lang."""
    lines = content.split("\n")
    result = []
    for line in lines:
        # ```{bash} or ```{tsv} etc.
        m = re.match(r"^(\s*)```\{(\w+)\}\s*$", line)
        if m:
            result.append(f"{m.group(1)}```{m.group(2)}")
            continue
        # ``` { .bash .copy } or ``` { .bash .no-copy }
        m = re.match(r"^(\s*)```\s*\{\s*\.(\w+)(?:\s+\.\w+)*\s*\}\s*$", line)
        if m:
            result.append(f"{m.group(1)}```{m.group(2)}")
            continue
        result.append(line)
    return "\n".join(result)


def convert_zoom_images(content: str) -> str:
    """Remove <a class="zoom"> wrappers around images."""
    return re.sub(
        r'<a class="zoom" href="[^"]*">\s*\n(!\[[^\]]*\]\([^)]+\))\s*\n</a>',
        r"\1",
        content,
    )


def _parse_grid_card(item_text: str) -> dict:
    """Parse a single grid card item into title, description, and link."""
    lines = [l.strip() for l in item_text.strip().split("\n")]

    title = ""
    description_parts = []
    link = ""
    past_separator = False

    for line in lines:
        if not title:
            # First line: icon + __Title__
            m = re.search(r"__(.+?)__", line)
            if m:
                title = m.group(1)
            continue
        if line == "---":
            past_separator = True
            continue
        if past_separator:
            # Check for link line: [:octicons-...: Text](url) or [Text](url)
            link_match = re.match(
                r"\[:?[a-z]+-[a-z0-9-]+:\s*(.+?)\]\((.+?)\)$", line
            )
            if not link_match:
                link_match = re.match(r"\[(.+?)\]\((.+?)\)$", line)
            if link_match:
                link = f"[{link_match.group(1)}]({link_match.group(2)})"
            elif line:
                description_parts.append(line)

    return {
        "title": title,
        "description": " ".join(description_parts),
        "link": link,
    }


def convert_grid_cards(content: str) -> str:
    """Convert <div class="grid cards" markdown> blocks to markdown lists."""
    pattern = re.compile(
        r'<div class="grid cards" markdown>\s*\n(.*?)\n</div>',
        re.DOTALL,
    )

    def replace_grid(m):
        block = m.group(1)
        # Split into individual card items (each starts with "-   ")
        items = re.split(r"\n-   ", block)
        # First item may start with "-   " after leading whitespace
        items = [items[0].lstrip().removeprefix("-   ")] + items[1:]
        items = [i for i in items if i.strip()]

        result_lines = []
        for item_text in items:
            card = _parse_grid_card(item_text)
            parts = [f"- **{card['title']}**"]
            if card["description"]:
                parts.append(f" -- {card['description']}")
            if card["link"]:
                if card["description"]:
                    parts.append(f". {card['link']}")
                else:
                    parts.append(f" -- {card['link']}")
            result_lines.append("".join(parts))

        return "\n".join(result_lines)

    return pattern.sub(replace_grid, content)


def _collect_indented_block(lines: list[str], start: int) -> list[str]:
    """Collect lines belonging to a 4-space-indented block.

    Tracks code fence state to avoid ending the block on blank lines
    inside fenced code.
    """
    block = []
    i = start
    in_code_fence = False

    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        # Track code fences within the indented block
        if stripped.startswith("    "):
            dedented = stripped[4:]
            if re.match(r"^```", dedented) and not in_code_fence:
                in_code_fence = True
            elif re.match(r"^```\s*$", dedented) and in_code_fence:
                in_code_fence = False

        if in_code_fence:
            block.append(line)
            i += 1
            continue

        if stripped == "":
            # Blank line: check if block continues after it
            j = i + 1
            while j < len(lines) and lines[j].rstrip() == "":
                j += 1
            if j < len(lines) and lines[j].startswith("    "):
                block.append(line)
                i += 1
                continue
            else:
                break
        elif line.startswith("    "):
            block.append(line)
            i += 1
        else:
            break

    return block


def _dedent_line(line: str, spaces: int = 4) -> str:
    """Strip exactly `spaces` leading spaces from a line."""
    if line.startswith(" " * spaces):
        return line[spaces:]
    return line


def convert_admonitions(content: str) -> str:
    """Convert !!! and ??? admonition syntax to Docusaurus format."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # !!! type "Title" or !!! type
        adm_match = re.match(r'^!!! (\w+)(?: "(.+)")?', line)
        if adm_match:
            raw_type = adm_match.group(1)
            title = adm_match.group(2)
            adm_type = ADMONITION_TYPE_MAP.get(raw_type, "note")

            if title:
                result.append(f":::{adm_type}[{title}]")
            else:
                result.append(f":::{adm_type}")

            i += 1
            block = _collect_indented_block(lines, i)
            for bl in block:
                result.append(_dedent_line(bl))
            i += len(block)

            result.append(":::")
            continue

        # ??? type "Title"
        col_match = re.match(r'^\?\?\?\+? (\w+) "(.+)"', line)
        if col_match:
            title = col_match.group(2)

            result.append("<details>")
            result.append(f"<summary>{title}</summary>")
            result.append("")

            i += 1
            block = _collect_indented_block(lines, i)
            for bl in block:
                result.append(_dedent_line(bl))
            i += len(block)

            result.append("")
            result.append("</details>")
            continue

        result.append(line)
        i += 1

    return "\n".join(result)


def convert_fa_icons(content: str) -> str:
    """Strip Font Awesome <i> tags."""
    return re.sub(r'<i class="fa-[^"]*"></i>\s*', "", content)


def convert_icon_syntax(content: str) -> str:
    """Strip :material-*:, :octicons-*:, :simple-*: icon syntax."""
    # Icon with attributes: :material-clock-fast:{ .lg .middle }
    content = re.sub(r":[a-z]+-[a-z0-9-]+:\{[^}]*\}\s*", "", content)
    # Standalone icon: :octicons-arrow-right-24:
    # In link text: [:octicons-arrow-right-24: Text] -> [Text]
    content = re.sub(r"\[:[a-z]+-[a-z0-9-]+:\s*", "[", content)
    # Standalone outside links
    content = re.sub(r":[a-z]+-[a-z0-9-]+:\s*", "", content)
    return content


def convert_image_attributes(content: str) -> str:
    """Convert ![alt](src){ width="X" } to <img> tags."""

    def replace_img(m):
        alt = m.group(1).replace("\n", " ").strip()
        src = m.group(2)
        width = m.group(3)
        return f'<img src="{src}" alt="{alt}" width="{width}" />'

    return re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)\{\s*width="([^"]+)"\s*\}',
        replace_img,
        content,
        flags=re.DOTALL,
    )


def convert_file(content: str) -> str:
    """Apply all conversions in pipeline order."""
    content = convert_code_fences(content)
    content = convert_zoom_images(content)
    content = convert_grid_cards(content)
    content = convert_admonitions(content)
    content = convert_fa_icons(content)
    content = convert_icon_syntax(content)
    content = convert_image_attributes(content)
    return content


def find_files(
    paths: list[str], exclude_dirs: list[str], base_dir: Path
) -> list[Path]:
    """Find all .md files to process, respecting exclusions."""
    files = []
    for path_str in paths:
        p = base_dir / path_str
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            for md in sorted(p.rglob("*.md")):
                try:
                    rel = md.relative_to(base_dir / "docs")
                    if any(rel.parts[0] == exc for exc in exclude_dirs):
                        continue
                except ValueError:
                    pass
                files.append(md)
    return files


def main():
    parser = argparse.ArgumentParser(
        description="Convert mkdocs-material markdown to Docusaurus format"
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["docs", "cli", "impact"],
        help="Files or directories to process (relative to project root)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=DEFAULT_EXCLUDES,
        help="Directories to exclude within docs/",
    )
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent.parent
    files = find_files(args.paths, args.exclude, base_dir)

    if args.verbose:
        print(f"Found {len(files)} files to process", file=sys.stderr)

    changed = 0
    for filepath in files:
        original = filepath.read_text()
        converted = convert_file(original)

        if original == converted:
            if args.verbose:
                print(f"  (no changes) {filepath.relative_to(base_dir)}", file=sys.stderr)
            continue

        changed += 1
        rel = filepath.relative_to(base_dir)

        if args.dry_run:
            diff = difflib.unified_diff(
                original.splitlines(keepends=True),
                converted.splitlines(keepends=True),
                fromfile=f"a/{rel}",
                tofile=f"b/{rel}",
            )
            sys.stdout.writelines(diff)
        else:
            filepath.write_text(converted)
            if args.verbose:
                print(f"  converted {rel}", file=sys.stderr)

    print(f"\n{changed} file(s) {'would be ' if args.dry_run else ''}modified", file=sys.stderr)


if __name__ == "__main__":
    main()
