#!/usr/bin/env python3
"""
Generate Docusaurus MDX pages for Bactopia modules from parsed metadata.
"""
import argparse
import json
import sys
from pathlib import Path

from generator_utils import (
    STATUS_BADGE, escape_mdx, normalize_tags, render_io_table, render_param_table,
    render_citations, tags_yaml,
    create_jinja_env, load_template,
)


def build_module_context(mod, data):
    """Build template context for a single module page."""
    scope = mod.get('scope', 'sample')
    tags = normalize_tags(mod.get('keywords', []) + [f'{scope}-scope'])

    badge_color = STATUS_BADGE.get(mod['status'], 'secondary')
    tool = mod.get('tool', {})
    tool_name = tool.get('name', '')
    tool_version = tool.get('version', '')
    scope_label = scope

    badge_parts = [f'<span class="badge badge--{badge_color}">{mod["status"]}</span>']
    if tool_name and tool_version:
        badge_parts.append(f'<span class="badge badge--secondary">{tool_name} v{tool_version}</span>')
    badge_parts.append(f'<span class="badge badge--info">{scope_label} scope</span>')
    badges = ' '.join(badge_parts)

    desc_parts = []
    if mod['summary']:
        desc_parts.append(escape_mdx(mod['summary']))
    if mod['description']:
        desc_parts.append('')
        desc_parts.append(escape_mdx(mod['description']))
    description = '\n'.join(desc_parts)

    # Notes
    notes_parts = []
    for note in mod.get('notes', []):
        title = note.get('title', '')
        body = note.get('body', '')
        if title:
            notes_parts.append(f':::note[{title}]')
        else:
            notes_parts.append(':::note')
        if body:
            notes_parts.append(escape_mdx(body))
        notes_parts.append(':::')
        notes_parts.append('')
    notes_section = '\n'.join(notes_parts)

    # Inputs
    inputs_section = render_io_table(
        mod.get('inputs', []), header='Inputs',
        nf_io=mod.get('nf_inputs'),
    )

    # Outputs
    outputs_section = render_io_table(
        mod.get('outputs', []), header='Outputs',
        nf_io=mod.get('nf_outputs'),
    )

    # Parameters
    params_parts = []
    params = mod.get('params', {})
    if params:
        params_parts.append('## Parameters')
        params_parts.append('')
        for group_key, group in params.items():
            table = render_param_table(group)
            if table:
                params_parts.append(table)
    params_section = '\n'.join(params_parts)

    # Used By
    used_by_parts = []
    sw_list = mod.get('used_by_subworkflows', [])
    wf_list = mod.get('used_by_workflows', [])
    if sw_list or wf_list:
        used_by_parts.append('## Used By')
        used_by_parts.append('')
        if sw_list:
            used_by_parts.append('### Subworkflows')
            used_by_parts.append('')
            for sw_name in sorted(sw_list):
                sw = data['subworkflows'].get(sw_name, {})
                sw_summary = sw.get('summary', '')
                used_by_parts.append(f'- [{sw_name}](/subworkflows/{sw_name}) - {sw_summary}')
            used_by_parts.append('')
        if wf_list:
            used_by_parts.append('### Workflows')
            used_by_parts.append('')
            for wf_name in sorted(wf_list):
                wf = data['workflows'].get(wf_name, {})
                wf_summary = wf.get('summary', '')
                wf_path = f'/workflows/bactopia-tools/{wf_name}' if wf.get('type') == 'tool' else f'/workflows/named-workflows/{wf_name}'
                used_by_parts.append(f'- [{wf_name}]({wf_path}) - {wf_summary}')
            used_by_parts.append('')
    used_by_section = '\n'.join(used_by_parts)

    # Citations
    citations_section = render_citations(mod.get('citations', []), data['citations'])

    return {
        'mod': mod,
        'data': data,
        'tags': tags,
        'badges': badges,
        'description': description,
        'notes_section': notes_section,
        'inputs_section': inputs_section,
        'outputs_section': outputs_section,
        'params_section': params_section,
        'used_by_section': used_by_section,
        'citations_section': citations_section,
    }


def main():
    parser = argparse.ArgumentParser(description='Generate module MDX pages from parsed Bactopia metadata')
    parser.add_argument('catalog', help='Path to parsed bactopia.json')
    parser.add_argument('--output-dir', '-o', default='modules',
                        help='Output directory for MDX files (default: modules)')
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

    modules = data.get('modules', {})
    for key in sorted(modules.keys()):
        mod = modules[key]
        template = load_template(env, 'module', key)
        context = build_module_context(mod, data)
        page = template.render(**context)
        (output_dir / f'{key}.mdx').write_text(page)

    # Index page
    index_template = env.get_template('module_index.j2')
    index_page = index_template.render(
        total=len(modules),
        modules=modules,
        sorted_keys=sorted(modules.keys()),
    )
    (output_dir / 'index.mdx').write_text(index_page)

    print(f'Generated {len(modules)} module pages + index in {output_dir}/')


if __name__ == '__main__':
    main()
