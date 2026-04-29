#!/usr/bin/env python3
"""Generate the grouped bactopia-tools/index.mdx from tool-categories.yml."""
import argparse
import sys
from pathlib import Path

import yaml


def parse_description(mdx_path):
    """Extract the description field from MDX frontmatter."""
    in_frontmatter = False
    for line in mdx_path.read_text().splitlines():
        if line.strip() == '---':
            if in_frontmatter:
                break
            in_frontmatter = True
            continue
        if in_frontmatter and line.startswith('description:'):
            desc = line.split(':', 1)[1].strip().strip('"').strip("'")
            return desc
    return ''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('categories_file', help='Path to tool-categories.yml')
    parser.add_argument('--tools-dir', default='bactopia-tools/',
                        help='Directory containing tool MDX files')
    parser.add_argument('--output', default='bactopia-tools/index.mdx',
                        help='Output index file path')
    args = parser.parse_args()

    tools_dir = Path(args.tools_dir)
    categories_data = yaml.safe_load(Path(args.categories_file).read_text())
    categories = categories_data['categories']

    tool_files = {
        p.stem for p in tools_dir.glob('*.mdx')
        if not p.stem.startswith('index')
    }

    mapped_tools = set()
    for cat in categories:
        for tool in cat['tools']:
            mapped_tools.add(tool)

    missing = tool_files - mapped_tools
    if missing:
        print(f"Error: {len(missing)} tool(s) not in categories mapping: "
              f"{', '.join(sorted(missing))}", file=sys.stderr)
        sys.exit(1)

    stale = mapped_tools - tool_files
    if stale:
        print(f"Warning: {len(stale)} tool(s) in mapping but no MDX file found: "
              f"{', '.join(sorted(stale))}", file=sys.stderr)

    total_tools = len(tool_files)
    num_categories = len(categories)

    lines = [
        '---',
        'title: Bactopia Tools',
        'description: All available Bactopia Tool workflows',
        'sidebar_position: 2',
        '---',
        '',
        '# Bactopia Tools',
        '',
        f'Bactopia Tools are additional analysis workflows that run specific tools on existing',
        f'Bactopia results. There are {total_tools} Bactopia Tools available across '
        f'{num_categories} categories.',
        'You can also [browse by tag](/bactopia-tools/tags).',
        '',
    ]

    for cat in categories:
        lines.append(f'## {cat["name"]}')
        lines.append('')
        lines.append(cat['description'])
        lines.append('')
        lines.append('| Workflow | Description |')
        lines.append('|----------|-------------|')

        for tool_name in sorted(cat['tools']):
            mdx_path = tools_dir / f'{tool_name}.mdx'
            if not mdx_path.exists():
                continue
            desc = parse_description(mdx_path)
            lines.append(f'| [{tool_name}](/bactopia-tools/{tool_name}) | {desc} |')

        lines.append('')

    output = Path(args.output)
    output.write_text('\n'.join(lines))
    print(f"Generated {output} ({total_tools} tools, {num_categories} categories)")


if __name__ == '__main__':
    main()
