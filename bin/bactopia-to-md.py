#! /usr/bin/env python3
"""
Convert the various `meta.yml` and `params.json` files into Markdown format
"""
import json
import yaml
from pathlib import Path
WORKFLOWS = {
    'bactopia': {
        'modules': ['gather', 'qc', 'assembler', 'prokka', 'bakta', 'sketcher', 'amrfinderplus', 'mlst', 'merlin'],
        'template': 'bactopia/bactopia-full.j2'
    }
}
SUBWORKFLOWS = 'params.available_workflows.bactopiatools.subworkflows'
MODULES = 'params.available_workflows.bactopiatools.modules'
MODULES_RENAME = {
    'abricate_run': 'abricate',
    'amrfinderplus_run': 'amrfinderplus',
    'ariba_run': 'ariba',
    'bakta_run': 'bakta',
    'blast_blastn': 'blastn',
    'blast_tblastn': 'tblastn',
    'blast_blastp': 'blastp',
    'blast_blastx': 'blastx',
    'blast_tblastx': 'tblastx',
    'checkm_lineagewf': 'checkm',
    'genotyphi_parse': 'genotyphi',
    'midas_species': 'midas',
    'mobsuite_recon': 'mobsuite',
    'mykrobe_predict': 'mykrobe',
    'rgi_main': 'rgi',
    'snippy_run': 'snippy'
}
IGNORE_LIST = [
    # Bactopia modules
    "LIST_OF_MODULES",
    "plasmidid"
]

WORKFLOW_RENAME = {
    'mlst': 'sequence-typing/mlst',
    'amrfinderplus': 'antimicrobial-resistance/amrfinderplus',
    'prokka': 'annotator/prokka',
    'bakta': 'annotator/bakta',
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

def get_bactopia_citations(docs_path):
    citations = {}
    with open(f'{docs_path}/docs/data/citations.yml', "rt") as citations_fh:
        citations = yaml.safe_load(citations_fh)
    return citations

def get_enhancements(docs_path):
    enhancements = {}
    with open(f'{docs_path}/docs/data/contributions.yml', "rt") as enhancements_fh:
        enhancements = yaml.safe_load(enhancements_fh)
    return enhancements

def get_generic_params(generic_path):
    generic = {}
    for params_json in sorted(Path(generic_path).glob('*.json')):
        print(params_json)
        with open(params_json, "rt") as params_fh:
            generic[str(params_json.stem)] = json.load(params_fh)
    return generic

def get_subworkflows(subworkflow_path, is_subworkflow, is_module):
    """   """
    subworkflows = {}
    total_modules = 0
    total_subworkflows = 0
    for meta_yml in sorted(Path(subworkflow_path).rglob('*meta.yml')):
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
    for params_json in sorted(Path(module_path).rglob('*params.json')):
        module_name = str(params_json).replace('/params.json', '')
        if 'local' in module_name:
            module_name = module_name.split('local/bactopia/')[1]
        else:
            # nf-core module
            module_name = module_name.split('/nf-core/')[1].replace('/', '_').replace('_run', '')
        if module_name in MODULES_RENAME:
            module_name = MODULES_RENAME[module_name]
        print(f"{module_name} - {params_json}")
        try:
            with open(params_json, "rt") as params_fh:
                modules[module_name] = json.load(params_fh)
        except Exception as e:
            IGNORE_LIST.append(module_name)
            print(f"skipping {module_name} - {params_json}")
    return modules

def read_nextflow_config(nf_config):
    """   """
    config = {}
    with open(nf_config, 'rt') as nf_fh:
        if "=" in line:
            for line in nf_fh:
                k,v = line.rstrip().split(' = ')
                config[k] = nf_to_list(v) if v.startswith('[') else v
    return config

def nf_to_list(param):
    return param.replace("'","").replace('[', '').replace(' ', "").replace(']', '').split(',')

def format_params(params, exclude=[]):
    params_md = []
    for group in params["definitions"].keys():
        if group not in exclude:
            if len(params["definitions"][group]["properties"].keys()):
                params_md.append(f'\n### <i class="fa-xl {params["definitions"][group]["fa_icon"]}"></i> {params["definitions"][group]["title"]}')
                params_md.append(f"{params['definitions'][group]['description']}\n")
                params_md.append(f'| Parameter | Description |')
                params_md.append(f'|:---|---|')
                for parameter in params["definitions"][group]["properties"].keys():
                    param = params["definitions"][group]["properties"][parameter]
                    default_val = param["default"] if "default" in param else ""
                    default_val = f', **Default:** `{default_val}`' if default_val else ""
                    params_md.append(
                        f'| <i class="fa-lg {param["fa_icon"]}"></i>` --{parameter}` |'
                        f' {param["description"].rstrip()} <br/>**Type:** `{param["type"]}`{default_val} |'
                    )
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
    enhancements = get_enhancements(args.docs_repo)

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
    for name, vals in sorted(subworkflows.items()):
        if name not in IGNORE_LIST:
            is_bactopia_tool = True if name in nf_config[SUBWORKFLOWS] or name in nf_config[MODULES] else False
            if is_bactopia_tool:
                module_params = []
                for module in vals['modules']:
                    module_name = module
                    if module_name not in IGNORE_LIST:
                        if module_name in MODULES_RENAME:
                            module_name = MODULES_RENAME[module_name]
                        print(f"working on {name} - {module}")
                        module_params += format_params(modules[module_name])
                params = {
                    'bactopia_tools': '\n'.join(format_params(generic["bactopia-tools"])),
                    'module':  '\n'.join(module_params),
                    'generic': '\n'.join(format_params(generic["generic"]))
                }
                if "docs" in vals:
                    print(f"working on {name} - {module}")
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
    with open(f'{args.docs_repo}/docs/impact-and-outreach/acknowledgements.md', 'wt') as md_fh:
        md_fh.write(output)

    # Build enhancements Page
    template = env.get_template('enhancements.j2')
    output = template.render(
        total_contributions=len(enhancements["tools"])+len(enhancements["conda_submissions"])+len(enhancements["conda_updates"])+len(enhancements["nfcore_modules"])+len(enhancements["other"]),
        conda_submissions=enhancements["conda_submissions"],
        conda_updates=enhancements["conda_updates"],
        nfcore_modules=enhancements["nfcore_modules"],
        tools=enhancements["tools"],
        other=enhancements["other"]
    )
    with open(f'{args.docs_repo}/docs/impact-and-outreach/enhancements.md', 'wt') as md_fh:
        md_fh.write(output)

    # Build mkdocs.yml Page
    template = env.get_template('mkdocs.j2')
    output = template.render(tools=subworkflows)
    with open(f'{args.docs_repo}/mkdocs.yml', 'wt') as md_fh:
        md_fh.write(output)

    # Build beginner's guide
    print(f"Working on Beginners Guide")
    template = env.get_template('bactopia/bactopia-beginners.j2')
    params = {
        'bactopia': '\n'.join(format_params(generic["bactopia"], exclude=['dataset_parameters'])),
        'module':  '\n'.join(module_params),
        'generic': '\n'.join(format_params(generic["generic"]))
    }
    output = template.render(
        params=params
    )
    with open(f'{args.docs_repo}/docs/beginners-guide.md', 'wt') as md_fh:
        md_fh.write(output)

    # Build workflow pages
    for workflow, wf_vals in WORKFLOWS.items():
        print(f"Working on {workflow}")
        template = env.get_template(wf_vals['template'])
        params = {
            'bactopia': '\n'.join(format_params(generic["bactopia"])),
            'generic': '\n'.join(format_params(generic["generic"]))
        }
        vals = {}
        for subworkflow in wf_vals['modules']:
            print(f"Working on {subworkflow}")
            vals[subworkflow] = subworkflows[subworkflow]

            module_params = []
            for module in vals[subworkflow]['modules']:
                module_name = module
                if module_name not in IGNORE_LIST:
                    if module_name in MODULES_RENAME:
                        module_name = MODULES_RENAME[module_name]
                    print(f"working on {subworkflow} - {module}")
                    module_params += format_params(modules[module_name])
            
            params[subworkflow] = '\n'.join(module_params)
            template2 = env.get_template('bactopia/bactopia-steps.j2')
            output = template2.render(
                meta=vals[subworkflow],
                params={'module': params[subworkflow]},
                citations=module_citations
            )

            with open(f'{args.docs_repo}/docs/bactopia/{WORKFLOW_RENAME[subworkflow] if subworkflow in WORKFLOW_RENAME else subworkflow}.md', 'wt') as md_fh:
                md_fh.write(output)

        output = template.render(
            meta=vals,
            params=params,
            citations=module_citations
        )
        with open(f'{args.docs_repo}/docs/full-guide.md', 'wt') as md_fh:
            md_fh.write(output)

    # Build citations page
    print(f"Working on Citations")
    bactopia_citations = get_bactopia_citations(args.docs_repo)
    template = env.get_template('citations.j2')
    output = template.render(
        citations=bactopia_citations,
        total=len(bactopia_citations['citations'])
    )
    with open(f'{args.docs_repo}/docs/impact-and-outreach/citations.md', 'wt') as md_fh:
            md_fh.write(output)
