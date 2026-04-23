---
title: defensefinder
description: A Bactopia Tool which uses defense-finder to rapidly identify all known anti-phage systems in a bacterial genome.

---
# Bactopia Tool - `defensefinder`
The `defensefinder` module uses the [defense-finder](https://github.com/mdmparis/defense-finder)
for the identification of all known anti-phage systems.


## Example Usage
```
bactopia --wf defensefinder \
  --bactopia /path/to/your/bactopia/results  
```

## Output Overview

Below is the default output structure for the `defensefinder` tool. Where possible the 
file descriptions below were modified from a tools description.

```bash
<BACOTPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── defensefinder
│           ├── <SAMPLE_NAME>.fna.prt
│           ├── <SAMPLE_NAME>.fna.prt.idx
│           ├── <SAMPLE_NAME>.fna_defense_finder_{genes|hmmer|systems}.tsv
│           ├── <SAMPLE_NAME>.macsydata.tar.gz
│           └── logs
│               ├── nf-defensefinder.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── defensefinder-<TIMESTAMP>
        ├── merged-results
        │   ├── defensefinder-{genes|hmmer|systems}.tsv
        │   └── logs
        │       └── defensefinder-{genes|hmmer|systems}-concat
        │           ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │           └── versions.yml
        └── nf-reports
            ├── defensefinder-dag.dot
            ├── defensefinder-report.html
            ├── defensefinder-timeline.html
            └── defensefinder-trace.txt

```



### Results

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| defensefinder-genes.tsv | A merged TSV of all genes found in the system for all samples |
| defensefinder-hmmer.tsv | A merged TSV of all HMM hits for all samples |
| defensefinder-systems.tsv | A merged TSV of all information about systems found for all samples |


#### defensefinder

Below is a description of the _per-sample_ results from [defense-finder](https://github.com/mdmparis/defense-finder).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.fna.prt | A FASTA file containing all proteins found in the system for a single sample |
| &lt;SAMPLE_NAME&gt;.fna.prt.idx | A index file for the proteins file |
| &lt;SAMPLE_NAME&gt;.fna_defense_finder_genes.tsv | A tab-delimited file with each gene found in the system for a single sample |
| &lt;SAMPLE_NAME&gt;.fna_defense_finder_hmmer.tsv | A tab-delimited file with each HMM hit for a single sample |
| &lt;SAMPLE_NAME&gt;.fna_defense_finder_systems.tsv | A tab-delimited file with information about each system found for a single sample |
| &lt;SAMPLE_NAME&gt;.macsydata.tar.gz | A raw MACSyFinder output file (requires --df_preserveraw) |





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
| defensefinder-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| defensefinder-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| defensefinder-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| defensefinder-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### defense-finder Parameters


| Parameter | Description |
|:---|---|
| ` --df_coverage` | Minimal percentage of coverage for each profiles <br/>**Type:** `number`, **Default:** `0.4` |
| ` --df_dbtype` | The macsyfinder --db-type option <br/>**Type:** `string`, **Default:** `ordered_replicon` |
| ` --df_preserveraw` | Preserve raw MacsyFinder outputs alongside Defense Finder results inside the output directory <br/>**Type:** `boolean` |
| ` --df_nocutga` | Advanced! Run macsyfinder in no-cut-ga mode. The validity of the genes and systems found is not guaranteed! <br/>**Type:** `boolean` |


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
If you use Bactopia and `defensefinder` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [DefenseFinder](https://github.com/mdmparis/defense-finder)  
    Tesson F, Hervé A, Mordret E, Touchon M, d’Humières C, Cury J, Bernheim A [Systematic and quantitative view of the antiviral arsenal of prokaryotes.](https://doi.org/10.1038/s41467-022-30269-9) Nature Communications, 13(1), 2561. (2022)
  
