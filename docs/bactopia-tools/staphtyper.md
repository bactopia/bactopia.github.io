---
title: staphtyper
description: A Bactopia Tool which includes multiple tools that are specific for typing certain features of _Staphylococcus aureus_.
---
# Bactopia Tool - `staphtyper`
The `staphtyper` subworkflow includes multiple tools that are specific for typing certain features
of *Staphylococcus aureus*. Currently `staphtyper` includes

1. [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE) - *agr* locus type and *agr* operon variants.
2. [spaTyper](https://github.com/HCGB-IGTP/spaTyper) - *spa* type
3. [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec) - SCCmec type

This tool will evolve with *S. aureus* genomics, so you can expect it to add more typing methods
(maybe even replace current methods) in the future. If a certain typing method for *S. aureus*
please feel free to suggest it be added!~


## Example Usage
```
bactopia --wf staphtyper \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `staphtyper` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       ├── agrvate
│       │   ├── <SAMPLE_NAME>-agr_gp.tab
│       │   ├── <SAMPLE_NAME>-blastn_log.txt
│       │   ├── <SAMPLE_NAME>-summary.tab
│       │   └── logs
│       │       ├── nf-agrvate.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── spatyper
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-spatyper.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       └── staphopiasccmec
│           ├── <SAMPLE_NAME>.tsv
│           └── logs
│               ├── nf-staphopiasccmec.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── staphtyper-<TIMESTAMP>
        ├── merged-results
        │   ├── agrvate.tsv
        │   ├── logs
        │   │   ├── agrvate-concat
        │   │   │   ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │   │   │   └── versions.yml
        │   │   ├── spatyper-concat
        │   │   │   ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │   │   │   └── versions.yml
        │   │   └── staphopiasccmec-concat
        │   │       ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │   │       └── versions.yml
        │   ├── spatyper.tsv
        │   └── staphopiasccmec.tsv
        └── nf-reports
            ├── staphtyper-dag.dot
            ├── staphtyper-report.html
            ├── staphtyper-timeline.html
            └── staphtyper-trace.txt

```

!!! info "Directory structure might be different"

    `staphtyper` is available as a standalone Bactopia Tool, as well as from
    the main Bactopia workflow (e.g. through Staphopia or Merlin). If executed 
    from Bactopia, the `staphtyper` directory structure might be different, but the
    output descriptions below still apply.



### Results

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| agrvate.tsv | A merged TSV file with `AgrVATE` results from all samples |
| spatyper.tsv | A merged TSV file with `spaTyper` results from all samples |
| staphopiasccmec.tsv | A merged TSV file with `staphopia-sccmec` results from all samples |


#### AgrVATE

Below is a description of the _per-sample_ results from [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE).


| Extension                     | Description |
|-------------------------------|-------------|
| -agr_gp.tab | A detailed report for _agr_ kmer matches |
| -blastn_log.txt | Log files from programs called by `AgrVATE` |
| -summary.tab | A final summary report for _agr_ typing |


#### spaTyper

Below is a description of the _per-sample_ results from [spaTyper](https://github.com/HCGB-IGTP/spaTyper).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `spaTyper` result |


#### staphopia-sccmec

Below is a description of the _per-sample_ results from [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `staphopia-sccmec` results |





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
| staphtyper-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| staphtyper-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| staphtyper-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| staphtyper-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


#### Program Versions

At the end of each run, each of the `versions.yml` files are merged into the files below.

| Filename                  | Description |
|---------------------------|-------------|
| software_versions.yml     | A complete list of programs and versions used by each process | 
| software_versions_mqc.yml | A complete list of programs and versions formatted for [MultiQC](https://multiqc.info/) |

## Parameters


### <i class="fa-xl fas fa-terminal"></i> Required Parameters
Define where the pipeline should find input data and save output data.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-bacterium"></i>` --bactopia` | The path to bactopia results to use as inputs <br/>**Type:** `string` |

### <i class="fa-xl fa-solid fa-filter"></i> Filtering Parameters
Use these parameters to specify which samples to include or exclude.

| Parameter | Description |
|:---|---|
| <i class="fa-lg far fa-square-plus"></i>` --include` | A text file containing sample names (one per line) to include from the analysis <br/>**Type:** `string` |
| <i class="fa-lg far fa-square-minus"></i>` --exclude` | A text file containing sample names (one per line) to exclude from the analysis <br/>**Type:** `string` |


### <i class="fa-xl fa-solid fa-toolbox"></i> AgrVATE Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fa-solid fa-toggle-on"></i>` --typing_only` | agr typing only. Skips agr operon extraction and frameshift detection <br/>**Type:** `boolean` |

### <i class="fa-xl fas fa-exclamation-circle"></i> spaTyper Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-archive"></i>` --repeats` | List of spa repeats <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-archive"></i>` --repeat_order` | List spa types and order of repeats <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --do_enrich` | Do PCR product enrichment <br/>**Type:** `boolean` |

### <i class="fa-xl fas fa-exclamation-circle"></i> staphopia-sccmec Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --hamming` | Report the results as hamming distances <br/>**Type:** `boolean` |


### <i class="fa-xl fa-solid fa-gears"></i> Optional Parameters
These optional parameters can be useful in certain settings.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-folder"></i>` --outdir` | Base directory to write results to <br/>**Type:** `string`, **Default:** `bactopia` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_compression` | Ouput files will not be compressed <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-folder"></i>` --datasets` | The path to cache datasets to <br/>**Type:** `string` |
| <i class="fa-lg fas fa-trash-restore"></i>` --keep_all_files` | Keeps all analysis files created <br/>**Type:** `boolean` |

### <i class="fa-xl fa-solid fa-arrow-up-right-dots"></i> Max Job Request Parameters
Set the top limit for requested resources for any single job.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-redo"></i>` --max_retry` | Maximum times to retry a process before allowing it to fail. <br/>**Type:** `integer`, **Default:** `3` |
| <i class="fa-lg fas fa-microchip"></i>` --max_cpus` | Maximum number of CPUs that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `4` |
| <i class="fa-lg fas fa-memory"></i>` --max_memory` | Maximum amount of memory (in GB) that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `32` |
| <i class="fa-lg far fa-clock"></i>` --max_time` | Maximum amount of time (in minutes) that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `120` |
| <i class="fa-lg fas fa-angle-double-up"></i>` --max_downloads` | Maximum number of samples to download at a time <br/>**Type:** `integer`, **Default:** `3` |

### <i class="fa-xl fa-solid fa-screwdriver-wrench"></i> Nextflow Configuration Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-cog"></i>` --nfconfig` | A Nextflow compatible config file for custom profiles, loaded last and will overwrite existing variables if set. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-copy"></i>` --publish_dir_mode` | Method used to save pipeline results to output directory. <br/>**Type:** `string`, **Default:** `copy` |
| <i class="fa-lg fas fa-cogs"></i>` --infodir` | Directory to keep pipeline Nextflow logs and reports. <br/>**Type:** `string`, **Default:** `${params.outdir}/pipeline_info` |
| <i class="fa-lg fas fa-recycle"></i>` --force` | Nextflow will overwrite existing output files. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-trash-alt"></i>` --cleanup_workdir` | After Bactopia is successfully executed, the `work` directory will be deleted. <br/>**Type:** `boolean` |

### <i class="fa-xl fas fa-university"></i> Institutional config options
Parameters used to describe centralized config profiles. These should not be edited.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-users-cog"></i>` --custom_config_version` | Git commit id for Institutional configs. <br/>**Type:** `string`, **Default:** `master` |
| <i class="fa-lg fas fa-users-cog"></i>` --custom_config_base` | Base directory for Institutional configs. <br/>**Type:** `string`, **Default:** `https://raw.githubusercontent.com/nf-core/configs/master` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_name` | Institutional config name. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_description` | Institutional config description. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_contact` | Institutional config contact information. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_url` | Institutional config URL link. <br/>**Type:** `string` |

### <i class="fa-xl fa-regular fa-address-card"></i> Nextflow Profile Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-folder"></i>` --condadir` | Directory to Nextflow should use for Conda environments <br/>**Type:** `string` |
| <i class="fa-lg fas fa-box"></i>` --registry` | Docker registry to pull containers from. <br/>**Type:** `string`, **Default:** `dockerhub` |
| <i class="fa-lg fas fa-folder"></i>` --datasets_cache` | Directory where downloaded datasets should be stored. <br/>**Type:** `string`, **Default:** `<BACTOPIA_DIR>/data/datasets` |
| <i class="fa-lg fas fa-folder"></i>` --singularity_cache_dir` | Directory where remote Singularity images are stored. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-toolbox"></i>` --singularity_pull_docker_container` | Instead of directly downloading Singularity images for use with Singularity, force the workflow to pull and convert Docker containers instead. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-recycle"></i>` --force_rebuild` | Force overwrite of existing pre-built environments. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-clipboard-list"></i>` --queue` | Comma-separated name of the queue(s) to be used by a job scheduler (e.g. AWS Batch or SLURM) <br/>**Type:** `string`, **Default:** `general,high-memory` |
| <i class="fa-lg fas fa-clipboard-list"></i>` --cluster_opts` | Additional options to pass to the executor. (e.g. SLURM: '--account=my_acct_name' <br/>**Type:** `string` |
| <i class="fa-lg fas fa-clipboard-list"></i>` --container_opts` | Additional options to pass to Apptainer, Docker, or Singularityu. (e.g. Singularity: '-D `pwd`' <br/>**Type:** `string` |
| <i class="fa-lg fas fa-toggle-off"></i>` --disable_scratch` | All intermediate files created on worker nodes of will be transferred to the head node. <br/>**Type:** `boolean` |

### <i class="fa-xl fa-solid fa-reply-all"></i> Helpful Parameters
Uncommonly used parameters that might be useful.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-palette"></i>` --monochrome_logs` | Do not use coloured log outputs. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-remove-format"></i>` --nfdir` | Print directory Nextflow has pulled Bactopia to <br/>**Type:** `boolean` |
| <i class="fa-lg far fa-clock"></i>` --sleep_time` | The amount of time (seconds) Nextflow will wait after setting up datasets before execution. <br/>**Type:** `integer`, **Default:** `5` |
| <i class="fa-lg fas fa-tasks"></i>` --validate_params` | Boolean whether to validate parameters against the schema at runtime <br/>**Type:** `boolean`, **Default:** `True` |
| <i class="fa-lg fas fa-question-circle"></i>` --help` | Display help text. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-bacteria"></i>` --wf` | Specify which workflow or Bactopia Tool to execute <br/>**Type:** `string`, **Default:** `bactopia` |
| <i class="fa-lg fas fa-list"></i>` --list_wfs` | List the available workflows and Bactopia Tools to use with '--wf' <br/>**Type:** `boolean` |
| <i class="fa-lg far fa-eye"></i>` --show_hidden_params` | Show all params when using `--help` <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-question-circle"></i>` --help_all` | An alias for --help --show_hidden_params <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-info"></i>` --version` | Display version text. <br/>**Type:** `boolean` |

## Citations
If you use Bactopia and `staphtyper` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE)  
    Raghuram V. [AgrVATE: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.](https://github.com/VishnuRaghuram94/AgrVATE) (GitHub)
  
- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [spaTyper](https://github.com/HCGB-IGTP/spaTyper)  
    Sanchez-Herrero JF, and Sullivan M [spaTyper: Staphylococcal protein A (spa) characterization pipeline](http://doi.org/10.5281/zenodo.4063625). Zenodo. (2020)
  
- [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec)  
    Petit III RA, Read TD [_Staphylococcus aureus_ viewed from the perspective of 40,000+ genomes.](http://dx.doi.org/10.7717/peerj.5261) _PeerJ_ 6, e5261 (2018)
  
