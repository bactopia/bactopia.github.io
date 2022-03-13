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

## Output Overview

Below is the default output structure for the `bakta` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
bakta/
├── <SAMPLE_NAME>
│   ├── <SAMPLE_NAME>.embl
│   ├── <SAMPLE_NAME>.faa
│   ├── <SAMPLE_NAME>.ffn
│   ├── <SAMPLE_NAME>.fna
│   ├── <SAMPLE_NAME>.gbff
│   ├── <SAMPLE_NAME>.gff3
│   ├── <SAMPLE_NAME>.hypotheticals.faa
│   ├── <SAMPLE_NAME>.hypotheticals.tsv
│   ├── <SAMPLE_NAME>.tsv
│   ├── <SAMPLE_NAME>.txt
│   └── logs
│       └── bakta
│           ├── <SAMPLE_NAME>.log
│           ├── nf-bakta.{begin,err,log,out,run,sh,trace}
│           └── versions.yml
├── logs
│   └── custom_dumpsoftwareversions
│       ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── bakta-dag.dot
│   ├── bakta-report.html
│   ├── bakta-timeline.html
│   └── bakta-trace.txt
├── software_versions.yml
└── software_versions_mqc.yml

```



### Results

#### Bakta

Below is a description of the _per-sample_ results from [Bakta](https://github.com/oschwengers/bakta).


| Extension          | Description |
|--------------------|-------------|
| .embl              | Annotations & sequences in (multi) EMBL format |
| .faa               | CDS/sORF amino acid sequences as FASTA |
| .ffn               | Feature nucleotide sequences as FASTA |
| .fna               | Replicon/contig DNA sequences as FASTA |
| .gbff              | Annotations & sequences in (multi) GenBank format |
| .gff3              | Annotations & sequences in GFF3 format |
| .hypotheticals.faa | Hypothetical protein CDS amino acid sequences as FASTA |
| .hypotheticals.tsv | Further information on hypothetical protein CDS as simple human readble tab separated values |
| .tsv               | Annotations as simple human readble tab separated values |
| .txt               | Broad summary of `Bakta` annotations |





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
| bakta-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| bakta-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| bakta-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| bakta-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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
If you use Bactopia and `bakta` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Bakta](https://github.com/oschwengers/bakta)  
    Schwengers O, Jelonek L, Dieckmann MA, Beyvers S, Blom J, Goesmann A [Bakta - rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.](https://doi.org/10.1099/mgen.0.000685) _Microbial Genomics_ 7(11) (2021)
  
