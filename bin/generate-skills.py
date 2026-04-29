#!/usr/bin/env python3
"""Extract structured metadata from Bactopia SKILL.md files for docs generation."""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml


CATEGORY_MAP = {
    "add-": "Scaffolding",
    "update-": "Maintenance",
    "merge-": "Maintenance",
    "review-": "Review & Quality",
    "run-": "Testing",
    "project-": "Project",
}

CATEGORY_ORDER = [
    "Scaffolding",
    "Maintenance",
    "Review & Quality",
    "Testing",
    "Project",
]


def categorize(name):
    """Assign a category based on the skill name prefix."""
    for prefix, category in CATEGORY_MAP.items():
        if name.startswith(prefix):
            return category
    return "Other"


def first_sentence(text):
    """Extract the first sentence from a description string."""
    text = re.sub(r"\s+", " ", text).strip()
    match = re.match(r"(.+?\.)\s", text + " ")
    return match.group(1) if match else text


def extract_summary(body):
    """Extract the first paragraph after the top-level heading."""
    lines = body.strip().splitlines()
    para_lines = []
    in_para = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            if in_para:
                break
            continue
        if not stripped:
            if in_para:
                break
            continue
        in_para = True
        para_lines.append(stripped)
    return " ".join(para_lines) if para_lines else ""


def find_cli_command(skill_dir, body):
    """Extract the CLI command name from the wrapper script or SKILL.md body."""
    scripts_dir = skill_dir / "scripts"
    if scripts_dir.is_dir():
        for script in sorted(scripts_dir.glob("run-*.sh")):
            text = script.read_text()
            match = re.search(r"exec.*?(bactopia-[\w-]+)", text)
            if match:
                return match.group(1)
    # Fallback: find the first bactopia-* command referenced in code blocks
    for match in re.finditer(r"`(bactopia-[\w-]+)`", body):
        cmd = match.group(1)
        if cmd not in ("bactopia-path", "bactopia-tool", "bactopia-tools"):
            return cmd
    return None


def parse_skill(skill_dir):
    """Parse a single SKILL.md and its wrapper script."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None

    content = skill_md.read_text()

    fm_match = re.match(r"^---\n(.+?)\n---\n(.*)$", content, re.DOTALL)
    if not fm_match:
        print(f"Warning: no frontmatter in {skill_md}", file=sys.stderr)
        return None

    frontmatter = yaml.safe_load(fm_match.group(1))
    body = fm_match.group(2)

    name = frontmatter.get("name", skill_dir.name)
    description = frontmatter.get("description", "")
    cli_command = find_cli_command(skill_dir, body)

    return {
        "name": name,
        "description": description,
        "first_sentence": first_sentence(description),
        "summary": extract_summary(body),
        "category": categorize(name),
        "cli_command": cli_command,
        "cli_page": f"/developers/cli/{cli_command}" if cli_command else None,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract metadata from Bactopia SKILL.md files"
    )
    parser.add_argument(
        "skills_dir",
        help="Path to the .claude/skills/ directory in the bactopia repo",
    )
    parser.add_argument(
        "--json", action="store_true", dest="as_json",
        help="Output as JSON (default: human-readable summary)",
    )
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    if not skills_dir.is_dir():
        print(f"Error: {skills_dir} is not a directory.", file=sys.stderr)
        sys.exit(1)

    skills = []
    for child in sorted(skills_dir.iterdir()):
        if not child.is_dir():
            continue
        skill = parse_skill(child)
        if skill:
            skills.append(skill)

    if not skills:
        print("No SKILL.md files found.", file=sys.stderr)
        sys.exit(1)

    if args.as_json:
        by_category = {}
        for cat in CATEGORY_ORDER:
            members = [s for s in skills if s["category"] == cat]
            if members:
                by_category[cat] = members
        output = {
            "total": len(skills),
            "categories": CATEGORY_ORDER,
            "by_category": by_category,
            "skills": skills,
        }
        json.dump(output, sys.stdout, indent=2)
        print()
    else:
        print(f"Found {len(skills)} skills:\n")
        for cat in CATEGORY_ORDER:
            members = [s for s in skills if s["category"] == cat]
            if not members:
                continue
            print(f"  {cat}:")
            for s in members:
                wraps = s["cli_command"] or "unknown"
                print(f"    {s['name']:30s} wraps {wraps}")
        print()


if __name__ == "__main__":
    main()
