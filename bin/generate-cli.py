#!/usr/bin/env python3
"""Generate Docusaurus MDX pages for bactopia-py CLI commands from parsed metadata."""
import argparse
import json
import sys
from pathlib import Path

from generator_utils import escape_mdx, format_default, create_jinja_env


def build_option_sections(cmd_data):
    """Organize options into groups, using option_groups ordering if available."""
    groups_spec = cmd_data.get("option_groups", [])
    options = {o["name"]: o for o in cmd_data.get("options", [])}

    if not groups_spec:
        return [{"name": "Options", "options": list(options.values())}]

    result = []
    used = set()
    for group in groups_spec:
        group_opts = []
        for opt_flag in group.get("options", []):
            for opt in options.values():
                if opt_flag in opt.get("opts", []) and opt["name"] not in used:
                    group_opts.append(opt)
                    used.add(opt["name"])
                    break
        if group_opts:
            result.append({"name": group["name"], "options": group_opts})

    ungrouped = [o for o in options.values() if o["name"] not in used]
    if ungrouped:
        result.append({"name": "Other Options", "options": ungrouped})

    return result


def build_command_context(cmd_data):
    """Build template context for a single CLI command page."""
    usage_parts = [cmd_data["name"]]
    if cmd_data.get("is_group"):
        usage_parts.append("COMMAND")
    for arg in cmd_data.get("arguments", []):
        usage_parts.append(arg["human_readable_name"])
    usage_parts.append("[OPTIONS]")

    option_groups = build_option_sections(cmd_data)

    if cmd_data.get("is_group") and cmd_data.get("subcommands"):
        for sub in cmd_data["subcommands"].values():
            sub["grouped_options"] = build_option_sections(sub)

    return {
        "cmd": cmd_data,
        "usage": " ".join(usage_parts),
        "option_groups": option_groups,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate CLI reference MDX pages from parsed cli.json"
    )
    parser.add_argument("catalog", help="Path to cli.json")
    parser.add_argument(
        "--output-dir", "-o", default="developers/cli",
        help="Output directory for MDX files",
    )
    parser.add_argument(
        "--template-dir", "-t", default="templates",
        help="Template directory",
    )
    args = parser.parse_args()

    catalog_path = Path(args.catalog)
    if not catalog_path.exists():
        print(f"Error: {catalog_path} not found. Run parse-cli.py first.", file=sys.stderr)
        sys.exit(1)

    with open(catalog_path) as f:
        data = json.load(f)

    env = create_jinja_env(args.template_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    commands = data.get("commands", {})
    template = env.get_template("cli_command.j2")

    for key in sorted(commands.keys()):
        context = build_command_context(commands[key])
        page = template.render(**context)
        (output_dir / f"{key}.mdx").write_text(page)

    index_template = env.get_template("cli_index.j2")
    index_page = index_template.render(
        version=data["meta"]["version"],
        categories=data["categories"],
        commands=commands,
    )
    (output_dir / "index.mdx").write_text(index_page)

    print(f"Generated {len(commands)} CLI pages + index in {output_dir}/")


if __name__ == "__main__":
    main()
