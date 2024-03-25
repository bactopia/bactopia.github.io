---
title: eggnog
description: A Bactopia Tool which uses eggNOG-mapper to assign functional annotation to protein sequences.
---
# Bactopia Tool - `eggnog`
The `eggnog` module uses [eggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper) to assign 
functional annotation to protein sequences. eggNOG-mapper uses orthologous groups and phylogenies
from the eggNOG database to more precisely functionally annotate than traditional homology methods.


## Example Usage
```
bactopia --wf eggnog \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `eggnog` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── eggnog
│           ├── <SAMPLE_NAME>.emapper.annotations
│           ├── <SAMPLE_NAME>.emapper.hits
│           ├── <SAMPLE_NAME>.emapper.seed_orthologs
│           └── logs
│               ├── nf-eggnog.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── eggnog-<TIMESTAMP>
        └── nf-reports
            ├── eggnog-dag.dot
            ├── eggnog-report.html
            ├── eggnog-timeline.html
            └── eggnog-trace.txt

```



### Results

#### eggNOG-mapper

Below is a description of the _per-sample_ results from [eggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper).
For full details about each of the eggNOG output files, see
[eggNOG-mapper - Outputs](https://github.com/eggnogdb/eggnog-mapper/wiki/eggNOG-mapper-v2.1.5-to-v2.1.7#Output_format).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.emapper.annotations | Results from the annotation phase |
| &lt;SAMPLE_NAME&gt;.emapper.hits | Results from the search phase, from HMMER, Diamond or MMseqs2 |
| &lt;SAMPLE_NAME&gt;.emapper.seed_orthologs | Results from parsing the hits |
| &lt;SAMPLE_NAME&gt;.emapper.annotations.xlsx | (Optional) Annotations in .xlsx format |
| &lt;SAMPLE_NAME&gt;.emapper.orthologs | (Optional) List of orthologs found for each query |
| &lt;SAMPLE_NAME&gt;.emapper.genepred.fasta | (Optional) Sequences of predicted CDS |
| &lt;SAMPLE_NAME&gt;.emapper.gff | (Optional) GFF of predicted CDS |
| &lt;SAMPLE_NAME&gt;.emapper.no_annotations.fasta | (Optional) Sequences without annotation |
| &lt;SAMPLE_NAME&gt;.emapper.pfam | (Optional) Positions of the PFAM domains identified |





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
| eggnog-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| eggnog-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| eggnog-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| eggnog-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### <i class="fa-xl fas fa-exclamation-circle"></i> eggNOG Downloader Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --eggnog_db` | Tarball or path to eggNOG databases <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --download_eggnog` | Required if downloading latest eggNOG database, will overwrite existing databases. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --eggnog_save_as_tarball` | Save the eggNOG database as a single tarball <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_diamond` | Do not install the diamond database <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --install_mmseq` | Install the MMseqs2 database <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --install_pfam` | Install the Pfam database, required for de novo annotation or realignment <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --install_hmm` | Install the HMMER database specified with --hmmer_taxid <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --hmmer_taxid` | Tax ID of eggNOG HMM database to download <br/>**Type:** `integer`, **Default:** `2` |

### <i class="fa-xl fas fa-exclamation-circle"></i> eggNOG Mapper Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --genepred` | Method to use for gene prediction <br/>**Type:** `string`, **Default:** `search` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mode` | Method to search against eggNOG sequences <br/>**Type:** `string`, **Default:** `diamond` |
| <i class="fa-lg fas fa-italic"></i>` --eggnog_opts` | Extra eggNOG Mapper options in quotes <br/>**Type:** `string` |


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
If you use Bactopia and `eggnog` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [eggNOG 5.0 Database](http://eggnog.embl.de/)  
    Huerta-Cepas J, Szklarczyk D, Heller D, Hernández-Plaza A, Forslund SK, Cook H, Mende DR, Letunic I, Rattei T, Jensen LJ, von Mering C, Bork P [eggNOG 5.0: a hierarchical, functionally and phylogenetically annotated orthology resource based on 5090 organisms and 2502 viruses.](https://doi.org/10.1093/nar/gky1085) _Nucleic Acids Res._ 47, D309–D314 (2019)
  
- [eggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper)  
    Huerta-Cepas J, Forslund K, Coelho LP, Szklarczyk D, Jensen LJ, von Mering C, Bork P [Fast Genome-Wide Functional Annotation through Orthology Assignment by eggNOG-Mapper.](http://dx.doi.org/10.1093/molbev/msx148) _Mol. Biol. Evol._ 34, 2115–2122 (2017)
  
