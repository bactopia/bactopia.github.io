"""Shared utilities for Bactopia documentation generators."""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, ChoiceLoader, select_autoescape


STATUS_BADGE = {
    'stable': 'success',
    'testing': 'warning',
    'experimental': 'danger',
}


def escape_mdx(text):
    """Escape characters that break MDX parsing."""
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    text = text.replace('{', '&#123;').replace('}', '&#125;')
    return text


def normalize_tags(keywords):
    """Normalize keywords into Docusaurus-compatible tag strings."""
    tags = []
    for kw in keywords:
        tag = kw.strip().lower().replace(' ', '-')
        if tag and tag not in tags:
            tags.append(tag)
    return tags


def format_default(value):
    """Format a parameter default value for display."""
    if value is None:
        return ''
    if isinstance(value, bool):
        return '`true`' if value else '`false`'
    if isinstance(value, str):
        return f'`{value}`' if value else ''
    return f'`{value}`'


def render_param_table(group, include_heading=True):
    """Render a parameter group as a markdown table."""
    props = group.get('properties', {})
    visible = {k: v for k, v in props.items() if not v.get('hidden', False)}
    if not visible:
        return ''

    lines = []
    if include_heading:
        lines.append(f'### {group["title"]}')
        lines.append('')
    if group.get('description'):
        lines.append(group['description'])
        lines.append('')

    lines.append('| Parameter | Type | Default | Description |')
    lines.append('|-----------|------|---------|-------------|')
    for name, prop in visible.items():
        ptype = prop.get('type', 'string')
        default = format_default(prop.get('default'))
        desc = escape_mdx(prop.get('description', ''))
        enum = prop.get('enum')
        if enum:
            choices = ', '.join(f'`{e}`' for e in enum)
            desc = f'{desc} (choices: {choices})'
        lines.append(f'| `--{name}` | {ptype} | {default} | {desc} |')
    lines.append('')
    return '\n'.join(lines)


def _render_record_code_block(record):
    """Render a fenced code block for a single NF record."""
    lines = ['```', 'record (']
    field_lines = []
    for field in record['fields']:
        field_lines.append(f'    {field["name"]}: {field["type"]}')
    lines.append(',\n'.join(field_lines))
    lines.append(')')
    lines.append('```')
    lines.append('')
    return lines


def _render_standalone_code_block(standalone):
    """Render a fenced code block for standalone typed declarations."""
    lines = ['```']
    for sa in standalone:
        lines.append(f'{sa["name"]}: {sa["type"]}')
    lines.append('```')
    lines.append('')
    return lines


def _render_fields_table(fields):
    """Render a fields table, choosing columns based on whether types are present."""
    lines = []
    has_types = any(f.get('type') for f in fields)
    if has_types:
        lines.append('| Field | Type | Description |')
        lines.append('|-------|------|-------------|')
        for field in fields:
            fname = f'`{field["name"]}`' if field['name'] else ''
            ftype = f'`{field["type"]}`' if field.get('type') else ''
            fdesc = escape_mdx(field.get('description', ''))
            lines.append(f'| {fname} | {ftype} | {fdesc} |')
    else:
        lines.append('| Field | Description |')
        lines.append('|-------|-------------|')
        for field in fields:
            fname = f'`{field["name"]}`' if field['name'] else ''
            fdesc = escape_mdx(field.get('description', ''))
            lines.append(f'| {fname} | {fdesc} |')
    lines.append('')
    return lines


def render_io_table(io_list, header='Inputs', nf_io=None):
    """Render @input or @output entries as a markdown section."""
    if not io_list:
        return ''

    lines = [f'## {header}', '']

    records = nf_io.get('records', []) if nf_io else []
    standalone = nf_io.get('standalone', []) if nf_io else []

    record_entries = [e for e in io_list if e.get('fields')]
    standalone_entries = [e for e in io_list if not e.get('fields')]

    # For take blocks (standalone only, no records): split by Channel<Record> vs others
    if standalone and not records:
        record_takes = [s for s in standalone if s['type'] == 'Channel<Record>']
        other_takes = [s for s in standalone if s['type'] != 'Channel<Record>']
        if record_takes:
            lines.extend(_render_standalone_code_block(record_takes))
    else:
        other_takes = standalone

    # Render record entries: code block then table for each
    for i, entry in enumerate(record_entries):
        if i < len(records):
            lines.extend(_render_record_code_block(records[i]))
        lines.extend(_render_fields_table(entry['fields']))

    # Render standalone entries: code block + merged table
    if standalone_entries:
        if other_takes:
            lines.extend(_render_standalone_code_block(other_takes))
        elif standalone and records:
            lines.extend(_render_standalone_code_block(standalone))

        has_types = any(e.get('type') for e in standalone_entries)
        if has_types:
            lines.append('| Name | Type | Description |')
            lines.append('|------|------|-------------|')
            for entry in standalone_entries:
                name = entry.get('name', '')
                etype = entry.get('type', '')
                desc = entry.get('description', '')
                lines.append(f'| `{name}` | `{etype}` | {desc} |')
        else:
            lines.append('| Name | Description |')
            lines.append('|------|-------------|')
            for entry in standalone_entries:
                name = entry.get('name', '')
                desc = entry.get('description', '')
                lines.append(f'| `{name}` | {desc} |')
        lines.append('')

    return '\n'.join(lines)


def render_citations(cite_keys, citations_db, include_bactopia=True):
    """Render a citations section from citation keys."""
    if not cite_keys:
        return ''

    lines = [
        '## Citations',
        '',
        'If you use this in your analysis, please cite the following.',
        '',
    ]

    def _render_one(cite):
        name = cite.get('name', '')
        link = cite.get('link', '')
        cite_text = cite.get('cite', '')
        if link:
            lines.append(f'- [{name}]({link})  ')
        else:
            lines.append(f'- **{name}**  ')
        if cite_text:
            lines.append(f'  {cite_text}')
        lines.append('')

    if include_bactopia and 'bactopia' not in cite_keys:
        bactopia_cite = citations_db.get('bactopia', {})
        if bactopia_cite:
            _render_one(bactopia_cite)

    for ck in cite_keys:
        cite = citations_db.get(ck, {})
        if cite:
            _render_one(cite)
        else:
            lines.append(ck)
            lines.append('')

    return '\n'.join(lines)


def tags_yaml(tags):
    """Render a tags list as YAML for frontmatter."""
    return '\n'.join(f'  - {t}' for t in tags)


def render_output_tree(raw_paths):
    """Render a list of file paths as a decorated tree."""
    if not raw_paths:
        return ''

    sample_name = raw_paths[0].split('/')[0] if raw_paths else ''

    # Collapse nf.command.* files into a single glob entry
    nf_command_dirs = set()
    filtered = []
    for p in raw_paths:
        basename = p.rsplit('/', 1)[-1]
        if basename.startswith('nf.command.'):
            parent = p.rsplit('/', 1)[0] if '/' in p else ''
            if parent not in nf_command_dirs:
                nf_command_dirs.add(parent)
                filtered.append(f'{parent}/nf.command.{{begin,err,log,out,run,sh,trace}}')
            continue
        filtered.append(p)

    # Identify the bactopia-runs subdirectory name to add <TIMESTAMP>
    runs_subdir = ''
    for p in filtered:
        parts = p.split('/')
        if len(parts) >= 2 and parts[0] == 'bactopia-runs':
            runs_subdir = parts[1]
            break

    cleaned = []
    for p in filtered:
        if sample_name:
            p = p.replace(sample_name, '<SAMPLE_NAME>')
        if runs_subdir:
            parts = p.split('/')
            parts = [f'{part}-<TIMESTAMP>' if part == runs_subdir else part for part in parts]
            p = '/'.join(parts)
        cleaned.append(p)

    tree = {}
    for p in cleaned:
        parts = p.split('/')
        node = tree
        for part in parts:
            if part not in node:
                node[part] = {}
            node = node[part]

    def _render_tree(node, prefix=''):
        lines = []
        entries = sorted(node.keys())
        for i, name in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = '└── ' if is_last else '├── '
            lines.append(f'{prefix}{connector}{name}')
            child_prefix = prefix + ('    ' if is_last else '│   ')
            lines.extend(_render_tree(node[name], child_prefix))
        return lines

    tree_lines = ['<BACTOPIA_DIR>']
    root_entries = sorted(tree.keys())
    for i, name in enumerate(root_entries):
        is_last = (i == len(root_entries) - 1)
        connector = '└── ' if is_last else '├── '
        tree_lines.append(f'{connector}{name}')
        child_prefix = '    ' if is_last else '│   '
        tree_lines.extend(_render_tree(tree[name], child_prefix))

    return (
        '### Expected Output Files\n\n'
        + '```\n'
        + '\n'.join(tree_lines)
        + '\n```\n'
    )


def render_shared_params(shared_params, schema_key, skip_keys=None):
    """Render shared parameter groups in collapsible details blocks."""
    schema = shared_params.get(schema_key, {})
    generic = shared_params.get('generic', {})
    skip_keys = skip_keys or set()

    sections = []

    for groups in [schema, generic]:
        for group_key, group in groups.items():
            if group_key in skip_keys:
                continue
            table = render_param_table(group, include_heading=False)
            if table:
                title = group.get('title', group_key)
                sections.append(
                    f'<details>\n<summary>{title}</summary>\n\n'
                    + table
                    + '</details>\n'
                )

    return '\n'.join(sections)


def create_jinja_env(template_dir='templates'):
    """Create a Jinja2 environment configured for Bactopia doc generation."""
    template_path = Path(template_dir)
    env = Environment(
        loader=FileSystemLoader(str(template_path)),
        keep_trailing_newline=True,
        lstrip_blocks=True,
        trim_blocks=True,
    )

    env.globals.update({
        'STATUS_BADGE': STATUS_BADGE,
        'escape_mdx': escape_mdx,
        'normalize_tags': normalize_tags,
        'format_default': format_default,
        'render_param_table': render_param_table,
        'render_io_table': render_io_table,
        'render_citations': render_citations,
        'render_shared_params': render_shared_params,
        'render_output_tree': render_output_tree,
        'tags_yaml': tags_yaml,
    })

    return env


def load_template(env, component_type, key):
    """Load a custom template if it exists, otherwise fall back to the base."""
    custom_path = f'custom/{component_type}s/{key}.j2'
    try:
        return env.get_template(custom_path)
    except Exception:
        return env.get_template(f'{component_type}.j2')
