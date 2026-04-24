#!/usr/bin/env python3
"""
Generate Docusaurus MDX pages for Bactopia workflows from parsed metadata.
"""
import argparse
import json
import sys
from pathlib import Path

from generator_utils import (
    STATUS_BADGE, escape_mdx, normalize_tags, render_param_table,
    render_citations, render_shared_params, render_output_tree, tags_yaml,
    create_jinja_env, load_template,
)


def build_workflow_context(wf, data):
    """Build template context for a single workflow page."""
    tags = normalize_tags(wf.get('keywords', []))
    wf_type_tag = 'named-workflow' if wf['type'] == 'named' else 'bactopia-tool'
    if wf_type_tag not in tags:
        tags.append(wf_type_tag)

    badges = ''

    desc_parts = []
    if wf['summary']:
        desc_parts.append(escape_mdx(wf['summary']))
    if wf['description']:
        desc_parts.append('')
        desc_parts.append(escape_mdx(wf['description']))
    description = '\n'.join(desc_parts)

    # Parameters: required first, then tool-specific, then remaining shared
    params_parts = ['## Parameters', '']

    shared_key = wf.get('params', {}).get('shared_schema', '')
    shared_params = data.get('shared_params', {})
    schema = shared_params.get(shared_key, {})

    # Required parameters first (always visible)
    required = schema.get('input_parameters', {})
    required_table = render_param_table(required) if required else ''
    if required_table:
        params_parts.append(required_table)

    # Tool-specific parameters
    tool_params = wf.get('params', {}).get('tool_specific', {})
    has_tool_params = False
    for group_key, group in tool_params.items():
        table = render_param_table(group)
        if table:
            params_parts.append(table)
            has_tool_params = True

    # Remaining shared parameters (skip input_parameters, already rendered)
    shared_block = render_shared_params(shared_params, shared_key, skip_keys={'input_parameters'})
    if shared_block:
        params_parts.append(shared_block)

    params_section = '\n'.join(params_parts) if (has_tool_params or shared_block or required_table) else ''

    # Outputs
    outputs_parts = []
    output_tree = wf.get('output_tree', [])
    published = wf.get('published_outputs', [])
    if published or output_tree:
        outputs_parts.append('## Outputs')
        outputs_parts.append('')
        tree_block = render_output_tree(output_tree)
        if tree_block:
            outputs_parts.append(tree_block)
        skip_sections = {'Execution Logs', 'Versions'}
        for section in published:
            if section['name'] in skip_sections:
                continue
            outputs_parts.append(f'### {section["name"]}')
            outputs_parts.append('')
            if section.get('notes'):
                for note in section['notes']:
                    outputs_parts.append(':::note')
                    outputs_parts.append(note)
                    outputs_parts.append(':::')
                    outputs_parts.append('')
            if section.get('files'):
                outputs_parts.append('| File | Description |')
                outputs_parts.append('|------|-------------|')
                for f in section['files']:
                    outputs_parts.append(f'| `{f["pattern"]}` | {f["description"]} |')
                outputs_parts.append('')
    outputs_section = '\n'.join(outputs_parts)

    # Composition
    comp_parts = []
    sw_list = wf.get('uses_subworkflows', [])
    if sw_list:
        comp_parts.append('## Composition')
        comp_parts.append('')
        comp_parts.append('This workflow uses the following subworkflows:')
        comp_parts.append('')
        for sw_name in sorted(sw_list):
            sw = data['subworkflows'].get(sw_name, {})
            sw_summary = sw.get('summary', '')
            comp_parts.append(f'- [{sw_name}](/developers/subworkflows/{sw_name}) - {sw_summary}')
        comp_parts.append('')
    composition_section = '\n'.join(comp_parts)

    # Citations
    citations_section = render_citations(wf.get('citations', []), data['citations'])

    tag_base = '/bactopia-tools' if wf['type'] == 'tool' else '/bactopia-pipelines'

    return {
        'wf': wf,
        'data': data,
        'tags': tags,
        'tag_base': tag_base,
        'badges': badges,
        'description': description,
        'params_section': params_section,
        'outputs_section': outputs_section,
        'composition_section': composition_section,
        'citations_section': citations_section,
    }


def main():
    parser = argparse.ArgumentParser(description='Generate workflow MDX pages from parsed Bactopia metadata')
    parser.add_argument('catalog', help='Path to parsed bactopia.json')
    parser.add_argument('--tools-dir', default='bactopia-tools',
                        help='Output directory for Bactopia Tools (default: bactopia-tools)')
    parser.add_argument('--pipelines-dir', default='bactopia-pipelines',
                        help='Output directory for Bactopia Pipelines (default: bactopia-pipelines)')
    parser.add_argument('--docs-dir', default='docs',
                        help='Output directory for main docs (default: docs)')
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
    tools_dir = Path(args.tools_dir)
    tools_dir.mkdir(parents=True, exist_ok=True)
    pipelines_dir = Path(args.pipelines_dir)
    pipelines_dir.mkdir(parents=True, exist_ok=True)
    docs_dir = Path(args.docs_dir)

    workflows = data.get('workflows', {})

    for key in sorted(workflows.keys()):
        wf = workflows[key]
        template = load_template(env, 'workflow', key)
        context = build_workflow_context(wf, data)
        page = template.render(**context)
        if wf['type'] == 'tool':
            (tools_dir / f'{key}.mdx').write_text(page)
        elif key == 'bactopia':
            page = page.replace(
                'title: bactopia\n',
                'title: Bactopia Workflow\nsidebar_label: Bactopia Workflow\nsidebar_position: 6\n',
                1,
            )
            page = page.replace('  - named-workflow\n', '', 1)
            (docs_dir / 'bactopia-workflow.mdx').write_text(page)
        else:
            (pipelines_dir / f'{key}.mdx').write_text(page)

    # Index pages
    named = {k: v for k, v in workflows.items() if v['type'] == 'named' and k != 'bactopia'}
    tools = {k: v for k, v in workflows.items() if v['type'] == 'tool'}

    named_index_template = env.get_template('named_workflows_index.j2')
    named_index_page = named_index_template.render(
        total=len(named),
        named=named,
        named_keys=sorted(named.keys()),
    )
    (pipelines_dir / 'index.mdx').write_text(named_index_page)

    tools_index_template = env.get_template('bactopia_tools_index.j2')
    tools_index_page = tools_index_template.render(
        total=len(tools),
        tools=tools,
        tools_keys=sorted(tools.keys()),
    )
    (tools_dir / 'index.mdx').write_text(tools_index_page)

    print(f'Generated {len(named)} pipeline + {len(tools)} tool workflow pages + indexes')


if __name__ == '__main__':
    main()
