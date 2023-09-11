---
title: Tutorial
description: >-
    A tutorial to get started with Bactopia using publicly available genomes.
---
For this tutorial, we walk through processing *S. aureus* samples associated with cystic
fibrosis lung infections. These samples are from the publication just below, and are
available from BioProject accession [PRJNA480016](https://www.ebi.ac.uk/ena/data/view/PRJNA480016).

* *Bernardy, Eryn E., et al. ["Whole-Genome Sequences of Staphylococcus aureus Isolates from Cystic Fibrosis Lung Infections."](https://doi.org/10.1128/MRA.01564-18) Microbiol Resour Announc 8.3 (2019): e01564-18.*

The goal of the tutorial is to:

* [ ] Verify Bactopia is working
* [ ] Use Bactopia to process:
    * [ ] Single sample from SRA/ENA
    * [ ] Multiple samples from SRA/ENA
    * [ ] Single local sample
    * [ ] Multiple local samples
    * [ ] Aggregate results from multiple samples
* [ ] Use Bactopia Tools to:
    * [ ] Run *S. aureus* specific analyses
    * [ ] Generate a tree using [Mashtree](bactopia-tools/mashtree.md)

Upon completion of this tutorial, you should be ready to process your own data using Bactopia!

!!! warning "Bactopia Should Be Installed"
    This tutorial assumes you have already installed Bactopia. If you have not, please check
    out how to at [Installation](installation.md).

!!! warning "Reach out if you have trouble with this tutorial"
    I try my best to make sure everything is working as expected, but understand that
    is not always the case. If you run into any issues with this tutorial, please let me
    know by submitting a [GitHub Issue](https://github.com/bactopia/bactopia/issues/new/choose).
    Hopefully, together we'll be able to figure out what is happening.

OK! Let's get this tutorial started!

## Selecting a Profile

Because Bactopia is written in Nextflow, it can be executed on many different environments.
For the purposes of this tutorial, we will be using the default profile, which will use Conda
environments to run the tools. However, if you are on a system with Singularity or Docker,
those are recommended over Conda environments.

If you want to use Docker, you would simply add `-profile docker` to the commands below.
Similarly, if you want to use Singularity, you would add `-profile singularity`.

??? info "Profiles can be extended to other systems (e.g. HPC and cloud)"
    Nextflow has built in support for numerous systems. If you are interested in using Bactopia
    on a system other than your local machine, please check out the
    [Nextflow Executors](https://www.nextflow.io/docs/latest/executor.html). Setting up a
    custom profile for this tutorial, is outside its scope, but if you are interested in doing
    so, feel free to reach out.

## Verify Bactopia is Working

Before we get started, we'll use the built in `test` profile to verify Bactopia is working
for you. This `test` profile will download a very small bacterial genome (~350kb genome size),
which will allow you to quickly test Bactopia.

To run the test, simply run the following command:

```{bash}
bactopia -profile test
```

??? info "Example commands to use Docker or Singularity"
    If you are using Docker, you would run the following command:
    ```{bash}
    bactopia -profile test,docker
    ```
    
    If you are using Singularity, you would run the following command:
    ```{bash}
    bactopia -profile test,singularity
    ```

!!! note "The first run might take a while"
    The first time you run Bactopia it will build the environments (Conda, Docker, or Singularity)
    needed for analysis. Depending on your internet connection this might take a little while.
    I recommend grabbing a coffee or going for a walk. This is only a one time build, future
    runs will be much faster.

Upon completion, you will hopefully be met with text like the following:

```{bash}
    Bactopia Execution Summary
    ---------------------------
    Bactopia Version : 3.0.0
    Nextflow Version : 23.04.1
    Command Line     : nextflow run /path/to/bactopia/main.nf -w /path/to/work/ -profile test
    Resumed          : false
    Completed At     : 2023-09-06T00:21:32.209500355Z
    Duration         : 4m 36s
    Success          : true
    Exit Code        : 0
    Error Report     : -
    Launch Dir       : /path/to/tutorial

Completed at: 06-Sep-2023 00:21:33
Duration    : 4m 36s
CPU hours   : 0.2
Succeeded   : 13
```

If you see similar text, you are ready to continue!

* [x] Verify Bactopia is working

## Samples on SRA/ENA

OK! We're ready to get started processing some bacterial genomes using Bactopia. For this section
we'll process genomes publicly available from the Sequence Read Archive (SRA) and 
European Nucleotide Archive (ENA).

### Single Sample

Let's start this by downloading a single sample from the [Sequence Read Archive](https://www.ncbi.nlm.nih.gov/sra)
(SRA), and processing it through Bactopia. To do this, you can use the `bactopia` command with
the `--accession` parameter, like the following command:

```{bash}
bactopia \
    --accession SRX4563634 \
    --coverage 100 \
    --genome_size 2800000 \
    --max_cpus 2 \
    --outdir ena-single-sample
```

Once you press enter, sit back, relax and watch the Nextflow give realtime updates for
SRX4563634's analysis! This analysis will have an **approximate completion time of ~15-30 minutes**,
depending on the number of cpus given and download times from ENA. While that is running,
we can go over a few of the parameters used in the command.

Here are the parameters used in the command:

| Parameter | Description |
| --------- | ----------- |
| `--accession` | The SRA Experiment accession to download and process. |
| `--coverage` | The estimated coverage to limit the FASTQs to. |
| `--genome_size` | The estimated genome size. |
| `--max_cpus` | The maximum number of cpus to use. |
| `--outdir` | The directory to store the results. |

In summary, we've told Bactopia to download the FASTQs associated with Experiment accession
SRX4563634 (`--accession SRX4563634`), limit the cleaned up FASTQ file to an estimated 100x coverage
(`--coverage 100`) based on the genome size of 2,800,000bp (`--genome_size 2800000`), to only
use 2 cpus per process (`--max_cpus 2`), and finally, write the outputs to the `ena-single-sample`
directory (`--outdir ena-single-sample`).

__*Some time later...*__

After some time, (_15 minutes on my end_), you will have results available to you
in `ena-single-sample/SRX4563634/`. Each of these outputs files are documented in detail
in the __*Workflow Steps*__ section of the documentation. Starting with the
[Gather Step](bactopia/gather.md)

??? info "Expected logging information"
    Nextflow will produce logging information explaining what is happening during the
    analysis. Here is example logging text you should see:
    ```{bash}
    executor >  local (13)
    [skipped  ] process > BACTOPIA:DATASETS                                               [100%] 1 of 1, stored: 1 ✔
    [08/0e0374] process > BACTOPIA:GATHER:GATHER_MODULE (SRX4563634)                      [100%] 1 of 1 ✔
    [dc/2efa12] process > BACTOPIA:GATHER:CSVTK_CONCAT (meta)                             [100%] 1 of 1 ✔
    [ec/f045fb] process > BACTOPIA:QC:QC_MODULE (SRX4563634)                              [100%] 1 of 1 ✔
    [3b/ec192d] process > BACTOPIA:ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)                [100%] 1 of 1 ✔
    [9f/f4db15] process > BACTOPIA:ASSEMBLER:CSVTK_CONCAT (assembly-scan)                 [100%] 1 of 1 ✔
    [84/131342] process > BACTOPIA:SKETCHER:SKETCHER_MODULE (SRX4563634)                  [100%] 1 of 1 ✔
    [12/b266ba] process > BACTOPIA:ANNOTATOR:PROKKA_MODULE (SRX4563634)                   [100%] 1 of 1 ✔
    [d5/7183c8] process > BACTOPIA:AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634)           [100%] 1 of 1 ✔
    [1c/cdac50] process > BACTOPIA:AMRFINDERPLUS:GENES_CONCAT (amrfinderplus-genes)       [100%] 1 of 1 ✔
    [47/e35d5b] process > BACTOPIA:AMRFINDERPLUS:PROTEINS_CONCAT (amrfinderplus-proteins) [100%] 1 of 1 ✔
    [29/28a819] process > BACTOPIA:MLST:MLST_MODULE (SRX4563634)                          [100%] 1 of 1 ✔
    [20/8d35e9] process > BACTOPIA:MLST:CSVTK_CONCAT (mlst)                               [100%] 1 of 1 ✔
    [e8/17f49c] process > BACTOPIA:DUMPSOFTWAREVERSIONS (1)                               [100%] 1 of 1 ✔

        Bactopia Execution Summary
        ---------------------------
        Bactopia Version : 3.0.0
        Nextflow Version : 23.04.1
        Command Line     : nextflow run /path/to/main.nf -w /path/to/work/ --accession SRX4563634 --coverage 100 --genome_size 2800000 --outdir ena-single-sample --max_cpus 2
        Resumed          : false
        Completed At     : 2023-09-06T00:50:51.995313157Z
        Duration         : 15m 7s
        Success          : true
        Exit Code        : 0
        Error Report     : -
        Launch Dir       : /path/to/tutorial
    ```

??? info "Expected output directory structure"
    After your Bactopia run has completed you should have a directory structure that looks
    like the following:
    ```{bash}
    ena-single-sample/
    ├── SRX4563634
    │   ├── main
    │   │   ├── annotator
    │   │   │   └── prokka
    │   │   │       └── logs
    │   │   ├── assembler
    │   │   │   └── logs
    │   │   ├── gather
    │   │   │   └── logs
    │   │   ├── qc
    │   │   │   ├── extra
    │   │   │   ├── logs
    │   │   │   └── summary
    │   │   └── sketcher
    │   │       └── logs
    │   └── tools
    │       ├── amrfinderplus
    │       │   └── logs
    │       └── mlst
    │           └── logs
    └── bactopia-runs
        └── bactopia-20230906-003544
            ├── merged-results
            │   └── logs
            │       ├── amrfinderplus-genes-concat
            │       ├── amrfinderplus-proteins-concat
            │       ├── assembly-scan-concat
            │       ├── meta-concat
            │       └── mlst-concat
            ├── nf-reports
            └── software-versions
                └── logs
    ```

* [x] Use Bactopia to process:
    * [x] Single sample from SRA/ENA

### Multiple Samples

Processing one sample is nice, but [PRJNA480016](https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA480016),
the study we're using for this tutorial has 66 samples. Don't worry, we won't be processing all
66 samples, but you can imagine almost every study will have more than one sample. Bactopia
allows you to process as many samples as you want, and it's pretty easy to do so.

For this tutorial, we are going to process 5 samples from [PRJNA480016](https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA480016).
To do this, we'll make use of the `bactopia search` command. This command allows you to search
for samples on SRA/ENA and generate a list of accessions for processing with Bactopia.

!!! tip "Check out the Beginner's Guide for more information on `bactopia search`"
    For now, we are just going to use `bactopia search` without much details on how it works.
    You use `bactopia search` for some fun things, to learn more about it, check out
    [Beginner's Guide -> Accessions](beginners-guide.md#accessions).

Let's go ahead and give `bactopia search` a try:

```{bash}
bactopia search \
    --query PRJNA480016 \
    --limit 5
```

This command will produce 4 files:

| Filename                  | Description                                                                    |
|---------------------------|--------------------------------------------------------------------------------|
| `bactopia-metadata.txt`   | A tab-delimited file of all results from the query                              |
| `bactopia-accessions.txt` | A list of Experiment accessions to be processed                                |
| `bactopia-filtered.txt`   | A list of any Experiment accessions that were filtered out, otherwise an empty |
| `bactopia-search.txt`     | A summary of the completed request                                             |

For this tutorial, `bactopia-accessions.txt` is the file we need. It contains five Experiment
accessions, a single one per line. Similar to this:

```{bash}
accession       runtype species genome_size
SRX4563690      illumina        Staphylococcus aureus   2800000
SRX4563681      illumina        Staphylococcus aureus   2800000
SRX4563689      illumina        Staphylococcus aureus   2800000
SRX4563687      illumina        Staphylococcus aureus   2800000
SRX4563682      illumina        Staphylococcus aureus   2800000
```

__*Note: you may have 5 different accessions from the PRJNA480016 project.*__

Before we use this file, let's explain what it contains. 

| Column | Description |
| ------ | ----------- |
| `accession`   | The Experiment accession to be downloaded                            |
| `runtype`     | Informs Bactopia how to process the data (e.g. Illumina or Nanopore) |
| `species`     | The species associated with the Experiment accession                 |
| `genome_size` | The expected genome size of the species pulled from NCBI             |


Now here comes the fun part! We don't need to run Bactopia 5 times for each accession,
instead we can pass the `bactopia-accession.txt` to Bactopia using the `--accessions`
parameter. Let's give it a try:

```{bash}
bactopia \
    --accessions bactopia-accessions.txt \
    --coverage 100 \
    --outdir ena-multiple-samples \
    --max_cpus 2
```

Instead of `--accession` we are now using `--accessions` which tells Bactopia to read the
provided file, in our case `bactopia-accessions.txt`, and download each Experiment accession
from SRA/ENA and then process them all at once.

!!! tip "Go take a break, this will be a little while"
    At this point, you might want to go for a walk or make yourself a coffee! This step has
    an **approximate completion time of ~15-120 minutes**. Again the total time will depend
    on your system and internet connection.

Once this is complete, the results for all five samples will be found in the
`ena-multiple-samples` directory. Each sample will have there own folder of results.

??? info "Expected logging information"
    Nextflow will produce logging information explaining what is happening during the
    analysis. Here is example logging text you should see:
    ```{bash}
    executor >  local (41)
    [skipped  ] process > BACTOPIA:DATASETS                                               [100%] 1 of 1, stored: 1 ✔
    [be/2db067] process > BACTOPIA:GATHER:GATHER_MODULE (SRX4563682)                      [100%] 5 of 5 ✔
    [ea/e3dba2] process > BACTOPIA:GATHER:CSVTK_CONCAT (meta)                             [100%] 1 of 1 ✔
    [e8/9b6c36] process > BACTOPIA:QC:QC_MODULE (SRX4563682)                              [100%] 5 of 5 ✔
    [43/07a775] process > BACTOPIA:ASSEMBLER:ASSEMBLER_MODULE (SRX4563682)                [100%] 5 of 5 ✔
    [81/ac44db] process > BACTOPIA:ASSEMBLER:CSVTK_CONCAT (assembly-scan)                 [100%] 1 of 1 ✔
    [97/0f8d92] process > BACTOPIA:SKETCHER:SKETCHER_MODULE (SRX4563682)                  [100%] 5 of 5 ✔
    [0a/498254] process > BACTOPIA:ANNOTATOR:PROKKA_MODULE (SRX4563682)                   [100%] 5 of 5 ✔
    [4a/a75b58] process > BACTOPIA:AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563682)           [100%] 5 of 5 ✔
    [b0/23c407] process > BACTOPIA:AMRFINDERPLUS:GENES_CONCAT (amrfinderplus-genes)       [100%] 1 of 1 ✔
    [ad/45dd2f] process > BACTOPIA:AMRFINDERPLUS:PROTEINS_CONCAT (amrfinderplus-proteins) [100%] 1 of 1 ✔
    [80/1b2e1e] process > BACTOPIA:MLST:MLST_MODULE (SRX4563682)                          [100%] 5 of 5 ✔
    [e3/72a4c9] process > BACTOPIA:MLST:CSVTK_CONCAT (mlst)                               [100%] 1 of 1 ✔
    [c7/e909dc] process > BACTOPIA:DUMPSOFTWAREVERSIONS (1)                               [100%] 1 of 1 ✔

        Bactopia Execution Summary
        ---------------------------
        Bactopia Version : 3.0.0
        Nextflow Version : 23.04.1
        Command Line     : nextflow run /path/to/main.nf -w /path/to/work/ --accessions bactopia-accessions.txt --coverage 100 --outdir ena-multiple-samples --max_cpus 2
        Resumed          : false
        Completed At     : 2023-09-06T01:53:40.466149409Z
        Duration         : 16m 12s
        Success          : true
        Exit Code        : 0
        Error Report     : -
        Launch Dir       : /path/to/tutorial
    ```

* [x] Use Bactopia to process:
    * [x] Single sample from SRA/ENA
    * [x] Multiple samples from SRA/ENA

Congratulations! At this point, you should have been able to use Bactopia to process multiple
publicly available genomes from SRA/ENA. Now let's move on to processing some local samples!

## Local Samples

For this, tutorial I thought about having a dataset for you to download, but we already
downloaded some samples! Instead, let's recycle some of the samples we downloaded from SRA/ENA.

First let's make a directory to put the FASTQs into:

```{bash}
mkdir fastqs
```

Now let's move some the FASTQs from our SRX4563634 sample into this folder.

```{bash}
cp ./ena-single-sample/SRX4563634/main/qc/SRX4563634*.fastq.gz fastqs
```

Finally let's also make a single-end version of SRX4563634.

```{bash}
cat fastqs/SRX4563634_R1.fastq.gz fastqs/SRX4563634_R2.fastq.gz > fastqs/SRX4563634-SE.fastq.gz
```

This should give use three local FASTQs to work with:

```{bash}
ls fastqs/
SRX4563634-SE.fastq.gz  SRX4563634_R1.fastq.gz  SRX4563634_R2.fastq.gz
```

With everything in place, let's get started processing some local samples!

* [ ] Use Bactopia to process:
    * [ ] Single local sample
    * [ ] Multiple local samples

### Single Sample

First, we'll process a single sample. This will be very similar to the single sample from
SRA/ENA above, with a few slight modifications. To process a single sample you can use the
`--r1`/`--r2` (paired-end), `--se` (single-end), and `--sample` parameters.

!!! tip "Learn more from the Beginner's Guide"
    To learn more about these parameters, check out the
    [Beginner's Guide -> Single Sample](beginners/#single-sample) section. Each of these
    parameters are described in detail.

#### Paired-End

For paired-end reads we'll be u will want to use `--R1`, `--R2`, and `--sample`. For this paired-end example we'll use SRX4563634 again which we've copied to the `fastqs` folder.

```{bash}
bactopia \
    --r1 fastqs/SRX4563634_R1.fastq.gz \
    --r2 fastqs/SRX4563634_R2.fastq.gz \
    --sample SRX4563634 \
    --coverage 100 \
    --genome_size 2800000 \
    --outdir local-single-sample \
    --max_cpus 2
```

In the command above, we used `--r1` and `--r2` parameters to inform Bactopia to process the
input reads as paired-end Illumina reads. The `--sample` parameter is used to name the output
files. Similar to before, we've also provided the `--coverage`, `--genome_size`, and `--max_cpus`
parameters.

By now you are probably getting the hang of this. Just like the previous  to the single SRA/ENA
sample, we can expect this to take **approximately ~15-30 minutes to complete**, so consider
taking a break.

Once complete, results can be found in `local-single-sample/`.

??? info "Expected logging information"
    Nextflow will produce logging information explaining what is happening during the
    analysis. Here is example logging text you should see:
    
    ```{bash}
    executor >  local (13)
    [skipped  ] process > BACTOPIA:DATASETS                                               [100%] 1 of 1, stored: 1 ✔
    [0b/addada] process > BACTOPIA:GATHER:GATHER_MODULE (SRX4563634)                      [100%] 1 of 1 ✔
    [e6/2528f0] process > BACTOPIA:GATHER:CSVTK_CONCAT (meta)                             [100%] 1 of 1 ✔
    [22/bc27bd] process > BACTOPIA:QC:QC_MODULE (SRX4563634)                              [100%] 1 of 1 ✔
    [ca/4d5c44] process > BACTOPIA:ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)                [100%] 1 of 1 ✔
    [b0/732cc7] process > BACTOPIA:ASSEMBLER:CSVTK_CONCAT (assembly-scan)                 [100%] 1 of 1 ✔
    [05/56cb35] process > BACTOPIA:SKETCHER:SKETCHER_MODULE (SRX4563634)                  [100%] 1 of 1 ✔
    [91/312af4] process > BACTOPIA:ANNOTATOR:PROKKA_MODULE (SRX4563634)                   [100%] 1 of 1 ✔
    [fa/515a6c] process > BACTOPIA:AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634)           [100%] 1 of 1 ✔
    [d5/0d9535] process > BACTOPIA:AMRFINDERPLUS:GENES_CONCAT (amrfinderplus-genes)       [100%] 1 of 1 ✔
    [0c/9b80f4] process > BACTOPIA:AMRFINDERPLUS:PROTEINS_CONCAT (amrfinderplus-proteins) [100%] 1 of 1 ✔
    [aa/d955da] process > BACTOPIA:MLST:MLST_MODULE (SRX4563634)                          [100%] 1 of 1 ✔
    [ea/84b6c9] process > BACTOPIA:MLST:CSVTK_CONCAT (mlst)                               [100%] 1 of 1 ✔
    [0c/7fccf1] process > BACTOPIA:DUMPSOFTWAREVERSIONS (1)                               [100%] 1 of 1 ✔

        Bactopia Execution Summary
        ---------------------------
        Bactopia Version : 3.0.0
        Nextflow Version : 23.04.1
        Command Line     : nextflow run /path/to/main.nf -w /path/to/work/ --r1 fastqs/SRX4563634_R1.fastq.gz --r2 fastqs/SRX4563634_R2.fastq.gz --sample SRX4563634 --coverage 100 --genome_size 2800000 --outdir local-single-sample --max_cpus 2
        Resumed          : false
        Completed At     : 2023-09-06T02:50:28.928305768Z
        Duration         : 7m 38s
        Success          : true
        Exit Code        : 0
        Error Report     : -
        Launch Dir       : /path/to/tutorial
    ```

#### Single-End

Now, you might be wondering _"single-end"_? Even though in modern Illumina runs, we'll
rarely run into single-end reads, they do exist. There are many early single-end Illumina
samples available from SRA/ENA. Due this, single-end support was built into Bactopia.

It's a simple change, to analyze single-end reads, instead of `--r1` and `--r2` we'll be
using `--se`. Let's give it a try using the `SRX4563634-SE.fastq.gz` file we created earlier`:

```{bash}
bactopia \
    --se fastqs/SRX4563634-SE.fastq.gz \
    --sample SRX4563634-SE \
    --coverage 100 \
    --genome_size 2800000 \
    --outdir local-single-sample \
    --max_cpus 2
```

With the command above, SRX4563634-SE will be processed as a single-end sample. For single-end
processing there are some paired-end only analyses (e.g. error correction) that will be skipped.
For the most part though, paried-end and single-end reads undergo the same analyses.

It's about the time for another break! This run will take **approximately ~15-30 minutes to complete**.

Once complete, your single-end results will be available in `local-single-sample`.

??? info "Expected logging information"
    Nextflow will produce logging information explaining what is happening during the
    analysis. Here is example logging text you should see:
    
    ```{bash}
    executor >  local (13)
    [skipped  ] process > BACTOPIA:DATASETS                                               [100%] 1 of 1, stored: 1 ✔
    [15/42dd1d] process > BACTOPIA:GATHER:GATHER_MODULE (SRX4563634-SE)                   [100%] 1 of 1 ✔
    [a4/37cac4] process > BACTOPIA:GATHER:CSVTK_CONCAT (meta)                             [100%] 1 of 1 ✔
    [1b/50f36f] process > BACTOPIA:QC:QC_MODULE (SRX4563634-SE)                           [100%] 1 of 1 ✔
    [fb/646763] process > BACTOPIA:ASSEMBLER:ASSEMBLER_MODULE (SRX4563634-SE)             [100%] 1 of 1 ✔
    [e8/4a3315] process > BACTOPIA:ASSEMBLER:CSVTK_CONCAT (assembly-scan)                 [100%] 1 of 1 ✔
    [b8/aac864] process > BACTOPIA:SKETCHER:SKETCHER_MODULE (SRX4563634-SE)               [100%] 1 of 1 ✔
    [3c/81380b] process > BACTOPIA:ANNOTATOR:PROKKA_MODULE (SRX4563634-SE)                [100%] 1 of 1 ✔
    [9b/7b9582] process > BACTOPIA:AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634-SE)        [100%] 1 of 1 ✔
    [4a/f2ad21] process > BACTOPIA:AMRFINDERPLUS:GENES_CONCAT (amrfinderplus-genes)       [100%] 1 of 1 ✔
    [b7/0b4b24] process > BACTOPIA:AMRFINDERPLUS:PROTEINS_CONCAT (amrfinderplus-proteins) [100%] 1 of 1 ✔
    [85/4ab00c] process > BACTOPIA:MLST:MLST_MODULE (SRX4563634-SE)                       [100%] 1 of 1 ✔
    [f4/002f5e] process > BACTOPIA:MLST:CSVTK_CONCAT (mlst)                               [100%] 1 of 1 ✔
    [03/ba2407] process > BACTOPIA:DUMPSOFTWAREVERSIONS (1)                               [100%] 1 of 1 ✔

        Bactopia Execution Summary
        ---------------------------
        Bactopia Version : 3.0.0
        Nextflow Version : 23.04.1
        Command Line     : nextflow run /path/to/main.nf -w /home/robert_petit/temp/bactopia3/tutorial/work/ --se fastqs/SRX4563634-SE.fastq.gz --sample SRX4563634-SE --coverage 100 --genome_size 2800000 --outdir local-single-sample --max_cpus 2
        Resumed          : false
        Completed At     : 2023-09-06T03:17:08.633994540Z
        Duration         : 10m 14s
        Success          : true
        Exit Code        : 0
        Error Report     : -
        Launch Dir       : /path/to/tutorial
    ```

If you made it this far, you're almost done!

* [x] Use Bactopia to process:
    * [x] Single local sample

### Multiple Samples (FOFN)

Here we go! Let's take all these samples we have and process them all at once! To do this,
Bactopia allows you to give a text file describing the input samples. This file of file names
(FOFN), contains sample names and location to associated FASTQs.

As you might have guessed, you don't need to create these FOFNs by hand, Bactopia can do it.
In this section we'll explore how we can use the `bactopia prepare` command to generate the
FOFN we need to process multiple samples.

!!! tip "Learn more from the Beginner's Guide"
    To learn more about these parameters, check out the
    [Beginner's Guide -> Local Samples](beginners/#local-samples) section. Each of these
    parameters are described in detail.

Let's recycle some more FASTQ files. Before we proceed lets move some more FASTQs into our
`fastqs` folder. For this we'll use the FASTQs from `ena-multiple-samples`. Let's copy them
over:

```{bash}
find ena-multiple-samples/ -name *.fastq.gz | \
    xargs -I {} cp {} fastqs/
```

We should how have FASTQs for 7 samples in our `fastqs` folder. With these let's generate
a FOFN using `bactopia prepare`:

```{bash}
bactopia prepare --path fastqs/
sample  runtype genome_size     species r1      r2      extra
SRX4563634      paired-end      0       UNKNOWN_SPECIES /path/to/fastqs/SRX4563634_R1.fastq.gz        /path/to/fastqs/SRX4563634_R2.fastq.gz
SRX4563634-SE   single-end      0       UNKNOWN_SPECIES /path/to/fastqs/SRX4563634-SE.fastq.gz
SRX4563681      paired-end      0       UNKNOWN_SPECIES /path/to/fastqs/SRX4563681_R1.fastq.gz        /path/to/fastqs/SRX4563681_R2.fastq.gz
SRX4563682      paired-end      0       UNKNOWN_SPECIES /path/to/fastqs/SRX4563682_R1.fastq.gz        /path/to/fastqs/SRX4563682_R2.fastq.gz
SRX4563687      paired-end      0       UNKNOWN_SPECIES /path/to/fastqs/SRX4563687_R1.fastq.gz        /path/to/fastqs/SRX4563687_R2.fastq.gz
SRX4563689      paired-end      0       UNKNOWN_SPECIES /path/to/fastqs/SRX4563689_R1.fastq.gz        /path/to/fastqs/SRX4563689_R2.fastq.gz
SRX4563690      paired-end      0       UNKNOWN_SPECIES /path/to/fastqs/SRX4563690_R1.fastq.gz        /path/to/fastqs/SRX4563690_R2.fastq.gz
```

This command will try to create a FOFN for you. For this turorial, the FASTQ names are pretty straight forward and should produce a correct FOFN (or at least it should! ... hopefully!). If that wasn't the case for you, there are ways to [tweak `bactopia prepare`](beginners-guide.md#bactopia-prepare).

Wait! We for got something, in the output above we have `0` for `genome_size` and
`UNKNOWN_SPECIES` for `species`. We can fix this by using the `--species` and `--genome-size`
options, let's try again:

```{bash}
bactopia prepare \
    --path fastqs/ \
    --species "Staphylococcus aureus" \
    --genome-size 2800000
sample  runtype genome_size     species r1      r2      extra
SRX4563634      paired-end      2800000 Staphylococcus aureus   /path/to/fastqs/SRX4563634_R1.fastq.gz        /path/to/fastqs/SRX4563634_R2.fastq.gz
SRX4563634-SE   single-end      2800000 Staphylococcus aureus   /path/to/fastqs/SRX4563634-SE.fastq.gz
SRX4563681      paired-end      2800000 Staphylococcus aureus   /path/to/fastqs/SRX4563681_R1.fastq.gz        /path/to/fastqs/SRX4563681_R2.fastq.gz
SRX4563682      paired-end      2800000 Staphylococcus aureus   /path/to/fastqs/SRX4563682_R1.fastq.gz        /path/to/fastqs/SRX4563682_R2.fastq.gz
SRX4563687      paired-end      2800000 Staphylococcus aureus   /path/to/fastqs/SRX4563687_R1.fastq.gz        /path/to/fastqs/SRX4563687_R2.fastq.gz
SRX4563689      paired-end      2800000 Staphylococcus aureus   /path/to/fastqs/SRX4563689_R1.fastq.gz        /path/to/fastqs/SRX4563689_R2.fastq.gz
SRX4563690      paired-end      2800000 Staphylococcus aureus   /path/to/fastqs/SRX4563690_R1.fastq.gz        /path/to/fastqs/SRX4563690_R2.fastq.gz
```

Much better! By adding the genome size, Bactopia can now reduce the total coverage to the
value provided by `--coverage`.

However, we need to write this to a file to use it. Let's do that now:

```{bash}
bactopia prepare \
    --path fastqs/ \
    --species "Staphylococcus aureus" \
    --genome-size 2800000 \
    > samples.txt
```

There we go! We now have everything we need to process all these samples using Bactopia. Now,
let's process these samples using the FOFN we just created.

```{bash}
bactopia \
    --samples samples.txt \
    --coverage 100 \
    --max_cpus 2 \
    --outdir local-multiple-samples
```

Instead of using `--r1`, `--r2`, `--se`, or `--sample`, we are instead using `--samples`.
The `--samples` parameter expects a FOFN generated by `bactopia prepare`, which it will then
use to setup analysis for each sample included.

Yep! You guessed it, time for another break! This step will take **approximatele ~15-120 minutes to complete**.
See you again soon!

__*Some time later...*__

Once this is complete, the results for each sample (within their own folder) will be found in the `local-multiple-samples` directory.

!!! tip "Using `--samples` is more CPU efficient, making it faster"
    The real benefit of using the FOFN method to process multiple samples is Nextflow's queue
    system will make better use of cpus. Processing multiple samples one at a time
    (via `--r1`/`--r2` or `--se`) will lead more instances of jobs waiting on other jobs
    to finish, during which cpus aren't being used.

??? info "Expected logging information"
    Nextflow will produce logging information explaining what is happening during the
    analysis. Here is example logging text you should see:
    
    ```{bash}
    [skipped  ] process > BACTOPIA:DATASETS                                               [100%] 1 of 1, stored: 1 ✔
    [9e/f962fc] process > BACTOPIA:GATHER:GATHER_MODULE (SRX4563689)                      [100%] 7 of 7 ✔
    [55/7512ca] process > BACTOPIA:GATHER:CSVTK_CONCAT (meta)                             [100%] 1 of 1 ✔
    [fd/8e5dbd] process > BACTOPIA:QC:QC_MODULE (SRX4563690)                              [100%] 7 of 7 ✔
    [29/5235d0] process > BACTOPIA:ASSEMBLER:ASSEMBLER_MODULE (SRX4563690)                [100%] 7 of 7 ✔
    [5c/2ee7f8] process > BACTOPIA:ASSEMBLER:CSVTK_CONCAT (assembly-scan)                 [100%] 1 of 1 ✔
    [a4/9e6960] process > BACTOPIA:SKETCHER:SKETCHER_MODULE (SRX4563690)                  [100%] 7 of 7 ✔
    [35/569283] process > BACTOPIA:ANNOTATOR:PROKKA_MODULE (SRX4563690)                   [100%] 7 of 7 ✔
    [0f/9aadaa] process > BACTOPIA:AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563690)           [100%] 7 of 7 ✔
    [e8/0f2eb5] process > BACTOPIA:AMRFINDERPLUS:GENES_CONCAT (amrfinderplus-genes)       [100%] 1 of 1 ✔
    [f5/c26c46] process > BACTOPIA:AMRFINDERPLUS:PROTEINS_CONCAT (amrfinderplus-proteins) [100%] 1 of 1 ✔
    [1a/3c6d44] process > BACTOPIA:MLST:MLST_MODULE (SRX4563690)                          [100%] 7 of 7 ✔
    [9b/600e24] process > BACTOPIA:MLST:CSVTK_CONCAT (mlst)                               [100%] 1 of 1 ✔
    [7a/eeb047] process > BACTOPIA:DUMPSOFTWAREVERSIONS (1)                               [100%] 1 of 1 ✔

        Bactopia Execution Summary
        ---------------------------
        Bactopia Version : 3.0.0
        Nextflow Version : 23.04.1
        Command Line     : nextflow run /path/to/main.nf -w /path/to/work/ --samples samples.txt --coverage 100 --max_cpus 2 --outdir local-multiple-samples
        Resumed          : false
        Completed At     : 2023-09-06T03:47:15.580898057Z
        Duration         : 12m 47s
        Success          : true
        Exit Code        : 0
        Error Report     : -
        Launch Dir       : /path/to/tutorial
    ```

* [x] Use Bactopia to process:
    * [x] Single local sample
    * [x] Multiple local samples

### Bactopia Summary

Now that we've processed numerous samples, it might be nice to get a quick overview of your
samples. For example, which ones passed, what were the sequence types, how did they assemble,
etc... It would also be nice to get this all into a single file. This is where the
`bactopia summary` command comes in. This command will generate a tab-delimited file with
results from each of the steps in Bactopia.

Let's give it a try, then we'll walk through some of the details. For this we'll use the
`local-multiple-samples` directory.

```{bash}
bactopia summary \
    --bactopia-path local-multiple-samples/
```

Upon completion this will produce three files:

| File                   | Description |
| ---------------------- | ----------- |
| `bactopia-report.tsv`  | A tab-delimited file with more than 70 columns of results from steps in Bactopia. |
| `bactopia-exclude.tsv` | A tab-delimited file with samples that should **_likely_** be excluded from further analysis |
| `bactopia-summary.txt` | A simple summary of quality grades and excluded counts. |

??? abstract "Example: `bactopia-resport.tsv` _(Warning! Its wide!)_"
    Below is an example of the `bactopia-report.tsv` file. As you can see there are a ton of
    columns! These columns include lots of information and works quite well with Excel or R.
    
    ```{tsv}
    sample	rank	reason	genome_size	species	runtype	original_runtype	mlst_scheme	mlst_st	annotator_total_CDS	annotator_total_rRNA	annotator_total_tRNA	annotator_total_tmRNA	assembler_total_contig	assembler_total_contig_length	assembler_max_contig_length	assembler_mean_contig_length	assembler_median_contig_length	assembler_min_contig_length	assembler_n50_contig_length	assembler_l50_contig_count	assembler_num_contig_non_acgtn	assembler_contig_percent_a	assembler_contig_percent_c	assembler_contig_percent_g	assembler_contig_percent_t	assembler_contig_percent_n	assembler_contig_non_acgtn	assembler_contigs_greater_1m	assembler_contigs_greater_100k	assembler_contigs_greater_10k	assembler_contigs_greater_1k	assembler_percent_contigs_greater_1m	assembler_percent_contigs_greater_100k	assembler_percent_contigs_greater_10k	assembler_percent_contigs_greater_1k	is_paired	is_compressed	qc_original_total_bp	qc_original_coverage	qc_original_read_total	qc_original_read_min	qc_original_read_mean	qc_original_read_std	qc_original_read_median	qc_original_read_max	qc_original_read_25th	qc_original_read_75th	qc_original_qual_min	qc_original_qual_mean	qc_original_qual_std	qc_original_qual_max	qc_original_qual_median	qc_original_qual_25th	qc_original_qual_75th	qc_final_is_paired	qc_final_total_bp	qc_final_coverage	qc_final_read_total	qc_final_read_min	qc_final_read_mean	qc_final_read_std	qc_final_read_median	qc_final_read_max	qc_final_read_25th	qc_final_read_75th	qc_final_qual_min	qc_final_qual_mean	qc_final_qual_std	qc_final_qual_max	qc_final_qual_median	qc_final_qual_25th	qc_final_qual_75th	annotator_total_repeat_region
    SRX4563690	gold	passed all cutoffs	2800000	Staphylococcus aureus	paired-end	paired-end	saureus	8	2648	4	59	1	22	2847871	859980	129448	47115	777	346443	3	0	34.86	15.28	17.38	32.48	0.00	0.00	0	8	14	20	0.00	36.36	63.64	90.91	true	true	279999959	100.0	1173310	30.5000	238.6410	73.9257	278	301	180	301	18	33.0331	3.8133	37	33.5000	30.5000	36.5000	True	279999959	100.0	1173310	30.5000	238.6410	73.9257	278	301	180	301	18	33.0331	3.8133	37	33.5000	30.5000	36.5000	
    SRX4563634-SE	bronze	Single-end reads	2800000	Staphylococcus aureus	single-end	single-end	saureus	8	2666	5	59	1	42	2866767	804144	68256	19360	506	150241	5	0	34.79	15.27	17.36	32.58	0.00	0.00	0	10	27	36	0.00	23.81	64.29	85.71	false	true	279999654	99.9999	1134630	31	246.776	67.8698	294	301	197	301	19	32.2018	4.12181	37	33	30	36	False	279999654	99.9999	1134630	31	246.776	67.8698	294	301	197	301	19	32.2018	4.12181	37	33	30	36	1.0
    SRX4563681	silver	Low coverage (91.14x, expect >= 100x)	2800000	Staphylococcus aureus	paired-end	paired-end	saureus	37	2710	4	56	1	47	2878360	481732	61241	31448	876	137601	7	0	33.97	16.08	16.58	33.37	0.00	0.00	0	11	32	45	0.00	23.40	68.09	95.74	true	true	255190690	91.1396	1091334	31	233.8335	72.8814	257	301	175	301	19	32.5926	4.0385	37	33.5000	30.5000	36	True	255190690	91.1396	1091334	31	233.8335	72.8814	257	301	175	301	19	32.5926	4.0385	37	33.5000	30.5000	36	
    SRX4563687	gold	passed all cutoffs	2800000	Staphylococcus aureus	paired-end	paired-end	saureus	5	2628	3	58	1	27	2819890	601960	104440	33076	750	389806	3	0	33.09	17.15	15.64	34.12	0.00	0.00	0	9	18	25	0.00	33.33	66.67	92.59	true	true	280000043	100.0	1164398	31	240.4680	71.0106	276.5000	301	185	301	19	32.4405	4.0673	37	33.5000	29.5000	36	True	279999531	99.9998	1164396	31	240.4680	71.0107	276.5000	301	185	301	19	32.4405	4.0673	37	33.5000	29.5000	36	
    SRX4563689	silver	Low coverage (83.26x, expect >= 100x)	2800000	Staphylococcus aureus	paired-end	paired-end	saureus	5	2575	5	58	1	24	2776912	473737	115704	52709	750	250837	4	0	33.37	16.60	16.19	33.84	0.00	0.00	0	11	16	23	0.00	45.83	66.67	95.83	true	true	233140431	83.2644	1015306	31	229.6255	72.2632	244	301	171	300.5000	19	32.5968	4.0349	37	33.5000	30	36	True	233140431	83.2644	1015306	31	229.6255	72.2632	244	301	171	300.5000	19	32.5968	4.0349	37	33.5000	30	36	
    SRX4563634	gold	passed all cutoffs	2800000	Staphylococcus aureus	paired-end	paired-end	saureus	8	2678	5	59	1	27	2875309	838477	106492	39259	855	304863	3	0	34.99	15.05	17.59	32.37	0.00	0.00	0	9	18	25	0.00	33.33	66.67	92.59	true	true	279999654	99.9999	1134630	31	246.7760	67.8666	293	301	197	301	19	32.2018	4.0873	37	33	29.5000	36	True	279999654	99.9999	1134630	31	246.7760	67.8666	293	301	197	301	19	32.2018	4.0873	37	33	29.5000	36	1.0
    SRX4563682	gold	passed all cutoffs	2800000	Staphylococcus aureus	paired-end	paired-end	saureus	5	2612	4	58	1	24	2798867	385705	116619	68098	1459	340863	4	0	34.37	15.47	17.28	32.88	0.00	0.00	0	8	18	24	0.00	33.33	75.00	100.00	true	true	280000143	100.0	1198514	31	233.6225	74.2875	259	301	174	301	17.5000	33.1307	3.8246	37	34	31	36.5000	True	279999695	99.9999	1198512	31	233.6225	74.2876	259	301	174	301	17.5000	33.1307	3.8246	37	34	31	36.5000	
    ```

??? abstract "Example: `bactopia-summary.txt`"
    Below is an example of the `bactopia-summary.txt` file. This file is a simple summary
    of counts.
    ```{bash}
    Bactopia Summary Report

    Total Samples: 7

    Passed: 7
        Gold: 4
        Silver: 2
        Bronze: 1

    Excluded: 0
        Failed Cutoff: 0
        QC Failure: 0

    Reports:
        Full Report (txt): ./bactopia-report.tsv
        Exclusion: ./bactopia-exclude.tsv
        Summary: ./bactopia-summary.txt

    Rank Cutoffs:
        Gold:
            Coverage >= 100x
            Quality >= Q30
            Read Length >= 95bp
            Total Contigs < 100
        Silver:
            Coverage >= 50x
            Quality >= Q20
            Read Length >= 75bp
            Total Contigs < 200
        Bronze:
            Coverage >= 20x
            Quality >= Q12
            Read Length >= 49bp
            Total Contigs < 500

    Assembly Length Exclusions:
        Minimum: None
        Maximum: None
    ```

You might be wondering what determines if a sample passes or fails, and what are
Gold, Silver, and Bronze. To be honest, the Olympics might have been happening when
we settled on Gold, Silver, Bronze, but turns out it works pretty well. Here's the
break down of each:

| Rank | Coverage | Quality | Read Length | Total Contigs |
| ---- | -------- | ------- | ----------- | ------------- |
| Gold   | >= 100x | >= Q30  | >= 95bp     | < 100         |
| Silver | >= 50x  | >= Q20  | >= 75bp     | < 200         |
| Bronze | >= 20x  | >= Q12  | >= 49bp     | < 500         |
| Fail   | < 20x   | < Q12   | < 49bp      | >= 500        |

??? tip "These cutoffs can be changed"
    These cutoffs might work for the majority, but its important to adjust them to your
    specific needs. For example, 100x coverage might be too high for your study, or maybe
    you want to exclude samples with more than 100 contigs. These cutoffs can be changed
    using the following parameters:
    
    | Parameter | Default | Description |
    | --------- | ------- | ----------- |
    | `--gold-coverage` | 100 | Minimum amount of coverage required for Gold status |
    | `--gold-quality` | 30 | Minimum per-read mean quality score required for Gold status |
    | `--gold-read-length` | 95 | Minimum mean read length required for Gold status |
    | `--gold-contigs` | 100 | Maximum contig count required for Gold status |
    | `--silver-coverage` | 50 | Minimum amount of coverage required for Silver status |
    | `--silver-quality` | 20 | Minimum per-read mean quality score required for Silver status |
    | `--silver-read-length` | 75 | Minimum mean read length required for Silver status |
    | `--silver-contigs` | 200 | Maximum contig count required for Silver status |
    | `--min-coverage` | 20 | Minimum amount of coverage required to pass |
    | `--min-quality` | 12 | Minimum per-read mean quality score required to pass |
    | `--min-read-length` | 49 | Minimum mean read length required to pass |
    | `--max-contigs` | 500 | Maximum contig count required to pass |
    | `--min-assembled-size` | 0 | Minimum assembled genome size |
    | `--max-assembled-size` | 0 | Maximum assembled genome size |

This was meant to be a quick introduction to the `bactopia summary` command. Overtime this
command is expected to evolve into a more robust summary of your samples.

* [x] Use Bactopia to process:
    * [x] Aggregate results from multiple samples

### Wrap-up

Congratulations! You've been able process many samples now with Bactopia! So far, in this
tutorial we covered how to process local and SRA/ENA samples. We also covered the
`bactopia search` and `bactopia prepare` to prepare file for multiple sample processing.
Finally, we covered the `bactopia summary` command to get a quick overview of your samples.

* [x] Use Bactopia to process:
    * [x] Single sample from SRA/ENA
    * [x] Multiple samples from SRA/ENA
    * [x] Single local sample
    * [x] Multiple local samples
    * [x] Aggregate results from multiple samples

__*BUT!*__ We're not done yet! Let's take a look into how we can further process these
samples using [Bactopia Tools](bactopia-tools/index.md). These are additional pre-made
workflows that make use of existing Bactopia outputs to dig even deeper in to your studies.

## Bactopia Tools

You might be asking yourself, _What are these "Bactopia Tools"?_(Or _Will this ever end?!?_)

Bactopia Tools, are powerful pre-made workflows that make use of existing Bactopia outputs.
These allow you to rapidly extend your analyses beyond what Bactopia provides out of the box.
For example, need to build a phylogenetic tree? Or, want to call SNPs against a reference?
Or, maybe just BLAST some genes against all your samples? There are Bactopia Tools for each
of these, and many, many more.

These Bactopia Tools, allow you to __Do More Science__ by providing a framework to rapidly
extend your analyses.

In this section will explore how you can use a few of these. Let's get started!

### Species Specific Analyses

All the samples we've processed so far have been from the same species, _Staphylococcus aureus_.
There is a Bactopia Tool call [staphtyper](bactopia-tools/staphtyper.md) that can be used to
run a few tools specific to _S. aureus_ analysis. Let's run our first Bactopia Tool using the
samples in `local-multiple-samples`:

```{bash}
bactopia \
    --wf staphtyper \
    --bactopia local-multiple-samples/
```

Before we move on, what is happening here? We are using the `--wf` parameter to tell Bactopia
to run the `staphtyper` workflow. The `--bactopia` parameter is used to tell Bactopia where
outputs from a previous Bactopia run are located.

With this information, Bactopia will verify that a `staphtyper` workflow exists and then
check the `local-multiple-samples` directory for the required inputs. If everything is
checks out, Bactopia will then run the `staphtyper` workflow.

Here's the logging information you should see:

```{bash}
executor >  local (2)
[9c/31f28f] process > BACTOPIATOOLS:STAPHTYPER:AGRVATE (SRX4563690)                           [100%] 7 of 7 ✔
[f7/b722d7] process > BACTOPIATOOLS:STAPHTYPER:SPATYPER (SRX4563634)                          [100%] 7 of 7 ✔
[68/067620] process > BACTOPIATOOLS:STAPHTYPER:STAPHOPIASCCMEC (SRX4563634)                   [100%] 7 of 7 ✔
[33/2e5476] process > BACTOPIATOOLS:STAPHTYPER:CSVTK_CONCAT_AGRVATE (agrvate)                 [100%] 1 of 1 ✔
[b9/a755e3] process > BACTOPIATOOLS:STAPHTYPER:CSVTK_CONCAT_SPATYPER (spatyper)               [100%] 1 of 1 ✔
[78/6a0552] process > BACTOPIATOOLS:STAPHTYPER:CSVTK_CONCAT_STAPHOPIASCCMEC (staphopiasccmec) [100%] 1 of 1 ✔
[c2/694b33] process > BACTOPIATOOLS:CUSTOM_DUMPSOFTWAREVERSIONS (1)                           [100%] 1 of 1 ✔

    Bactopia Tools: `staphtyper Execution Summary
    ---------------------------
    Bactopia Version : 3.0.0
    Nextflow Version : 23.04.1
    Command Line     : nextflow run /path/to/main.nf -w /path/to/work/ --wf staphtyper --bactopia local-multiple-samples/
    Resumed          : false
    Completed At     : 2023-09-06T04:01:04.918782203Z
    Duration         : 19.6s
    Success          : true
    Exit Code        : 0
    Error Report     : -
    Launch Dir       : /path/to/tutorial
```

Pretty cool (_and fast!_) huh? By just adding `--wf` and `--bactopia` we were able to rapidly
three different _S. aureus_ tools against our samples. In addition, the outputs for each of
these analyses were combined into a single file for easy viewing.

!!! tip "Visit `staphtyper` documentation to learn more"
    To learn more about `staphtyper` and the outputs it produces, check out the
    [staphtyper documentation](bactopia-tools/staphtyper.md). It's worth noting,
    **all** Bactopia Tools will have a similar documentation page.

* [x] Use Bactopia Tools to:
    * [x] Run *S. aureus* specific analyses
    * [ ] Generate a tree using [Mashtree](bactopia-tools/mashtree.md)

### Building a Tree

Now that we've run some _S. aureus_ specific analyses, let's try something a little different.
Let's build a tree using [Mashtree](bactopia-tools/mashtree.md), which builds the tree using
Mash distances.

For this tutorial, we are using Mashtree, because it is quick, and if you've made it this
far, you probably want to be done soon!

Let's knock this out using the `local-multiple-samples` samples, but first, let's exclude
the single-end sample `SRX4563634-SE` from the analysis, to demonstrate the usage of `--exclude`.

!!! tip "Including and Excluding samples from Bactopia Tool analysis"
    Every Bactopia tool has the following two parameters available:
    
    | Parameter | Description |
    | --------- | ----------- |
    | `--include` | A list of samples (one sample per line) to _**include**_ in the analysis.   |
    | `--exclude` | A list of samples (one sample per line) to _**exclude**_ from the analysis. |
    
    This is a useful feature to include or exclude samples from a Bactopia Tool analysis for
    a specific reason. For example, let's imagine `bactopia summary` identified a sample that
    failed quality checks, and should be excluded from analysis. You can pass the `bactopia-exclude.tsv`
    produced to `--exclude` to ensure those failed samples are not included in the analysis.
    
    Similarly, let's say you only wanted to run a Bactopia Tool only on specific samples, let's
    say building a tree from an outbreak. You can pass this list of samples to `--include` to
    only run the Bactopia Tool on those samples.

First, let's create a file with the sample we want to exclude:

```{bash}
echo "SRX4563634-SE" > exclude.txt
```

Now, we'll run `mashtree` using the `local-multiple-samples` directory, but excluding `SRX4563634-SE`,
using `--exclude` and the `exclude.txt` we just made:

```{bash}
bactopia \
    --wf mashtree \
    --bactopia local-multiple-samples/ \
    --exclude exclude.txt
```

Not much changed here, by simply changing `staphtyper` to `mashtree` we were able to rapidly
build a tree using Mash distances. Here's the logging information you should see, take notice
where is says 1 was excluded and 6 were included:

```{bash}

Excluding 1 samples from the analysis
Found 6 samples to process

If this looks wrong, now's your chance to back out (CTRL+C 3 times).
Sleeping for 5 seconds...
--------------------------------------------------------------------
executor >  local (2)
[ff/c7abcb] process > BACTOPIATOOLS:MASHTREE:MASHTREE_MODULE (mashtree) [100%] 1 of 1 ✔
[1d/f97b25] process > BACTOPIATOOLS:CUSTOM_DUMPSOFTWAREVERSIONS (1)     [100%] 1 of 1 ✔

    Bactopia Tools: `mashtree Execution Summary
    ---------------------------
    Bactopia Version : 3.0.0
    Nextflow Version : 23.04.1
    Command Line     : nextflow run /path/to/main.nf --wf mashtree --bactopia local-multiple-samples/ --run_name tutorial
    Resumed          : false
    Completed At     : 2023-09-06T04:14:07.721594313Z
    Duration         : 12.4s
    Success          : true
    Exit Code        : 0
    Error Report     : -
    Launch Dir       : /path/to/tutorial
```

!!! tip "Visit `mashtree` documentation to learn more"
    To learn more about `mashtree` and the outputs it produces, check out the
    [mashtree documentation](bactopia-tools/mashtree.md). Again, each Bactopia
    Tool will have a similar documentation page.

### Wrap-up

You did it! I hope with two simple examples, I hope you've gained an appreciation for how
Bactopia Tools can help make things easier for you.

* [x] Use Bactopia Tools to:
    * [x] Run *S. aureus* specific analyses
    * [x] Generate a tree using [Mashtree](bactopia-tools/mashtree.md)

By this point, you are probably done! Let's finish this!

## What's next?

This tutorial has covered a lot! Let's recap what we've done:

* [x] Verify Bactopia is working
* [x] Use Bactopia to process:
    * [x] Single sample from SRA/ENA
    * [x] Multiple samples from SRA/ENA
    * [x] Single local sample
    * [x] Multiple local samples
    * [x] Aggregate results from multiple samples
* [x] Use Bactopia Tools to:
    * [x] Run *S. aureus* specific analyses
    * [x] Generate a tree using [Mashtree](bactopia-tools/mashtree.md)

Hopefully you have succeeded (yay! 🎉) and would like to use Bactopia on your own data!

Please keep in mind, this tutorial didn't cover how to process Oxford Nanopore reads, or
assemblies. There is so much more we can cover, if there are some you would like to see,
or any issues you might have run into, please let me know by submitting a
[GitHub Issue](https://github.com/bactopia/bactopia/issues).
