#!/usr/bin/env python3
"""Generate Docusaurus MD page for Bactopia acknowledgements from bactopia.json."""
import argparse
import json
import sys
from pathlib import Path

from generator_utils import create_jinja_env


CATEGORY_ORDER = [
    ('datasets_ariba', 'Ariba Reference Datasets'),
    ('datasets_minmer', 'Minmer Datasets'),
    ('datasets_generic', 'Everything Else'),
]


def load_acknowledgements(json_path):
    """Load citations from bactopia.json and group by category."""
    with open(json_path) as f:
        data = json.load(f)

    citations = data.get('citations', {})

    datasets = {}
    tools = {}
    influences = {}

    for key, entry in citations.items():
        cat = entry.get('category', '')
        if cat.startswith('datasets_'):
            datasets.setdefault(cat, []).append(entry)
        elif cat == 'tools':
            tools[key] = entry
        elif cat == 'influences':
            influences[key] = entry

    dataset_sections = []
    for cat_key, cat_title in CATEGORY_ORDER:
        items = datasets.get(cat_key, [])
        if items:
            dataset_sections.append({'title': cat_title, 'entries': items})

    total_datasets = sum(len(s['entries']) for s in dataset_sections)

    return {
        'influences': influences,
        'dataset_sections': dataset_sections,
        'total_datasets': total_datasets,
        'tools': tools,
        'total': total_datasets + len(tools) + len(influences),
    }


def main():
    parser = argparse.ArgumentParser(description='Generate acknowledgements MD page')
    parser.add_argument('bactopia_json', help='Path to bactopia.json')
    parser.add_argument('--output', '-o', default='impact/acknowledgements.md',
                        help='Output file path (default: impact/acknowledgements.md)')
    parser.add_argument('--template-dir', '-t', default='templates',
                        help='Template directory (default: templates)')
    args = parser.parse_args()

    json_path = Path(args.bactopia_json)
    if not json_path.exists():
        print(f'Error: {json_path} not found.', file=sys.stderr)
        sys.exit(1)

    ack = load_acknowledgements(json_path)

    env = create_jinja_env(args.template_dir)
    template = env.get_template('acknowledgements.j2')

    page = template.render(**ack)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(page)

    print(f'Generated acknowledgements page: {ack["total_datasets"]} datasets, '
          f'{len(ack["tools"])} tools, {len(ack["influences"])} influences at {output_path}')


if __name__ == '__main__':
    main()
