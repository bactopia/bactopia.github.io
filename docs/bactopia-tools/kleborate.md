---
title: Bactopia Tools - kleborate
description: A Bactopia Tool which uses Kleborate to screen genome assemblies of _Klebsiella pneumoniae_ and the _Klebsiella pneumoniae_ species complex (KpSC).
---
# Bactopia Tool - `kleborate`
The `kleborate` module uses [Kleborate](https://github.com/katholt/Kleborate) to screen genome assemblies of 
_Klebsiella pneumoniae_ and the _Klebsiella pneumoniae_ species complex (KpSC). Kleborate predicts:

- MLST, species,
- ICEKp associated virulence loci
- virulence plasmid associated loci
- antimicrobial resistance determinants,
- K (capsule) and O antigen (LPS) serotype prediction.


## Example Usage
```
bactopia --wf kleborate \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `kleborate` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
kleborate
├── <SAMPLE_NAME>
│   ├── <SAMPLE_NAME>.results.txt
│   └── logs
│       └── kleborate
│           ├── nf-kleborate.{begin,err,log,out,run,sh,trace}
│           └── versions.yml
├── logs
│   ├── csvtk_concat
│   │   ├── nf-csvtk_concat.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   └── custom_dumpsoftwareversions
│       ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── kleborate-dag.dot
│   ├── kleborate-report.html
│   ├── kleborate-timeline.html
│   └── kleborate-trace.txt
├── kleborate.tsv
├── software_versions.yml
└── software_versions_mqc.yml

```

!!! info "Directory structure might be different"

    `kleborate` is available as a standalone Bactopia Tool, as well as from
    the main Bactopia workflow (e.g. through Staphopia or Merlin). If executed 
    from Bactopia, the `kleborate` directory structure might be different, but the
    output descriptions below still apply.



### Results

#### Top Level

Below are results that are in the base directory.


| Filename    | Description |
|-------------|-------------|
| kleborate.tsv | A merged TSV file with `Kleborate` results from all samples |


#### Kleborate

Below is a description of the _per-sample_ results from [Kleborate](https://github.com/katholt/Kleborate).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.results.tsv  | A tab-delimited file with `Kleborate` result, see [Kleborate - Example output](https://github.com/katholt/Kleborate/wiki/Tests-and-example-outputs#example-output) for more details |





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
| kleborate-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| kleborate-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| kleborate-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| kleborate-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### Kleborate Parameters


| Parameter | Description | Default |
|---|---|---|
| `--skip_resistance` | Turn off resistance genes screening | False |
| `--skip_kaptive` | Turn off Kaptive screening of K and O loci | False |
| `--min_identity` | Minimum alignment percent identity for main results | 90.0 |
| `--kleborate_min_coverage` | Minimum alignment percent coverage for main results | 80.0 |
| `--min_spurious_identity` | Minimum alignment percent identity for spurious results | 80.0 |
| `--min_spurious_coverage` | Minimum alignment percent coverage for spurious results | 40.0 |
| `--min_kaptive_confidence` | Minimum Kaptive confidence to call K/O loci - confidence levels below this will be reported as unknown | Good |
| `--force_index` | Rebuild the BLAST index at the start of execution | False |


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
If you use Bactopia and `kleborate` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Kaptive](https://github.com/katholt/Kaptive)  
    Wyres KL, Wick RR, Gorrie C, Jenney A, Follador R, Thomson NR, Holt KE [Identification of Klebsiella capsule synthesis loci from whole genome data.](https://doi.org/10.1099/mgen.0.000102) _Microbial genomics_ 2(12) (2016)
  
- [Kleborate](https://github.com/katholt/Kleborate)  
    Lam MMC, Wick RR, Watts, SC, Cerdeira LT, Wyres KL, Holt KE [A genomic surveillance framework and genotyping tool for Klebsiella pneumoniae and its related species complex.](https://doi.org/10.1038/s41467-021-24448-3) _Nat Commun_ 12, 4188 (2021)
  
