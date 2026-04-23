---
title: ismapper
description: A Bactopia Tool which uses ISMapper to search for insertion sites in your samples.
---
# Bactopia Tool - `ismapper`
The `ismapper` module uses [ISMapper](https://github.com/jhawkey/IS_mapper) to search for 
insertion sites in your samples.


## Example Usage
```
bactopia --wf ismapper \
  --bactopia /path/to/your/bactopia/results  
```

## Output Overview

Below is the default output structure for the `ismapper` tool. Where possible the 
file descriptions below were modified from a tools description.

```bash
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── ismapper
│           └── ismapper
│               ├── <INSERTION_NAME>
│               │   ├── <SAMPLE_NAME>_<FASTA_ENTRY>_{left_final,right_final}.fastq
│               │   ├── <SAMPLE_NAME>__<REFERENCE>_closest.bed
│               │   ├── <SAMPLE_NAME>__<REFERENCE>_intersect.bed
│               │   ├── <SAMPLE_NAME>__<REFERENCE>_table.txt
│               │   ├── <SAMPLE_NAME>_{left,right}_<REFERENCE>_finalcov.bed
│               │   ├── <SAMPLE_NAME>_{left,right}_<REFERENCE>_merged.sorted.bed
│               │   └── <SAMPLE_NAME>_{left,right}_<REFERENCE>_unpaired.bed
│               └── logs
│                   ├── SRR2838702.log
│                   ├── nf-ismapper.{begin,err,log,out,run,sh,trace}
│                   └── versions.yml
└── bactopia-runs
    └── ismapper-<TIMESTAMP>
        └── nf-reports
            ├── ismapper-dag.dot
            ├── ismapper-report.html
            ├── ismapper-timeline.html
            └── ismapper-trace.txt

```



### Results

#### ISMapper

Below is a description of the _per-sample_ results from [ISMapper](https://github.com/jhawkey/IS_mapper).


| Extension                     | Description |
|-------------------------------|-------------|
| _final.fastq | Sequences (FASTQ format) that mapped to the flanking regions of the IS query. |
| _closest.bed | Merged regions that are close but do not overlap. |
| _intersect.bed | An intersection of merged regions from the left and right flanks. |
| _table.txt | A [detailed description](https://github.com/jhawkey/IS_mapper#single-isolate-output) of the IS query results. |
| _finalcov.bed | Contains information about the coverage of the IS query |
| _merged.sorted.bed | Merged overlapping regions that passed coverage cutoffs |
| _unpaired.bed | All unpaired mappings to the IS query |





### Audit Trail

Below are files that can assist you in understanding which parameters and program versions were used.

#### Logs 

Each process that is executed will have a folder named `logs`. In this folder are helpful
files for you to review if the need ever arises.

| Extension    | Description |
|--------------|-------------|
| .begin       | An empty file used to designate the process started |
| .err         | Contains STDERR outputs from the process |
| .log         | Contains both STDERR and STDOUT outputs from the process |
| .out         | Contains STDOUT outputs from the process |
| .run         | The script Nextflow uses to stage/unstage files and queue processes based on given profile |
| .sh          | The script executed by bash for the process  |
| .trace       | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report for the process |
| versions.yml | A YAML formatted file with program versions |

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

| Parameter | Description |
|:---|---|
| ` --bactopia` | The path to bactopia results to use as inputs <br/>**Type:** `string` |

### Filtering Parameters
Use these parameters to specify which samples to include or exclude.

| Parameter | Description |
|:---|---|
| ` --include` | A text file containing sample names (one per line) to include from the analysis <br/>**Type:** `string` |
| ` --exclude` | A text file containing sample names (one per line) to exclude from the analysis <br/>**Type:** `string` |


### ISMapper Parameters


| Parameter | Description |
|:---|---|
| ` --reference` | Reference genome for typing against in GenBank format <br/>**Type:** `string` |
| ` --insertions` | Multifasta file with insertion sequence(s) to be mapped to <br/>**Type:** `string` |
| ` --min_clip` | Minimum size for softclipped region to be extracted from initial mapping <br/>**Type:** `integer`, **Default:** `10` |
| ` --max_clip` | Maximum size for softclipped regions to be included <br/>**Type:** `integer`, **Default:** `30` |
| ` --cutoff` | Minimum depth for mapped region to be kept in bed file <br/>**Type:** `integer`, **Default:** `6` |
| ` --novel_gap_size` | Distance in base pairs between left and right flanks to be called a novel hit <br/>**Type:** `integer`, **Default:** `15` |
| ` --min_range` | Minimum percent size of the gap to be called a known hit <br/>**Type:** `number`, **Default:** `0.9` |
| ` --max_range` | Maximum percent size of the gap to be called a known hit <br/>**Type:** `number`, **Default:** `1.1` |
| ` --merging` | Value for merging left and right hits in bed files together to simply calculation of closest and intersecting regions <br/>**Type:** `integer`, **Default:** `100` |
| ` --ismap_all` | Switch on all alignment reporting for bwa <br/>**Type:** `boolean` |
| ` --ismap_minqual` | Mapping quality score for bwa <br/>**Type:** `integer`, **Default:** `30` |


### Optional Parameters
These optional parameters can be useful in certain settings.

| Parameter | Description |
|:---|---|
| ` --outdir` | Base directory to write results to <br/>**Type:** `string`, **Default:** `bactopia` |
| ` --skip_compression` | Ouput files will not be compressed <br/>**Type:** `boolean` |
| ` --datasets` | The path to cache datasets to <br/>**Type:** `string` |
| ` --keep_all_files` | Keeps all analysis files created <br/>**Type:** `boolean` |

### Max Job Request Parameters
Set the top limit for requested resources for any single job.

| Parameter | Description |
|:---|---|
| ` --max_retry` | Maximum times to retry a process before allowing it to fail. <br/>**Type:** `integer`, **Default:** `3` |
| ` --max_cpus` | Maximum number of CPUs that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `4` |
| ` --max_memory` | Maximum amount of memory that can be requested for any single job. <br/>**Type:** `string`, **Default:** `128.GB` |
| ` --max_time` | Maximum amount of time that can be requested for any single job. <br/>**Type:** `string`, **Default:** `240.h` |
| ` --max_downloads` | Maximum number of samples to download at a time <br/>**Type:** `integer`, **Default:** `3` |

### Nextflow Configuration Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| ` --nfconfig` | A Nextflow compatible config file for custom profiles, loaded last and will overwrite existing variables if set. <br/>**Type:** `string` |
| ` --publish_dir_mode` | Method used to save pipeline results to output directory. <br/>**Type:** `string`, **Default:** `copy` |
| ` --infodir` | Directory to keep pipeline Nextflow logs and reports. <br/>**Type:** `string`, **Default:** `${params.outdir}/pipeline_info` |
| ` --force` | Nextflow will overwrite existing output files. <br/>**Type:** `boolean` |
| ` --cleanup_workdir` | After Bactopia is successfully executed, the `work` directory will be deleted. <br/>**Type:** `boolean` |

### Institutional config options
Parameters used to describe centralized config profiles. These should not be edited.

| Parameter | Description |
|:---|---|
| ` --custom_config_version` | Git commit id for Institutional configs. <br/>**Type:** `string`, **Default:** `master` |
| ` --custom_config_base` | Base directory for Institutional configs. <br/>**Type:** `string`, **Default:** `https://raw.githubusercontent.com/nf-core/configs/master` |
| ` --config_profile_name` | Institutional config name. <br/>**Type:** `string` |
| ` --config_profile_description` | Institutional config description. <br/>**Type:** `string` |
| ` --config_profile_contact` | Institutional config contact information. <br/>**Type:** `string` |
| ` --config_profile_url` | Institutional config URL link. <br/>**Type:** `string` |

### Nextflow Profile Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| ` --condadir` | Directory to Nextflow should use for Conda environments <br/>**Type:** `string` |
| ` --registry` | Docker registry to pull containers from. <br/>**Type:** `string`, **Default:** `dockerhub` |
| ` --datasets_cache` | Directory where downloaded datasets should be stored. <br/>**Type:** `string`, **Default:** `<BACTOPIA_DIR>/data/datasets` |
| ` --singularity_cache_dir` | Directory where remote Singularity images are stored. <br/>**Type:** `string` |
| ` --singularity_pull_docker_container` | Instead of directly downloading Singularity images for use with Singularity, force the workflow to pull and convert Docker containers instead. <br/>**Type:** `boolean` |
| ` --force_rebuild` | Force overwrite of existing pre-built environments. <br/>**Type:** `boolean` |
| ` --queue` | Comma-separated name of the queue(s) to be used by a job scheduler (e.g. AWS Batch or SLURM) <br/>**Type:** `string`, **Default:** `general,high-memory` |
| ` --cluster_opts` | Additional options to pass to the executor. (e.g. SLURM: '--account=my_acct_name' <br/>**Type:** `string` |
| ` --container_opts` | Additional options to pass to Apptainer, Docker, or Singularityu. (e.g. Singularity: '-D `pwd`' <br/>**Type:** `string` |
| ` --disable_scratch` | All intermediate files created on worker nodes of will be transferred to the head node. <br/>**Type:** `boolean` |

### Helpful Parameters
Uncommonly used parameters that might be useful.

| Parameter | Description |
|:---|---|
| ` --monochrome_logs` | Do not use coloured log outputs. <br/>**Type:** `boolean` |
| ` --nfdir` | Print directory Nextflow has pulled Bactopia to <br/>**Type:** `boolean` |
| ` --sleep_time` | The amount of time (seconds) Nextflow will wait after setting up datasets before execution. <br/>**Type:** `integer`, **Default:** `5` |
| ` --validate_params` | Boolean whether to validate parameters against the schema at runtime <br/>**Type:** `boolean`, **Default:** `True` |
| ` --help` | Display help text. <br/>**Type:** `boolean` |
| ` --wf` | Specify which workflow or Bactopia Tool to execute <br/>**Type:** `string`, **Default:** `bactopia` |
| ` --list_wfs` | List the available workflows and Bactopia Tools to use with '--wf' <br/>**Type:** `boolean` |
| ` --show_hidden_params` | Show all params when using `--help` <br/>**Type:** `boolean` |
| ` --help_all` | An alias for --help --show_hidden_params <br/>**Type:** `boolean` |
| ` --version` | Display version text. <br/>**Type:** `boolean` |

## Citations
If you use Bactopia and `ismapper` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [ISMapper](https://github.com/jhawkey/IS_mapper)  
    Hawkey J, Hamidian M, Wick RR, Edwards DJ, Billman-Jacobe H, Hall RM, Holt KE [ISMapper: identifying transposase insertion sites in bacterial genomes from short read sequence data](http://dx.doi.org/10.1186/s12864-015-1860-2). _BMC Genomics_ 16, 667 (2015)
  
