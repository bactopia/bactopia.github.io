---
tags:
---



# Bactopia Tool - `pangenome`
The `pangenome` subworkflow allows you to create a pan-genome with [PIRATE](https://github.com/SionBayliss/PIRATE) (or [Roary](https://github.com/sanger-pathogens/Roary)) of your samples.
You can further supplement your pan-genome by including completed genomes. This is possible using the `--species` or `--accessions` parameters. If used, [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) will download available completed genomes available from RefSeq. Any downloaded genomes will be annotated with [Prokka](https://github.com/tseemann/prokka) to create compatible GFF3 files.
A phylogeny, based on the core-genome alignment, will be created by [IQ-Tree](https://github.com/Cibiv/IQ-TREE). Optionally a recombination-masked core-genome alignment can be created with [ClonalFrameML](https://github.com/xavierdidelot/ClonalFrameML) and [maskrc-svg](https://github.com/kwongj/maskrc-svg).
Finally, the core genome pair-wise SNP distance for each sample is also calculated with [snp-dists](https://github.com/tseemann/snp-dists) and additional pan-genome wide association studies can be conducted using [Scoary](https://github.com/AdmiralenOla/Scoary).

## Example Usage
```
bactopia --wf pangenome \
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


### ClonalFrameML Parameters


| Parameter | Description | Default |
|---|---|---|
| `--emsim` | Number of simulations to estimate uncertainty in the EM results | 100 |
| `--clonal_opts` | Extra ClonalFrameML options in quotes |  |
| `--skip_recombination` | Skip ClonalFrameML execution in subworkflows | False |

### IQ-TREE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--m` | Substitution model name | MFP |
| `--bb` | Ultrafast bootstrap replicates | 1000 |
| `--alrt` | SH-like approximate likelihood ratio test replicates | 1000 |
| `--asr` | Ancestral state reconstruction by empirical Bayes | False |
| `--iqtree_opts` | Extra IQ-TREE options in quotes. |  |
| `--skip_phylogeny` | Skip IQ-TREE execution in subworkflows | False |

### NCBI Genome Download Parameters


| Parameter | Description | Default |
|---|---|---|
| `--species` | Name of the species to download assemblies |  |
| `--accession` | An NCBI Assembly accession to be downloaded |  |
| `--accessions` | An file of NCBI Assembly accessions (one per line) to be downloaded |  |
| `--format` | Comma separated list of formats to download | fasta |
| `--section` | NCBI section to download | refseq |
| `--assembly_level` | Comma separated list of assembly levels to download | complete |
| `--kingdom` | Comma separated list of formats to download | bacteria |
| `--limit` | Limit the number of assemblies to download |  |

### PIRATE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--steps` | Percent identity thresholds to use for pangenome construction | 50,60,70,80,90,95,98 |
| `--features` | Comma-delimited features to use for pangenome construction | CDS |
| `--para_off` | Switch off paralog identification | False |
| `--z` | Retain all PIRATE intermediate files | False |
| `--pan_opt` | Additional arguments to pass to pangenome contruction. |  |

### Prokka Parameters


| Parameter | Description | Default |
|---|---|---|
| `--proteins` | FASTA file of trusted proteins to first annotate from |  |
| `--prodigal_tf` | Training file to use for Prodigal |  |
| `--prokka_coverage` | Minimum coverage on query protein | 80 |
| `--prokka_evalue` | Similarity e-value cut-off | 1e-09 |
| `--prokka_opts` | Extra Prokka options in quotes. |  |

### Roary Parameters


| Parameter | Description | Default |
|---|---|---|
| `--use_prank` | Use PRANK instead of MAFFT for core gene | False |
| `--use_roary` | Use Roary instead of PIRATE in the 'pangenome' subworkflow | False |
| `--i` | Minimum percentage identity for blastp | 95 |
| `--cd` | Percentage of isolates a gene must be in to be core | 99 |
| `--g` | Maximum number of clusters | 50000 |
| `--s` | Do not split paralogs | False |
| `--ap` | Allow paralogs in core alignment | False |
| `--iv` | MCL inflation value | 1.5 |

### Scoary Parameters


| Parameter | Description | Default |
|---|---|---|
| `--traits` | Input trait table (CSV) to test for associations |  |
| `--p_value_cutoff` | For statistical tests, genes with higher p-values will not be reported | 0.05 |
| `--correction` | Apply the indicated filtration measure. | I |
| `--permute` | Perform N number of permutations of the significant results post-analysis | 0 |
| `--start_col` | On which column in the gene presence/absence file do individual strain info start | 15 |

### SNP-Dists Parameters


| Parameter | Description | Default |
|---|---|---|
| `--a` | Count all differences not just [AGTC] | False |
| `--b` | Keep top left corner cell | False |
| `--csv` | Output CSV instead of TSV | False |
| `--k` | Keep case, don't uppercase all letters | False |


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
If you use Bactopia and `pangenome` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [ClonalFramML](https://github.com/xavierdidelot/ClonalFrameML)  
    Didelot X, Wilson DJ [ClonalFrameML: Efficient Inference of Recombination in Whole Bacterial Genomes.](https://doi.org/10.1371/journal.pcbi.1004041) _PLoS Comput Biol_ 11(2) e1004041 (2015)
  
- [IQ-TREE](https://github.com/Cibiv/IQ-TREE)  
    Nguyen L-T, Schmidt HA, von Haeseler A, Minh BQ [IQ-TREE: A fast and effective stochastic algorithm for estimating maximum likelihood phylogenies.](https://doi.org/10.1093/molbev/msu300) _Mol. Biol. Evol._ 32:268-274 (2015)
  
- [ModelFinder](https://github.com/Cibiv/IQ-TREE)  
    Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS [ModelFinder - Fast model selection for accurate phylogenetic estimates.](https://doi.org/10.1038/nmeth.4285) _Nat. Methods_ 14:587-589 (2017)
  
- [UFBoot2](https://github.com/Cibiv/IQ-TREE)  
    Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS [UFBoot2: Improving the ultrafast bootstrap approximation.](https://doi.org/10.1093/molbev/msx281) _Mol. Biol. Evol._ 35:518–522 (2018)
  
- [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)  
    Blin K [ncbi-genome-download: Scripts to download genomes from the NCBI FTP servers](https://github.com/kblin/ncbi-genome-download) (GitHub)
  
- [PIRATE](http://github.com/SionBayliss/PIRATE)  
    Bayliss SC, Thorpe HA, Coyle NM, Sheppard SK, Feil EJ [PIRATE: A fast and scalable pangenomics toolbox for clustering diverged orthologues in bacteria.](https://doi.org/10.1093/gigascience/giz119) _Gigascience_ 8 (2019)
  
- [Prokka](https://github.com/tseemann/prokka)  
    Seemann T [Prokka: rapid prokaryotic genome annotation](http://dx.doi.org/10.1093/bioinformatics/btu153) _Bioinformatics_ 30, 2068–2069 (2014)
  
- [Roary](https://github.com/sanger-pathogens/Roary)  
    Page AJ, Cummins CA, Hunt M, Wong VK, Reuter S, Holden MTG, Fookes M, Falush D, Keane JA, Parkhill J [Roary: rapid large-scale prokaryote pan genome analysis.](https://doi.org/10.1093/bioinformatics/btv421) _Bioinformatics_ 31, 3691–3693 (2015)
  
- [Scoary](https://github.com/AdmiralenOla/Scoary)  
    Brynildsrud O, Bohlin J, Scheffer L, Eldholm V [Rapid scoring of genes in microbial pan-genome-wide association studies with Scoary.](https://doi.org/10.1186/s13059-016-1108-8) _Genome Biol._ 17:238 (2016)
  
- [snp-dists](https://github.com/tseemann/snp-dists)  
    Seemann T [snp-dists - Pairwise SNP distance matrix from a FASTA sequence alignment.](https://github.com/tseemann/snp-dists) (GitHub)
  
