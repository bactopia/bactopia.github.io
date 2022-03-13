#! /usr/bin/env python3
"""
Convert the various `meta.yml` and `params.json` files into Markdown format
"""
import json
import yaml
from pathlib import Path
WORKFLOWS = 'params.available_workflows.bactopia'
SUBWORKFLOWS = 'params.available_workflows.bactopiatools.subworkflows'
MODULES = 'params.available_workflows.bactopiatools.modules'
MODULES_RENAME = {
    'abricate_run': 'abricate', 'amrfinderplus_run': 'amrfinderplus', 
    'checkm_lineagewf': 'checkm', 'mobsuite_recon': 'mobsuite',
    'rgi_main': 'rgi'
}

def get_citations(citation_path):
    """ """
    citations = {}
    module_citations = {}
    with open(f'{citation_path}/citations.yml', "rt") as citations_fh:
        citations = yaml.safe_load(citations_fh)
        for group, refs in citations.items():
            for ref, vals in refs.items():
                module_citations[ref] = vals
    return [citations, module_citations]

def get_generic_params(generic_path):
    generic = {}
    for params_json in Path(generic_path).glob('*.json'):
        with open(params_json, "rt") as params_fh:
            generic[str(params_json.stem)] = json.load(params_fh)
    return generic

def get_subworkflows(subworkflow_path, is_subworkflow, is_module):
    """   """
    subworkflows = {}
    total_modules = 0
    total_subworkflows = 0
    for meta_yml in Path(subworkflow_path).rglob('*meta.yml'):
        subworkflow_name = str(meta_yml).replace('/meta.yml', '').split('local/')[1]
        with open(meta_yml, "rt") as meta_fh:
            subworkflows[subworkflow_name] = yaml.safe_load(meta_fh)
            if subworkflow_name in is_subworkflow:
                total_subworkflows += 1
                subworkflows[subworkflow_name]['is_subworkflow'] = True
                subworkflows[subworkflow_name]['is_module'] = False
            elif subworkflow_name in is_module:
                total_modules += 1
                subworkflows[subworkflow_name]['is_subworkflow'] = False
                subworkflows[subworkflow_name]['is_module'] = True
            else:
                subworkflows[subworkflow_name]['is_subworkflow'] = False
                subworkflows[subworkflow_name]['is_module'] = False
    return [subworkflows, total_subworkflows, total_modules]

def get_modules(module_path):
    """ Find all modules in modules path. """
    modules = {}
    for params_json in Path(module_path).rglob('*params.json'):
        module_name = str(params_json).replace('/params.json', '')
        if 'local' in module_name:
            module_name = module_name.split('local/bactopia/')[1]
        else:
            # nf-core module
            module_name = module_name.split('/nf-core/modules/')[1].replace('/', '_').replace('_run', '')
        if module_name in MODULES_RENAME:
            module_name = MODULES_RENAME[module_name]
        print(f"{module_name} - {params_json}")
        with open(params_json, "rt") as params_fh:
            modules[module_name] = json.load(params_fh)
    return modules

def read_nextflow_config(nf_config):
    """   """
    config = {}
    with open(nf_config, 'rt') as nf_fh:
        for line in nf_fh:
            k,v = line.rstrip().split(' = ')
            config[k] = nf_to_list(v) if v.startswith('[') else v
    return config

def nf_to_list(param):
    return param.replace("'","").replace('[', '').replace(' ', "").replace(']', '').split(',')

def format_params(params):
    params_md = []
    for group in params["definitions"].keys():
        # params_md.append(f"\n### {params['definitions'][group]['fa_icon']} {params['definitions'][group]['title']}")
        params_md.append(f"\n### {params['definitions'][group]['title']}")
        params_md.append(f"{params['definitions'][group]['description']}\n")
        params_md.append(f'| Parameter | Description | Default |')
        params_md.append(f'|---|---|---|')
        for parameter in params["definitions"][group]["properties"].keys():
            param = params["definitions"][group]["properties"][parameter]
            default_val = param["default"] if "default" in param else ""
            # params_md.append(f'| {param["fa_icon"]} `--{parameter}` | {param["description"]} | {default_val} |')
            params_md.append(f'| `--{parameter}` | {param["description"]} | {default_val} |')
    return params_md

if __name__ == '__main__':
    import argparse as ap
    import glob
    import sys
    import time
    from jinja2 import Environment, FileSystemLoader

    parser = ap.ArgumentParser(
        prog='bactopia-to-md',
        conflict_handler='resolve',
        description=('Convert various meta.yml and params.json files into markdown')
    )

    parser.add_argument('bactopia_repo', metavar="STR", type=str,
                        help='Directory for the Bactopia repo')
    parser.add_argument('docs_repo', metavar="STR", type=str,
                        help='Directory for the Bactopia Docs repo')
    parser.add_argument('--output', metavar='STR', type=str, default="./docs",
                        help='Where to output files')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    nf_config = read_nextflow_config(f'{args.bactopia_repo}/nextflow_config.txt')
    subworkflows, total_subworkflows, total_modules = get_subworkflows(f'{args.bactopia_repo}/subworkflows', nf_config[SUBWORKFLOWS], nf_config[MODULES])
    modules = get_modules(f'{args.bactopia_repo}/modules')
    generic = get_generic_params(f'{args.bactopia_repo}/conf/schema')
    citations, module_citations = get_citations(args.bactopia_repo)

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    # Build Bactopia Tools Page
    template = env.get_template('bactopia-tools.j2')
    output = template.render(
        tools=subworkflows,
        total_bactopia_tools=total_subworkflows + total_modules,
        total_subworkflows=total_subworkflows,
        total_modules=total_modules
    )
    with open(f'{args.docs_repo}/docs/bactopia-tools/index.md', 'wt') as md_fh:
        md_fh.write(output)

    # Build each Bactopia Tool Page
    for name, vals in subworkflows.items():
        is_bactopia_tool = False if name in nf_config[WORKFLOWS] else True
        if is_bactopia_tool:
            module_params = []
            for module in vals['modules']:
                print(f"working on {name} - {module}")
                module_params += format_params(modules[module])
            params = {
                'bactopia_tools': '\n'.join(format_params(generic["bactopia-tools"])),
                'module':  '\n'.join(module_params),
                'generic': '\n'.join(format_params(generic["generic"]))
            }
            if "docs" in vals:
                template = env.get_template('bactopia-tools-single.j2')
                output = template.render(
                    meta=vals,
                    params=params,
                    citations=module_citations
                )
                with open(f'{args.docs_repo}/docs/bactopia-tools/{name}.md', 'wt') as md_fh:
                    md_fh.write(output)

    # Build Acknowledgements Page
    template = env.get_template('acknowledgements.j2')
    output = template.render(
        citations=citations, 
        total=len(citations["datasets_ariba"])+len(citations["datasets_generic"])+len(citations["datasets_minmer"])+len(citations["tools"]),
        total_datasets=len(citations["datasets_ariba"])+len(citations["datasets_generic"])+len(citations["datasets_minmer"])
    )
    with open(f'{args.docs_repo}/docs/acknowledgements.md', 'wt') as md_fh:
        md_fh.write(output)

    # Build mkdocs.yml Page
    template = env.get_template('mkdocs.j2')
    output = template.render(tools=subworkflows)
    with open(f'{args.docs_repo}/mkdocs.yml', 'wt') as md_fh:
        md_fh.write(output)
