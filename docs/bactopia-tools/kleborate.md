---
tags:
   - enterics
   - fasta
   - klebsiella
   - serotype
---



# Bactopia Tool - `kleborate`
The `kleborate` module uses [Kleborate](https://github.com/katholt/Kleborate) to screen genome assemblies of 
_Klebsiella pneumoniae_ and the _Klebsiella pneumoniae_ species complex (KpSC). Kleborate predicts:

- MLST, species,
- ICEKp associated virulence loci
- virulence plasmid associated loci
- antimicrobial resistance determinants,
- K (capsule) and O antigen (LPS) serotype prediction.


## Example Usage
```
bactopia --wf kleborate \
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


### Kleborate Parameters


| Parameter | Description | Default |
|---|---|---|
| `--skip_resistance` | Turn off resistance genes screening | False |
| `--skip_kaptive` | Turn off Kaptive screening of K and O loci | False |
| `--min_identity` | Minimum alignment percent identity for main results | 90.0 |
| `--min_coverage` | Minimum alignment percent coverage for main results | 80.0 |
| `--min_spurious_identity` | Minimum alignment percent identity for spurious results | 80.0 |
| `--min_spurious_coverage` | Minimum alignment percent coverage for spurious results | 40.0 |
| `--min_kaptive_confidence` | Minimum Kaptive confidence to call K/O loci - confidence levels below this will be reported as unknown | Good |
| `--force_index` | Rebuild the BLAST index at the start of execution | False |


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
If you use Bactopia and `kleborate` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Kaptive](https://github.com/katholt/Kaptive)  
    Wyres KL, Wick RR, Gorrie C, Jenney A, Follador R, Thomson NR, Holt KE [Identification of Klebsiella capsule synthesis loci from whole genome data.](https://doi.org/10.1099/mgen.0.000102) _Microbial genomics_ 2(12) (2016)
  
- [Kleborate](https://github.com/katholt/Kleborate)  
    Lam MMC, Wick RR, Watts, SC, Cerdeira LT, Wyres KL, Holt KE [A genomic surveillance framework and genotyping tool for Klebsiella pneumoniae and its related species complex.](https://doi.org/10.1038/s41467-021-24448-3) _Nat Commun_ 12, 4188 (2021)
  
