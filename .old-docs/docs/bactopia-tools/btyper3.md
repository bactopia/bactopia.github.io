---
title: btyper3
description: A Bactopia Tool which uses BTyper3 to classify Bacillus cereus group isolates from genome assemblies.

---
# Bactopia Tool - `btyper3`
The `btyper3` module uses [BTyper3](https://github.com/lmc297/BTyper3) to classify
Bacillus cereus group isolates from genome assemblies.


## Example Usage
```
bactopia --wf btyper3 \
  --bactopia /path/to/your/bactopia/results  
```

## Output Overview

Below is the default output structure for the `btyper3` tool. Where possible the 
file descriptions below were modified from a tools description.

```bash
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── btyper3
│           ├── <SAMPLE_NAME>_final_results.txt
│           ├── bt
│           │   └── <SAMPLE_NAME>_bt.txt
│           ├── logs
│           │   ├── <SAMPLE_NAME>.log
│           │   ├── nf-btyper3.{begin,err,log,out,run,sh,trace}
│           │   └── versions.yml
│           ├── mlst
│           │   └── <SAMPLE_NAME>_mlst.txt
│           ├── panC
│           │   └── <SAMPLE_NAME>_panC.txt
│           ├── species
│           │   └── <SAMPLE_NAME>_species_fastani.txt
│           ├── subspecies
│           │   └── <SAMPLE_NAME>_subspecies_fastani.txt
│           ├── typestrains
│           │   └── <SAMPLE_NAME>_typestrains_fastani.txt
│           └── virulence
│               └── <SAMPLE_NAME>_virulence.txt
└── bactopia-runs
    └── btyper3-<TIMESTAMP>
        ├── merged-results
        │   ├── btyper3.tsv
        │   └── logs
        │       └── btyper3-concat
        │           ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │           └── versions.yml
        └── nf-reports
            ├── btyper3-dag.dot
            ├── btyper3-report.html
            ├── btyper3-timeline.html
            └── btyper3-trace.txt

```



### Results

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| btyper3.tsv | A merged TSV file with `BTyper3` results from all samples |


#### btyper3

Below is a description of the _per-sample_ results from [BTyper3](https://github.com/lmc297/BTyper3).


| Extension                     | Description |
|-------------------------------|-------------|
| _final_results.txt | A final tab-delimited file of BTyper3 results |
| _bt.txt | BLAST results from Bt genes detection |
| _mlst.txt | BLAST results against a MLST database |
| _panC.txt | BLAST results from panC group assignment |
| _species_fastani.txt | FastANI results for species assignment |
| _subspecies_fastani.txt | FastANI results for subspecies assignment |
| _typestrains_fastani.txt | FastANI results for type strain comparison |
| _virulence.txt | BLAST results against a virulence database |





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
| btyper3-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| btyper3-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| btyper3-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| btyper3-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### BTyper3 Parameters


| Parameter | Description |
|:---|---|
| ` --bt_virulence_identity` | Minimum percent amino acid/nucleotide identity threshold for a virulence gene to be considered present <br/>**Type:** `integer`, **Default:** `70` |
| ` --bt_virulence_coverage` | Minimum percent coverage threshold for a virulence gene to be considered present <br/>**Type:** `integer`, **Default:** `80` |
| ` --bt_identity` | Minimum percent amino acid identity threshold for a Bt toxin gene to be considered present <br/>**Type:** `integer`, **Default:** `50` |
| ` --bt_coverage` | Minimum percent coverage threshold for a Bt toxin gene to be considered present <br/>**Type:** `integer`, **Default:** `70` |
| ` --bt_overlap` | Specify maximum proportion of overlap for overlapping Bt toxin genes to be considered separate genes <br/>**Type:** `integer`, **Default:** `70` |
| ` --bt_opts` | Additional options to pass to BTyper3 <br/>**Type:** `string` |


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
If you use Bactopia and `btyper3` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [BTyper3](https://github.com/lmc297/BTyper3)  
    Carroll LM, Wiedmann M, Kovac J [Proposal of a Taxonomic Nomenclature for the Bacillus cereus Group Which Reconciles Genomic Definitions of Bacterial Species with Clinical and Industrial Phenotypes.](https://doi.org/10.1128/mBio.00034-20) _mBio_, 11(1). (2020)
  
- [BTyper3](https://github.com/lmc297/BTyper3)  
    Carroll LM, Cheng RA, Kovac J [No Assembly Required: Using BTyper3 to Assess the Congruency of a Proposed Taxonomic Framework for the Bacillus cereus Group With Historical Typing Methods.](https://doi.org/10.3389/fmicb.2020.580691) _Frontiers in Microbiology_, 11, 580691. (2020)
  
