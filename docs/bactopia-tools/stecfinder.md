---
title: stecfinder
description: A Bactopia Tool which uses STECFinder to identify the serotype of Shigatoxin producing _E. coli_ (STEC).

---
# Bactopia Tool - `stecfinder`
The `stecfinder` module uses [STECFinder](https://github.com/LanLab/STECFinder) to identify
the serotype of Shigatoxin producing _E. coli_ (STEC). STECFinder identifies the serotype
as well as the O-antigen and H-antigens.


## Example Usage
```
bactopia --wf stecfinder \
  --bactopia /path/to/your/bactopia/results  
```

## Output Overview

Below is the default output structure for the `stecfinder` tool. Where possible the 
file descriptions below were modified from a tools description.

```bash
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── stecfinder
│           ├── <SAMPLE_NAME>.tsv
│           └── logs
│               ├── nf-stecfinder.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── stecfinder-<TIMESTAMP>
        ├── merged-results
        │   ├── logs
        │   │   └── stecfinder-concat
        │   │       ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │   │       └── versions.yml
        │   └── stecfinder.tsv
        └── nf-reports
            ├── stecfinder-dag.dot
            ├── stecfinder-report.html
            ├── stecfinder-timeline.html
            └── stecfinder-trace.txt

```



### Results

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| stecfinder.tsv | A summary of the `stecfinder` results for all samples |


#### STECFinder

Below is a description of the _per-sample_ results from [STECFinder](https://github.com/LanLab/STECFinder).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | The `stecfinder` results in tab-delimited format. See [STECFinder Column Descriptions](https://github.com/LanLab/STECFinder#column-descriptions) for more details. |





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
| stecfinder-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| stecfinder-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| stecfinder-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| stecfinder-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### STECFinder Parameters


| Parameter | Description |
|:---|---|
| ` --stecfinder_use_reads` | Paired-end Illumina reads will be used instead of assemblies <br/>**Type:** `boolean` |
| ` --stecfinder_hits` | Show detailed gene search results <br/>**Type:** `boolean` |
| ` --stecfinder_cutoff` | Minimum read coverage for gene to be called <br/>**Type:** `number`, **Default:** `10.0` |
| ` --stecfinder_length` | Percentage of gene length needed for positive call <br/>**Type:** `number`, **Default:** `50.0` |
| ` --stecfinder_ipah_length` | Percentage of ipaH gene length needed for positive gene call <br/>**Type:** `number`, **Default:** `10.0` |
| ` --stecfinder_ipah_depth` | Minimum depth for positive ipaH gene call (requires --stecfinder_use_reads) <br/>**Type:** `number`, **Default:** `1.0` |
| ` --stecfinder_stx_length` | Percentage of stx gene length needed for positive gene call <br/>**Type:** `number`, **Default:** `10.0` |
| ` --stecfinder_stx_depth` | Minimum depth for positive stx gene call (requires --stecfinder_use_reads) <br/>**Type:** `number`, **Default:** `10.0` |
| ` --stecfinder_o_length` | Percentage of wz_ gene length needed for positive call <br/>**Type:** `number`, **Default:** `60.0` |
| ` --stecfinder_o_depth` | Minimum depth for positive qz_ gene call (requires --stecfinder_use_reads) <br/>**Type:** `number`, **Default:** `1.0` |
| ` --stecfinder_h_length` | Percentage of fliC gene length needed for positive call <br/>**Type:** `number`, **Default:** `60.0` |
| ` --stecfinder_h_depth` | Minimum depth for positive fliC gene call (requires --stecfinder_use_reads) <br/>**Type:** `number`, **Default:** `1.0` |


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
If you use Bactopia and `stecfinder` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [STECFinder](https://github.com/LanLab/STECFinder)  
    Zhang X, Payne M, Kaur S, and Lan R [Improved Genomic Identification, Clustering, and Serotyping of Shiga Toxin-Producing Escherichia coli Using Cluster/Serotype-Specific Gene Markers.](https://doi.org/10.3389/fcimb.2021.772574) _Frontiers in Cellular and Infection Microbiology_, 11, 772574. (2021)
  
