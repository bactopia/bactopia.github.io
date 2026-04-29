#!/usr/bin/env python3
"""Parse bactopia-py CLI commands via Click introspection and write cli.json."""
import argparse
import copy
import importlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import click
import rich_click.rich_click as rc_globals

import bactopia

CONSOLE_SCRIPTS = {
    "bactopia-citations": ("bactopia.cli.citations", "user"),
    "bactopia-datasets": ("bactopia.cli.datasets", "user"),
    "bactopia-download": ("bactopia.cli.download", "user"),
    "bactopia-prepare": ("bactopia.cli.prepare", "user"),
    "bactopia-search": ("bactopia.cli.search", "user"),
    "bactopia-summary": ("bactopia.cli.summary", "user"),
    "bactopia-update": ("bactopia.cli.update", "user"),
    "bactopia-status": ("bactopia.cli.status", "user"),
    "bactopia-sysinfo": ("bactopia.cli.sysinfo", "user"),
    "bactopia-workflows": ("bactopia.cli.workflows", "user"),
    "bactopia-atb-formatter": ("bactopia.cli.atb.atb_formatter", "user"),
    "bactopia-atb-downloader": ("bactopia.cli.atb.atb_downloader", "user"),
    "bactopia-merge-schemas": ("bactopia.cli.helpers.merge_schemas", "user"),
    "bactopia-pubmlst-setup": ("bactopia.cli.pubmlst.setup", "user"),
    "bactopia-prune": ("bactopia.cli.prune", "user"),
    "bactopia-pubmlst-build": ("bactopia.cli.pubmlst.build", "user"),
    "bactopia-test": ("bactopia.cli.testing", "user"),
    "bactopia-lint": ("bactopia.cli.lint", "user"),
    "bactopia-catalog": ("bactopia.cli.catalog", "user"),
    "bactopia-review-tests": ("bactopia.cli.review", "user"),
    "bactopia-docs": ("bactopia.cli.docs", "user"),
    "bactopia-scaffold": ("bactopia.cli.scaffold", "user"),
    "bactopia-check-fastqs": ("bactopia.cli.pipeline.check_fastqs", "pipeline"),
    "bactopia-check-assembly-accession": ("bactopia.cli.pipeline.check_assembly_accession", "pipeline"),
    "bactopia-cleanup-coverage": ("bactopia.cli.pipeline.cleanup_coverage", "pipeline"),
    "bactopia-mask-consensus": ("bactopia.cli.pipeline.mask_consensus", "pipeline"),
    "bactopia-kraken-bracken-summary": ("bactopia.cli.pipeline.kraken_bracken_summary", "pipeline"),
    "bactopia-scrubber-summary": ("bactopia.cli.pipeline.scrubber_summary", "pipeline"),
    "bactopia-teton-prepare": ("bactopia.cli.pipeline.teton_prepare", "pipeline"),
    "bactopia-bracken-to-excel": ("bactopia.cli.pipeline.bracken_to_excel", "pipeline"),
}

CATEGORIES = {
    "user": {
        "label": "User & Developer Commands",
        "description": "Commands for preparing inputs, querying databases, and developing Bactopia components.",
    },
    "pipeline": {
        "label": "Pipeline Utility Scripts",
        "description": "Internal scripts called by Nextflow modules during pipeline execution.",
    },
}


def find_click_command(module):
    """Find the Click command object in a module."""
    for attr in vars(module).values():
        if isinstance(attr, click.Command):
            return attr
    return None


def format_type(param_type):
    """Format a Click parameter type for display."""
    if hasattr(param_type, "choices"):
        return "CHOICE"
    name = str(param_type)
    if name.startswith("<") or "object at" in name:
        type_class = type(param_type).__name__.upper()
        return type_class if type_class != "PARAMTYPE" else "STRING"
    return name


def extract_param(param):
    """Extract structured data from a Click parameter."""
    if isinstance(param, click.Argument):
        return {
            "kind": "argument",
            "name": param.name,
            "type": format_type(param.type),
            "required": param.required,
            "nargs": param.nargs,
            "human_readable_name": param.human_readable_name,
            "help": getattr(param, "help", None) or "",
        }
    default = param.default
    if default is not None and "Sentinel" in str(type(default)):
        default = None

    return {
        "kind": "option",
        "name": param.name,
        "opts": list(param.opts) + list(param.secondary_opts or []),
        "type": format_type(param.type),
        "required": getattr(param, "required", False),
        "default": default,
        "is_flag": getattr(param, "is_flag", False),
        "help": getattr(param, "help", "") or "",
        "choices": list(param.type.choices) if hasattr(param.type, "choices") else None,
    }


def extract_command(cmd_name, cmd, category, option_groups):
    """Extract structured data from a Click command."""
    params = [extract_param(p) for p in cmd.params]
    arguments = [p for p in params if p["kind"] == "argument"]
    options = [p for p in params if p["kind"] == "option"]

    result = {
        "name": cmd_name,
        "help": cmd.help or "",
        "is_group": isinstance(cmd, click.Group),
        "category": category,
        "arguments": arguments,
        "options": options,
        "option_groups": option_groups.get(cmd_name, []),
    }

    if isinstance(cmd, click.Group):
        subcommands = {}
        for sub_name, sub_cmd in sorted(cmd.commands.items()):
            sub_params = [extract_param(p) for p in sub_cmd.params]
            sub_arguments = [p for p in sub_params if p["kind"] == "argument"]
            sub_options = [p for p in sub_params if p["kind"] == "option"]
            subcommands[sub_name] = {
                "name": sub_name,
                "help": sub_cmd.help or "",
                "arguments": sub_arguments,
                "options": sub_options,
                "option_groups": option_groups.get(f"{cmd_name} {sub_name}", []),
            }
        result["subcommands"] = subcommands

    return result


def main():
    parser = argparse.ArgumentParser(description="Parse bactopia-py CLI commands into JSON")
    parser.add_argument("--output", "-o", default="data/cli.json", help="Output JSON path")
    args = parser.parse_args()

    commands = {}
    category_commands = {"user": [], "pipeline": []}
    errors = []

    for cmd_name, (module_path, category) in sorted(CONSOLE_SCRIPTS.items()):
        try:
            rc_globals.OPTION_GROUPS = {}
            mod = importlib.import_module(module_path)
            option_groups = copy.deepcopy(rc_globals.OPTION_GROUPS)

            cmd = find_click_command(mod)
            if cmd is None:
                errors.append(f"{cmd_name}: no Click command found in {module_path}")
                continue
            commands[cmd_name] = extract_command(cmd_name, cmd, category, option_groups)
            category_commands[category].append(cmd_name)
        except Exception as e:
            errors.append(f"{cmd_name}: {e}")

    if errors:
        for err in errors:
            print(f"Warning: {err}", file=sys.stderr)

    categories = {}
    for key, meta in CATEGORIES.items():
        categories[key] = {
            **meta,
            "commands": sorted(category_commands[key]),
        }

    output = {
        "meta": {
            "version": bactopia.__version__,
            "generated": datetime.now(timezone.utc).isoformat(),
        },
        "categories": categories,
        "commands": commands,
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"Parsed {len(commands)} CLI commands -> {output_path}")


if __name__ == "__main__":
    main()
