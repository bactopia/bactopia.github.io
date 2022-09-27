---
title: meta.docs.meta.title
description: meta.docs.meta.description
tags:
---



# Bactopia Tool - `busco`
The `busco` module uses [BUSCO](https://gitlab.com/ezlab/busco) (_or Benchmarking Universal Single-Copy Orthologs_) 
to assess the completeness of your assembly.


## Example Usage
```
bactopia --wf busco \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `busco` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
busco/
├── <LINEAGE>
│   ├── <SAMPLE_NAME>
│   │   ├── logs/
│   │   ├── prodigal_output/
│   │   ├── run_<LINEAGE>/
│   │   │   ├── busco_sequences
│   │   │   ├── full_table.tsv
│   │   │   ├── hmmer_output/
│   │   │   ├── missing_busco_list.tsv
│   │   │   ├── short_summary.json
│   │   │   └── short_summary.txt
│   │   ├── short_summary.specific.<LINEAGE>.<SAMPLE_NAME>.json
│   │   └── short_summary.specific.<LINEAGE>.<SAMPLE_NAME>.txt
│   ├── <LINEAGE>-summary.txt
│   └── logs
│       └── busco.log
├── logs
│   ├── busco
│   │   └── <LINEAGE>
│   │       ├── nf-busco.{begin,err,log,out,run,sh,trace}
│   │       └── versions.yml
│   ├── csvtk_concat
│   │   ├── nf-csvtk_concat.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   └── custom_dumpsoftwareversions
│       ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── busco-dag.dot
│   ├── busco-report.html
│   ├── busco-timeline.html
│   └── busco-trace.txt
├── busco.tsv
├── software_versions.yml
└── software_versions_mqc.yml

```



### Results

#### Top Level

Below are results that are in the base directory.


| Filename    | Description                                |
|-------------|--------------------------------------------|
| busco.tsv   | A merged TSV of all lineages used by BUSCO |


#### busco

Below is a description of the _per-lineage_ results from [BUSCO](https://gitlab.com/ezlab/busco).


| Filename/Folder                                                             | Description                                                                         |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <LINEAGE>/<LINEAGE>-summary.txt                                             | Tab-delimited lineage results for all samples                                       |
| <LINEAGE>/logs/busco.log                                                    | Detailed information about the BUSCO run                                            |
| <LINEAGE>/<SAMPLE_NAME>/logs/                                               | Log files for individual tools per-sample                                           |
| <LINEAGE>/<SAMPLE_NAME>/prodigal_output/                                    | Outputs from the Prodigal gene-prediction step                                      |
| <LINEAGE>/<SAMPLE_NAME>/run_<LINEAGE>/busco_sequences                       | FASTA format file for each BUSCO gene identified                                    |
| <LINEAGE>/<SAMPLE_NAME>/run_<LINEAGE>/full_table.tsv                        | Complete results in a tab-delimited format with scores and lengths of BUSCO matches |
| <LINEAGE>/<SAMPLE_NAME>/run_<LINEAGE>/hmmer_output                          | Tab-delimited output from HMMER                                                     |
| <LINEAGE>/<SAMPLE_NAME>/run_<LINEAGE>/missing_busco_list.tsv                | Tab-delimited list of missing BUSCOs                                                |
| <LINEAGE>/<SAMPLE_NAME>/run_<LINEAGE>/short_summary.json                    | A summary of BUSCO matches in JSON format                                           |
| <LINEAGE>/<SAMPLE_NAME>/run_<LINEAGE>/short_summary.txt                     | A summary of BUSCO matches                                                          |
| <LINEAGE>/<SAMPLE_NAME>/short_summary.specific.<LINEAGE>.<SAMPLE_NAME>.json | A summary of BUSCO matches in JSON format per-sample                                |
| <LINEAGE>/<SAMPLE_NAME>/short_summary.specific.<LINEAGE>.<SAMPLE_NAME>.txt  | A summary of BUSCO matches per-sample                                               |





### Audit Trail

Below are files that can assist you in understanding which parameters and program versions were used.

#### Logs 

Each process that is executed will have a `logs` folder containing helpful files for you to review
if the need ever arises.

| Filename                      | Description |
|-------------------------------|-------------|
| nf-&lt;PROCESS_NAME&gt;.begin | An empty file used to designate the process started |
| nf-&lt;PROCESS_NAME&gt;.err   | Contains STDERR outputs from the process |
| nf-&lt;PROCESS_NAME&gt;.log   | Contains both STDERR and STDOUT outputs from the process |
| nf-&lt;PROCESS_NAME&gt;.out   | Contains STDOUT outputs from the process |
| nf-&lt;PROCESS_NAME&gt;.run   | The script Nextflow uses to stage/unstage files and queue processes based on given profile |
| nf-&lt;PROCESS_NAME&gt;.sh    | The script executed by bash for the process  |
| nf-&lt;PROCESS_NAME&gt;.trace | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report for the process |
| versions.yml                  | A YAML formatted file with program versions |

#### Nextflow Reports

These Nextflow reports provide great a great summary of your run. These can be used to optimize
resource usage and estimate expected costs if using cloud platforms.

| Filename | Description |
|----------|-------------|
| busco-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| busco-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| busco-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| busco-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


#### Program Versions

At the end of each run, each of the `versions.yml` files are merged into the files below.

| Filename                  | Description |
|---------------------------|-------------|
| software_versions.yml     | A complete list of programs and versions used by each process | 
| software_versions_mqc.yml | A complete list of programs and versions formatted for [MultiQC](https://multiqc.info/) |

## Parameters


### Required Parameters
Define where the pipeline should find input data and save output data.

| Parameter | Description | Default |
|---|---|---|
| `--bactopia` | The path to bactopia results to use as inputs |  |

### Filtering Parameters
Use these parameters to specify which samples to include or exclude.

| Parameter | Description | Default |
|---|---|---|
| `--include` | A text file containing sample names (one per line) to include from the analysis |  |
| `--exclude` | A text file containing sample names (one per line) to exclude from the analysis |  |


### BUSCO Parameters


| Parameter | Description | Default |
|---|---|---|
| `--busco_lineage` | Specify the name of the BUSCO lineage to be used (can separate by comma) | bacteria_odb10 |
| `--busco_evalue` | E-value cutoff for BLAST searches. Allowed formats, 0.001 or 1e-03 | 1e-03 |
| `--busco_limit` | Total candidate regions to consider per BUSCO | 3 |
| `--metaeuk_parameters` | Additional Metaeuk first-pass arguments contained within a single pair of quotation marks, separated by commas |  |
| `--metaeuk_rerun_parameters` | Additional Metaeuk second-pass arguments contained within a single pair of quotation marks, separated by commas |  |
| `--use_augustus` | Use augustus gene predictor for eukaryote runs | False |
| `--augustus_parameters` | Additional Augustus arguments contained within a single pair of quotation marks, separated by commas |  |
| `--augustus_species` | Specify a species for Augustus training |  |
| `--augustus_long` | Optimization Augustus self-training mode | False |


### Optional Parameters
These optional parameters can be useful in certain settings.

| Parameter | Description | Default |
|---|---|---|
| `--outdir` | Base directory to write results to | ./ |
| `--run_name` | Name of the directory to hold results | bactopia |
| `--skip_compression` | Ouput files will not be compressed | False |
| `--keep_all_files` | Keeps all analysis files created | False |

### Max Job Request Parameters
Set the top limit for requested resources for any single job.

| Parameter | Description | Default |
|---|---|---|
| `--max_retry` | Maximum times to retry a process before allowing it to fail. | 3 |
| `--max_cpus` | Maximum number of CPUs that can be requested for any single job. | 4 |
| `--max_memory` | Maximum amount of memory (in GB) that can be requested for any single job. | 32 |
| `--max_time` | Maximum amount of time (in minutes) that can be requested for any single job. | 120 |
| `--max_downloads` | Maximum number of samples to download at a time | 3 |

### Nextflow Configuration Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description | Default |
|---|---|---|
| `--nfconfig` | A Nextflow compatible config file for custom profiles, loaded last and will overwrite existing variables if set. |  |
| `--publish_dir_mode` | Method used to save pipeline results to output directory. | copy |
| `--infodir` | Directory to keep pipeline Nextflow logs and reports. | ${params.outdir}/pipeline_info |
| `--force` | Nextflow will overwrite existing output files. | False |
| `--cleanup_workdir` | After Bactopia is successfully executed, the `work` directory will be deleted. | False |

### Nextflow Profile Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description | Default |
|---|---|---|
| `--condadir` | Directory to Nextflow should use for Conda environments |  |
| `--registry` | Docker registry to pull containers from. | dockerhub |
| `--singularity_cache` | Directory where remote Singularity images are stored. |  |
| `--singularity_pull_docker_container` | Instead of directly downloading Singularity images for use with Singularity, force the workflow to pull and convert Docker containers instead. |  |
| `--force_rebuild` | Force overwrite of existing pre-built environments. | False |
| `--queue` | Comma-separated name of the queue(s) to be used by a job scheduler (e.g. AWS Batch or SLURM) | general,high-memory |
| `--cluster_opts` | Additional options to pass to the executor. (e.g. SLURM: '--account=my_acct_name' |  |
| `--disable_scratch` | All intermediate files created on worker nodes of will be transferred to the head node. | False |

### Helpful Parameters
Uncommonly used parameters that might be useful.

| Parameter | Description | Default |
|---|---|---|
| `--monochrome_logs` | Do not use coloured log outputs. |  |
| `--nfdir` | Print directory Nextflow has pulled Bactopia to |  |
| `--sleep_time` | The amount of time (seconds) Nextflow will wait after setting up datasets before execution. | 5 |
| `--validate_params` | Boolean whether to validate parameters against the schema at runtime | True |
| `--help` | Display help text. |  |
| `--wf` | Specify which workflow or Bactopia Tool to execute | bactopia |
| `--list_wfs` | List the available workflows and Bactopia Tools to use with '--wf' |  |
| `--show_hidden_params` | Show all params when using `--help` |  |
| `--help_all` | An alias for --help --show_hidden_params |  |
| `--version` | Display version text. |  |

## Citations
If you use Bactopia and `busco` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [BUSCO](https://gitlab.com/ezlab/busco)  
    Manni M, Berkeley MR, Seppey M, Simão FA, Zdobnov EM [BUSCO Update: Novel and Streamlined Workflows along with Broader and Deeper Phylogenetic Coverage for Scoring of Eukaryotic, Prokaryotic, and Viral Genomes.](https://doi.org/10.1093/molbev/msab199) _Molecular Biology and Evolution_ 38(10), 4647–4654. (2021)
  
