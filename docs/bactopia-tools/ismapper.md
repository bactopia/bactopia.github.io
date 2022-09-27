---
title: Bactopia Tools - ismapper
description: A Bactopia Tool which uses ISMapper to search for insertion sites in your samples.
----
# Bactopia Tool - `ismapper`
The `ismapper` module uses [ISMapper](https://github.com/jhawkey/IS_mapper) to search for 
insertion sites in your samples.


## Example Usage
```
bactopia --wf ismapper \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `ismapper` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
ismapper/
├── <SAMPLE_NAME>
│   ├── <INSERTION_NAME>
│   │   └── <FASTA_ENTRY>
│   │       ├── <SAMPLE_NAME>_<FASTA_ENTRY>_{left_final,right_final}.fastq
│   │       ├── <SAMPLE_NAME>__<REFERENCE>_closest.bed
│   │       ├── <SAMPLE_NAME>__<REFERENCE>_intersect.bed
│   │       ├── <SAMPLE_NAME>__<REFERENCE>_table.txt
│   │       ├── <SAMPLE_NAME>_{left,right}_<REFERENCE>_finalcov.bed
│   │       ├── <SAMPLE_NAME>_{left,right}_<REFERENCE>_merged.sorted.bed
│   │       └── <SAMPLE_NAME>_{left,right}_<REFERENCE>_unpaired.bed
│   └── logs
│       └── ismapper
│           └── <INSERTION_NAME>
│               ├── <SAMPLE_NAME>.log
│               ├── nf-ismapper.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
├── logs
│   └── custom_dumpsoftwareversions
│       ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── ismapper-dag.dot
│   ├── ismapper-report.html
│   ├── ismapper-timeline.html
│   └── ismapper-trace.txt
├── software_versions.yml
└── software_versions_mqc.yml

```



### Results

#### ISMapper

Below is a description of the _per-sample_ results from [ISMapper](https://github.com/jhawkey/IS_mapper).


| Extension | Description |
|-----------|-------------|
| _final.fastq | Sequences (FASTQ format) that mapped to the flanking regions of the IS query |
| _closest.bed | Merged regions that are close but do not overlap |
| _intersect.bed | An intersection of merged regions from the left and right flanks. |
| _table.txt | A [detailed description](https://github.com/jhawkey/IS_mapper#single-isolate-output) of the IS query results. |
| _finalcov.bed | Contains information about the coverage of the IS query |
| _merged.sorted.bed | Merged overlapping regions that passed coverage cutoffs |
| _unpaired.bed | All unpaired mappings to the IS query  |





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
| ismapper-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| ismapper-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| ismapper-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| ismapper-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### ISMapper Parameters


| Parameter | Description | Default |
|---|---|---|
| `--reference` | Reference genome for typing against in GenBank format |  |
| `--insertions` | Multifasta file with insertion sequence(s) to be mapped to |  |
| `--min_clip` | Minimum size for softclipped region to be extracted from initial mapping | 10 |
| `--max_clip` | Maximum size for softclipped regions to be included | 30 |
| `--cutoff` | Minimum depth for mapped region to be kept in bed file | 6 |
| `--novel_gap_size` | Distance in base pairs between left and right flanks to be called a novel hit | 15 |
| `--min_range` | Minimum percent size of the gap to be called a known hit | 0.9 |
| `--max_range` | Maximum percent size of the gap to be called a known hit | 1.1 |
| `--merging` | Value for merging left and right hits in bed files together to simply calculation of closest and intersecting regions | 100 |
| `--ismap_all` | Switch on all alignment reporting for bwa | False |
| `--ismap_minqual` | Mapping quality score for bwa | 30 |


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
If you use Bactopia and `ismapper` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [ISMapper](https://github.com/jhawkey/IS_mapper)  
    Hawkey J, Hamidian M, Wick RR, Edwards DJ, Billman-Jacobe H, Hall RM, Holt KE [ISMapper: identifying transposase insertion sites in bacterial genomes from short read sequence data](http://dx.doi.org/10.1186/s12864-015-1860-2). _BMC Genomics_ 16, 667 (2015)
  
