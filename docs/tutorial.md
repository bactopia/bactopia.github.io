---
title: Tutorial
description: >-
    A tutorial to get started with Bactopia using publicly available genomes.
sidebar_position: 4
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
    * [ ] Generate a tree using [Mashtree](/bactopia-tools/mashtree)

Upon completion of this tutorial, you should be ready to process your own data using Bactopia!

:::warning[Bactopia Should Be Installed]
This tutorial assumes you have already installed Bactopia. If you have not, please check
out how to at [Installation](./installation).
:::

:::warning[Reach out if you have trouble with this tutorial]
I try my best to make sure everything is working as expected, but understand that
is not always the case. If you run into any issues with this tutorial, please let me
know by submitting a [GitHub Issue](https://github.com/bactopia/bactopia/issues/new/choose).
Hopefully, together we'll be able to figure out what is happening.
:::

OK! Let's get this tutorial started!

## Selecting a Profile

Because Bactopia is written in Nextflow, it can be executed on many different environments.
For the purposes of this tutorial, we will be using the default profile, which will use Conda
environments to run the tools. However, if you are on a system with Singularity or Docker,
those are recommended over Conda environments.

If you want to use Docker, you would simply add `-profile docker` to the commands below.
Similarly, if you want to use Singularity, you would add `-profile singularity`.

<details>
<summary>Profiles can be extended to other systems (e.g. HPC and cloud)</summary>

Nextflow has built in support for numerous systems. If you are interested in using Bactopia
on a system other than your local machine, please check out the
[Nextflow Executors](https://www.nextflow.io/docs/latest/executor.html). Setting up a
custom profile for this tutorial, is outside its scope, but if you are interested in doing
so, feel free to reach out.

</details>

## Verify Bactopia is Working

Before we get started, we'll use the built in `test` profile to verify Bactopia is working
for you. This `test` profile will download a very small bacterial genome (~350kb genome size),
which will allow you to quickly test Bactopia.

To run the test, simply run the following command:

```bash
bactopia -profile test,standard
```

In the above example `standard` is a profile that makes use of Conda environments.

<details>
<summary>Example commands to use Docker or Singularity</summary>

If you are using Docker, you would run the following command:
```bash
bactopia -profile test,docker
```

If you are using Singularity, you would run the following command:
```bash
bactopia -profile test,singularity
```

</details>

:::note[The first run might take a while]
The first time you run Bactopia it will build the environments (Conda, Docker, or Singularity)
needed for analysis. Depending on your internet connection this might take a little while.
I recommend grabbing a coffee or going for a walk. This is only a one time build, future
runs will be much faster.
:::

Upon completion, you will hopefully be met with text like the following:

```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[67/254aed] GATHER:GATHER_MODULE (SRR2838702)            [100%] 1 of 1 ✔
[48/e17b5c] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[90/a4499c] QC:QC_MODULE (SRR2838702)                    [100%] 1 of 1 ✔
[13/caba51] ASSEMBLER:ASSEMBLER_MODULE (SRR2838702)      [100%] 1 of 1 ✔
[8a/3b2e31] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[6b/d0dfa7] SKETCHER:SKETCHER_MODULE (SRR2838702)        [100%] 1 of 1 ✔
[e0/b1d5b9] PROKKA:PROKKA_MODULE (SRR2838702)            [100%] 1 of 1 ✔
[2c/900d9e] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRR2838702) [100%] 1 of 1 ✔
[12/c2fcd1] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[82/800c26] MLST:MLST_MODULE (SRR2838702)                [100%] 1 of 1 ✔
[9c/5206fe] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 10:55:13
Duration    : 3m 29s
CPU hours   : 0.2
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none -profile test,docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : test,docker
Completed At     : 2026-04-29T10:55:13.036123110-06:00
Duration         : 3m 29s
Resumed          : false
Success          : true
Merged Results   : bactopia/bactopia-runs/bactopia-20260429-105142


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia bactopia --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia bactopia --wf pangenome
bactopia -profile docker --bactopia bactopia --wf merlin
bactopia -profile docker --bactopia bactopia --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
What cheese can never be yours? Nacho cheese!
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

```bash
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
the Gather Step

<details>
<summary>Expected logging information</summary>

Nextflow will produce logging information explaining what is happening during the
analysis. Here is example logging text you should see:
```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[ee/03bca9] GATHER:GATHER_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[1c/00a83a] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[5f/e313c3] QC:QC_MODULE (SRX4563634)                    [100%] 1 of 1 ✔
[f0/76d7d3] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)      [100%] 1 of 1 ✔
[e0/ed8bf7] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[05/bc5789] SKETCHER:SKETCHER_MODULE (SRX4563634)        [100%] 1 of 1 ✔
[b8/5c3c0b] PROKKA:PROKKA_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[71/1c2646] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634) [100%] 1 of 1 ✔
[f1/d82589] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[76/d9b39f] MLST:MLST_MODULE (SRX4563634)                [100%] 1 of 1 ✔
[b1/3c8b94] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:05:37
Duration    : 8m 55s
CPU hours   : 0.3
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --accession SRX4563634 --coverage 100 --genome_size 2800000 --max_cpus 2 --outdir ena-single-sample -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:05:37.643590738-06:00
Duration         : 8m 55s
Resumed          : false
Success          : true
Merged Results   : ena-single-sample/bactopia-runs/bactopia-20260429-105641


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia ena-single-sample --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia ena-single-sample --wf pangenome
bactopia -profile docker --bactopia ena-single-sample --wf merlin
bactopia -profile docker --bactopia ena-single-sample --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
When does a joke become a 'dad' joke? When it becomes apparent!
```

</details>

<details>
<summary>Expected output directory structure</summary>

After your Bactopia run has completed you should have a directory structure that looks
like the following:
```bash
tree ena-single-sample/
ena-single-sample/
├── bactopia-runs
│   └── bactopia-20260429-105641
│       ├── merged-results
│       │   ├── amrfinderplus.tsv
│       │   ├── assembly-scan.tsv
│       │   ├── logs
│       │   │   ├── amrfinderplus-concat
│       │   │   │   ├── nf.command.begin
│       │   │   │   ├── nf.command.err
│       │   │   │   ├── nf.command.log
│       │   │   │   ├── nf.command.out
│       │   │   │   ├── nf.command.run
│       │   │   │   ├── nf.command.sh
│       │   │   │   ├── nf.command.trace
│       │   │   │   └── versions.yml
│       │   │   ├── assembly-scan-concat
│       │   │   │   ├── nf.command.begin
│       │   │   │   ├── nf.command.err
│       │   │   │   ├── nf.command.log
│       │   │   │   ├── nf.command.out
│       │   │   │   ├── nf.command.run
│       │   │   │   ├── nf.command.sh
│       │   │   │   ├── nf.command.trace
│       │   │   │   └── versions.yml
│       │   │   ├── meta-concat
│       │   │   │   ├── nf.command.begin
│       │   │   │   ├── nf.command.err
│       │   │   │   ├── nf.command.log
│       │   │   │   ├── nf.command.out
│       │   │   │   ├── nf.command.run
│       │   │   │   ├── nf.command.sh
│       │   │   │   ├── nf.command.trace
│       │   │   │   └── versions.yml
│       │   │   └── mlst-concat
│       │   │       ├── nf.command.begin
│       │   │       ├── nf.command.err
│       │   │       ├── nf.command.log
│       │   │       ├── nf.command.out
│       │   │       ├── nf.command.run
│       │   │       ├── nf.command.sh
│       │   │       ├── nf.command.trace
│       │   │       └── versions.yml
│       │   ├── meta.tsv
│       │   └── mlst.tsv
│       └── nf-reports
│           ├── bactopia-dag.dot
│           ├── bactopia-report.html
│           ├── bactopia-timeline.html
│           └── bactopia-trace.txt
└── SRX4563634
    ├── main
    │   ├── annotator
    │   │   └── prokka
    │   │       ├── logs
    │   │       │   ├── nf.command.begin
    │   │       │   ├── nf.command.err
    │   │       │   ├── nf.command.log
    │   │       │   ├── nf.command.out
    │   │       │   ├── nf.command.run
    │   │       │   ├── nf.command.sh
    │   │       │   ├── nf.command.trace
    │   │       │   ├── SRX4563634.err
    │   │       │   ├── SRX4563634.log
    │   │       │   └── versions.yml
    │   │       ├── SRX4563634-blastdb.tar.gz
    │   │       ├── SRX4563634.faa.gz
    │   │       ├── SRX4563634.ffn.gz
    │   │       ├── SRX4563634.fna.gz
    │   │       ├── SRX4563634.fsa.gz
    │   │       ├── SRX4563634.gbk.gz
    │   │       ├── SRX4563634.gff.gz
    │   │       ├── SRX4563634.sqn.gz
    │   │       ├── SRX4563634.tbl.gz
    │   │       ├── SRX4563634.tsv
    │   │       └── SRX4563634.txt
    │   ├── assembler
    │   │   ├── logs
    │   │   │   ├── nf.command.begin
    │   │   │   ├── nf.command.err
    │   │   │   ├── nf.command.log
    │   │   │   ├── nf.command.out
    │   │   │   ├── nf.command.run
    │   │   │   ├── nf.command.sh
    │   │   │   ├── nf.command.trace
    │   │   │   ├── shovill.log
    │   │   │   └── versions.yml
    │   │   ├── SRX4563634.fna.gz
    │   │   ├── SRX4563634.tsv
    │   │   └── supplemental
    │   │       ├── flash.hist
    │   │       ├── flash.histogram
    │   │       ├── illumina.txt
    │   │       └── shovill.corrections
    │   ├── gather
    │   │   ├── logs
    │   │   │   ├── nf.command.begin
    │   │   │   ├── nf.command.err
    │   │   │   ├── nf.command.log
    │   │   │   ├── nf.command.out
    │   │   │   ├── nf.command.run
    │   │   │   ├── nf.command.sh
    │   │   │   ├── nf.command.trace
    │   │   │   └── versions.yml
    │   │   └── SRX4563634-meta.tsv
    │   ├── qc
    │   │   ├── logs
    │   │   │   ├── nf.command.begin
    │   │   │   ├── nf.command.err
    │   │   │   ├── nf.command.log
    │   │   │   ├── nf.command.out
    │   │   │   ├── nf.command.run
    │   │   │   ├── nf.command.sh
    │   │   │   ├── nf.command.trace
    │   │   │   ├── SRX4563634-fastp.log
    │   │   │   └── versions.yml
    │   │   ├── SRX4563634_R1.fastq.gz
    │   │   ├── SRX4563634_R2.fastq.gz
    │   │   └── supplemental
    │   │       ├── SRX4563634.fastp.html
    │   │       ├── SRX4563634.fastp.json
    │   │       ├── SRX4563634_R1-final_fastqc.html
    │   │       ├── SRX4563634_R1-final_fastqc.zip
    │   │       ├── SRX4563634_R1-final.json
    │   │       ├── SRX4563634_R1-original_fastqc.html
    │   │       ├── SRX4563634_R1-original_fastqc.zip
    │   │       ├── SRX4563634_R1-original.json
    │   │       ├── SRX4563634_R2-final_fastqc.html
    │   │       ├── SRX4563634_R2-final_fastqc.zip
    │   │       ├── SRX4563634_R2-final.json
    │   │       ├── SRX4563634_R2-original_fastqc.html
    │   │       ├── SRX4563634_R2-original_fastqc.zip
    │   │       └── SRX4563634_R2-original.json
    │   └── sketcher
    │       ├── logs
    │       │   ├── nf.command.begin
    │       │   ├── nf.command.err
    │       │   ├── nf.command.log
    │       │   ├── nf.command.out
    │       │   ├── nf.command.run
    │       │   ├── nf.command.sh
    │       │   ├── nf.command.trace
    │       │   └── versions.yml
    │       ├── SRX4563634-k21.msh
    │       ├── SRX4563634-k31.msh
    │       ├── SRX4563634-mash-refseq88-k21.txt
    │       ├── SRX4563634.sig
    │       └── SRX4563634-sourmash-gtdb-rs207-k31.txt
    └── tools
        ├── amrfinderplus
        │   ├── logs
        │   │   ├── nf.command.begin
        │   │   ├── nf.command.err
        │   │   ├── nf.command.log
        │   │   ├── nf.command.out
        │   │   ├── nf.command.run
        │   │   ├── nf.command.sh
        │   │   ├── nf.command.trace
        │   │   └── versions.yml
        │   └── SRX4563634.tsv
        └── mlst
            ├── logs
            │   ├── nf.command.begin
            │   ├── nf.command.err
            │   ├── nf.command.log
            │   ├── nf.command.out
            │   ├── nf.command.run
            │   ├── nf.command.sh
            │   ├── nf.command.trace
            │   └── versions.yml
            └── SRX4563634.tsv

30 directories, 141 files
```

</details>

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

:::tip[Check out the Beginner's Guide for more information on `bactopia search`]
For now, we are just going to use `bactopia search` without much details on how it works.
You use `bactopia search` for some fun things, to learn more about it, check out
[Beginner's Guide -> Accessions](./beginners-guide#accessions).
:::

Let's go ahead and give `bactopia search` a try:

```bash
bactopia search \
    --query PRJNA480016 \
    --limit 5 \
    --use-ncbi-genome-size
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

```bash
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

```bash
bactopia \
    --accessions bactopia-accessions.txt \
    --coverage 100 \
    --outdir ena-multiple-samples \
    --max_cpus 2
```

Instead of `--accession` we are now using `--accessions` which tells Bactopia to read the
provided file, in our case `bactopia-accessions.txt`, and download each Experiment accession
from SRA/ENA and then process them all at once.

:::tip[Go take a break, this will be a little while]
At this point, you might want to go for a walk or make yourself a coffee! This step has
an **approximate completion time of ~15-120 minutes**. Again the total time will depend
on your system and internet connection.
:::

Once this is complete, the results for all five samples will be found in the
`ena-multiple-samples` directory. Each sample will have there own folder of results.

<details>
<summary>Expected logging information</summary>

Nextflow will produce logging information explaining what is happening during the
analysis. Here is example logging text you should see:
```bash
executor >  local (39)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[e6/6018f9] GATHER:GATHER_MODULE (SRX4563688)            [100%] 5 of 5 ✔
[53/b1868a] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[0e/05679c] QC:QC_MODULE (SRX4563688)                    [100%] 5 of 5 ✔
[d7/aaf093] ASSEMBLER:ASSEMBLER_MODULE (SRX4563688)      [100%] 5 of 5 ✔
[d2/04970a] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[46/6ef407] SKETCHER:SKETCHER_MODULE (SRX4563688)        [100%] 5 of 5 ✔
[50/4e3e72] PROKKA:PROKKA_MODULE (SRX4563688)            [100%] 5 of 5 ✔
[62/d43d72] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563688) [100%] 5 of 5 ✔
[76/a4e627] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[f2/1d3aa4] MLST:MLST_MODULE (SRX4563688)                [100%] 5 of 5 ✔
[80/19f956] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:21:01
Duration    : 10m 59s
CPU hours   : 3.9
Succeeded   : 39

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --accessions bactopia-accessions.txt --coverage 100 --outdir ena-multiple-samples --max_cpus 4 -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:21:01.214462971-06:00
Duration         : 11m
Resumed          : false
Success          : true
Merged Results   : ena-multiple-samples/bactopia-runs/bactopia-20260429-111000


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia ena-multiple-samples --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia ena-multiple-samples --wf pangenome
bactopia -profile docker --bactopia ena-multiple-samples --wf merlin
bactopia -profile docker --bactopia ena-multiple-samples --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
What kind of music do planets listen to? Neptunes!
```

</details>

* [x] Use Bactopia to process:
    * [x] Single sample from SRA/ENA
    * [x] Multiple samples from SRA/ENA

Congratulations! At this point, you should have been able to use Bactopia to process multiple
publicly available genomes from SRA/ENA. Now let's move on to processing some local samples!

## Local Samples

For this, tutorial I thought about having a dataset for you to download, but we already
downloaded some samples! Instead, let's recycle some of the samples we downloaded from SRA/ENA.

First let's make a directory to put the FASTQs into:

```bash
mkdir fastqs
```

Now let's move some the FASTQs from our SRX4563634 sample into this folder.

```bash
cp ./ena-single-sample/SRX4563634/main/qc/SRX4563634*.fastq.gz fastqs
```

Finally let's also make a single-end version of SRX4563634.

```bash
cat fastqs/SRX4563634_R1.fastq.gz fastqs/SRX4563634_R2.fastq.gz > fastqs/SRX4563634-SE.fastq.gz
```

This should give use three local FASTQs to work with:

```bash
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

:::tip[Learn more from the Beginner's Guide]
To learn more about these parameters, check out the
[Beginner's Guide -> Single Sample](./beginners-guide#single-sample) section. Each of these
parameters are described in detail.
:::

#### Paired-End

For paired-end reads we'll be u will want to use `--R1`, `--R2`, and `--sample`. For this paired-end example we'll use SRX4563634 again which we've copied to the `fastqs` folder.

```bash
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

<details>
<summary>Expected logging information</summary>

Nextflow will produce logging information explaining what is happening during the
analysis. Here is example logging text you should see:

```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[f2/02a83e] GATHER:GATHER_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[67/4c51ca] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[8c/d85d58] QC:QC_MODULE (SRX4563634)                    [100%] 1 of 1 ✔
[6a/c11313] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)      [100%] 1 of 1 ✔
[b7/a83b77] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[16/ba5aef] SKETCHER:SKETCHER_MODULE (SRX4563634)        [100%] 1 of 1 ✔
[ae/c0cc9f] PROKKA:PROKKA_MODULE (SRX4563634)            [100%] 1 of 1 ✔
[4d/40bbaf] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634) [100%] 1 of 1 ✔
[1a/d416b4] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[35/d75a90] MLST:MLST_MODULE (SRX4563634)                [100%] 1 of 1 ✔
[c2/98573c] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:44:07
Duration    : 7m
CPU hours   : 0.6
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --r1 fastqs/SRX4563634_R1.fastq.gz --r2 fastqs/SRX4563634_R2.fastq.gz --sample SRX4563634 --coverage 100 --genome_size 2800000 --outdir local-single-sample --max_cpus 4 -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:44:07.351753090-06:00
Duration         : 7m 1s
Resumed          : false
Success          : true
Merged Results   : local-single-sample/bactopia-runs/bactopia-20260429-113705


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia local-single-sample --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia local-single-sample --wf pangenome
bactopia -profile docker --bactopia local-single-sample --wf merlin
bactopia -profile docker --bactopia local-single-sample --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
What do you call a cow with no legs? Ground beef!
```

</details>

#### Single-End

Now, you might be wondering _"single-end"_? Even though in modern Illumina runs, we'll
rarely run into single-end reads, they do exist. There are many early single-end Illumina
samples available from SRA/ENA. Due this, single-end support was built into Bactopia.

It's a simple change, to analyze single-end reads, instead of `--r1` and `--r2` we'll be
using `--se`. Let's give it a try using the `SRX4563634-SE.fastq.gz` file we created earlier`:

```bash
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

<details>
<summary>Expected logging information</summary>

Nextflow will produce logging information explaining what is happening during the
analysis. Here is example logging text you should see:

```bash
executor >  local (11)
[skipped  ] DATASETS:DATASETS_MODULE                        [100%] 1 of 1, stored: 1 ✔
[3f/ac6144] GATHER:GATHER_MODULE (SRX4563634-SE)            [100%] 1 of 1 ✔
[b9/4aceb0] GATHER:CSVTK_CONCAT (meta)                      [100%] 1 of 1 ✔
[53/b4c1fd] QC:QC_MODULE (SRX4563634-SE)                    [100%] 1 of 1 ✔
[7b/81dffd] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634-SE)      [100%] 1 of 1 ✔
[17/25f551] ASSEMBLER:CSVTK_CONCAT (assembly-scan)          [100%] 1 of 1 ✔
[cb/1b89ef] SKETCHER:SKETCHER_MODULE (SRX4563634-SE)        [100%] 1 of 1 ✔
[27/f7c3e5] PROKKA:PROKKA_MODULE (SRX4563634-SE)            [100%] 1 of 1 ✔
[a2/9ffd0c] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634-SE) [100%] 1 of 1 ✔
[d5/257b5e] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)      [100%] 1 of 1 ✔
[d6/3402fe] MLST:MLST_MODULE (SRX4563634-SE)                [100%] 1 of 1 ✔
[bb/760752] MLST:CSVTK_CONCAT (mlst)                        [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 11:55:49
Duration    : 7m 47s
CPU hours   : 0.3
Succeeded   : 11

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --se fastqs/SRX4563634-SE.fastq.gz --sample SRX4563634-SE --coverage 100 --genome_size 2800000 --outdir local-single-sample --max_cpus 2 -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T11:55:49.702989944-06:00
Duration         : 7m 47s
Resumed          : false
Success          : true
Merged Results   : local-single-sample/bactopia-runs/bactopia-20260429-114801


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia local-single-sample --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia local-single-sample --wf pangenome
bactopia -profile docker --bactopia local-single-sample --wf merlin
bactopia -profile docker --bactopia local-single-sample --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
Where do lizards go after their tails fall off? The retail store!
```

</details>

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

:::tip[Learn more from the Beginner's Guide]
To learn more about these parameters, check out the
[Beginner's Guide -> Local Samples](./beginners-guide#local-samples) section. Each of these
parameters are described in detail.
:::

Let's recycle some more FASTQ files. Before we proceed lets move some more FASTQs into our
`fastqs` folder. For this we'll use the FASTQs from `ena-multiple-samples`. Let's copy them
over:

```bash
find ena-multiple-samples/ -name *.fastq.gz | \
    xargs -I {} cp {} fastqs/
```

We should how have FASTQs for 7 samples in our `fastqs` folder. With these let's generate
a FOFN using `bactopia prepare`:

```bash
bactopia prepare --path fastqs/
sample  runtype genome_size     species r1      r2      se      ont     assembly
SRX4563634      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R2.fastq.gz
SRX4563634-SE   single-end      0       UNKNOWN_SPECIES                 /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634-SE.fastq.gz
SRX4563678      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R2.fastq.gz
SRX4563680      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R2.fastq.gz
SRX4563684      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R2.fastq.gz
SRX4563686      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R2.fastq.gz
SRX4563688      paired-end      0       UNKNOWN_SPECIES /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R2.fastq.gz
```

This command will try to create a FOFN for you. For this tutorial, the FASTQ names are pretty straight forward and should produce a correct FOFN (or at least it should! ... hopefully!). If that wasn't the case for you, there are ways to [tweak `bactopia prepare`](./beginners-guide#bactopia-prepare).

Wait! We for got something, in the output above we have `0` for `genome_size` and
`UNKNOWN_SPECIES` for `species`. We can fix this by using the `--species` and `--genome-size`
options, let's try again:

```bash
bactopia prepare \
    --path fastqs/ \
    --species "Staphylococcus aureus" \
    --genome-size 2800000
sample  runtype genome_size     species r1      r2      se      ont     assembly
SRX4563634      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634_R2.fastq.gz
SRX4563634-SE   single-end      2800000 Staphylococcus aureus                   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563634-SE.fastq.gz
SRX4563678      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563678_R2.fastq.gz
SRX4563680      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563680_R2.fastq.gz
SRX4563684      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563684_R2.fastq.gz
SRX4563686      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563686_R2.fastq.gz
SRX4563688      paired-end      2800000 Staphylococcus aureus   /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R1.fastq.gz      /home/rpetit3/bactopia-tutorial/fastqs/SRX4563688_R2.fastq.gz
```

Much better! By adding the genome size, Bactopia can now reduce the total coverage to the
value provided by `--coverage`.

However, we need to write this to a file to use it. Let's do that now:

```bash
bactopia prepare \
    --path fastqs/ \
    --species "Staphylococcus aureus" \
    --genome-size 2800000 \
    > samples.txt
```

There we go! We now have everything we need to process all these samples using Bactopia. Now,
let's process these samples using the FOFN we just created.

```bash
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

:::tip[Using `--samples` is more CPU efficient, making it faster]
The real benefit of using the FOFN method to process multiple samples is Nextflow's queue
system will make better use of cpus. Processing multiple samples one at a time
(via `--r1`/`--r2` or `--se`) will lead more instances of jobs waiting on other jobs
to finish, during which cpus aren't being used.
:::

<details>
<summary>Expected logging information</summary>

Nextflow will produce logging information explaining what is happening during the
analysis. Here is example logging text you should see:

```bash
executor >  local (53)
[skipped  ] DATASETS:DATASETS_MODULE                     [100%] 1 of 1, stored: 1 ✔
[2e/454798] GATHER:GATHER_MODULE (SRX4563634)            [100%] 7 of 7 ✔
[0f/47679f] GATHER:CSVTK_CONCAT (meta)                   [100%] 1 of 1 ✔
[6b/941117] QC:QC_MODULE (SRX4563680)                    [100%] 7 of 7 ✔
[42/913683] ASSEMBLER:ASSEMBLER_MODULE (SRX4563634)      [100%] 7 of 7 ✔
[e2/048276] ASSEMBLER:CSVTK_CONCAT (assembly-scan)       [100%] 1 of 1 ✔
[5b/b2ac99] SKETCHER:SKETCHER_MODULE (SRX4563634)        [100%] 7 of 7 ✔
[c8/64642a] PROKKA:PROKKA_MODULE (SRX4563634)            [100%] 7 of 7 ✔
[8c/577268] AMRFINDERPLUS:AMRFINDERPLUS_RUN (SRX4563634) [100%] 7 of 7 ✔
[2c/0dfff6] AMRFINDERPLUS:CSVTK_CONCAT (amrfinderplus)   [100%] 1 of 1 ✔
[7d/2da0da] MLST:MLST_MODULE (SRX4563634)                [100%] 7 of 7 ✔
[1b/4f229b] MLST:CSVTK_CONCAT (mlst)                     [100%] 1 of 1 ✔
Completed at: 29-Apr-2026 12:24:25
Duration    : 9m 48s
CPU hours   : 2.5
Succeeded   : 53

WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Execution Summary
-------------------------------
Workflow         : bactopia
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --samples samples.txt --coverage 100 --max_cpus 2 --outdir local-multiple-samples -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T12:24:25.163874442-06:00
Duration         : 9m 48s
Resumed          : false
Success          : true
Merged Results   : local-multiple-samples/bactopia-runs/bactopia-20260429-121435


Further analyze your samples using Bactopia Tools, with the following command:
--------------------------------------------------------------------------------
bactopia -profile docker --bactopia local-multiple-samples --wf <REPLACE_WITH_BACTOPIA_TOOL_NAME>

Examples:
bactopia -profile docker --bactopia local-multiple-samples --wf pangenome
bactopia -profile docker --bactopia local-multiple-samples --wf merlin
bactopia -profile docker --bactopia local-multiple-samples --wf sccmec

See the full list of available Bactopia Tools: bactopia --list_wfs

Message of the Day
-------------------------------
Learn more about Bactopia at https://bactopia.io/
```

</details>

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

```bash
bactopia summary \
    --bactopia-path local-multiple-samples/
2026-04-29 12:45:12 INFO     2026-04-29 12:45:12:root:INFO - Found 7 samples in local-multiple-samples/ to process                                                    summary.py:341
                    INFO     2026-04-29 12:45:12:root:INFO - Writing report: ./bactopia-report.tsv                                                                    summary.py:432
                    INFO     2026-04-29 12:45:12:root:INFO - Writing exclusion report: ./bactopia-exclude.tsv                                                         summary.py:436
                    INFO     2026-04-29 12:45:12:root:INFO - Writing summary report: ./bactopia-summary.txt
```

Upon completion this will produce three files:

| File                   | Description |
| ---------------------- | ----------- |
| `bactopia-report.tsv`  | A tab-delimited file with more than 70 columns of results from steps in Bactopia. |
| `bactopia-exclude.tsv` | A tab-delimited file with samples that should **_likely_** be excluded from further analysis |
| `bactopia-summary.txt` | A simple summary of quality grades and excluded counts. |

<details>
<summary>Example: `bactopia-report.tsv` _(Warning! Its wide!)_</summary>

Below is an example of the `bactopia-report.tsv` file. As you can see there are a ton of
columns! These columns include lots of information and works quite well with Excel or R.

```tsv
sample  rank    reason  genome_size     species runtype original_runtype        mlst_scheme     mlst_st assembler_total_contig  assembler_total_contig_length   assembler_max_conti _length assembler_mean_contig_length    assembler_median_contig_length  assembler_min_contig_length     assembler_n50_contig_length     assembler_l50_contig_count      assembler_n m_contig_non_acgtn      assembler_contig_percent_a      assembler_contig_percent_c      assembler_contig_percent_g      assembler_contig_percent_t      assembler_contig_percent_n  ssembler_contig_non_acgtn       assembler_contigs_greater_1m    assembler_contigs_greater_100k  assembler_contigs_greater_10k   assembler_contigs_greater_1k    assembler_percent_c ntigs_greater_1m        assembler_percent_contigs_greater_100k  assembler_percent_contigs_greater_10k   assembler_percent_contigs_greater_1k    is_paired       is_compressed   ann tator_total_CDS annotator_total_rRNA    annotator_total_tRNA    qc_original_total_bp    qc_original_coverage    qc_original_read_total  qc_original_read_min    qc_original_read_me n       qc_original_read_std    qc_original_read_median qc_original_read_max    qc_original_read_25th   qc_original_read_75th   qc_original_qual_min    qc_original_qual_mean   qc_ riginal_qual_std        qc_original_qual_max    qc_original_qual_median qc_original_qual_25th   qc_original_qual_75th   qc_final_is_paired      qc_final_total_bp       qc_final_co erage   qc_final_read_total     qc_final_read_min       qc_final_read_mean      qc_final_read_std       qc_final_read_median    qc_final_read_max       qc_final_read_25th      qc_ inal_read_75th  qc_final_qual_min       qc_final_qual_mean      qc_final_qual_std       qc_final_qual_max       qc_final_qual_median    qc_final_qual_25th      qc_final_qual_75th
SRX4563680      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      24      2785142 552034  116047  47976   854     401 93      3       0       33.91   16.13   16.50   33.46   0.00    0.00    0       8       17      22      0.00    33.33   70.83   91.67   true    true    2579    3       59      280 00113   100.0   1156364 22.5000 242.1385        70.4918 282     301     188     301     19      32.4292 4.0463  37      33      29.5000 36      True    280000113       100.0   115 364     22.5000 242.1385        70.4918 282     301     188     301     19      32.4292 4.0463  37      33      29.5000 36
SRX4563684      silver  Low coverage (85.07x, expect >= 100x)   2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      67      2899294 524852  43273   394
        521     160269  5       0       34.51   15.32   17.49   32.67   0.00    0.00    0       9       28      58      0.00    13.43   41.79   86.57   true    true    2725    3   8       238189696       85.0677 985930  27.5000 241.5890        69.2295 274     301     188     301     19      32.4652 4.0385  37      33      30      36      True    238189696   5.0677  985930  27.5000 241.5890        69.2295 274     301     188     301     19      32.4652 4.0385  37      33      30      36
SRX4563686      silver  Low coverage (90.43x, expect >= 100x)   2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      24      2782895 606699  115953  517 1       1071    289301  4       0       33.60   16.43   16.35   33.63   0.00    0.00    0       8       17      24      0.00    33.33   70.83   100.00  true    true    2568    4   8       253197833       90.42779999999999       1063712 25      238.0325        71.9346 268.5000        301     181     301     19      32.5022 4.0360  37      33.5000 30      36  rue     253197833       90.42779999999999       1063712 25      238.0325        71.9346 268.5000        301     181     301     19      32.5022 4.0360  37      33.5000 30      36
SRX4563634      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      26      2875932 838470  110612  23259   855     346 58      3       0       35.00   15.02   17.62   32.36   0.00    0.00    0       8       16      24      0.00    30.77   61.54   92.31   true    true    2682    5       59      280 00172   100.0001        1135318 25      246.6270        67.9079 293     301     197     301     19      32.2062 4.0878  37      33      29.5000 36      True    280000172       100 0001    1135318 25      246.6270        67.9079 293     301     197     301     19      32.2062 4.0878  37      33      29.5000 36
SRX4563678      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      30      2708907 356005  90296   68738   570     201 73      6       0       34.64   15.50   17.26   32.60   0.00    0.00    0       11      21      29      0.00    36.67   70.00   96.67   true    true    2469    6       55      280 00172   100.0   1196990 20      233.9205        73.6150 258.5000        301     175     301     18.5000 33.2099 3.7695  37      34      31      36.5000 True    280000172       100 0       1196990 20      233.9205        73.6150 258.5000        301     175     301     18.5000 33.2099 3.7695  37      34      31      36.5000
SRX4563634-SE   bronze  Single-end reads        2800000 Staphylococcus aureus   single-end      single-end      SCHEME  ST      42      2866760 804138  68256   21805   506     150 23      5       0       34.79   15.27   17.36   32.58   0.00    0.00    0       10      28      37      0.00    23.81   66.67   88.10   false   true    2665    5       59      280 00172   100.0   1135318 25      246.627 67.9105 294     301     197     301     19      32.2063 4.12132 37      33      30      36      False   280000172       100.0   1135318 25  46.627  67.9105 294     301     197     301     19      32.2063 4.12132 37      33      30      36
SRX4563688      gold    passed all cutoffs      2800000 Staphylococcus aureus   paired-end      paired-end      SCHEME  ST      21      2778300 606249  132300  52250   790     389 17      3       0       33.64   16.33   16.47   33.56   0.00    0.00    0       9       14      19      0.00    42.86   66.67   90.48   true    true    2576    5       58      280 00312   100.0002        1195526 24.5000 234.2070        71.1001 254.5000        301     178     301     18.5000 34.2879 3.3316  37      35.5000 33      37      True    280000312   00.0002 1195526 24.5000 234.2070        71.1001 254.5000        301     178     301     18.5000 34.2879 3.3316  37      35.5000 33      37
```

</details>

<details>
<summary>Example: `bactopia-summary.txt`</summary>

Below is an example of the `bactopia-summary.txt` file. This file is a simple summary
of counts.
```bash
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

</details>

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

<details>
<summary>These cutoffs can be changed</summary>

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

</details>

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
samples using [Bactopia Tools](/bactopia-tools/). These are additional pre-made
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
There is a Bactopia Tool call [staphtyper](/bactopia-tools/staphtyper) that can be used to
run a few tools specific to _S. aureus_ analysis. Let's run our first Bactopia Tool using the
samples in `local-multiple-samples`:

```bash
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

```bash
executor >  local (24)
[ae/f98c1e] STAPHTYPER:AGRVATE:AGRVATE_MODULE (SRX4563688)      [100%] 7 of 7 ✔
[26/28fe35] STAPHTYPER:AGRVATE:CSVTK_CONCAT (agrvate)           [100%] 1 of 1 ✔
[20/752007] STAPHTYPER:SPATYPER:SPATYPER_MODULE (SRX4563680)    [100%] 7 of 7 ✔
[43/9bba69] STAPHTYPER:SPATYPER:CSVTK_CONCAT (spatyper)         [100%] 1 of 1 ✔
[ea/518783] STAPHTYPER:SCCMEC:SCCMEC_MODULE (SRX4563680)        [100%] 7 of 7 ✔
[51/655b71] STAPHTYPER:SCCMEC:CSVTK_CONCAT (sccmec)             [100%] 1 of 1 ✔
WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Tool Execution Summary
-------------------------------
Workflow         : staphtyper
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/workflows/bactopia-tools/staphtyper/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --wf staphtyper --bactopia local-multiple-samples/ -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T12:48:22.408539959-06:00
Duration         : 15.6s
Resumed          : false
Success          : true
Merged Results   : local-multiple-samples//bactopia-runs/staphtyper-20260429-124805


Message of the Day
-------------------------------
When is a door not a door? When it's ajar!
```

Pretty cool (_and fast!_) huh? By just adding `--wf` and `--bactopia` we were able to rapidly
three different _S. aureus_ tools against our samples. In addition, the outputs for each of
these analyses were combined into a single file for easy viewing.

:::tip[Visit `staphtyper` documentation to learn more]
To learn more about `staphtyper` and the outputs it produces, check out the
[staphtyper documentation](/bactopia-tools/staphtyper). It's worth noting,
**all** Bactopia Tools will have a similar documentation page.
:::

* [x] Use Bactopia Tools to:
    * [x] Run *S. aureus* specific analyses
    * [ ] Generate a tree using [Mashtree](/bactopia-tools/mashtree)

### Building a Tree

Now that we've run some _S. aureus_ specific analyses, let's try something a little different.
Let's build a tree using [Mashtree](/bactopia-tools/mashtree), which builds the tree using
Mash distances.

For this tutorial, we are using Mashtree, because it is quick, and if you've made it this
far, you probably want to be done soon!

Let's knock this out using the `local-multiple-samples` samples, but first, let's exclude
the single-end sample `SRX4563634-SE` from the analysis, to demonstrate the usage of `--exclude`.

:::tip[Including and Excluding samples from Bactopia Tool analysis]
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
:::

First, let's create a file with the sample we want to exclude:

```bash
echo "SRX4563634-SE" > exclude.txt
```

Now, we'll run `mashtree` using the `local-multiple-samples` directory, but excluding `SRX4563634-SE`,
using `--exclude` and the `exclude.txt` we just made:

```bash
bactopia \
    --wf mashtree \
    --bactopia local-multiple-samples/ \
    --exclude exclude.txt
```

Not much changed here, by simply changing `staphtyper` to `mashtree` we were able to rapidly
build a tree using Mash distances. Here's the logging information you should see, take notice
where is says 1 was excluded and 6 were included:

```bash
Validating parameters for Bactopia Tools...
Validation complete.
Excluding 1 samples from the analysis
Found 6 samples to process

If this looks wrong, now's your chance to back out (CTRL+C 3 times).
Sleeping for 5 seconds...

--------------------------------------------------------------------
executor >  local (1)
[95/dbe13d] MASHTREE:MASHTREE_MODULE (mashtree) [100%] 1 of 1 ✔
WARN: Graphviz is required to render the execution DAG in the given format -- See http://www.graphviz.org for more info.

--------------------------------------------------------------------

Bactopia Tool Execution Summary
-------------------------------
Workflow         : mashtree
Bactopia Version : 4.0.0
Nextflow Version : 26.04.0
Command Line     : nextflow run /path/to/bactopia/env/workflows/bactopia-tools/mashtree/main.nf -w /home/rpetit3/bactopia-tutorial/work/ -output-format none --wf mashtree --bactopia local-multiple-samples/ --exclude exclude.txt -profile docker
Launch Dir       : /home/rpetit3/bactopia-tutorial
Profile          : docker
Completed At     : 2026-04-29T12:49:37.337015453-06:00
Duration         : 8.4s
Resumed          : false
Success          : true
Merged Results   : local-multiple-samples//bactopia-runs/mashtree-20260429-124927


Message of the Day
-------------------------------
What do you call a sleeping bull? A bulldozer!
```

:::tip[Visit `mashtree` documentation to learn more]
To learn more about `mashtree` and the outputs it produces, check out the
[mashtree documentation](/bactopia-tools/mashtree). Again, each Bactopia
Tool will have a similar documentation page.
:::

### Wrap-up

You did it! I hope with two simple examples, I hope you've gained an appreciation for how
Bactopia Tools can help make things easier for you.

* [x] Use Bactopia Tools to:
    * [x] Run *S. aureus* specific analyses
    * [x] Generate a tree using [Mashtree](/bactopia-tools/mashtree)

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
    * [x] Generate a tree using [Mashtree](/bactopia-tools/mashtree)

Hopefully you have succeeded (yay! 🎉) and would like to use Bactopia on your own data!

Please keep in mind, this tutorial didn't cover how to process Oxford Nanopore reads, or
assemblies. There is so much more we can cover, if there are some you would like to see,
or any issues you might have run into, please let me know by submitting a
[GitHub Issue](https://github.com/bactopia/bactopia/issues).
