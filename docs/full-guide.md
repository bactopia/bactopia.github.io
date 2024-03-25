---
title: Full Guide
description: >-
    An full guide for using Bactopia. Including a detailed description of each step in the pipeline.
---

Bactopia is a complete pipeline for the analysis of bacterial genomes, which includes
more than 150 bioinformatics tools. In this section, each step of the pipeline will
be described in detail. This includes the input data, output data, and the parameters
for each step.

<a class="zoom" href="assets/bactopia-workflow.png">
![Bactopia Workflow](assets/bactopia-workflow.png)
</a>

Looking at the workflow overview below, it might not look like much is happening, but I can
assure you that a lot is going on. The workflow is broken down into 8 steps, which are:

1. **Gather** - Collect all the data in one place
2. **QC** - Quality control of the data
3. **Assembler** - Assemble the reads into contigs
4. **Annotator** - Annotate the contigs
5. **Sketcher** - Create a sketch of the contigs, and query databases
6. **Sequence Typing** - Determine the sequence type of the contigs
7. **Antibiotic Resistance** - Determine the antibiotic resistance of the contigs and proteins
8. **Merlin** - Automatically run species-specific tools based on distance

This guide is meant to be extensive, so it will be very detailed. If you are looking for
a guide to get started quickly, please check out the [Beginner's Guide](beginners-guide.md).

Otherwise, let's get started!

## Step 1 - Gather

The main purpose of the `gather` step is to get all the samples into a single place. This
includes downloading samples from ENA/SRA or NCBI Assembly. The tools used are:

| Tool | Description |
|------|-------------|
| [art](https://www.niehs.nih.gov/research/resources/software/biostatistics/art/index.cfm) | For simulating error-free reads for an input assembly |
| [fastq-dl](https://github.com/rpetit3/fastq-dl) | Downloading FASTQ files from ENA/SRA |
| [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) | Downloading FASTA files from NCBI Assembly |

This `gather` step also does basic QC checks to help prevent downstream failures.


### Outputs
#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| meta.tsv | A tab-delimited file with bactopia metadata for all samples |






#### gather

Below is a description of the _per-sample_ results from the `gather` subworkflow.


| Filename                      | Description |
|-------------------------------|-------------|
| -meta.tsv | A tab-delimited file with bactopia metadata for each sample |






#### Failed Quality Checks

Built into Bactopia are few basic quality checks to help prevent downstream failures.
If a sample fails one of these checks, it will be excluded from further analysis. By
excluding these samples, complete pipeline failures are prevented.


| Filename                      | Description |
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





### Parameters


#### <i class="fa-xl fas fa-terminal"></i> Required
The following parameters are how you will provide either local or remote samples to be processed by Bactopia.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-alt"></i>` --samples` | A FOFN (via bactopia prepare) with sample names and paths to FASTQ/FASTAs to process <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-archive"></i>` --r1` | First set of compressed (gzip) Illumina paired-end FASTQ reads (requires --r2 and --sample) <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-archive"></i>` --r2` | Second set of compressed (gzip) Illumina paired-end FASTQ reads (requires --r1 and --sample) <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-archive"></i>` --se` | Compressed (gzip) Illumina single-end FASTQ reads  (requires --sample) <br/>**Type:** `string` |
| <i class="fa-lg fas fa-level-up"></i>` --ont` | Compressed (gzip) Oxford Nanopore FASTQ reads  (requires --sample) <br/>**Type:** `string` |
| <i class="fa-lg fas fa-level-up"></i>` --hybrid` | Create hybrid assembly using Unicycler.  (requires --r1, --r2, --ont and --sample) <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-level-up"></i>` --short_polish` | Create hybrid assembly from long-read assembly and short read polishing.  (requires --r1, --r2, --ont and --sample) <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-file"></i>` --sample` | Sample name to use for the input sequences <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --accessions` | A file containing ENA/SRA Experiment accessions or NCBI Assembly accessions to processed <br/>**Type:** `string` |
| <i class="fa-lg fas fa-font"></i>` --accession` | Sample name to use for the input sequences <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-archive"></i>` --assembly` | A assembled genome in compressed FASTA format. (requires --sample) <br/>**Type:** `string` |
| <i class="fa-lg fas fa-level-up"></i>` --check_samples` | Validate the input FOFN provided by --samples <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> Dataset
Define where the pipeline should find input data and save output data.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-bacterium"></i>` --species` | Name of species for species-specific dataset to use <br/>**Type:** `string` |
| <i class="fa-lg fas fa-print"></i>` --ask_merlin` | Ask Merlin to execute species specific Bactopia tools based on Mash distances <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --coverage` | Reduce samples to a given coverage, requires a genome size <br/>**Type:** `integer`, **Default:** `100` |
| <i class="fa-lg fas fa-arrows-alt-h"></i>` --genome_size` | Expected genome size (bp) for all samples, required for read error correction and read subsampling <br/>**Type:** `string`, **Default:** `0` |
| <i class="fa-lg fas fa-print"></i>` --use_bakta` | Use Bakta for annotation, instead of Prokka <br/>**Type:** `boolean` |

### Citations
If you use Bactopia and `gather` results in your analysis, please cite the following.

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
  


## Step 2 - QC

The `qc` module uses  a variety of tools to perform quality control on Illumina and
Oxford Nanopore reads. The tools used are:

| Tool | Technology | Description |
|------|------------|-------------|
| [bbtools](https://jgi.doe.gov/data-and-tools/bbtools/) | Illumina | A suite of tools for manipulating reads |
| [fastp](https://github.com/OpenGene/fastp) | Illumina | A tool designed to provide fast all-in-one preprocessing for FastQ files |
| [fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) | Illumina | A quality control tool for high throughput sequence data |
| [fastq_scan](https://github.com/rpetit3/fastq-scan) | Nanopore | A tool for quickly scanning FASTQ files |
| [lighter](https://github.com/mourisl/Lighter) | Illumina | A tool for correcting sequencing errors in Illumina reads |
| [NanoPlot](https://github.com/wdecoster/NanoPlot) | Nanopore | A tool for plotting long read sequencing data |
| [nanoq](https://github.com/esteinig/nanoq) | Nanopore | A tool for calculating quality metrics for Oxford Nanopore reads |
| [porechop](https://github.com/rrwick/Porechop) | Nanopore | A tool for removing adapters from Oxford Nanopore reads |
| [rasusa](https://github.com/mbhall88/rasusa) | Nanopore | Randomly subsample sequencing reads to a specified coverage |

Similar to the `gather` step, the `qc` step will also stop samples that fail to meet
basic QC checks from continuing downstream.


### Outputs

#### Quality Control

Below is a description of the _per-sample_ results from `qc` subworkflow.


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.fastq.gz | A gzipped FASTQ file containing the cleaned Illumina single-end, or Oxford Nanopore reads |
| &lt;SAMPLE_NAME&gt;_R{1\|2}.fastq.gz | A gzipped FASTQ file containing the cleaned Illumina paired-end reads |
| &lt;SAMPLE_NAME&gt;-{final\|original}.json | A JSON file containing the QC results generated by [fastq-scan](https://github.com/rpetit3/fastq-scan) |
| &lt;SAMPLE_NAME&gt;-{final\|original}_fastqc.html | (Illumina Only) A HTML report of the QC results generated by [fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) |
| &lt;SAMPLE_NAME&gt;-{final\|original}_fastqc.zip | (Illumina Only) A zip file containing the complete set of [fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) results |
| &lt;SAMPLE_NAME&gt;-{final\|original}_fastp.json | (Illumina Only) A JSON file containing the QC results generated by [fastp](https://github.com/OpenGene/fastp) |
| &lt;SAMPLE_NAME&gt;-{final\|original}_fastp.html | (Illumina Only) A HTML report of the QC results generated by [fastp](https://github.com/OpenGene/fastp) |
| &lt;SAMPLE_NAME&gt;-{final\|original}_NanoPlot-report.html | (ONT Only) A HTML report of the QC results generated by [NanoPlot](https://github.com/wdecoster/NanoPlot) |
| &lt;SAMPLE_NAME&gt;-{final\|original}_NanoPlot.tar.gz | (ONT Only) A tarball containing the complete set of [NanoPlot](https://github.com/wdecoster/NanoPlot) results |






#### Failed Quality Checks

Built into Bactopia are few basic quality checks to help prevent downstream failures.
If a sample fails one of these checks, it will be excluded from further analysis. By
excluding these samples, complete pipeline failures are prevented.


| Filename                      | Description |
|-------------------------------|-------------|
| .error-fastq.gz | A gzipped FASTQ file of Illumina Single-End or Oxford Nanopore reads that failed QC |
| _R{1\|2}.error-fastq.gz | A gzipped FASTQ file of Illumina Single-End or Oxford Nanopore reads that failed QC |
| -low-read-count-error.txt | Sample failed read count checks and excluded from further analysis |
| -low-sequence-coverage-error.txt | Sample failed sequenced coverage checks and excluded from further analysis |
| -low-sequence-depth-error.txt | Sample failed sequenced basepair checks and excluded from further analysis |



!!! info "Poor samples are excluded to prevent downstream failures"
    Samples that fail any of the QC checks will be excluded from further analysis.
    Those samples will generate a `*-error.txt` file with the error message. Excluding
    these samples prevents downstream failures that cause the whole workflow to fail.



??? warning "Example Error: After QC, too few reads remain"
    If after cleaning reads, a sample has less than the minimum required reads, the
    sample will be excluded from further analysis. You can adjust this minimum read
    count using the `--min_reads` parameter.

    __Example Text from &lt;SAMPLE_NAME&gt;-low-read-count-error.txt__  
    _&lt;SAMPLE_NAME&gt; FASTQ(s) contain `X` total reads. This does not exceed the required
    minimum `Y` read count. Further analysis is discontinued._

??? warning "Example Error: After QC, too little sequence coverage remains"
    If after cleaning reads, a sample has failed to meet the minimum sequence 
    coverage required, the sample will be excluded from further analysis. You can
    adjust this minimum read count using the `--min_coverage` parameter.

    __Note:__ This check is only performed when a genome size is available.

    __Example Text from &lt;SAMPLE_NAME&gt;-low-sequence-coverage-error.txt__  
    _After QC, &lt;SAMPLE_NAME&gt; FASTQ(s) contain `X` total basepairs. This does not
    exceed the required minimum `Y` bp (`Z`x coverage). Further analysis is
    discontinued._

??? warning "Example Error: After QC, too little sequenced basepairs remain"
    If after cleaning reads, a sample has failed to meet the minimum number of
    sequenced basepairs, the sample will be excluded from further analysis. You can
    adjust this minimum read count using the `--min_basepairs` parameter.

    __Example Text from &lt;SAMPLE_NAME&gt;-low-sequence-depth-error.txt__  
    _&lt;SAMPLE_NAME&gt; FASTQ(s) contain `X` total basepairs. This does not exceed the
    required minimum `Y` bp. Further analysis is discontinued._






### <i class="fa-xl fas fa-exclamation-circle"></i> QC Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-fast-forward"></i>` --use_bbmap` | Illumina reads will be QC'd using BBMap <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --use_porechop` | Use Porechop to remove adapters from ONT reads <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --skip_qc` | The QC step will be skipped and it will be assumed the inputs sequences have already been QCed. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --skip_qc_plots` | QC Plot creation by FastQC or Nanoplot will be skipped <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --skip_error_correction` | FLASH error correction of reads will be skipped. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-file-alt"></i>` --adapters` | A FASTA file containing adapters to remove <br/>**Type:** `string`, **Default:** `/home/robert_petit/bactopia/data/EMPTY_ADAPTERS` |
| <i class="fa-lg fas fa-hashtag"></i>` --adapter_k` | Kmer length used for finding adapters. <br/>**Type:** `integer`, **Default:** `23` |
| <i class="fa-lg fas fa-file-alt"></i>` --phix` | phiX174 reference genome to remove <br/>**Type:** `string`, **Default:** `/home/robert_petit/bactopia/data/EMPTY_PHIX` |
| <i class="fa-lg fas fa-hashtag"></i>` --phix_k` | Kmer length used for finding phiX174. <br/>**Type:** `integer`, **Default:** `31` |
| <i class="fa-lg fas fa-boxes"></i>` --ktrim` | Trim reads to remove bases matching reference kmers <br/>**Type:** `string`, **Default:** `r` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --mink` | Look for shorter kmers at read tips down to this length, when k-trimming or masking. <br/>**Type:** `integer`, **Default:** `11` |
| <i class="fa-lg fas fa-hashtag"></i>` --hdist` | Maximum Hamming distance for ref kmers (subs only) <br/>**Type:** `integer`, **Default:** `1` |
| <i class="fa-lg fas fa-boxes"></i>` --tpe` | When kmer right-trimming, trim both reads to the minimum length of either <br/>**Type:** `string`, **Default:** `t` |
| <i class="fa-lg fas fa-boxes"></i>` --tbo` | Trim adapters based on where paired reads overlap <br/>**Type:** `string`, **Default:** `t` |
| <i class="fa-lg fas fa-boxes"></i>` --qtrim` | Trim read ends to remove bases with quality below trimq. <br/>**Type:** `string`, **Default:** `rl` |
| <i class="fa-lg fas fa-hashtag"></i>` --trimq` | Regions with average quality BELOW this will be trimmed if qtrim is set to something other than f <br/>**Type:** `integer`, **Default:** `6` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --maq` | Reads with average quality (after trimming) below this will be discarded <br/>**Type:** `integer`, **Default:** `10` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --minlength` | Reads shorter than this after trimming will be discarded <br/>**Type:** `integer`, **Default:** `35` |
| <i class="fa-lg fas fa-hashtag"></i>` --ftm` | If positive, right-trim length to be equal to zero, modulo this number <br/>**Type:** `integer`, **Default:** `5` |
| <i class="fa-lg fas fa-boxes"></i>` --tossjunk` | Discard reads with invalid characters as bases <br/>**Type:** `string`, **Default:** `t` |
| <i class="fa-lg fas fa-boxes"></i>` --ain` | When detecting pair names, allow identical names <br/>**Type:** `string`, **Default:** `f` |
| <i class="fa-lg fas fa-boxes"></i>` --qout` | PHRED offset to use for output FASTQs <br/>**Type:** `string`, **Default:** `33` |
| <i class="fa-lg fas fa-hashtag"></i>` --maxcor` | Max number of corrections within a 20bp window <br/>**Type:** `integer`, **Default:** `1` |
| <i class="fa-lg fas fa-hashtag"></i>` --sampleseed` | Set to a positive number to use as the random number generator seed for sampling <br/>**Type:** `integer`, **Default:** `42` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --ont_minlength` | ONT Reads shorter than this will be discarded <br/>**Type:** `integer`, **Default:** `1000` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --ont_minqual` | Minimum average read quality filter of ONT reads <br/>**Type:** `integer` |
| <i class="fa-lg fas fa-italic"></i>` --porechop_opts` | Extra Porechop options in quotes <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --nanoplot_opts` | Extra NanoPlot options in quotes <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --bbduk_opts` | Extra BBDuk options in quotes <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --fastp_opts` | Extra fastp options in quotes <br/>**Type:** `string` |

### Citations
If you use Bactopia and `qc` results in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [BBTools](https://jgi.doe.gov/data-and-tools/bbtools/)  
    Bushnell B [BBMap short read aligner, and other bioinformatic tools.](http://sourceforge.net/projects/bbmap/) (Link)
  
- [fastp](https://github.com/OpenGene/fastp)  
    Chen S, Zhou Y, Chen Y, and Gu J [fastp: an ultra-fast all-in-one FASTQ preprocessor.](https://doi.org/10.1093/bioinformatics/bty560) _Bioinformatics_, 34(17), i884–i890. (2018)
  
- [fastq-scan](https://github.com/rpetit3/fastq-scan)  
    Petit III RA [fastq-scan: generate summary statistics of input FASTQ sequences.](https://github.com/rpetit3/fastq-scan) (GitHub)
  
- [FastQC](https://github.com/s-andrews/FastQC)  
    Andrews S [FastQC: a quality control tool for high throughput sequence data.](http://www.bioinformatics.babraham.ac.uk/projects/fastqc) (WebLink)
  
- [Lighter](https://github.com/mourisl/Lighter)  
    Song L, Florea L, Langmead B [Lighter: Fast and Memory-efficient Sequencing Error Correction without Counting](https://doi.org/10.1186/s13059-014-0509-9). _Genome Biol._ 15(11):509 (2014)
  
- [NanoPlot](https://github.com/wdecoster/NanoPlot)  
    De Coster W, D’Hert S, Schultz DT, Cruts M, Van Broeckhoven C [NanoPack: visualizing and processing long-read sequencing data](https://doi.org/10.1093/bioinformatics/bty149) _Bioinformatics_ Volume 34, Issue 15 (2018) 
  
- [Nanoq](https://github.com/esteinig/nanoq)  
    Steinig E [Nanoq: Minimal but speedy quality control for nanopore reads in Rust](https://github.com/esteinig/nanoq) (GitHub)
  
- [Pigz](https://zlib.net/pigz/)  
    Adler M. [pigz: A parallel implementation of gzip for modern multi-processor, multi-core machines.](https://zlib.net/pigz/) _Jet Propulsion Laboratory_ (2015)
  
- [Porechop](https://github.com/rrwick/Porechop)  
    Wick RR, Judd LM, Gorrie CL, Holt KE. [Completing bacterial genome assemblies with multiplex MinION sequencing.](https://doi.org/10.1099/mgen.0.000132) _Microb Genom._ 3(10):e000132 (2017)
  
- [Rasusa](https://github.com/mbhall88/rasusa)  
    Hall MB [Rasusa: Randomly subsample sequencing reads to a specified coverage.](https://doi.org/10.5281/zenodo.3731394) (2019).
  


## Step 3 - Assembler

The `assembler` module uses a variety of assembly tools to create an assembly of
Illumina and Oxford Nanopore reads. The tools used are:

| Tool | Description |
|------|-------------|
| [Dragonflye](https://github.com/rpetit3/dragonflye) | Assembly of Oxford Nanopore reads, as well as hybrid assembly with short-read polishing |
| [Shovill](https://github.com/tseemann/shovill) | Assembly of Illumina paired-end reads |
| [Shovill-SE](https://github.com/rpetit/shovill) | Assembly of Illumina single-end reads |
| [Unicycler](https://github.com/rrwick/Unicycler) | Hybrid assembly, using short-reads first then long-reads |

Summary statistics for each assembly are generated using [assembly-scan](https://github.com/rpetit3/assembly-scan).


### Outputs

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| assembly-scan.tsv | Assembly statistics for all samples |






#### Dragonflye

Below is a description of the _per-sample_ results for Oxford Nanopore reads using
[Dragonflye](https://github.com/rpetit3/dragonflye).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.fna.gz | The final assembly produced by Dragonflye |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file containing assembly statistics |
| flye-info.txt | A log file containing information about the Flye assembly |
| \{flye\|miniasm\|raven\}-unpolished.fasta.gz | Raw unprocessed assembly produced by the used assembler |
| \{flye\|miniasm\|raven\}-unpolished.gfa.gz | Raw unprocessed assembly graph produced by the used assembler |






#### Shovill

Below is a description of the _per-sample_ results for Illumina reads using
[Shovill](https://github.com/tseemann/shovill) or [Shovill-SE](https://github.com/rpetit3/shovill).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.fna.gz | The final assembly produced by Dragonflye |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file containing assembly statistics |
| flash.hist | (Paired-End Only) Numeric histogram of merged read lengths. |
| flash.histogram | (Paired-End Only) Visual histogram of merged read lengths |
| \{megahit\|spades\|velvet\}-unpolished.gfa.gz | Raw unprocessed assembly graph produced by the used assembler |
| shovill.corrections | List of post-assembly corrections made by Shovill |






#### Hybrid Assembly (Unicycler)

Below is a description of the _per-sample_ results for a hybrid assembly using
[Unicycler](https://github.com/rrwick/Unicycler) (`--hybrid`). When using Unicycler,
the short-reads are assembled first, then the long-reads are used to polish the
assembly.


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.fna.gz | The final assembly produced by Dragonflye |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file containing assembly statistics |
| unicycler-unpolished.fasta.gz | Raw unprocessed assembly produced by Unicycler |
| unicycler-unpolished.fasta.gz | Raw unprocessed assembly graph produced by Unicycler |






#### Hybrid Assembly (Short Read Polishing)

Below is a description of the _per-sample_ results for a hybrid assembly using
[Dragonflye](https://github.com/rpetit3/dragonflye) (`--short_polish`). When using
Dragonflye, the long-reads are assembled first, then the short-reads are used
to polish the assembly.

!!! tip "Prefer `--short_polish` over `--hybrid` with recent ONT sequencing"
    Using [Unicycler](https://github.com/rrwick/Unicycler) (`--hybrid`) to create a hybrid
    assembly works great when you have low-coverage noisy long-reads. However, if you are
    using recent ONT sequencing, you likely have high-coverage and using the `--short_polish`
    method is going to yeild better results (_and be faster!_) than `--hybrid`.


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.fna.gz | The final assembly produced by Dragonflye |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file containing assembly statistics |
| flye-info.txt | A log file containing information about the Flye assembly |
| \{flye\|miniasm\|raven\}-unpolished.fasta.gz | Raw unprocessed assembly produced by the used assembler |
| \{flye\|miniasm\|raven\}-unpolished.gfa.gz | Raw unprocessed assembly graph produced by the used assembler |






#### Failed Quality Checks

Built into Bactopia are few basic quality checks to help prevent downstream failures.
If a sample fails one of these checks, it will be excluded from further analysis. By
excluding these samples, complete pipeline failures are prevented.


| Filename                      | Description |
|-------------------------------|-------------|
| -assembly-error.txt | Sample failed read count checks and excluded from further analysis |



!!! info "Poor samples are excluded to prevent downstream failures"
    Samples that fail any of the QC checks will be excluded from further analysis.
    Those samples will generate a `*-error.txt` file with the error message. Excluding
    these samples prevents downstream failures that cause the whole workflow to fail.



??? warning "Example Error: Assembled Successfully, but 0 Contigs"
    If a sample assembles successfully, but 0 contigs are formed, the sample will be
    excluded from further analysis.

    __Example Text from &lt;SAMPLE_NAME&gt;-assembly-error.txt__  
    _&lt;SAMPLE_NAME&gt; assembled successfully, but 0 contigs were formed. Please investigate
    &lt;SAMPLE_NAME&gt; to determine a cause (e.g. metagenomic, contaminants, etc...) for this
    outcome. Further assembly-based analysis of &lt;SAMPLE_NAME&gt; will be discontinued._

??? warning "Example Error: Assembled successfully, but poor assembly size"
    If you sample assembles successfully, but the assembly size is less than the minimum
    allowed genome size, the sample will be excluded from further analysis. You can
    adjust this minimum size using the `--min_genome_size` parameter.

    __Example Text from &lt;SAMPLE_NAME&gt;-assembly-error.txt__  
    _&lt;SAMPLE_NAME&gt; assembled size (000 bp) is less than the minimum allowed genome
    size (000 bp). If this is unexpected, please investigate &lt;SAMPLE_NAME&gt; to
    determine a cause (e.g. metagenomic, contaminants, etc...) for the poor assembly.
    Otherwise, adjust the `--min_genome_size` parameter to fit your need. Further
    assembly based analysis of &lt;SAMPLE_NAME&gt; will be discontinued._






### <i class="fa-xl fas fa-exclamation-circle"></i> Assembler Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-boxes"></i>` --shovill_assembler` | Assembler to be used by Shovill <br/>**Type:** `string`, **Default:** `skesa` |
| <i class="fa-lg fas fa-boxes"></i>` --dragonflye_assembler` | Assembler to be used by Dragonflye <br/>**Type:** `string`, **Default:** `flye` |
| <i class="fa-lg fas fa-cut"></i>` --use_unicycler` | Use unicycler for paired end assembly <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_contig_len` | Minimum contig length <0=AUTO> <br/>**Type:** `integer`, **Default:** `500` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_contig_cov` | Minimum contig coverage <0=AUTO> <br/>**Type:** `integer`, **Default:** `2` |
| <i class="fa-lg fas fa-italic"></i>` --contig_namefmt` | Format of contig FASTA IDs in 'printf' style <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --shovill_opts` | Extra assembler options in quotes for Shovill <br/>**Type:** `string` |
| <i class="fa-lg fas fa-hashtag"></i>` --shovill_kmers` | K-mers to use <blank=AUTO> <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --dragonflye_opts` | Extra assembler options in quotes for Dragonflye <br/>**Type:** `string` |
| <i class="fa-lg fas fa-cut"></i>` --trim` | Enable adaptor trimming <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --no_stitch` | Disable read stitching for paired-end reads <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --no_corr` | Disable post-assembly correction <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-boxes"></i>` --unicycler_mode` | Bridging mode used by Unicycler <br/>**Type:** `string`, **Default:** `normal` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_polish_size` | Contigs shorter than this value (bp) will not be polished using Pilon <br/>**Type:** `integer`, **Default:** `10000` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_component_size` | Graph dead ends smaller than this size (bp) will be removed from the final graph <br/>**Type:** `integer`, **Default:** `1000` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_dead_end_size` | Graph dead ends smaller than this size (bp) will be removed from the final graph <br/>**Type:** `integer`, **Default:** `1000` |
| <i class="fa-lg fas fa-redo"></i>` --nanohq` | For Flye, use '--nano-hq' instead of --nano-raw <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-font"></i>` --medaka_model` | The model to use for Medaka polishing <br/>**Type:** `string` |
| <i class="fa-lg fas fa-hashtag"></i>` --medaka_rounds` | The number of Medaka polishing rounds to conduct <br/>**Type:** `integer` |
| <i class="fa-lg fas fa-hashtag"></i>` --racon_rounds` | The number of Racon polishing rounds to conduct <br/>**Type:** `integer`, **Default:** `1` |
| <i class="fa-lg fas fa-fast-forward"></i>` --no_polish` | Skip the assembly polishing step <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --no_miniasm` | Skip miniasm+Racon bridging <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-fast-forward"></i>` --no_rotate` | Do not rotate completed replicons to start at a standard gene <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-redo"></i>` --reassemble` | If reads were simulated, they will be used to create a new assembly. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --polypolish_rounds` | Number of polishing rounds to conduct with Polypolish for short read polishing <br/>**Type:** `integer`, **Default:** `1` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --pilon_rounds` | Number of polishing rounds to conduct with Pilon for short read polishing <br/>**Type:** `integer` |

### Citations
If you use Bactopia and `assembler` results in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [any2fasta](https://github.com/tseemann/any2fasta)  
    Seemann T [any2fasta: Convert various sequence formats to FASTA](https://github.com/tseemann/any2fasta) (GitHub)
  
- [assembly-scan](https://github.com/rpetit3/assembly-scan)  
    Petit III RA [assembly-scan: generate basic stats for an assembly](https://github.com/rpetit3/assembly-scan) (GitHub)
  
- [BWA](https://github.com/lh3/bwa/)  
    Li H [Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM](http://arxiv.org/abs/1303.3997). _arXiv_ [q-bio.GN] (2013)
  
- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [Dragonflye](https://github.com/rpetit3/dragonflye)  
    Petit III RA [Dragonflye: Assemble bacterial isolate genomes from Nanopore reads.](https://github.com/rpetit3/dragonflye) (GitHub)
  
- [FLASH](https://ccb.jhu.edu/software/FLASH/)  
    Magoč T, Salzberg SL [FLASH: fast length adjustment of short reads to improve genome assemblies.](https://doi.org/10.1093/bioinformatics/btr507) _Bioinformatics_ 27.21 2957-2963 (2011)
  
- [Flye](https://github.com/fenderglass/Flye)  
    Kolmogorov M, Yuan J, Lin Y, Pevzner P [Assembly of Long Error-Prone Reads Using Repeat Graphs](https://doi.org/10.1038/s41587-019-0072-8) _Nature Biotechnology_ (2019)
  
- [Medaka](https://github.com/nanoporetech/medaka)  
    ONT Research [Medaka: Sequence correction provided by ONT Research](https://github.com/nanoporetech/medaka) (GitHub)
  
- [MEGAHIT](https://github.com/voutcn/megahit)  
    Li D, Liu C-M, Luo R, Sadakane K, Lam T-W [MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph.](https://doi.org/10.1093/bioinformatics/btv033) _Bioinformatics_ 31.10 1674-1676 (2015)
  
- [Miniasm](https://github.com/lh3/miniasm)  
    Li H [Miniasm: Ultrafast de novo assembly for long noisy reads](https://github.com/lh3/miniasm) (GitHub)
  
- [Minimap2](https://github.com/lh3/minimap2)  
    Li H [Minimap2: pairwise alignment for nucleotide sequences.](https://doi.org/10.1093/bioinformatics/bty191) _Bioinformatics_ 34:3094-3100 (2018)
  
- [Nanoq](https://github.com/esteinig/nanoq)  
    Steinig E [Nanoq: Minimal but speedy quality control for nanopore reads in Rust](https://github.com/esteinig/nanoq) (GitHub)
  
- [Pigz](https://zlib.net/pigz/)  
    Adler M. [pigz: A parallel implementation of gzip for modern multi-processor, multi-core machines.](https://zlib.net/pigz/) _Jet Propulsion Laboratory_ (2015)
  
- [Pilon](https://github.com/broadinstitute/pilon/)  
    Walker BJ, Abeel T,  Shea T, Priest M, Abouelliel A, Sakthikumar S, Cuomo CA, Zeng Q, Wortman J, Young SK, Earl AM [Pilon: an integrated tool for comprehensive microbial variant detection and genome assembly improvement.](https://doi.org/10.1371/journal.pone.0112963) _PloS one_ 9.11 e112963 (2014)
  
- [Racon](https://github.com/lbcb-sci/racon)  
    Vaser R, Sović I, Nagarajan N, Šikić M [Fast and accurate de novo genome assembly from long uncorrected reads.](http://dx.doi.org/10.1101/gr.214270.116) _Genome Res_ 27, 737–746 (2017)
  
- [Rasusa](https://github.com/mbhall88/rasusa)  
    Hall MB [Rasusa: Randomly subsample sequencing reads to a specified coverage.](https://doi.org/10.5281/zenodo.3731394) (2019).
  
- [Raven](https://github.com/lbcb-sci/raven)  
    Vaser R, Šikić M [Time- and memory-efficient genome assembly with Raven.](https://doi.org/10.1038/s43588-021-00073-4) _Nat Comput Sci_ 1, 332–336 (2021)
  
- [samclip](https://github.com/tseemann/samclip)  
    Seemann T [Samclip: Filter SAM file for soft and hard clipped alignments](https://github.com/tseemann/samclip) (GitHub)
  
- [Samtools](https://github.com/samtools/samtools)  
    Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R [The Sequence Alignment/Map format and SAMtools](http://dx.doi.org/10.1093/bioinformatics/btp352). _Bioinformatics_ 25, 2078–2079 (2009)
  
- [Shovill](https://github.com/tseemann/shovill)  
    Seemann T [Shovill: De novo assembly pipeline for Illumina paired reads](https://github.com/tseemann/shovill) (GitHub)
  
- [Shovill-SE](https://github.com/rpetit3/shovill)  
    Petit III RA [Shovill-SE: A fork of Shovill that includes support for single end reads.](https://github.com/rpetit3/shovill) (GitHub)
  
- [SKESA](https://github.com/ncbi/SKESA)  
    Souvorov A, Agarwala R, Lipman DJ [SKESA: strategic k-mer extension for scrupulous assemblies.](https://doi.org/10.1186/s13059-018-1540-z) _Genome Biology_ 19:153 (2018)
  
- [SPAdes](https://github.com/ablab/spades)  
    Bankevich A, Nurk S, Antipov D, Gurevich AA, Dvorkin M, Kulikov AS, Lesin VM, Nikolenko SI, Pham S, Prjibelski AD, Pyshkin AV, Sirotkin AV, Vyahhi N, Tesler G, Alekseyev MA, Pevzner PA [SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing.](https://doi.org/10.1089/cmb.2012.0021) _Journal of computational biology_ 19.5 455-477 (2012)
  
- [Unicycler](https://github.com/rrwick/Unicycler)  
    Wick RR, Judd LM, Gorrie CL, Holt KE [Unicycler: Resolving bacterial genome assemblies from short and long sequencing reads.](http://dx.doi.org/10.1371/journal.pcbi.1005595) _PLoS Comput. Biol._ 13, e1005595 (2017)
  
- [Velvet](https://github.com/dzerbino/velvet)  
    Zerbino DR, Birney E [Velvet: algorithms for de novo short read assembly using de Bruijn graphs.](http://www.genome.org/cgi/doi/10.1101/gr.074492.107) _Genome research_ 18.5 821-829 (2008)
  


## Step 4 - Annotator

### Outputs

#### Prokka

Below is a description of the _per-sample_ results from [Prokka](https://github.com/tseemann/prokka).


| Filename                      | Description |
|-------------------------------|-------------|
| .blastdb.tar.gz | A gzipped tar archive of BLAST+ database of the contigs, genes, and proteins |
| .faa.gz | Protein FASTA file of the translated CDS sequences. |
| .ffn.gz | Nucleotide FASTA file of all the prediction transcripts (CDS, rRNA, tRNA, tmRNA, misc_RNA) |
| .fna.gz | Nucleotide FASTA file of the input contig sequences. |
| .gbk.gz | This is a standard GenBank file derived from the master .gff. If the input to prokka was a multi-FASTA, then this will be a multi-GenBank, with one record for each sequence. |
| .gff.gz | This is the master annotation in GFF3 format, containing both sequences and annotations. It can be viewed directly in Artemis or IGV. |
| .sqn.gz | An ASN1 format "Sequin" file for submission to GenBank. It needs to be edited to set the correct taxonomy, authors, related publication etc. |
| .tbl.gz | Feature Table file, used by "tbl2asn" to create the .sqn file. |
| .tsv | Tab-separated file of all features (locus_tag,ftype,len_bp,gene,EC_number,COG,product) |
| .txt | Statistics relating to the annotated features found. |




#### Bakta

Below is a description of the _per-sample_ results from [Bakta](https://github.com/oschwengers/bakta).


| Filename                      | Description |
|-------------------------------|-------------|
| .blastdb.tar.gz | A gzipped tar archive of BLAST+ database of the contigs, genes, and proteins |
| .embl.gz | Annotations & sequences in (multi) EMBL format |
| .faa.gz | CDS/sORF amino acid sequences as FASTA |
| .ffn.gz | Feature nucleotide sequences as FASTA |
| .fna.gz | Replicon/contig DNA sequences as FASTA |
| .gbff.gz | Annotations & sequences in (multi) GenBank format |
| .gff3.gz | Annotations & sequences in GFF3 format |
| .hypotheticals.faa.gz | Hypothetical protein CDS amino acid sequences as FASTA |
| .hypotheticals.tsv | Further information on hypothetical protein CDS as simple human readable tab separated values |
| .tsv | Annotations as simple human readable tab separated values |
| .txt | Broad summary of `Bakta` annotations |




### Parameters


#### <i class="fa-xl fas fa-exclamation-circle"></i> Prokka


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-alt"></i>` --proteins` | FASTA file of trusted proteins to first annotate from <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --prodigal_tf` | Training file to use for Prodigal <br/>**Type:** `string` |
| <i class="fa-lg fas fa-check"></i>` --compliant` | Force Genbank/ENA/DDJB compliance <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-school"></i>` --centre` | Sequencing centre ID <br/>**Type:** `string`, **Default:** `Bactopia` |
| <i class="fa-lg fas fa-hashtag"></i>` --prokka_coverage` | Minimum coverage on query protein <br/>**Type:** `integer`, **Default:** `80` |
| <i class="fa-lg fas fa-italic"></i>` --prokka_evalue` | Similarity e-value cut-off <br/>**Type:** `string`, **Default:** `1e-09` |
| <i class="fa-lg fas fa-italic"></i>` --prokka_opts` | Extra Prokka options in quotes. <br/>**Type:** `string` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> Bakta Download


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-alt"></i>` --bakta_db` | Tarball or path to the Bakta database <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --bakta_db_type` | Which Bakta DB to download 'full' (~30GB) or 'light' (~2GB) <br/>**Type:** `string`, **Default:** `full` |
| <i class="fa-lg fas fa-file-alt"></i>` --bakta_save_as_tarball` | Save the Bakta database as a tarball <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --download_bakta` | Download the Bakta database to the path given by --bakta_db <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> Bakta


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-alt"></i>` --proteins` | FASTA file of trusted proteins to first annotate from <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --prodigal_tf` | Training file to use for Prodigal <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --replicons` | Replicon information table (tsv/csv) <br/>**Type:** `string` |
| <i class="fa-lg fas fa-hashtag"></i>` --min_contig_length` | Minimum contig size to annotate <br/>**Type:** `integer`, **Default:** `1` |
| <i class="fa-lg fas fa-italic"></i>` --keep_contig_headers` | Keep original contig headers <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --compliant` | Force Genbank/ENA/DDJB compliance <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_trna` | Skip tRNA detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_tmrna` | Skip tmRNA detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_rrna` | Skip rRNA detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_ncrna` | Skip ncRNA detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_ncrna_region` | Skip ncRNA region detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_crispr` | Skip CRISPR array detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_cds` | Skip CDS detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_sorf` | Skip sORF detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_gap` | Skip gap detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --skip_ori` | Skip oriC/oriT detection & annotation <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --bakta_opts` | Extra Backa options in quotes. Example: '--gram +' <br/>**Type:** `string` |

### Citations
If you use Bactopia and `annotator` results in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Prokka](https://github.com/tseemann/prokka)  
    Seemann T [Prokka: rapid prokaryotic genome annotation](http://dx.doi.org/10.1093/bioinformatics/btu153) _Bioinformatics_ 30, 2068–2069 (2014)
  


- [Bakta](https://github.com/oschwengers/bakta)  
    Schwengers O, Jelonek L, Dieckmann MA, Beyvers S, Blom J, Goesmann A [Bakta - rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.](https://doi.org/10.1099/mgen.0.000685) _Microbial Genomics_ 7(11) (2021)
  


## Step 5 - Sketcher

The `sketcher` module uses [Mash](https://github.com/marbl/Mash) and
[Sourmash](https://github.com/dib-lab/sourmash) to create sketches and query
[RefSeq](https://www.ncbi.nlm.nih.gov/refseq/) and [GTDB](https://gtdb.ecogenomic.org/).


### Outputs

#### sketcher

Below is a description of the _per-sample_ results from the `sketcher` subworkflow.


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-k{21\|31}.msh | A Mash sketch of the input assembly for k=21 and k=31 |
| &lt;SAMPLE_NAME&gt;-mash-refseq88-k21.txt | The results of querying the Mash sketch against RefSeq88 |
| &lt;SAMPLE_NAME&gt;-sourmash-gtdb-rs207-k31.txt | The results of querying the Sourmash sketch against GTDB-rs207 |
| &lt;SAMPLE_NAME&gt;.sig | A Sourmash sketch of the input assembly for k=21, k=31, and k=51 |





### <i class="fa-xl fas fa-exclamation-circle"></i> Sketcher Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-hashtag"></i>` --sketch_size` | Sketch size. Each sketch will have at most this many non-redundant min-hashes. <br/>**Type:** `integer`, **Default:** `10000` |
| <i class="fa-lg fas fa-hashtag"></i>` --sourmash_scale` | Choose number of hashes as 1 in FRACTION of input k-mers <br/>**Type:** `integer`, **Default:** `10000` |
| <i class="fa-lg fas fa-fast-forward"></i>` --no_winner_take_all` | Disable winner-takes-all strategy for identity estimates <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-hashtag"></i>` --screen_i` | Minimum identity to report. <br/>**Type:** `number`, **Default:** `0.8` |

### Citations
If you use Bactopia and `sketcher` results in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Genome Taxonomy Database](https://gtdb.ecogenomic.org/)  
    Parks DH, Chuvochina M, Rinke C, Mussig AJ, Chaumeil P-A, Hugenholtz P [GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically consistent, rank normalized and complete genome-based taxonomy](https://doi.org/10.1093/nar/gkab776) _Nucleic Acids Research_ gkab776 (2021)
  
- [Mash](https://github.com/marbl/Mash)  
    Ondov BD, Treangen TJ, Melsted P, Mallonee AB, Bergman NH, Koren S, Phillippy AM [Mash: fast genome and metagenome distance estimation using MinHash](http://dx.doi.org/10.1186/s13059-016-0997-x). _Genome Biol_ 17, 132 (2016)
  
- [Mash](https://github.com/marbl/Mash)  
    Ondov BD, Starrett GJ, Sappington A, Kostic A, Koren S, Buck CB, Phillippy AM [Mash Screen: high-throughput sequence containment estimation for genome discovery](https://doi.org/10.1186/s13059-019-1841-x) _Genome Biol_ 20, 232 (2019)
  
- [NCBI RefSeq Database](https://www.ncbi.nlm.nih.gov/refseq/)  
    O'Leary NA, Wright MW, Brister JR, Ciufo S, Haddad D, McVeigh R, Rajput B, Robbertse B, Smith-White B, Ako-Adjei D, Astashyn A, Badretdin A, Bao Y, Blinkova O0, Brover V, Chetvernin V, Choi J, Cox E, Ermolaeva O, Farrell CM, Goldfarb T, Gupta T, Haft D, Hatcher E, Hlavina W, Joardar VS, Kodali VK, Li W, Maglott D, Masterson P, McGarvey KM, Murphy MR, O'Neill K, Pujar S, Rangwala SH, Rausch D, Riddick LD, Schoch C, Shkeda A, Storz SS, Sun H, Thibaud-Nissen F, Tolstoy I, Tully RE, Vatsan AR, Wallin C, Webb D, Wu W, Landrum MJ, Kimchi A, Tatusova T, DiCuccio M, Kitts P, Murphy TD, Pruitt KD [Reference sequence (RefSeq) database at NCBI: current status, taxonomic expansion, and functional annotation.](https://doi.org/10.1093/nar/gkv1189) _Nucleic Acids Res._ 44, D733–45 (2016)
  
- [Sourmash](https://github.com/dib-lab/sourmash)  
    Brown CT, Irber L [sourmash: a library for MinHash sketching of DNA](http://dx.doi.org/10.21105/joss.00027). _JOSS_ 1, 27 (2016)
  


## Step 6 - Sequence Typing

### Outputs

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| mlst.tsv | A merged TSV file with `mlst` results from all samples |


#### mlst

Below is a description of the _per-sample_ results from [mlst](https://github.com/tseemann/mlst).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `mlst` result, see [mlst - Usage](https://github.com/tseemann/mlst#usage) for more details |





### <i class="fa-xl fas fa-exclamation-circle"></i> Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --scheme` | Don't autodetect, force this scheme on all inputs <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --minid` | Minimum DNA percent identity of full allelle to consider 'similar' <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mincov` | Minimum DNA percent coverage to report partial allele at all <br/>**Type:** `integer`, **Default:** `10` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --minscore` | Minumum score out of 100 to match a scheme <br/>**Type:** `integer`, **Default:** `50` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --nopath` | Strip filename paths from FILE column <br/>**Type:** `boolean` |

### Citations
If you use Bactopia and `sequence typing` results in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [mlst](https://github.com/tseemann/mlst)  
    Seemann T [mlst: scan contig files against PubMLST typing schemes](https://github.com/tseemann/mlst) (GitHub)
  
- [PubMLST.org](https://pubmlst.org/)  
    Jolley KA, Bray JE, Maiden MCJ [Open-access bacterial population genomics: BIGSdb software, the PubMLST.org website and their applications.](http://dx.doi.org/10.12688/wellcomeopenres.14826.1) _Wellcome Open Res_ 3, 124 (2018)
  


## Step 7 - Antibiotic Resistance

### Outputs

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| amrfinderplus-genes.tsv | A merged TSV file with `AMRFinder+` results using nucleotide inputs |
| amrfinderplus-proteins.tsv | A merged TSV file with `AMRFinder+` results using protein inputs |


#### AMRFinder+

Below is a description of the _per-sample_ results from [AMRFinder+](https://github.com/ncbi/amr).


| Filename                      | Description |
|-------------------------------|-------------|
| -genes.tsv | A TSV file with `AMRFinder+` results using nucleotide inputs |
| -proteins.tsv | A TSV file with `AMRFinder+` results using protein inputs |





### <i class="fa-xl fas fa-exclamation-circle"></i> Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --ident_min` | Minimum proportion of identical amino acids in alignment for hit (0..1) <br/>**Type:** `number`, **Default:** `-1` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --coverage_min` | Minimum coverage of the reference protein (0..1) <br/>**Type:** `number`, **Default:** `0.5` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --organism` | Taxonomy group to run additional screens against <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --translation_table` | NCBI genetic code for translated BLAST <br/>**Type:** `integer`, **Default:** `11` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --amrfinder_noplus` | Disable running AMRFinder+ with the --plus option <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --report_common` | Report proteins common to a taxonomy group <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --report_all_equal` | Report all equally-scoring BLAST and HMM matches <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --amrfinder_opts` | Extra AMRFinder+ options in quotes. <br/>**Type:** `string` |

### Citations
If you use Bactopia and `antibiotic resistance` results in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [AMRFinderPlus](https://github.com/ncbi/amr)  
    Feldgarden M, Brover V, Haft DH, Prasad AB, Slotta DJ, Tolstoy I, Tyson GH, Zhao S, Hsu C-H, McDermott PF, Tadesse DA, Morales C, Simmons M, Tillman G, Wasilenko J, Folster JP, Klimke W [Validating the NCBI AMRFinder Tool and Resistance Gene Database Using Antimicrobial Resistance Genotype-Phenotype Correlations in a Collection of NARMS Isolates](https://doi.org/10.1128/AAC.00483-19). _Antimicrob. Agents Chemother._ (2019)
  
- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  


## Step 8 - Merlin

### Outputs

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| agrvate.tsv | A merged TSV file with `AgrVATE` results from all samples |
| ectyper.tsv | A merged TSV file with `ECTyper` results from all samples |
| emmtyper.tsv | A merged TSV file with `emmtyper` results from all samples |
| genotyphi.tsv | A merged TSV file with `genotyphi` results from all samples |
| hicap.tsv | A merged TSV file with `hicap` results from all samples |
| hpsuissero.tsv | A merged TSV file with `HpsuisSero` results from all samples |
| kleborate.tsv | A merged TSV file with `Kleborate` results from all samples |
| legsta.tsv | A merged TSV file with `legsta` results from all samples |
| lissero.tsv | A merged TSV file with `LisSero` results from all samples |
| meningotype.tsv | A merged TSV file with `meningotype` results from all samples |
| ngmaster.tsv | A merged TSV file with `ngmaster` results from all samples |
| pasty.tsv | A merged TSV file with `pasty` results from all samples |
| pbptyper.tsv | A merged TSV file with `pbptyper` results from all samples |
| seqsero2.tsv | A merged TSV file with `seqsero2` results from all samples |
| seroba.tsv | A merged TSV file with `seroba` results from all samples |
| shigatyper.tsv | A merged TSV file with `ShigaTyper` results from all samples |
| shigeifinder.tsv | A merged TSV file with `ShigEiFinder` results from all samples |
| sistr.tsv | A merged TSV file with `SISTR` results from all samples |
| spatyper.tsv | A merged TSV file with `spaTyper` results from all samples |
| ssuissero.tsv | A merged TSV file with `SsuisSero` results from all samples |
| staphopiasccmec.tsv | A merged TSV file with `staphopia-sccmec` results from all samples |
| stecfinder.tsv | A merged TSV file with `stecfinder` results from all samples |


#### AgrVATE

Below is a description of the _per-sample_ results from [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE).


| Filename                      | Description |
|-------------------------------|-------------|
| -agr_gp.tab | A detailed report for _agr_ kmer matches |
| -blastn_log.txt | Log files from programs called by `AgrVATE` |
| -summary.tab | A final summary report for _agr_ typing |


#### ECTyper

Below is a description of the _per-sample_ results from [ECTyper](https://github.com/phac-nml/ecoli_serotyping).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `ECTyper` result, see [ECTyper - Report format](https://github.com/phac-nml/ecoli_serotyping#report-format) for details |
| blast_output_alleles.txt | Allele report generated from BLAST results |


#### emmtyper

Below is a description of the _per-sample_ results from [emmtyper](https://github.com/MDU-PHL/emmtyper).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `emmtyper` result, see [emmtyper - Result format](https://github.com/MDU-PHL/emmtyper#result-format) for details |


#### hicap

Below is a description of the _per-sample_ results from [hicap](https://github.com/scwatts/hicap).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.gbk | GenBank file and cap locus annotations |
| &lt;SAMPLE_NAME&gt;.svg | Visualization of annotated cap locus |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `hicap` results |


#### HpsuisSero

Below is a description of the _per-sample_ results from [HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_serotyping_res.tsv | A tab-delimited file with `HpsuisSero` result |


#### GenoTyphi

Below is a description of the _per-sample_ results from [GenoTyphi](https://github.com/katholt/genotyphi). A
full description of the GenoTyphi output is available at [GenoTyphi - Output](https://github.com/katholt/genotyphi/blob/main/README.md#explanation-of-columns-in-the-output)


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_predictResults.tsv | A tab-delimited file with `GenoTyphi` results |
| &lt;SAMPLE_NAME&gt;.csv | The output of `mykrobe predict` in comma-separated format |
| &lt;SAMPLE_NAME&gt;.json | The output of `mykrobe predict` in JSON format |


#### Kleborate

Below is a description of the _per-sample_ results from [Kleborate](https://github.com/katholt/Kleborate).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.results.txt | A tab-delimited file with `Kleborate` result, see  [Kleborate - Example output](https://github.com/katholt/Kleborate/wiki/Tests-and-example-outputs#example-output) for more details. |


#### legsta

Below is a description of the _per-sample_ results from [legsta](https://github.com/tseemann/legsta).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `legsta` result, see [legsta - Output](https://github.com/tseemann/legsta#output) for more details |


#### LisSero

Below is a description of the _per-sample_ results from [LisSero](https://github.com/MDU-PHL/LisSero).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `LisSero` results |


#### Mash

Below is a description of the _per-sample_ results from [Mash](https://github.com/marbl/Mash).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-dist.txt | A tab-delimited file with `mash dist` results |


#### meningotype

Below is a description of the _per-sample_ results from [meningotype](https://github.com/MDU-PHL/meningotype) .


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `meningotype` result |


#### ngmaster

Below is a description of the _per-sample_ results from [ngmaster](https://github.com/MDU-PHL/ngmaster).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `ngmaster` results |


#### pasty

Below is a description of the _per-sample_ results from [pasty](https://github.com/rpetit3/pasty).


| Filename                      | Description |
|-------------------------------|-------------|
| .blastn.tsv | A tab-delimited file of all blast hits |
| .details.tsv | A tab-delimited file with details for each serogroup |
| .tsv | A tab-delimited file with the predicted serogroup |


#### pbptyper

Below is a description of the _per-sample_ results from [pbptyper](https://github.com/rpetit3/pbptyper).


| Filename                      | Description |
|-------------------------------|-------------|
| .tblastn.tsv | A tab-delimited file of all blast hits |
| .tsv | A tab-delimited file with the predicted PBP type |


#### SeqSero2

Below is a description of the _per-sample_ results from [SeqSero2](https://github.com/denglab/SeqSero2).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_result.tsv | A tab-delimited file with `SeqSero2` results |
| &lt;SAMPLE_NAME&gt;_result.txt | A text file with key-value pairs of `SeqSero2` results |


#### Seroba

Below is a description of the _per-sample_ results from [Seroba](https://github.com/sanger-pathogens/seroba).
More details about the outputs are available from [Seroba - Output](https://sanger-pathogens.github.io/seroba/#output).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with the predicted serotype |
| detailed_serogroup_info.txt | Detailed information about the predicted results |


#### ShigaTyper

Below is a description of the _per-sample_ results from [ShigaTyyper](https://github.com/CFSAN-Biostatistics/shigatyper).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-hits.tsv | Detailed statistics about each individual gene hit |
| &lt;SAMPLE_NAME&gt;.tsv | The final predicted serotype by `ShigaTyper` |


#### ShigEiFinder

Below is a description of the _per-sample_ results from [ShigEiFinder](https://github.com/LanLab/ShigEiFinder).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with the predicted Shigella or EIEC serotype |


#### SISTR

Below is a description of the _per-sample_ results from [SISTR](https://github.com/phac-nml/sistr_cmd).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-allele.fasta.gz | A FASTA file of the cgMLST allele search results |
| &lt;SAMPLE_NAME&gt;-allele.json.gz | JSON formated cgMLST allele search results, see  [SISTR - cgMLST search results](https://github.com/phac-nml/sistr_cmd#cgmlst-allele-search-results) for more details |
| &lt;SAMPLE_NAME&gt;-cgmlst.csv | A comma-delimited summary of the cgMLST allele search results |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `SISTR` results, see [SISTR - Primary results](https://github.com/phac-nml/sistr_cmd#primary-results-output--o-sistr-results) for more details |


#### spaTyper

Below is a description of the _per-sample_ results from [spaTyper](https://github.com/HCGB-IGTP/spaTyper).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `spaTyper` result |


#### SsuisSero

Below is a description of the _per-sample_ results from [SsuisSero](https://github.com/jimmyliu1326/SsuisSero).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_serotyping_res.tsv | A tab-delimited file with `SsuisSero` results |


#### staphopia-sccmec

Below is a description of the _per-sample_ results from [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `staphopia-sccmec` results |


#### TBProfiler

Below is a description of the _per-sample_ results from [TBProfiler](https://github.com/jodyphelan/TBProfiler).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.results.csv | A CSV formated `TBProfiler` result file of resistance and strain type |
| &lt;SAMPLE_NAME&gt;.results.json | A JSON formated `TBProfiler` result file of resistance and strain type |
| &lt;SAMPLE_NAME&gt;.results.txt | A text file with `TBProfiler` results |
| &lt;SAMPLE_NAME&gt;.bam | BAM file with alignment details |
| &lt;SAMPLE_NAME&gt;.targets.csq.vcf.gz | VCF with variant info again reference genomes |




###

#### <i class="fa-xl fas fa-exclamation-circle"></i> mashdist 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mash_sketch` | The reference sequence as a Mash Sketch (.msh file) <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mash_seed` | Seed to provide to the hash function <br/>**Type:** `integer`, **Default:** `42` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mash_table` |  Table output (fields will be blank if they do not meet the p-value threshold) <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mash_m` | Minimum copies of each k-mer required to pass noise filter for reads <br/>**Type:** `integer`, **Default:** `1` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mash_w` | Probability threshold for warning about low k-mer size. <br/>**Type:** `number`, **Default:** `0.01` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --max_p` | Maximum p-value to report. <br/>**Type:** `number`, **Default:** `1.0` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --max_dist` | Maximum distance to report. <br/>**Type:** `number`, **Default:** `1.0` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --merlin_dist` | Maximum distance to report when using Merlin . <br/>**Type:** `number`, **Default:** `0.1` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --full_merlin` | Go full Merlin and run all species-specific tools, no matter the Mash distance <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --use_fastqs` | Query with FASTQs instead of the assemblies <br/>**Type:** `boolean` |

#### <i class="fa-xl fa-solid fa-toolbox"></i> AgrVATE 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fa-solid fa-toggle-on"></i>` --typing_only` | agr typing only. Skips agr operon extraction and frameshift detection <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> ECTyper 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --opid` | Percent identity required for an O antigen allele match <br/>**Type:** `integer`, **Default:** `90` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --opcov` | Minumum percent coverage required for an O antigen allele match <br/>**Type:** `integer`, **Default:** `90` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --hpid` | Percent identity required for an H antigen allele match <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --hpcov` | Minumum percent coverage required for an H antigen allele match <br/>**Type:** `integer`, **Default:** `50` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --verify` | Enable E. coli species verification <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --print_alleles` | Prints the allele sequences if enabled as the final column <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> emmtyper 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --emmtyper_wf` | Workflow for emmtyper to use. <br/>**Type:** `string`, **Default:** `blast` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --cluster_distance` | Distance between cluster of matches to consider as different clusters <br/>**Type:** `integer`, **Default:** `500` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --percid` | Minimal percent identity of sequence <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --culling_limit` | Total hits to return in a position <br/>**Type:** `integer`, **Default:** `5` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mismatch` | Threshold for number of mismatch to allow in BLAST hit <br/>**Type:** `integer`, **Default:** `5` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --align_diff` | Threshold for difference between alignment length and subject length in BLAST <br/>**Type:** `integer`, **Default:** `5` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --gap` | Threshold gap to allow in BLAST hit <br/>**Type:** `integer`, **Default:** `2` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --min_perfect` | Minimum size of perfect match at 3 primer end <br/>**Type:** `integer`, **Default:** `15` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --min_good` | Minimum size where there must be 2 matches for each mismatch <br/>**Type:** `integer`, **Default:** `15` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --max_size` | Maximum size of PCR product <br/>**Type:** `integer`, **Default:** `2000` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> hicap 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-boxes"></i>` --database_dir` | Directory containing locus database <br/>**Type:** `string` |
| <i class="fa-lg fas fa-boxes"></i>` --model_fp` | Path to prodigal model <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --full_sequence` | Write the full input sequence out to the genbank file rather than just the region surrounding and including the locus <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --hicap_debug` | hicap will print debug messages <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --gene_coverage` | Minimum percentage coverage to consider a single gene complete <br/>**Type:** `number`, **Default:** `0.8` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --gene_identity` | Minimum percentage identity to consider a single gene complete <br/>**Type:** `number`, **Default:** `0.7` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --broken_gene_length` | Minimum length to consider a broken gene <br/>**Type:** `integer`, **Default:** `60` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --broken_gene_identity` | Minimum percentage identity to consider a broken gene <br/>**Type:** `number`, **Default:** `0.8` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> GenoTyphi 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --kmer` | K-mer length <br/>**Type:** `integer`, **Default:** `21` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --min_depth` | Minimum depth <br/>**Type:** `integer`, **Default:** `1` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --model` | Genotype model used. <br/>**Type:** `string`, **Default:** `kmer_count` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --report_all_calls` | Report all calls <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --mykrobe_opts` | Extra Mykrobe options in quotes <br/>**Type:** `string` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> Kleborate 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_resistance` | Turn off resistance genes screening <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_kaptive` | Turn off Kaptive screening of K and O loci <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_identity` | Minimum alignment percent identity for main results <br/>**Type:** `number`, **Default:** `90.0` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --kleborate_min_coverage` | Minimum alignment percent coverage for main results <br/>**Type:** `number`, **Default:** `80.0` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_spurious_identity` | Minimum alignment percent identity for spurious results <br/>**Type:** `number`, **Default:** `80.0` |
| <i class="fa-lg fas fa-angle-double-down"></i>` --min_spurious_coverage` | Minimum alignment percent coverage for spurious results <br/>**Type:** `number`, **Default:** `40.0` |
| <i class="fa-lg fas fa-boxes"></i>` --min_kaptive_confidence` | Minimum Kaptive confidence to call K/O loci - confidence levels below this will be reported as unknown <br/>**Type:** `string`, **Default:** `Good` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --force_index` | Rebuild the BLAST index at the start of execution <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> legsta 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --noheader` | Don't print header row <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> LisSero 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --min_id` | Minimum percent identity to accept a match <br/>**Type:** `number`, **Default:** `95.0` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --min_cov` | Minimum coverage of the gene to accept a match <br/>**Type:** `number`, **Default:** `95.0` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> meningotype 
You can use these parameters to fine-tune your meningotype analysis

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --finetype` | perform porA and fetA fine typing <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --porB` | perform porB sequence typing (NEIS2020) <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --bast` | perform Bexsero antigen sequence typing (BAST) <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mlst` | perform MLST <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --all` | perform MLST, porA, fetA, porB, BAST typing <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> ngmaster 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --csv` | output comma-separated format (CSV) rather than tab-separated <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> pasty 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --pasty_min_pident` | Minimum percent identity to count a hit <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --pasty_min_coverage` | Minimum percent coverage to count a hit <br/>**Type:** `integer`, **Default:** `95` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> pbptyper 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --pbptyper_min_pident` | Minimum percent identity to count a hit <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --pbptyper_min_coverage` | Minimum percent coverage to count a hit <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --pbptyper_min_ani` | Minimum S. pneumoniae ANI to predict PBP Type <br/>**Type:** `integer`, **Default:** `95` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> SeqSero2 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --run_mode` | Workflow to run. 'a' allele mode, or 'k' k-mer mode <br/>**Type:** `string`, **Default:** `k` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --input_type` | Input format to analyze. 'assembly' or 'fastq' <br/>**Type:** `string`, **Default:** `assembly` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --bwa_mode` | Algorithms for bwa mapping for allele mode <br/>**Type:** `string`, **Default:** `mem` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> SISTR 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --full_cgmlst` |  Use the full set of cgMLST alleles which can include highly similar alleles <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> spaTyper 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-archive"></i>` --repeats` | List of spa repeats <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-archive"></i>` --repeat_order` | List spa types and order of repeats <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --do_enrich` | Do PCR product enrichment <br/>**Type:** `boolean` |

#### <i class="fa-xl fas fa-exclamation-circle"></i> staphopia-sccmec 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --hamming` | Report the results as hamming distances <br/>**Type:** `boolean` |

### Citations
If you use Bactopia and `merlin` results in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE)  
    Raghuram V. [AgrVATE: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.](https://github.com/VishnuRaghuram94/AgrVATE) (GitHub)
  
- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [ECTyper](https://github.com/phac-nml/ecoli_serotyping)  
    Laing C, Bessonov K, Sung S, La Rose C [ECTyper - In silico prediction of _Escherichia coli_ serotype](https://github.com/phac-nml/ecoli_serotyping) (GitHub)  
- [emmtyper](https://github.com/MDU-PHL/emmtyper)  
    Tan A, Seemann T, Lacey D, Davies M, Mcintyre L, Frost H, Williamson D, Gonçalves da Silva A [emmtyper - emm Automatic Isolate Labeller](https://github.com/MDU-PHL/emmtyper) (GitHub)
  
- [GenoTyphi](https://github.com/katholt/genotyphi)  
    Wong VK, Baker S, Connor TR, Pickard D, Page AJ, Dave J, Murphy N, Holliman R, Sefton A, Millar M, Dyson ZA, Dougan G, Holt KE, & International Typhoid Consortium. [An extended genotyping framework for Salmonella enterica serovar Typhi, the cause of human typhoid](https://doi.org/10.1038/ncomms12827) _Nature Communications_ 7, 12827. (2016)
  
- [hicap](https://github.com/scwatts/hicap)  
    Watts SC, Holt KE [hicap: in silico serotyping of the Haemophilus influenzae capsule locus.](https://doi.org/10.1128/JCM.00190-19) _Journal of Clinical Microbiology_ JCM.00190-19 (2019)
  
- [HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero)  
    Lui J [HpsuisSero: Rapid _Haemophilus parasuis_ serotyping](https://github.com/jimmyliu1326/HpsuisSero) (GitHub)
  
- [Kleborate](https://github.com/katholt/Kleborate)  
    Lam MMC, Wick RR, Watts, SC, Cerdeira LT, Wyres KL, Holt KE [A genomic surveillance framework and genotyping tool for Klebsiella pneumoniae and its related species complex.](https://doi.org/10.1038/s41467-021-24448-3) _Nat Commun_ 12, 4188 (2021)
  
- [legsta](https://github.com/tseemann/legsta)  
    Seemann T [legsta: In silico Legionella pneumophila Sequence Based Typing](https://github.com/tseemann/legsta) (GitHub)
  
- [LisSero](https://github.com/MDU-PHL/LisSero)  
    Kwong J, Zhang J, Seeman T, Horan, K, Gonçalves da Silva A [LisSero - _In silico_ serotype prediction for _Listeria monocytogenes_](https://github.com/MDU-PHL/LisSero) (GitHub)
  
- [Mash](https://github.com/marbl/Mash)  
    Ondov BD, Treangen TJ, Melsted P, Mallonee AB, Bergman NH, Koren S, Phillippy AM [Mash: fast genome and metagenome distance estimation using MinHash](http://dx.doi.org/10.1186/s13059-016-0997-x). _Genome Biol_ 17, 132 (2016)
  
- [meningotype](https://github.com/MDU-PHL/meningotype)  
    Kwong JC, Gonçalves da Silva A, Stinear TP, Howden BP, & Seemann T [meningotype: in silico typing for _Neisseria meningitidis_.](https://github.com/MDU-PHL/meningotype) (GitHub)
  
- [Mykrobe](https://github.com/Mykrobe-tools/mykrobe)  
    Hunt M, Bradley P, Lapierre SG, Heys S, Thomsit M, Hall MB, Malone KM, Wintringer P, Walker TM, Cirillo DM, Comas I, Farhat MR, Fowler P, Gardy J, Ismail N, Kohl TA, Mathys V, Merker M, Niemann S, Omar SV, Sintchenko V, Smith G, Supply P, Tahseen S, Wilcox M, Arandjelovic I, Peto TEA, Crook, DW, Iqbal Z [Antibiotic resistance prediction for Mycobacterium tuberculosis from genome sequence data with Mykrobe](https://doi.org/10.12688/wellcomeopenres.15603.1) _Wellcome Open Research_ 4, 191. (2019)
  
- [ngmaster](https://github.com/MDU-PHL/ngmaster)  
    Kwong J, Gonçalves da Silva A, Schultz M, Seeman T [ngmaster - _In silico_ multi-antigen sequence typing for _Neisseria gonorrhoeae_ (NG-MAST)](https://github.com/MDU-PHL/ngmaster) (GitHub)
  
- [pasty](https://github.com/rpetit3/pasty)  
    Petit III RA [pasty: in silico serogrouping of _Pseudomonas aeruginosa_ isolates](https://github.com/rpetit3/pasty) (GitHub)
  
- [pbptyper](https://github.com/rpetit3/pbptyper)  
    Petit III RA [pbptyper: In silico Penicillin Binding Protein (PBP) typer for _Streptococcus pneumoniae_ assemblies](https://github.com/rpetit3/pbptyper) (GitHub)
  
- [SeqSero2](https://github.com/denglab/SeqSero2)  
    Zhang S, Den-Bakker HC, Li S, Dinsmore BA, Lane C, Lauer AC, Fields PI, Deng X. [SeqSero2: rapid and improved Salmonella serotype determination using whole genome sequencing data.](https://doi.org/10.1128/AEM.01746-19) _Appl Environ Microbiology_ 85(23):e01746-19 (2019)
  
- [ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper)  
    Wu Y, Lau HK, Lee T, Lau DK, Payne J [In Silico Serotyping Based on Whole-Genome Sequencing Improves the Accuracy of Shigella Identification.](https://doi.org/10.1128/AEM.00165-19) *Applied and Environmental Microbiology*, 85(7). (2019)
  
- [ShigEiFinder](https://github.com/LanLab/ShigEiFinder)  
    Zhang X, Payne M, Nguyen T, Kaur S, Lan R [Cluster-specific gene markers enhance Shigella and enteroinvasive Escherichia coli in silico serotyping.](https://doi.org/10.1099/mgen.0.000704) Microbial Genomics, 7(12). (2021)
  
- [SISTR](https://github.com/phac-nml/sistr_cmd)  
    Yoshida CE, Kruczkiewicz P, Laing CR, Lingohr EJ, Gannon VPJ, Nash JHE, Taboada EN [The Salmonella In Silico Typing Resource (SISTR): An Open Web-Accessible Tool for Rapidly Typing and Subtyping Draft Salmonella Genome Assemblies.](https://doi.org/10.1371/journal.pone.0147101) _PloS One_, 11(1), e0147101. (2016)
  
- [spaTyper](https://github.com/HCGB-IGTP/spaTyper)  
    Sanchez-Herrero JF, and Sullivan M [spaTyper: Staphylococcal protein A (spa) characterization pipeline](http://doi.org/10.5281/zenodo.4063625). Zenodo. (2020)
  
- [SsuisSero](https://github.com/jimmyliu1326/SsuisSero)  
    Lui J [SsuisSero: Rapid _Streptococcus suis_ serotyping](https://github.com/jimmyliu1326/SsuisSero) (GitHub)
  
- [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec)  
    Petit III RA, Read TD [_Staphylococcus aureus_ viewed from the perspective of 40,000+ genomes.](http://dx.doi.org/10.7717/peerj.5261) _PeerJ_ 6, e5261 (2018)
  
- [TBProfiler](https://github.com/jodyphelan/TBProfiler)  
    Phelan JE, O’Sullivan DM, Machado D, Ramos J, Oppong YEA, Campino S, O’Grady J, McNerney R, Hibberd ML, Viveiros M, Huggett JF, Clark TG [Integrating informatics tools and portable sequencing technology for rapid detection of resistance to anti-tuberculous drugs.](https://doi.org/10.1186/s13073-019-0650-x) _Genome Med_ 11, 41 (2019)
  


## Additional Parameters


### <i class="fa-xl fa-solid fa-gears"></i> Optional 
These optional parameters can be useful in certain settings.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-folder"></i>` --outdir` | Base directory to write results to <br/>**Type:** `string`, **Default:** `bactopia` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_compression` | Ouput files will not be compressed <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-folder"></i>` --datasets` | The path to cache datasets to <br/>**Type:** `string` |
| <i class="fa-lg fas fa-trash-restore"></i>` --keep_all_files` | Keeps all analysis files created <br/>**Type:** `boolean` |

### <i class="fa-xl fa-solid fa-arrow-up-right-dots"></i> Max Job Request 
Set the top limit for requested resources for any single job.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-redo"></i>` --max_retry` | Maximum times to retry a process before allowing it to fail. <br/>**Type:** `integer`, **Default:** `3` |
| <i class="fa-lg fas fa-microchip"></i>` --max_cpus` | Maximum number of CPUs that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `4` |
| <i class="fa-lg fas fa-memory"></i>` --max_memory` | Maximum amount of memory (in GB) that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `32` |
| <i class="fa-lg far fa-clock"></i>` --max_time` | Maximum amount of time (in minutes) that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `120` |
| <i class="fa-lg fas fa-angle-double-up"></i>` --max_downloads` | Maximum number of samples to download at a time <br/>**Type:** `integer`, **Default:** `3` |

### <i class="fa-xl fa-solid fa-screwdriver-wrench"></i> Nextflow Configuration 
 to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-cog"></i>` --nfconfig` | A Nextflow compatible config file for custom profiles, loaded last and will overwrite existing variables if set. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-copy"></i>` --publish_dir_mode` | Method used to save pipeline results to output directory. <br/>**Type:** `string`, **Default:** `copy` |
| <i class="fa-lg fas fa-cogs"></i>` --infodir` | Directory to keep pipeline Nextflow logs and reports. <br/>**Type:** `string`, **Default:** `${params.outdir}/pipeline_info` |
| <i class="fa-lg fas fa-recycle"></i>` --force` | Nextflow will overwrite existing output files. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-trash-alt"></i>` --cleanup_workdir` | After Bactopia is successfully executed, the `work` directory will be deleted. <br/>**Type:** `boolean` |

### <i class="fa-xl fas fa-university"></i> Institutional config options
 used to describe centralized config profiles. These should not be edited.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-users-cog"></i>` --custom_config_version` | Git commit id for Institutional configs. <br/>**Type:** `string`, **Default:** `master` |
| <i class="fa-lg fas fa-users-cog"></i>` --custom_config_base` | Base directory for Institutional configs. <br/>**Type:** `string`, **Default:** `https://raw.githubusercontent.com/nf-core/configs/master` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_name` | Institutional config name. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_description` | Institutional config description. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_contact` | Institutional config contact information. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-users-cog"></i>` --config_profile_url` | Institutional config URL link. <br/>**Type:** `string` |

### <i class="fa-xl fa-regular fa-address-card"></i> Nextflow Profile 
 to fine-tune your Nextflow setup.

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

### <i class="fa-xl fa-solid fa-reply-all"></i> Helpful 
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