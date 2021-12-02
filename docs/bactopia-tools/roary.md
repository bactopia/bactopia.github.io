---
tags:
---



# Bactopia Tool - `roary`
The `roary` module uses [Roary](https://github.com/sanger-pathogens/Roary) to create a pan-genome of 
your samples.


## Example Usage
```
bactopia --wf roary \
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


### Optional Parameters
These optional parameters can be useful in certain settings.

| Parameter | Description | Default |
|---|---|---|
| `--outdir` | Base directory to write results and Nextflow related outputs to | ./ |
| `--run_name` | Name of the directory to hold results (e.g. ${params.outdir}/${params.run_name}/<SAMPLE_NAME> | bactopia |
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
| `--queue` | Comma-separated name of the queue(s) to be used by a job scheduler (e.g. AWS Batch or SLURM) | general,high-memory |
| `--disable_scratch` | All intermediate files created on worker nodes of will be transferred to the head node. | False |

### AWS Batch Profile (-profile awsbatch) Parameters
Parameters to fine-tune your AWS Batch setup.

| Parameter | Description | Default |
|---|---|---|
| `--aws_region` | AWS Region to be used by Nextflow | us-east-1 |
| `--aws_volumes` | Volumes to be mounted from the EC2 instance to the Docker container | /opt/conda:/mnt/conda |
| `--aws_cli_path` | Path to the AWS CLI for Nextflow to use. | /home/ec2-user/conda/bin/aws |
| `--aws_upload_storage_class` | The S3 storage slass to use for storing files on S3 | STANDARD |
| `--aws_max_parallel_transfers` | The number of parallele transfers between EC2 and S3 | 8 |
| `--aws_delay_between_attempts` | The duration of sleep (in seconds) between each transfer between EC2 and S3 | 15 |
| `--aws_max_transfer_attempts` | The maximum number of times to retry transferring a file between EC2 and S3 | 3 |
| `--aws_max_retry` | The maximum number of times to retry a process on AWS Batch | 4 |
| `--aws_ecr_registry` | The ECR registry containing Bactopia related containers. |  |

### Helpful Parameters
Uncommonly used parameters that might be useful.

| Parameter | Description | Default |
|---|---|---|
| `--monochrome_logs` | Do not use coloured log outputs. |  |
| `--nfdir` | Print directory Nextflow has pulled Bactopia to |  |
| `--sleep_time` | The amount of time (seconds) Nextflow will wait after setting up datasets before execution. | 5 |
| `--validate_params` | Boolean whether to validate parameters against the schema at runtime | True |
| `--help` | Display help text. |  |
| `--show_hidden_params` | Show all params when using `--help` |  |
| `--help_all` | An alias for --help --show_hidden_params |  |
| `--version` | Display version text. |  |

## Citations
If you use Bactopia and `roary` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Roary](https://github.com/sanger-pathogens/Roary)  
    Page AJ, Cummins CA, Hunt M, Wong VK, Reuter S, Holden MTG, Fookes M, Falush D, Keane JA, Parkhill J [Roary: rapid large-scale prokaryote pan genome analysis.](https://doi.org/10.1093/bioinformatics/btv421) _Bioinformatics_ 31, 3691–3693 (2015)
  
