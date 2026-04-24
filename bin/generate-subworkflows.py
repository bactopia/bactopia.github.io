#!/usr/bin/env python3
"""
Generate Docusaurus MDX pages for Bactopia subworkflows from parsed metadata.
"""
import argparse
import json
import sys
from pathlib import Path

from generator_utils import (
    STATUS_BADGE, escape_mdx, normalize_tags, render_io_table, render_citations, tags_yaml,
    create_jinja_env, load_template,
)


def build_subworkflow_context(sw, data):
    """Build template context for a single subworkflow page."""
    scope = sw.get('scope', 'sample')
    tags = normalize_tags(sw.get('keywords', []) + [f'{scope}-scope'])

    badge_color = STATUS_BADGE.get(sw['status'], 'secondary')
    scope_label = sw.get('scope', 'sample')
    badges = (
        f'<span class="badge badge--{badge_color}">{sw["status"]}</span> '
        f'<span class="badge badge--info">{scope_label} scope</span>'
    )

    desc_parts = []
    if sw['summary']:
        desc_parts.append(escape_mdx(sw['summary']))
    if sw['description']:
        desc_parts.append('')
        desc_parts.append(escape_mdx(sw['description']))
    description = '\n'.join(desc_parts)

    # Take (inputs)
    inputs_section = render_io_table(
        sw.get('inputs', []), header='Take',
        nf_io=sw.get('nf_inputs'),
    )

    # Emit (outputs)
    PUBLISHED_NAMES = {'sample_outputs', 'run_outputs'}
    outputs = sw.get('outputs', [])
    outputs_section = ''
    if outputs:
        published = [o for o in outputs if o.get('name') in PUBLISHED_NAMES]
        downstream = [o for o in outputs if o.get('name') not in PUBLISHED_NAMES]

        lines = ['## Emit', '']

        def _render_emit_group(entries, lines):
            for out in entries:
                name = out.get('name', '')
                fields = out.get('fields', [])
                if name:
                    lines.append(f'#### `{name}`')
                    lines.append('')
                if fields:
                    lines.append('| Output | Description |')
                    lines.append('|--------|-------------|')
                    for field in fields:
                        fname = f'`{field["name"]}`' if field['name'] else ''
                        lines.append(f'| {fname} | {field.get("description", "")} |')
                    lines.append('')
                elif out.get('description'):
                    lines.append(out['description'])
                    lines.append('')
                elif name:
                    scope = 'sample' if 'sample' in name else 'run'
                    lines.append(f'No {scope}-scope outputs.')
                    lines.append('')

        lines.append('### Published')
        lines.append('')
        lines.append('The `sample_outputs` and `run_outputs` emissions are aggregates of output files that will be published in the entry workflow.')
        lines.append('')
        _render_emit_group(published, lines)

        if downstream:
            lines.append('### Downstream Inputs')
            lines.append('')
            lines.append('The following emissions are meant to be used as inputs to downstream subworkflows.')
            lines.append('')
            _render_emit_group(downstream, lines)

        outputs_section = '\n'.join(lines)

    # Composition
    comp_parts = []
    sw_list = sw.get('subworkflows', [])
    if sw_list:
        comp_parts.append('## Subworkflow Composition')
        comp_parts.append('')
        comp_parts.append('This subworkflow calls the following subworkflows:')
        comp_parts.append('')
        for sw_name in sw_list:
            sub = data['subworkflows'].get(sw_name, {})
            sub_summary = sub.get('summary', '')
            comp_parts.append(f'- [{sw_name}](/subworkflows/{sw_name}) - {sub_summary}')
        comp_parts.append('')

    mod_list = sw.get('modules', [])
    if mod_list:
        comp_parts.append('## Module Composition')
        comp_parts.append('')
        comp_parts.append('This subworkflow calls the following modules:')
        comp_parts.append('')
        for mod_name in mod_list:
            mod = data['modules'].get(mod_name, {})
            mod_summary = mod.get('summary', '')
            comp_parts.append(f'- [{mod_name}](/modules/{mod_name}) - {mod_summary}')
        comp_parts.append('')
    composition_section = '\n'.join(comp_parts)

    # Used By
    used_by_parts = []
    wf_list = sw.get('used_by_workflows', [])
    if wf_list:
        used_by_parts.append('## Used By')
        used_by_parts.append('')
        used_by_parts.append('This subworkflow is used by the following workflows:')
        used_by_parts.append('')
        for wf_name in sorted(wf_list):
            wf = data['workflows'].get(wf_name, {})
            wf_summary = wf.get('summary', '')
            wf_path = f'/workflows/bactopia-tools/{wf_name}' if wf.get('type') == 'tool' else f'/workflows/named-workflows/{wf_name}'
            used_by_parts.append(f'- [{wf_name}]({wf_path}) - {wf_summary}')
        used_by_parts.append('')
    used_by_section = '\n'.join(used_by_parts)

    # Citations
    citations_section = render_citations(sw.get('citations', []), data['citations'])

    return {
        'sw': sw,
        'data': data,
        'tags': tags,
        'badges': badges,
        'description': description,
        'inputs_section': inputs_section,
        'outputs_section': outputs_section,
        'composition_section': composition_section,
        'used_by_section': used_by_section,
        'citations_section': citations_section,
    }


def main():
    parser = argparse.ArgumentParser(description='Generate subworkflow MDX pages from parsed Bactopia metadata')
    parser.add_argument('catalog', help='Path to parsed bactopia.json')
    parser.add_argument('--output-dir', '-o', default='subworkflows',
                        help='Output directory for MDX files (default: subworkflows)')
    parser.add_argument('--template-dir', '-t', default='templates',
                        help='Template directory (default: templates)')
    args = parser.parse_args()

    catalog_path = Path(args.catalog)
    if not catalog_path.exists():
        print(f'Error: {catalog_path} not found. Run parse-bactopia.py first.', file=sys.stderr)
        sys.exit(1)

    with open(catalog_path) as f:
        data = json.load(f)

    env = create_jinja_env(args.template_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    subworkflows = data.get('subworkflows', {})
    for key in sorted(subworkflows.keys()):
        sw = subworkflows[key]
        template = load_template(env, 'subworkflow', key)
        context = build_subworkflow_context(sw, data)
        page = template.render(**context)
        (output_dir / f'{key}.mdx').write_text(page)

    # Index page
    index_template = env.get_template('subworkflow_index.j2')
    index_page = index_template.render(
        total=len(subworkflows),
        subworkflows=subworkflows,
        sorted_keys=sorted(subworkflows.keys()),
    )
    (output_dir / 'index.mdx').write_text(index_page)

    print(f'Generated {len(subworkflows)} subworkflow pages + index in {output_dir}/')


if __name__ == '__main__':
    main()
