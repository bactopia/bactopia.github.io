---
tags:
---



# Bactopia Tool - `ariba`
The `ariba` module uses [ARIBA](https://github.com/sanger-pathogens/ariba) 
to rapidly identify genes in a database by creating local assemblies.


## Example Usage
```
bactopia --wf ariba \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `ariba` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
ariba/
├── <DATABASE>
│   └── <SAMPLE_NAME>
│       ├── card
│       │   ├── assembled_genes.fa.gz
│       │   ├── assembled_seqs.fa.gz
│       │   ├── assemblies.fa.gz
│       │   ├── debug.report.tsv
│       │   ├── log.clusters.gz
│       │   ├── report.tsv
│       │   ├── summary.csv
│       │   └── version_info.txt
│       └── logs
│           └── ariba
│               ├── nf-ariba.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
├── logs
│   ├── csvtk_concat
│   │   ├── nf-csvtk_concat.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   └── custom_dumpsoftwareversions
│       ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── ariba-dag.dot
│   ├── ariba-report.html
│   ├── ariba-timeline.html
│   └── ariba-trace.txt
├── ariba-report.tsv
├── ariba-summary.csv
├── software_versions.yml
└── software_versions_mqc.yml

```

!!! info "Directory structure might be different"

    `ariba` is available as a standalone Bactopia Tool, as well as from
    the main Bactopia workflow (e.g. through Staphopia or Merlin). If executed 
    from Bactopia, the `ariba` directory structure might be different, but the
    output descriptions below still apply.



### Results

#### Top Level

Below are results that are in the base directory.


| Filename    | Description |
|-------------|-------------|
| ariba-report.tsv | A merged TSV file with `ARIBA` results from all samples |
| ariba-summary.csv | A merged CSV file created with `ariba summary` |


#### ARIBA

Below is a description of the _per-sample_ results from [ARIBA](https://github.com/sanger-pathogens/ariba/wiki/Task:-run).


| Filename              | Description |
|-----------------------|-------------|
| assembled_genes.fa.gz | All the assembled genes |
| assembled_seqs.fa.gz  | All the assembled sequences that match the reference |
| assemblies.fa.gz      | All the raw local assembles |
| debug.report.tsv      | Contains the results from `report.tsv` in addition to synonymous mutations |
| log.clusters.gz       | A log of the ARIBA analysis |
| report.tsv            | A report of the ARIBA analysis results |
| summary.csv           | A summary of the report created using `ariba summary` |
| version_info.txt      | Containes info on the versions of ARIBA and its dependencies |





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
| ariba-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| ariba-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| ariba-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| ariba-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### Ariba GetRef Parameters


| Parameter | Description | Default |
|---|---|---|
| `--ariba_dir` | Path to save or retrieve Ariba databases |  |
| `--ariba_db` | A database to query, if unavailable it will be downloaded to the path given by --ariba_dir |  |

### Ariba Run Parameters


| Parameter | Description | Default |
|---|---|---|
| `--nucmer_min_id` | Minimum alignment identity (delta-filter -i) | 90 |
| `--nucmer_min_len` | Minimum alignment identity (delta-filter -i) | 20 |
| `--nucmer_breaklen` | Value to use for -breaklen when running nucmer | 200 |
| `--assembly_cov` | Target read coverage when sampling reads for assembly | 50 |
| `--min_scaff_depth` | Minimum number of read pairs needed as evidence for scaffold link between two contigs | 10 |
| `--spades_options` | Extra options to pass to Spades assembler |  |
| `--assembled_threshold` | If proportion of gene assembled (regardless of into how many contigs) is at least this value then the flag gene_assembled is set | 0.95 |
| `--gene_nt_extend` | Max number of nucleotides to extend ends of gene matches to look for start/stop codons | 30 |
| `--unique_threshold` | If proportion of bases in gene assembled more than once is <= this value, then the flag unique_contig is set | 0.03 |
| `--ariba_no_clean` | Do not clean up intermediate files created by Ariba. |  |


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
If you use Bactopia and `ariba` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Ariba](https://github.com/sanger-pathogens/ariba)  
    Hunt M, Mather AE, Sánchez-Busó L, Page AJ, Parkhill J, Keane JA, Harris SR [ARIBA: rapid antimicrobial resistance genotyping directly from sequencing reads](http://dx.doi.org/10.1099/mgen.0.000131). _Microb Genom_ 3, e000131 (2017)
  
