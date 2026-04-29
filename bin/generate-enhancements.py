#!/usr/bin/env python3
"""Generate Docusaurus MD page for Bactopia enhancements from contributions.yml."""
import argparse
import sys
from pathlib import Path

import yaml

from generator_utils import create_jinja_env


def main():
    parser = argparse.ArgumentParser(description='Generate enhancements MD page')
    parser.add_argument('contributions_yaml', help='Path to contributions.yml')
    parser.add_argument('--output', '-o', default='impact/enhancements.md',
                        help='Output file path (default: impact/enhancements.md)')
    parser.add_argument('--template-dir', '-t', default='templates',
                        help='Template directory (default: templates)')
    args = parser.parse_args()

    yaml_path = Path(args.contributions_yaml)
    if not yaml_path.exists():
        print(f'Error: {yaml_path} not found.', file=sys.stderr)
        sys.exit(1)

    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    tools = data.get('tools', [])
    conda_submissions = data.get('conda_submissions', [])
    conda_updates = data.get('conda_updates', [])
    nfcore_modules = data.get('nfcore_modules', [])
    other = data.get('other', [])

    total = (len(tools) + len(conda_submissions) + len(conda_updates)
             + len(nfcore_modules) + len(other))

    env = create_jinja_env(args.template_dir)
    template = env.get_template('enhancements.j2')

    page = template.render(
        tools=tools,
        conda_submissions=conda_submissions,
        conda_updates=conda_updates,
        nfcore_modules=nfcore_modules,
        other=other,
        total_contributions=total,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(page)

    print(f'Generated enhancements page: {len(tools)} tools, '
          f'{len(conda_submissions)} submissions, {len(conda_updates)} updates, '
          f'{len(nfcore_modules)} nf-core, {len(other)} other ({total} total) '
          f'at {output_path}')


if __name__ == '__main__':
    main()
