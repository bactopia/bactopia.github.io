---
tags:
   - alignment
   - phylogeny
---



# Bactopia Tool - `iqtree`
The `iqtree` module uses [IQ-TREE](https://github.com/Cibiv/IQ-TREE) to create phylogenetic trees
based on a multiple sequence alignment. In most cases the `iqtree` module will be used in a 
subworkflow where an alignment is created.


## Example Usage
```
bactopia --wf iqtree \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

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


### IQ-TREE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--m` | Substitution model name | MFP |
| `--bb` | Ultrafast bootstrap replicates | 1000 |
| `--alrt` | SH-like approximate likelihood ratio test replicates | 1000 |
| `--asr` | Ancestral state reconstruction by empirical Bayes | False |
| `--iqtree_opts` | Extra IQ-TREE options in quotes. |  |
| `--skip_phylogeny` | Skip IQ-TREE execution in subworkflows | False |


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
If you use Bactopia and `iqtree` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [IQ-TREE](https://github.com/Cibiv/IQ-TREE)  
    Nguyen L-T, Schmidt HA, von Haeseler A, Minh BQ [IQ-TREE: A fast and effective stochastic algorithm for estimating maximum likelihood phylogenies.](https://doi.org/10.1093/molbev/msu300) _Mol. Biol. Evol._ 32:268-274 (2015)
  
- [ModelFinder](https://github.com/Cibiv/IQ-TREE)  
    Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS [ModelFinder - Fast model selection for accurate phylogenetic estimates.](https://doi.org/10.1038/nmeth.4285) _Nat. Methods_ 14:587-589 (2017)
  
- [UFBoot2](https://github.com/Cibiv/IQ-TREE)  
    Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS [UFBoot2: Improving the ultrafast bootstrap approximation.](https://doi.org/10.1093/molbev/msx281) _Mol. Biol. Evol._ 35:518–522 (2018)
  
