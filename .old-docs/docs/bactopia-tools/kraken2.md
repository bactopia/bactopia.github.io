---
title: kraken2
description: A Bactopia Tool which uses Kraken2 to assign taxonomic classifications to your sequence reads.
---
# Bactopia Tool - `kraken2`
The `kraken2` module uses [Kraken2](https://github.com/DerrickWood/kraken2) to assign taxonomic 
classifications to your sequence reads.


## Example Usage
```
bactopia --wf kraken2 \
  --bactopia /path/to/your/bactopia/results  
```

## Output Overview

Below is the default output structure for the `kraken2` tool. Where possible the 
file descriptions below were modified from a tools description.

```bash
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── kraken2
│           ├── <SAMPLE_NAME>.classified_{1|2}.fastq.gz
│           ├── <SAMPLE_NAME>.kraken2.report.txt
│           ├── <SAMPLE_NAME>.unclassified_{1,2}.fastq.gz
│           └── logs
│               ├── nf-kraken2.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── kraken2-<TIMESTAMP>
        └── nf-reports
            ├── kraken2-dag.dot
            ├── kraken2-report.html
            ├── kraken2-timeline.html
            └── kraken2-trace.txt

```



### Results

#### Kraken2

Below is a description of the _per-sample_ results from [Kraken2](https://github.com/DerrickWood/kraken2).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.classified_{1|2}.fastq.gz | Reads classified to belong to any of the taxa on the Kraken2 database. |
| &lt;SAMPLE_NAME&gt;.kraken2.report.txt | Kraken2 report containing stats about classified and not classified reads See [Kraken2 - Output Formats](https://github.com/DerrickWood/kraken2/wiki/Manual#output-formats) for more details |
| &lt;SAMPLE_NAME&gt;.unclassified_{1,2}.fastq.gz | Reads not classified to belong to any of the taxa on the Kraken2 database. |





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
| kraken2-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| kraken2-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| kraken2-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| kraken2-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### Kraken2 Parameters


| Parameter | Description |
|:---|---|
| ` --kraken2_db` | The a single tarball or path to a Kraken2 formatted database <br/>**Type:** `string` |
| ` --quick_mode` | Quick operation (use first hit or hits) <br/>**Type:** `boolean` |
| ` --confidence` | Confidence score threshold between 0 and 1 <br/>**Type:** `number` |
| ` --minimum_base_quality` | Minimum base quality used in classification <br/>**Type:** `integer` |
| ` --use_mpa_style` | Format report output like Kraken 1's kraken-mpa-report <br/>**Type:** `boolean` |
| ` --report_zero_counts` | Report counts for ALL taxa, even if counts are zero <br/>**Type:** `boolean` |
| ` --report_minimizer_data` | Include minimizer and distinct minimizer count information in report <br/>**Type:** `boolean` |
| ` --use_names` | Print scientific names instead of just taxids <br/>**Type:** `boolean` |
| ` --memory_mapping` | Avoid loading database into RAM <br/>**Type:** `boolean` |
| ` --minimum_hit_groups` | Minimum number of hit groups needed to make a call <br/>**Type:** `integer`, **Default:** `2` |
| ` --remove_filtered_reads` | Discard the classified and unclassified FASTQs produced by Kraken2 <br/>**Type:** `boolean` |


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
If you use Bactopia and `kraken2` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Kraken2](https://github.com/DerrickWood/kraken2)  
    Wood DE, Lu J, Langmead B [Improved metagenomic analysis with Kraken 2.](https://doi.org/10.1186/s13059-019-1891-0) *Genome Biology*, 20(1), 257. (2019)
  
