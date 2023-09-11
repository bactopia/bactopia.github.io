---
title: bracken
description: A Bactopia Tool which uses Bracken (and Kraken2) to estimate taxonomic abundance of samples.

---
# Bactopia Tool - `bracken`
The `bracken` module uses [Bracken](https://github.com/jenniferlu717/Bracken) to estimate
taxonomic abundance of samples. This Bactopia Tool will also run [Kraken2](https://ccb.jhu.edu/software/kraken2/), 
automatically and generate [Krona](https://github.com/marbl/Krona) charts for both Bracken and Kraken2.


## Example Usage
```
bactopia --wf bracken \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `bracken` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── bracken
│           ├── <SAMPLE_NAME>.bracken.abundances.txt
│           ├── <SAMPLE_NAME>.bracken.adjusted.abundances.txt
│           ├── <SAMPLE_NAME>.bracken.krona.html
│           ├── <SAMPLE_NAME>.bracken.report.txt
│           ├── <SAMPLE_NAME>.bracken.tsv
│           ├── <SAMPLE_NAME>.classified_{1,2}.fastq.gz
│           ├── <SAMPLE_NAME>.kraken2.krona.html
│           ├── <SAMPLE_NAME>.kraken2.output.txt
│           ├── <SAMPLE_NAME>.kraken2.report.txt
│           ├── <SAMPLE_NAME>.unclassified_{1,2}.fastq.gz
│           └── logs
│               ├── nf-bracken.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── bracken-<TIMESTAMP>
        └── nf-reports
            ├── bracken-dag.dot
            ├── bracken-report.html
            ├── bracken-timeline.html
            └── bracken-trace.txt

```



### Results

#### Bracken & Kraken2

Below is a description of the _per-sample_ results from [Bracken](https://github.com/jenniferlu717/Bracken)
and [Kraken2](https://github.com/DerrickWood/kraken2).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.bracken.abundances.txt | Bracken abundance estimates for each taxon. |
| &lt;SAMPLE_NAME&gt;.bracken.adjusted.abundances.txt | Bracken abundance estimates for each taxon adjusted for inclusion of unclassified reads |
| &lt;SAMPLE_NAME&gt;.bracken.krona.html | Krona chart of Bracken abundance estimates |
| &lt;SAMPLE_NAME&gt;.bracken.report.txt | Bracken report containing stats about classified and not classified reads See [Bracken - Output Formats](https://ccb.jhu.edu/software/bracken/index.shtml?t=manual) |
| &lt;SAMPLE_NAME&gt;.classified_{1|2}.fastq.gz | Reads classified to belong to any of the taxa on the Kraken2 database. |
| &lt;SAMPLE_NAME&gt;.kraken2.krona.html | Krona chart of Kraken2 abundance estimates |
| &lt;SAMPLE_NAME&gt;.kraken2.output.txt | Kraken2 output file containing the taxonomic classification of each read |
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
| bracken-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| bracken-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| bracken-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| bracken-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### <i class="fa-xl fas fa-exclamation-circle"></i> Kraken2 and Bracken Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_db` | The a single tarball or path to a Kraken2 formatted database <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_quick_mode` | Quick operation (use first hit or hits) <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_confidence` | Confidence score threshold between 0 and 1 <br/>**Type:** `number` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_minimum_base_quality` | Minimum base quality used in classification <br/>**Type:** `integer` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_use_mpa_style` | Format report output like Kraken 1's kraken-mpa-report <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_report_zero_counts` | Report counts for ALL taxa, even if counts are zero <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_report_minimizer_data` | Include minimizer and distinct minimizer count information in report <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_use_names` | Print scientific names instead of just taxids <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_memory_mapping` | Avoid loading database into RAM <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kraken2_minimum_hit_groups` | Minimum number of hit groups needed to make a call <br/>**Type:** `integer`, **Default:** `2` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --bracken_read_length` | Read length to get all classifications for (0 = determine at runtime) <br/>**Type:** `integer` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --bracken_level` | Level to estimate abundance at <br/>**Type:** `string`, **Default:** `S` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --bracken_threshold` | Reads required PRIOR to abundance estimation to perform re-estimation <br/>**Type:** `integer` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_krona` | Skip the creation of a Krona report <br/>**Type:** `boolean` |


### <i class="fa-xl fa-solid fa-gears"></i> Optional Parameters
These optional parameters can be useful in certain settings.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-folder"></i>` --outdir` | Base directory to write results to <br/>**Type:** `string`, **Default:** `./` |
| <i class="fa-lg fas fa-folder"></i>` --run_name` | Name of the directory to hold results <br/>**Type:** `string`, **Default:** `bactopia` |
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

### <i class="fa-xl fa-regular fa-address-card"></i> Nextflow Profile Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-folder"></i>` --condadir` | Directory to Nextflow should use for Conda environments <br/>**Type:** `string` |
| <i class="fa-lg fas fa-box"></i>` --registry` | Docker registry to pull containers from. <br/>**Type:** `string`, **Default:** `dockerhub` |
| <i class="fa-lg fas fa-folder"></i>` --datasets_cache` | Directory where downloaded datasets should be stored. <br/>**Type:** `string`, **Default:** `<BACTOPIA_DIR>/data/datasets` |
| <i class="fa-lg fas fa-folder"></i>` --singularity_cache` | Directory where remote Singularity images are stored. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-toolbox"></i>` --singularity_pull_docker_container` | Instead of directly downloading Singularity images for use with Singularity, force the workflow to pull and convert Docker containers instead. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-recycle"></i>` --force_rebuild` | Force overwrite of existing pre-built environments. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-clipboard-list"></i>` --queue` | Comma-separated name of the queue(s) to be used by a job scheduler (e.g. AWS Batch or SLURM) <br/>**Type:** `string`, **Default:** `general,high-memory` |
| <i class="fa-lg fas fa-clipboard-list"></i>` --cluster_opts` | Additional options to pass to the executor. (e.g. SLURM: '--account=my_acct_name' <br/>**Type:** `string` |
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
If you use Bactopia and `bracken` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Bracken](https://github.com/jenniferlu717/Bracken)  
    Lu J, Breitwieser FP, Thielen P, and Salzberg SL [Bracken: estimating species abundance in metagenomics data.](https://doi.org/10.7717/peerj-cs.104) _PeerJ Computer Science_, 3, e104. (2017)
  
- [Kraken2](https://github.com/DerrickWood/kraken2)  
    Wood DE, Lu J, Langmead B [Improved metagenomic analysis with Kraken 2.](https://doi.org/10.1186/s13059-019-1891-0) *Genome Biology*, 20(1), 257. (2019)
  
- [Krona](https://github.com/marbl/Krona)  
    Ondov BD, Bergman NH, and Phillippy AM [Interactive metagenomic visualization in a Web browser.](https://doi.org/10.1186/1471-2105-12-385) _BMC Bioinformatics_, 12, 385. (2011)
  
