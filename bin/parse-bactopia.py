#!/usr/bin/env python3
"""
Parse Bactopia v4 metadata (catalog.json, groovydoc, schema.json, citations.yml)
into a unified JSON file for documentation generators.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


def parse_groovydoc(text):
    """Extract and parse the /** ... */ groovydoc block from a main.nf file."""
    m = re.search(r'/\*\*(.*?)\*/', text, re.DOTALL)
    if not m:
        return {}

    raw = m.group(1)
    lines = []
    for line in raw.split('\n'):
        stripped = line.strip()
        if stripped.startswith('* '):
            lines.append(stripped[2:])
        elif stripped == '*':
            lines.append('')
        elif stripped.startswith('*'):
            lines.append(stripped[1:])

    result = {
        'summary': '',
        'description': '',
        'status': '',
        'keywords': [],
        'tags': {},
        'citations': [],
        'notes': [],
        'subworkflows': [],
        'modules': [],
        'inputs': [],
        'outputs': [],
        'sections': [],
    }

    summary_lines = []
    body_lines = []
    in_body = False
    current_tag = None
    current_tag_value = []
    current_section = None

    def flush_tag():
        nonlocal current_tag, current_tag_value, current_section
        if current_tag is None:
            return

        value = '\n'.join(current_tag_value).strip()

        if current_tag == 'status':
            result['status'] = value

        elif current_tag == 'keywords':
            result['keywords'] = [k.strip() for k in value.split(',') if k.strip()]

        elif current_tag == 'tags':
            for token in value.split():
                if ':' in token:
                    k, v = token.split(':', 1)
                    k = k.strip()
                    v = v.strip()
                    if k == 'features':
                        result['tags'][k] = [f.strip() for f in v.split(',') if f.strip()]
                    else:
                        result['tags'][k] = v

        elif current_tag == 'citation':
            for part in re.split(r'[,\n]', value):
                part = part.strip()
                if part:
                    result['citations'].append(part)

        elif current_tag == 'note':
            first_line, _, rest = value.partition('\n')
            result['notes'].append({
                'title': first_line.strip(),
                'body': rest.strip(),
            })

        elif current_tag == 'subworkflows':
            for part in re.split(r'[,\n]', value):
                part = part.strip().split(' as ')[0].strip()
                if part:
                    result['subworkflows'].append(part)

        elif current_tag == 'modules':
            for part in re.split(r'[,\n]', value):
                part = part.strip().split(' as ')[0].strip()
                if part:
                    result['modules'].append(part)

        elif current_tag == 'input':
            input_entry = parse_io_block(value)
            result['inputs'].append(input_entry)

        elif current_tag == 'output':
            output_entry = parse_io_block(value)
            result['outputs'].append(output_entry)

        elif current_tag == 'section':
            current_section = {'name': value, 'notes': [], 'files': []}
            result['sections'].append(current_section)

        elif current_tag == 'publish':
            if current_section is not None:
                pattern, _, desc = value.partition(' ')
                desc = desc.strip()
                while '  ' in desc:
                    desc = desc.replace('  ', ' ')
                current_section['files'].append({
                    'pattern': pattern.strip(),
                    'description': desc,
                })

        current_tag = None
        current_tag_value = []

    for line in lines:
        tag_match = re.match(r'^@(\w+)\s*(.*)', line)

        if tag_match:
            flush_tag()
            tag_name = tag_match.group(1)
            tag_rest = tag_match.group(2).strip()

            if tag_name == 'note' and current_section is not None:
                current_section['notes'].append(tag_rest)
            elif tag_name == 'publish':
                current_tag = 'publish'
                current_tag_value = [tag_rest]
                flush_tag()
            else:
                current_tag = tag_name
                current_tag_value = [tag_rest]
                in_body = False
        elif current_tag is not None:
            current_tag_value.append(line)
        elif not in_body and line == '':
            if summary_lines:
                in_body = True
        elif in_body:
            body_lines.append(line)
        else:
            summary_lines.append(line)

    flush_tag()

    result['summary'] = ' '.join(summary_lines).strip()
    result['description'] = '\n'.join(body_lines).strip()

    return result


def parse_io_block(value):
    """Parse an @input or @output block into structured data."""
    lines = value.split('\n')
    first_line = lines[0].strip().rstrip('?')
    if first_line.startswith('record('):
        name = first_line
    else:
        parts = first_line.split(None, 1)
        name = parts[0] if parts else first_line
    fields = []
    description_lines = []
    if not first_line.startswith('record('):
        parts = first_line.split(None, 1)
        if len(parts) > 1:
            description_lines.append(parts[1])
    for line in lines[1:]:
        line = line.strip()
        field_match = re.match(r'^-\s*`(\w+\??)`\s*:\s*(.*)', line)
        if field_match:
            fields.append({
                'name': field_match.group(1).rstrip('?'),
                'description': field_match.group(2).strip(),
            })
        elif line.startswith('- '):
            text = line[2:].strip()
            fields.append({'name': '', 'description': text})
        elif line:
            description_lines.append(line)
    description = ' '.join(description_lines).strip()
    return {'name': name, 'description': description, 'fields': fields}


COMMON_OUTPUT_DESCRIPTIONS = {
    'meta': 'Sample information record',
    'results': 'All output files to be published',
    'logs': 'Optional program specific log files',
    'nf_logs': 'Nextflow-specific log files (e.g. .command.{begin|err|log|out|run|sh|trace})',
    'versions': 'A YAML formatted file with program versions',
}


def parse_nf_input_block(text):
    """Parse the Nextflow input: block to extract field type information."""
    m = re.search(r'\n\s+input:\s*\n(.*?)\n\s+(?:output|stage):', text, re.DOTALL)
    if not m:
        return {'records': [], 'standalone': []}

    block = m.group(1)
    records = []
    standalone = []

    for rec_match in re.finditer(r'record\s*\(\s*(.*?)\)', block, re.DOTALL):
        rec_body = rec_match.group(1)
        fields = []
        for field_match in re.finditer(r'(\w+)\s*:\s*([\w<>?]+)', rec_body):
            fields.append({
                'name': field_match.group(1),
                'type': field_match.group(2),
            })
        if fields:
            records.append({'fields': fields})

    record_span_end = 0
    for rec_match in re.finditer(r'record\s*\(.*?\)', block, re.DOTALL):
        record_span_end = max(record_span_end, rec_match.end())

    remaining = block[record_span_end:]
    for sa_match in re.finditer(
        r'(\w+)\s*:\s*((?:Set<)?(?:Path|String|Integer|Boolean|Record)(?:>)?\??)', remaining
    ):
        standalone.append({
            'name': sa_match.group(1),
            'type': sa_match.group(2),
        })

    return {'records': records, 'standalone': standalone}


def _derive_output_type(value_expr):
    """Derive a type string from a Nextflow output value expression."""
    value_expr = value_expr.strip()
    if re.match(r'^\w+$', value_expr) and not value_expr.startswith(('file', 'files')):
        return 'Record'
    if value_expr.startswith('file('):
        if 'optional: true' in value_expr or 'optional:true' in value_expr:
            return 'Path?'
        return 'Path'
    if value_expr.startswith('files('):
        if 'optional: true' in value_expr or 'optional:true' in value_expr:
            return 'Set<Path?>'
        return 'Set<Path>'
    if value_expr.startswith('['):
        return 'Set<Path>'
    return 'Path'


def parse_nf_output_block(text):
    """Parse the Nextflow output: block to extract field type information."""
    m = re.search(r'\n\s+output:\s*\n(.*?)\n\s+(?:script|exec|shell):', text, re.DOTALL)
    if not m:
        return {'records': []}

    block = m.group(1)
    records = []

    for rec_match in re.finditer(r'record\s*\(\s*(.*?)\n\s*\)', block, re.DOTALL):
        rec_body = rec_match.group(1)
        fields = []
        clean_lines = []
        in_list = 0
        for line in rec_body.split('\n'):
            stripped = line.strip()
            if stripped.startswith('//'):
                continue
            in_list += stripped.count('[') - stripped.count(']')
            if in_list > 0 and not re.match(r'^\s*\w+\s*:', line):
                continue
            clean_lines.append(line)
        clean_body = '\n'.join(clean_lines)

        for field_match in re.finditer(
            r'(\w+)\s*:\s*(.+?)(?:,\s*$|\s*$)', clean_body, re.MULTILINE
        ):
            fname = field_match.group(1)
            fvalue = field_match.group(2).strip().rstrip(',')
            ftype = _derive_output_type(fvalue)
            fields.append({'name': fname, 'type': ftype})

        if fields:
            records.append({'fields': fields})

    return {'records': records}


def merge_io_types(groovydoc_inputs, nf_inputs):
    """Merge NF-parsed type info into groovydoc @input entries."""
    type_map = {}
    for rec in nf_inputs.get('records', []):
        for field in rec.get('fields', []):
            type_map[field['name']] = field['type']
    for sa in nf_inputs.get('standalone', []):
        type_map[sa['name']] = sa['type']

    result = []
    for entry in groovydoc_inputs:
        new_entry = dict(entry)
        new_fields = []
        for field in entry.get('fields', []):
            new_field = dict(field)
            fname = field['name'].rstrip('?')
            if fname in type_map:
                new_field['type'] = type_map[fname]
            new_fields.append(new_field)
        new_entry['fields'] = new_fields
        # For standalone entries (no fields), attach the type directly
        if not new_fields:
            entry_name = entry.get('name', '').rstrip('?')
            if entry_name in type_map:
                new_entry['type'] = type_map[entry_name]
        result.append(new_entry)
    return result


def merge_io_types_output(groovydoc_outputs, nf_outputs):
    """Merge NF-parsed type info into groovydoc @output entries, ordered by NF record."""
    nf_records = nf_outputs.get('records', [])

    # Build description lookup from groovydoc fields
    desc_map = {}
    for entry in groovydoc_outputs:
        for field in entry.get('fields', []):
            fname = field['name'].rstrip('?')
            if field.get('description'):
                desc_map[fname] = field['description']

    result = []
    for i, entry in enumerate(groovydoc_outputs):
        new_entry = dict(entry)

        if i < len(nf_records):
            # Build fields in NF record order
            new_fields = []
            for nf_field in nf_records[i]['fields']:
                fname = nf_field['name']
                desc = desc_map.get(fname, COMMON_OUTPUT_DESCRIPTIONS.get(fname, ''))
                new_fields.append({
                    'name': fname,
                    'type': nf_field['type'],
                    'description': desc,
                })
            new_entry['fields'] = new_fields
        else:
            # Fallback: no matching NF record, keep groovydoc fields as-is
            new_entry['fields'] = list(entry.get('fields', []))

        result.append(new_entry)
    return result


def parse_nf_take_block(text):
    """Parse the Nextflow take: block from a subworkflow to extract parameter types."""
    m = re.search(r'\n\s+take:\s*\n(.*?)\n\s+main:', text, re.DOTALL)
    if not m:
        return {'standalone': []}

    block = m.group(1)
    standalone = []
    for line_match in re.finditer(r'(\w+)\s*:\s*([\w<>?]+)', block):
        standalone.append({
            'name': line_match.group(1),
            'type': line_match.group(2),
        })

    return {'standalone': standalone}


def merge_take_types(groovydoc_inputs, take_inputs):
    """Merge NF take: block types into groovydoc @input entries for subworkflows."""
    take_params = take_inputs.get('standalone', [])

    record_takes = [p for p in take_params if p['type'] == 'Channel<Record>']
    standalone_takes = {p['name']: p['type'] for p in take_params if p['type'] != 'Channel<Record>'}

    result = []
    rec_idx = 0
    for entry in groovydoc_inputs:
        new_entry = dict(entry)
        if entry.get('fields'):
            if rec_idx < len(record_takes):
                new_entry['take_name'] = record_takes[rec_idx]['name']
                new_entry['take_type'] = record_takes[rec_idx]['type']
                rec_idx += 1
            new_entry['fields'] = list(entry['fields'])
        else:
            entry_name = entry.get('name', '').rstrip('?')
            if entry_name in standalone_takes:
                new_entry['type'] = standalone_takes[entry_name]
        result.append(new_entry)
    return result


def load_schema(schema_path):
    """Load a JSON schema and extract parameter definitions from $defs."""
    if not schema_path.exists():
        return {}
    with open(schema_path) as f:
        schema = json.load(f)
    defs = schema.get('$defs', schema.get('definitions', {}))
    params = {}
    for group_key, group_val in defs.items():
        if not isinstance(group_val, dict) or 'properties' not in group_val:
            continue
        params[group_key] = {
            'title': group_val.get('title', group_key),
            'description': group_val.get('description', ''),
            'fa_icon': group_val.get('fa_icon', ''),
            'properties': {},
        }
        for prop_key, prop_val in group_val.get('properties', {}).items():
            params[group_key]['properties'][prop_key] = {
                'type': prop_val.get('type', 'string'),
                'default': prop_val.get('default'),
                'description': prop_val.get('description', ''),
                'help': prop_val.get('help', ''),
                'fa_icon': prop_val.get('fa_icon', ''),
                'hidden': prop_val.get('hidden', False),
                'enum': prop_val.get('enum'),
                'pattern': prop_val.get('pattern'),
            }
    return params


def load_citations(citations_path):
    """Load citations.yml and flatten all categories into a single lookup dict."""
    if not citations_path.exists():
        return {}
    with open(citations_path) as f:
        raw = yaml.safe_load(f)
    flat = {}
    for category_key, category_val in raw.items():
        if isinstance(category_val, dict):
            for tool_key, tool_val in category_val.items():
                if isinstance(tool_val, dict):
                    flat[tool_key] = {
                        'name': tool_val.get('name', tool_key),
                        'link': tool_val.get('link', ''),
                        'description': tool_val.get('description', ''),
                        'cite': tool_val.get('cite', '').strip(),
                        'category': category_key,
                    }
    return flat


def clean_tool_info(tool):
    """Clean tool name/version when conda build strings leak in (e.g. name=version build)."""
    if not tool:
        return tool
    tool = dict(tool)
    name = tool.get('name', '')
    if '=' in name:
        parts = name.split('=', 1)
        tool['name'] = parts[0]
        tool['version'] = parts[1]
    return tool


def build_source_url(path):
    """Construct a GitHub source URL from a relative path."""
    path = path.rstrip('/')
    if path == '.':
        return 'https://github.com/bactopia/bactopia'
    return f'https://github.com/bactopia/bactopia/tree/main/{path}'


def parse_output_tree(snap_path):
    """Parse a nf-test snapshot file to extract output file paths."""
    if not snap_path.exists():
        return []
    with open(snap_path) as f:
        data = json.load(f)
    first_key = next(iter(data), None)
    if not first_key:
        return []
    content = data[first_key].get('content', [])
    if len(content) < 2 or not isinstance(content[1], list):
        return []
    return content[1]


def parse_bactopia(repo_path):
    """Parse all Bactopia v4 metadata into a unified data structure."""
    repo = Path(repo_path)
    catalog_path = repo / 'catalog.json'
    citations_path = repo / 'data' / 'citations.yml'

    with open(catalog_path) as f:
        catalog = json.load(f)

    citations = load_citations(citations_path)

    shared_schemas = {}
    for schema_name in ['generic', 'bactopia-tools', 'bactopia']:
        schema_file = repo / 'conf' / 'schema' / f'{schema_name}.json'
        if schema_file.exists():
            shared_schemas[schema_name] = load_schema(schema_file)

    shared_param_keys = set()
    for schema_params in shared_schemas.values():
        shared_param_keys.update(schema_params.keys())

    modules = {}
    for key, val in catalog['modules'].items():
        main_nf = repo / val['path'] / 'main.nf'
        groovydoc = {}
        nf_inputs = {'records': [], 'standalone': []}
        nf_outputs = {'records': []}
        if main_nf.exists():
            nf_text = main_nf.read_text()
            groovydoc = parse_groovydoc(nf_text)
            nf_inputs = parse_nf_input_block(nf_text)
            nf_outputs = parse_nf_output_block(nf_text)

        inputs_with_types = merge_io_types(groovydoc.get('inputs', []), nf_inputs)
        outputs_with_types = merge_io_types_output(groovydoc.get('outputs', []), nf_outputs)

        schema_path = repo / val['path'] / 'schema.json'
        params = load_schema(schema_path)

        modules[key] = {
            'key': key,
            'summary': groovydoc.get('summary', '') or val.get('description', ''),
            'description': groovydoc.get('description', ''),
            'path': val['path'],
            'source_url': build_source_url(val['path']),
            'scope': val.get('scope', ''),
            'process_name': val.get('process_name', ''),
            'tool': clean_tool_info(val.get('tool', {})),
            'status': groovydoc.get('status', ''),
            'keywords': groovydoc.get('keywords', []),
            'tags': groovydoc.get('tags', val.get('tags', {})),
            'citations': groovydoc.get('citations', []),
            'notes': groovydoc.get('notes', []),
            'inputs': inputs_with_types,
            'outputs': outputs_with_types,
            'nf_inputs': nf_inputs,
            'nf_outputs': nf_outputs,
            'params': params,
            'used_by_subworkflows': [],
            'used_by_workflows': [],
        }

    subworkflows = {}
    for key, val in catalog['subworkflows'].items():
        main_nf = repo / val['path'] / 'main.nf'
        groovydoc = {}
        nf_inputs = {'standalone': []}
        if main_nf.exists():
            nf_text = main_nf.read_text()
            groovydoc = parse_groovydoc(nf_text)
            nf_inputs = parse_nf_take_block(nf_text)

        inputs_with_types = merge_take_types(groovydoc.get('inputs', []), nf_inputs)

        catalog_modules = val.get('calls', {}).get('modules', [])
        groovydoc_modules = groovydoc.get('modules', [])
        module_list = groovydoc_modules if groovydoc_modules else catalog_modules

        catalog_sws = val.get('calls', {}).get('subworkflows', [])
        groovydoc_sws = groovydoc.get('subworkflows', [])
        subworkflow_list = groovydoc_sws if groovydoc_sws else catalog_sws

        subworkflows[key] = {
            'key': key,
            'summary': groovydoc.get('summary', '') or val.get('description', ''),
            'description': groovydoc.get('description', ''),
            'path': val['path'],
            'source_url': build_source_url(val['path']),
            'scope': val.get('scope', ''),
            'status': groovydoc.get('status', ''),
            'keywords': groovydoc.get('keywords', []),
            'tags': groovydoc.get('tags', val.get('tags', {})),
            'citations': groovydoc.get('citations', []),
            'modules': module_list,
            'subworkflows': subworkflow_list,
            'inputs': inputs_with_types,
            'outputs': groovydoc.get('outputs', []),
            'nf_inputs': nf_inputs,
            'used_by_workflows': [],
        }

    workflows = {}
    for key, val in catalog['workflows'].items():
        main_nf = repo / val['path'] / 'main.nf'
        groovydoc = {}
        if main_nf.exists():
            groovydoc = parse_groovydoc(main_nf.read_text())

        schema_path = repo / val['path'] / 'nextflow_schema.json'
        all_params = load_schema(schema_path)
        tool_params = {k: v for k, v in all_params.items() if k not in shared_param_keys}

        catalog_subworkflows = val.get('subworkflows', [])
        groovydoc_subworkflows = groovydoc.get('subworkflows', [])
        subworkflow_list = groovydoc_subworkflows if groovydoc_subworkflows else catalog_subworkflows

        wf_type = val.get('type', 'tool')
        shared_schema_key = 'bactopia' if wf_type == 'named' else 'bactopia-tools'

        snap_path = repo / val['path'] / 'tests' / 'main.nf.test.snap'
        output_tree = parse_output_tree(snap_path)

        workflows[key] = {
            'key': key,
            'type': wf_type,
            'summary': groovydoc.get('summary', '') or val.get('description', ''),
            'description': groovydoc.get('description', ''),
            'path': val['path'],
            'source_url': build_source_url(val['path']),
            'ext': val.get('ext', []),
            'status': groovydoc.get('status', ''),
            'keywords': groovydoc.get('keywords', []),
            'tags': groovydoc.get('tags', val.get('tags', {})),
            'citations': groovydoc.get('citations', []),
            'subworkflows': subworkflow_list,
            'inputs': groovydoc.get('inputs', []),
            'published_outputs': groovydoc.get('sections', []),
            'notes': groovydoc.get('notes', []),
            'output_tree': output_tree,
            'params': {
                'tool_specific': tool_params,
                'shared_schema': shared_schema_key,
            },
            'uses_subworkflows': [],
            'uses_modules': [],
        }

    # Build reverse-lookup maps
    for wf_key, wf in workflows.items():
        seen_modules = set()
        for sw_name in wf.get('subworkflows', []):
            if sw_name in subworkflows:
                subworkflows[sw_name]['used_by_workflows'].append(wf_key)
                wf['uses_subworkflows'].append(sw_name)
                for mod_name in subworkflows[sw_name].get('modules', []):
                    if mod_name in modules:
                        modules[mod_name]['used_by_workflows'].append(wf_key)
                        seen_modules.add(mod_name)
        wf['uses_modules'] = sorted(seen_modules)

    for sw_key, sw in subworkflows.items():
        for mod_name in sw.get('modules', []):
            if mod_name in modules:
                modules[mod_name]['used_by_subworkflows'].append(sw_key)

    # Deduplicate reverse-lookup lists
    for mod in modules.values():
        mod['used_by_subworkflows'] = sorted(set(mod['used_by_subworkflows']))
        mod['used_by_workflows'] = sorted(set(mod['used_by_workflows']))
    for sw in subworkflows.values():
        sw['used_by_workflows'] = sorted(set(sw['used_by_workflows']))

    return {
        'meta': {
            'bactopia_version': catalog.get('bactopia_version', ''),
            'generated': datetime.now(timezone.utc).isoformat(),
            'bactopia_repo': str(repo.resolve()),
        },
        'citations': citations,
        'shared_params': shared_schemas,
        'modules': modules,
        'subworkflows': subworkflows,
        'workflows': workflows,
    }


def main():
    parser = argparse.ArgumentParser(description='Parse Bactopia v4 metadata for doc generation')
    parser.add_argument('repo', help='Path to the Bactopia v4 repository')
    parser.add_argument('--output', '-o', default='data/bactopia.json',
                        help='Output JSON path (default: data/bactopia.json)')
    args = parser.parse_args()

    repo = Path(args.repo)
    if not (repo / 'catalog.json').exists():
        print(f'Error: {repo / "catalog.json"} not found', file=sys.stderr)
        sys.exit(1)

    result = parse_bactopia(repo)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)

    n_mod = len(result['modules'])
    n_sw = len(result['subworkflows'])
    n_wf = len(result['workflows'])
    n_cit = len(result['citations'])
    print(f'Parsed {n_mod} modules, {n_sw} subworkflows, {n_wf} workflows, {n_cit} citations')
    print(f'Output written to {output_path}')


if __name__ == '__main__':
    main()
