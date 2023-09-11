---
title: gather
description: A Bactopia Tool which gathers all the input samples into a single place, including downloading samples from ENA/SRA or NCBI Assembly.

---

The main purpose of the `gather` step is to get all the samples into a single place. This
includes downloading samples from ENA/SRA or NCBI Assembly. The tools used are:

| Tool | Description |
|------|-------------|
| [art](https://www.niehs.nih.gov/research/resources/software/biostatistics/art/index.cfm) | For simulating error-free reads for an input assembly |
| [fastq-dl](https://github.com/rpetit3/fastq-dl) | Downloading FASTQ files from ENA/SRA |
| [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) | Downloading FASTA files from NCBI Assembly |

This `gather` step also does basic QC checks to help prevent downstream failures.


## Output Overview

Below is the default output structure for the `gather` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── main
│       └── gather
│           ├── logs
│           │   ├── nf-gather.{begin,err,log,out,run,sh,trace}
│           │   └── versions.yml
│           ├── <SAMPLE_NAME>-gzip-error.txt
│           ├── <SAMPLE_NAME>-low-basepair-proportion-error.txt
│           ├── <SAMPLE_NAME>-low-read-count-error.txt
│           ├── <SAMPLE_NAME>-low-sequence-depth-error.txt
│           └── <SAMPLE_NAME>-meta.tsv
└── bactopia-runs
    └── bactopia-<TIMESTAMP>
        ├── merged-results
        │   ├── logs
        │   │   └── meta-concat
        │   │       ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │   │       └── versions.yml
        │   └── meta.tsv
        └── nf-reports
            ├── bactopia-dag.dot
            ├── bactopia-report.html
            ├── bactopia-timeline.html
            └── bactopia-trace.txt

```



### Results

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| meta.tsv | A tab-delimited file with bactopia metadata for all samples |






#### gather

Below is a description of the _per-sample_ results from the `gather` subworkflow.


| Extension                     | Description |
|-------------------------------|-------------|
| -meta.tsv | A tab-delimited file with bactopia metadata for each sample |






#### Failed Quality Checks

Built into Bactopia are few basic quality checks to help prevent downstream failures.
If a sample fails one of these checks, it will be excluded from further analysis. By
excluding these samples, complete pipeline failures are prevented.


| Extension                     | Description |
|-------------------------------|-------------|
| -gzip-error.txt | Sample failed Gzip checks and excluded from further analysis |
| -low-basepair-proportion-error.txt | Sample failed basepair proportion checks and excluded from further analysis |
| -low-read-count-error.txt | Sample failed read count checks and excluded from further analysis |
| -low-sequence-depth-error.txt | Sample failed sequenced basepair checks and excluded from further analysis |



!!! info "Poor samples are excluded to prevent downstream failures"
    Samples that fail any of the QC checks will be excluded from further analysis.
    Those samples will generate a `*-error.txt` file with the error message. Excluding
    these samples prevents downstream failures that cause the whole workflow to fail.



??? warning "Example Error: Input FASTQ(s) failed Gzip checks"
    If input FASTQ(s) fail to pass Gzip test, the sample will be excluded from
    further analysis.

    __Example Text from &lt;SAMPLE_NAME&gt;-gzip-error.txt__  
    _&lt;SAMPLE_NAME&gt; FASTQs failed Gzip tests. Please check the input FASTQs. Further
    analysis is discontinued._

??? warning "Example Error: Input FASTQs have disproportionate number of reads"
    If input FASTQ(s) for a sample have disproportionately different number of reads
    between the two pairs, the sample will be excluded from further analysis. You can
    adjust this minimum read count using the `--min_proportion` parameter.

    __Example Text from &lt;SAMPLE_NAME&gt;-low-basepair-proportion-error.txt__  
    _&lt;SAMPLE_NAME&gt; FASTQs failed to meet the minimum shared basepairs (`X``). They
    shared `Y` basepairs, with R1 having `A` bp and R2 having `B` bp. Further
    analysis is discontinued._

??? warning "Example Error: Input FASTQ(s) has too few reads"
    If input FASTQ(s) for a sample have less than the minimum required reads, the
    sample will be excluded from further analysis. You can adjust this minimum read
    count using the `--min_reads` parameter.

    __Example Text from &lt;SAMPLE_NAME&gt;-low-read-count-error.txt__  
    _&lt;SAMPLE_NAME&gt; FASTQ(s) contain `X` total reads. This does not exceed the required
    minimum `Y` read count. Further analysis is discontinued._

??? warning "Example Error: Input FASTQ(s) has too little sequenced basepairs"
    If input FASTQ(s) for a sample fails to meet the minimum number of sequenced
    basepairs, the sample will be excluded from further analysis. You can
    adjust this minimum read count using the `--min_basepairs` parameter.

    __Example Text from &lt;SAMPLE_NAME&gt;-low-sequence-depth-error.txt__  
    _&lt;SAMPLE_NAME&gt; FASTQ(s) contain `X` total basepairs. This does not exceed the
    required minimum `Y` bp. Further analysis is discontinued._





### Audit Trail

Below are files that can assist you in understanding which parameters and program versions
were used.

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

## Parameters


### <i class="fa-xl fas fa-exclamation-circle"></i> Gather 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-fast-forward"></i>` --skip_fastq_check` | Skip minimum requirement checks for input FASTQs <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_basepairs` | The minimum amount of basepairs required to continue downstream analyses. <br/>**Type:** `integer`, **Default:** `2241820` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_reads` | The minimum amount of reads required to continue downstream analyses. <br/>**Type:** `integer`, **Default:** `7472` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_coverage` | The minimum amount of coverage required to continue downstream analyses. <br/>**Type:** `integer`, **Default:** `10` |
| <i class="fa-lg fas fa-balance-scale-left"></i>` --min_proportion` | The minimum proportion of basepairs for paired-end reads to continue downstream analyses. <br/>**Type:** `number`, **Default:** `0.5` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_genome_size` | The minimum estimated genome size allowed for the input sequence to continue downstream analyses. <br/>**Type:** `integer`, **Default:** `100000` |
| <i class="fa-lg fas fa-angle-double-up"></i>` --max_genome_size` | The maximum estimated genome size allowed for the input sequence to continue downstream analyses. <br/>**Type:** `integer`, **Default:** `18040666` |
| <i class="fa-lg fas fa-redo"></i>` --attempts` | Maximum times to attempt downloads <br/>**Type:** `integer`, **Default:** `3` |
| <i class="fa-lg fas fa-globe-europe"></i>` --use_ena` | Download FASTQs from ENA <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-save"></i>` --no_cache` | Skip caching the assembly summary file from ncbi-genome-download <br/>**Type:** `boolean` |

## Citations
If you use Bactopia and `gather` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [ART](https://www.niehs.nih.gov/research/resources/software/biostatistics/art/index.cfm)  
    Huang W, Li L, Myers JR, Marth GT [ART: a next-generation sequencing read simulator.](http://dx.doi.org/10.1093/bioinformatics/btr708) _Bioinformatics_ 28, 593–594 (2012)
  
- [fastq-dl](https://github.com/rpetit3/fastq-dl)  
    Petit III RA [fastq-dl: Download FASTQ files from SRA or ENA repositories.](https://github.com/rpetit3/fastq-dl) (GitHub)
  
- [fastq-scan](https://github.com/rpetit3/fastq-scan)  
    Petit III RA [fastq-scan: generate summary statistics of input FASTQ sequences.](https://github.com/rpetit3/fastq-scan) (GitHub)
  
- [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)  
    Blin K [ncbi-genome-download: Scripts to download genomes from the NCBI FTP servers](https://github.com/kblin/ncbi-genome-download) (GitHub)
  
- [Pigz](https://zlib.net/pigz/)  
    Adler M. [pigz: A parallel implementation of gzip for modern multi-processor, multi-core machines.](https://zlib.net/pigz/) _Jet Propulsion Laboratory_ (2015)
  
