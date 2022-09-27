---
title: Bactopia Tools - mashtree
description: A Bactopia Tool which uses Mashtree to create a tree of your samples using Mash distances.
----
# Bactopia Tool - `mashtree`
The `mashtree` module uses [Mashtree](https://github.com/lskatz/mashtree) to create a tree of your samples
using [Mash](https://github.com/marbl/Mash) distances. 

You can also use `--species` or `-accessions` to see how your samples compare to completed genomes. If used, 
[ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) will download available completed 
genomes available from RefSeq and they will be included in your tree.


## Example Usage
```
bactopia --wf mashtree \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `mashtree` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
mashtree/
├── logs
│   ├── custom_dumpsoftwareversions
│   │   ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   └── mashtree
│       ├── nf-mashtree.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── mashtree-dag.dot
│   ├── mashtree-report.html
│   ├── mashtree-timeline.html
│   └── mashtree-trace.txt
├── mashtree.dnd
├── mashtree.tsv
├── software_versions.yml
└── software_versions_mqc.yml

```



### Results

#### Top Level

Below are results that are in the base directory.


| Filename    | Description |
|-------------|-------------|
| mashtree.dnd | A Newick formatted tree file |
| mashtree.tsv | A TSV matrix of pair-wise Mash distances |





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
| mashtree-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| mashtree-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| mashtree-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| mashtree-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### Mashtree Parameters


| Parameter | Description | Default |
|---|---|---|
| `--trunclength` | How many characters to keep in a filename | 250 |
| `--sortorder` | For neighbor-joining, the sort order can make a difference. | ABC |
| `--genomesize` | Genome size of the input samples | 5000000 |
| `--mindepth` | If mindepth is zero, then it will be chosen in a smart but slower method, to discard lower-abundance kmers. | 5 |
| `--kmerlength` | Hashes will be based on strings of this many nucleotides | 21 |
| `--sketchsize` | Each sketch will have at most this many non-redundant min-hashes | 10000 |


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
If you use Bactopia and `mashtree` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Mash](https://github.com/marbl/Mash)  
    Ondov BD, Treangen TJ, Melsted P, Mallonee AB, Bergman NH, Koren S, Phillippy AM [Mash: fast genome and metagenome distance estimation using MinHash](http://dx.doi.org/10.1186/s13059-016-0997-x). _Genome Biol_ 17, 132 (2016)
  
- [Mashtree](https://github.com/lskatz/mashtree)  
    Katz LS, Griswold T, Morrison S, Caravas J, Zhang S, den Bakker HC, Deng X, Carleton HA [Mashtree: a rapid comparison of whole genome sequence files.](https://doi.org/10.21105/joss.01762) _Journal of Open Source Software_, 4(44), 1762 (2019)
  
- [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)  
    Blin K [ncbi-genome-download: Scripts to download genomes from the NCBI FTP servers](https://github.com/kblin/ncbi-genome-download) (GitHub)
  
