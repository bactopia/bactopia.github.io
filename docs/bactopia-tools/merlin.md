---
tags:
---



# Bactopia Tool - `merlin`


## Example Usage
```
bactopia --wf merlin \
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


### mashdist Parameters


| Parameter | Description | Default |
|---|---|---|
| `--mash_sketch` | The reference sequence as a Mash Sketch (.msh file) |  |
| `--mash_seed` | Seed to provide to the hash function | 42 |
| `--mash_table` |  Table output (fields will be blank if they do not meet the p-value threshold) | False |
| `--mash_m` | Minimum copies of each k-mer required to pass noise filter for reads | 1 |
| `--mash_w` | Probability threshold for warning about low k-mer size. | 0.01 |
| `--max_p` | Maximum p-value to report. | 1.0 |
| `--max_dist` | Maximum distance to report. | 1.0 |
| `--merlin_dist` | Maximum distance to report when using Merlin . | 0.1 |
| `--full_merlin` | Go full Merlin and run all species-specific tools, no matter the Mash distance | False |
| `--use_fastqs` | Query with FASTQs instead of the assemblies | False |

### AgrVATE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--typing_only` | agr typing only. Skips agr operon extraction and frameshift detection | False |

### ECTyper Parameters


| Parameter | Description | Default |
|---|---|---|
| `--opid` | Percent identity required for an O antigen allele match | 90 |
| `--opcov` | Minumum percent coverage required for an O antigen allele match | 90 |
| `--hpid` | Percent identity required for an H antigen allele match | 95 |
| `--hpcov` | Minumum percent coverage required for an H antigen allele match | 50 |
| `--verify` | Enable E. coli species verification | False |
| `--print_alleles` | Prints the allele sequences if enabled as the final column | False |

### emmtyper Parameters


| Parameter | Description | Default |
|---|---|---|
| `--emmtyper_wf` | Workflow for emmtyper to use. | blast |
| `--cluster_distance` | Distance between cluster of matches to consider as different clusters | 500 |
| `--percid` | Minimal percent identity of sequence | 95 |
| `--culling_limit` | Total hits to return in a position | 5 |
| `--mismatch` | Threshold for number of mismatch to allow in BLAST hit | 5 |
| `--align_diff` | Threshold for difference between alignment length and subject length in BLAST | 5 |
| `--gap` | Threshold gap to allow in BLAST hit | 2 |
| `--min_perfect` | Minimum size of perfect match at 3 primer end | 15 |
| `--min_good` | Minimum size where there must be 2 matches for each mismatch | 15 |
| `--max_size` | Maximum size of PCR product | 2000 |

### hicap Parameters


| Parameter | Description | Default |
|---|---|---|
| `--database_dir` | Directory containing locus database |  |
| `--model_fp` | Path to prodigal model |  |
| `--full_sequence` | Write the full input sequence out to the genbank file rather than just the region surrounding and including the locus | False |
| `--hicap_debug` | hicap will print debug messages | False |
| `--gene_coverage` | Minimum percentage coverage to consider a single gene complete | 0.8 |
| `--gene_identity` | Minimum percentage identity to consider a single gene complete | 0.7 |
| `--broken_gene_length` | Minimum length to consider a broken gene | 60 |
| `--broken_gene_identity` | Minimum percentage identity to consider a broken gene | 0.8 |

### Kleborate Parameters


| Parameter | Description | Default |
|---|---|---|
| `--skip_resistance` | Turn off resistance genes screening | False |
| `--skip_kaptive` | Turn off Kaptive screening of K and O loci | False |
| `--min_identity` | Minimum alignment percent identity for main results | 90.0 |
| `--kleborate_min_coverage` | Minimum alignment percent coverage for main results | 80.0 |
| `--min_spurious_identity` | Minimum alignment percent identity for spurious results | 80.0 |
| `--min_spurious_coverage` | Minimum alignment percent coverage for spurious results | 40.0 |
| `--min_kaptive_confidence` | Minimum Kaptive confidence to call K/O loci - confidence levels below this will be reported as unknown | Good |
| `--force_index` | Rebuild the BLAST index at the start of execution | False |

### LisSero Parameters


| Parameter | Description | Default |
|---|---|---|
| `--min_id` | Minimum percent identity to accept a match | 95.0 |
| `--min_cov` | Minimum coverage of the gene to accept a match | 95.0 |

### meningotype Parameters
You can use these parameters to fine-tune your meningotype analysis

| Parameter | Description | Default |
|---|---|---|
| `--finetype` | perform porA and fetA fine typing | False |
| `--porB` | perform porB sequence typing (NEIS2020) | False |
| `--bast` | perform Bexsero antigen sequence typing (BAST) | False |
| `--mlst` | perform MLST | False |
| `--all` | perform MLST, porA, fetA, porB, BAST typing | False |

### ngmaster Parameters


| Parameter | Description | Default |
|---|---|---|
| `--csv` | output comma-separated format (CSV) rather than tab-separated | False |

### SeqSero2 Parameters


| Parameter | Description | Default |
|---|---|---|
| `--run_mode` | Workflow to run. 'a' allele mode, or 'k' k-mer mode | k |
| `--input_type` | Input format to analyze. 'assembly' or 'fastq' | assembly |
| `--bwa_mode` | Algorithms for bwa mapping for allele mode | mem |

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

### TBProfiler Parameters


| Parameter | Description | Default |
|---|---|---|
| `--call_whole_genome` | Call whole genome | False |
| `--mapper` | Mapping tool to use. If you are using nanopore data it will default to minimap2 | bwa |
| `--caller` | Variant calling tool to use | freebayes |
| `--calling_params` | Extra variant caller options in quotes |  |
| `--tb_min_depth` | Minimum depth required to call variant | 10 |
| `--tb_af` | Minimum allele frequency to call variants | 0.1 |
| `--tb_reporting_af` | Minimum allele frequency to use variants for prediction | 0.1 |
| `--coverage_fraction_threshold` | Cutoff used to calculate fraction of region covered by <= this value | 0 |
| `--suspect` | Use the suspect suite of tools to add ML predictions | False |
| `--no_flagstat` | Don't collect flagstats | False |
| `--no_delly` | Don't run delly | False |


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
If you use Bactopia and `merlin` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

