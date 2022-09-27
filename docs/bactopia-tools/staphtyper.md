---
title: Bactopia Tools - staphtyper
description: A Bactopia Tool which includes multiple tools that are specific for typing certain features of _Staphylococcus aureus_.
----
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
staphtyper/
├── <SAMPLE_NAME>
│   ├── agrvate
│   │   ├── <SAMPLE_NAME>-agr_gp.tab
│   │   ├── <SAMPLE_NAME>-blastn_log.txt
│   │   └── <SAMPLE_NAME>-summary.tab
│   ├── logs
│   │   ├── agrvate
│   │   │   ├── nf-agrvate.{begin,err,log,out,run,sh,trace}
│   │   │   └── versions.yml
│   │   ├── spatyper
│   │   │   ├── nf-spatyper.{begin,err,log,out,run,sh,trace}
│   │   │   └── versions.yml
│   │   └── staphopiasccmec
│   │       ├── nf-staphopiasccmec.{begin,err,log,out,run,sh,trace}
│   │       └── versions.yml
│   ├── spatyper
│   │   └── <SAMPLE_NAME>.tsv
│   └── staphopiasccmec
│       └── <SAMPLE_NAME>.tsv
├── logs
│   ├── csvtk_concat
│   │   ├── agrvate
│   │   │   ├── nf-csvtk_concat.{begin,err,log,out,run,sh,trace}
│   │   │   └── versions.yml
│   │   ├── spatyper
│   │   │   ├── nf-csvtk_concat.{begin,err,log,out,run,sh,trace}
│   │   │   └── versions.yml
│   │   └── staphopiasccmec
│   │       ├── nf-csvtk_concat.{begin,err,log,out,run,sh,trace}
│   │       └── versions.yml
│   └── custom_dumpsoftwareversions
│       ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── staphtyper-dag.dot
│   ├── staphtyper-report.html
│   ├── staphtyper-timeline.html
│   └── staphtyper-trace.txt
├── agrvate.tsv
├── software_versions.yml
├── software_versions_mqc.yml
├── spatyper.tsv
└── staphopiasccmec.tsv

```

!!! info "Directory structure might be different"

    `staphtyper` is available as a standalone Bactopia Tool, as well as from
    the main Bactopia workflow (e.g. through Staphopia or Merlin). If executed 
    from Bactopia, the `staphtyper` directory structure might be different, but the
    output descriptions below still apply.



### Results

#### Top Level

Below are results that are in the base directory.


| Filename    | Description |
|-------------|-------------|
| agrvate.tsv | A merged TSV file with `AgrVATE` results from all samples |
| spatyper.tsv  | A merged TSV file with `spaTyper` results from all samples |
| staphopiasccmec.tsv  | A merged TSV file with `staphopia-sccmec` results from all samples |


#### AgrVATE

Below is a description of the _per-sample_ results from [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE).


| Extension       | Description |
|-----------------|-------------|
| -agr_gp.tab     | Detailed report for _agr_ kmer matches |
| -blastn_log.txt | Log files from programs called by `AgrVATE` |
| -summary.tab    | A final summary report for _agr_ typing |


#### spaTyper

Below is a description of the _per-sample_ results from [spaTyper](https://github.com/HCGB-IGTP/spaTyper).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `spaTyper` results |


#### staphopia-sccmec

Below is a description of the _per-sample_ results from [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `staphopia-sccmec` results |





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


### AgrVATE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--typing_only` | agr typing only. Skips agr operon extraction and frameshift detection | False |

### spaTyper Parameters


| Parameter | Description | Default |
|---|---|---|
| `--repeats` | List of spa repeats |  |
| `--repeat_order` | List spa types and order of repeats |  |
| `--do_enrich` | Do PCR product enrichment | False |

### staphopia-sccmec Parameters


| Parameter | Description | Default |
|---|---|---|
| `--hamming` | Report the results as hamming distances | False |


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
If you use Bactopia and `staphtyper` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE)  
    Raghuram V. [AgrVATE: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.](https://github.com/VishnuRaghuram94/AgrVATE) (GitHub)
  
- [spaTyper](https://github.com/HCGB-IGTP/spaTyper)  
    Sanchez-Herrero JF, and Sullivan M [spaTyper: Staphylococcal protein A (spa) characterization pipeline](http://doi.org/10.5281/zenodo.4063625). Zenodo. (2020)
  
- [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec)  
    Petit III RA, Read TD [_Staphylococcus aureus_ viewed from the perspective of 40,000+ genomes.](http://dx.doi.org/10.7717/peerj.5261) _PeerJ_ 6, e5261 (2018)
  
