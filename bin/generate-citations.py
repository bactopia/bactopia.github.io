#!/usr/bin/env python3
"""Generate Docusaurus MD page for Bactopia citations from citations.yml."""
import argparse
import sys
from pathlib import Path

import yaml

from generator_utils import create_jinja_env


def load_citations(citations_path):
    """Load citations from YAML and extract year from date."""
    with open(citations_path) as f:
        raw = yaml.safe_load(f)

    citations = raw.get('citations', [])
    for entry in citations:
        d = entry.get('date', '')
        if hasattr(d, 'strftime'):
            entry['year'] = d.strftime('%Y')
        else:
            entry['year'] = str(d)[:4]
    return citations


def main():
    parser = argparse.ArgumentParser(description='Generate citations MD page')
    parser.add_argument('citations_yaml', help='Path to citations.yml')
    parser.add_argument('--output', '-o', default='impact/citations.md',
                        help='Output file path (default: impact/citations.md)')
    parser.add_argument('--template-dir', '-t', default='templates',
                        help='Template directory (default: templates)')
    args = parser.parse_args()

    citations_path = Path(args.citations_yaml)
    if not citations_path.exists():
        print(f'Error: {citations_path} not found.', file=sys.stderr)
        sys.exit(1)

    citations = load_citations(citations_path)

    env = create_jinja_env(args.template_dir)
    template = env.get_template('citations.j2')

    page = template.render(total=len(citations), citations=citations)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(page)

    print(f'Generated citations page with {len(citations)} entries at {output_path}')


if __name__ == '__main__':
    main()
