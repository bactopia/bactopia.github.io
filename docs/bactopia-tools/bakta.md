---
tags:
   - annotation
   - fasta
   - prokaryote
---



# Bactopia Tool - `bakta`
The `bakta` module uses [Bakta](https://github.com/oschwengers/bakta) to rapidly annotate bacterial 
genomes and plasmids in a standardized fashion. Bakta makes use of a large database ([40+ GB](https://doi.org/10.5281/zenodo.4247252))
to provide extensive annotations including: tRNA, tmRNA, rRNA, ncRNA, CRISPR, CDS, and sORFs.


## Example Usage
```
bactopia --wf bakta \
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


### Bakta Parameters


| Parameter | Description | Default |
|---|---|---|
| `--bakta_db` | Path to the Bakta database |  |
| `--proteins` | FASTA file of trusted proteins to first annotate from |  |
| `--prodigal_tf` | Training file to use for Prodigal |  |
| `--replicons` | Replicon information table (tsv/csv) |  |
| `--min_contig_length` | Minimum contig size to annotate | 1 |
| `--keep_contig_headers` | Keep original contig headers | False |
| `--compliant` | Force Genbank/ENA/DDJB compliance | False |
| `--skip_trna` | Skip tRNA detection & annotation | False |
| `--skip_tmrna` | Skip tmRNA detection & annotation | False |
| `--skip_rrna` | Skip rRNA detection & annotation | False |
| `--skip_ncrna` | Skip ncRNA detection & annotation | False |
| `--skip_ncrna_region` | Skip ncRNA region detection & annotation | False |
| `--skip_crispr` | Skip CRISPR array detection & annotation | False |
| `--skip_cds` | Skip CDS detection & annotation | False |
| `--skip_sorf` | Skip sORF detection & annotation | False |
| `--skip_gap` | Skip gap detection & annotation | False |
| `--skip_ori` | Skip oriC/oriT detection & annotation | False |
| `--bakta_opts` | Extra Backa options in quotes. Example: '--gram +' |  |


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
If you use Bactopia and `bakta` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Bakta](https://github.com/oschwengers/bakta)  
    Schwengers O, Jelonek L, Dieckmann MA, Beyvers S, Blom J, Goesmann A [Bakta - rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.](https://doi.org/10.1099/mgen.0.000685) _Microbial Genomics_ 7(11) (2021)
  