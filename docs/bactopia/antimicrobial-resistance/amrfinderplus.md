---
title: amrfinderplus
description: A Bactopia Tool which uses AMRFinder+ to screen assemblies and proteins for antimicrobial resistance and virulence genes.
---

The `amrfinderplus` module uses [AMRFinder+](https://github.com/ncbi/amr) to screen assemblies and proteins
for antimicrobial resistance and virulence genes.


## Output Overview

Below is the default output structure for the `amrfinderplus` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── amrfinderplus
│           ├── <SAMPLE_NAME>-genes.tsv
│           ├── <SAMPLE_NAME>-proteins.tsv
│           └── logs
│               ├── nf-amrfinderplus.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── amrfinderplus-<TIMESTAMP>
        ├── merged-results
        │   ├── amrfinderplus-genes.tsv
        │   ├── amrfinderplus-proteins.tsv
        │   └── logs
        │       └── amrfinderplus-{genes|proteins|-concat
        │           ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │           └── versions.yml
        └── nf-reports
            ├── amrfinderplus-dag.dot
            ├── amrfinderplus-report.html
            ├── amrfinderplus-timeline.html
            └── amrfinderplus-trace.txt

```



### Results

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| amrfinderplus-genes.tsv | A merged TSV file with `AMRFinder+` results using nucleotide inputs |
| amrfinderplus-proteins.tsv | A merged TSV file with `AMRFinder+` results using protein inputs |






#### AMRFinder+

Below is a description of the _per-sample_ results from [AMRFinder+](https://github.com/ncbi/amr).


| Extension                     | Description |
|-------------------------------|-------------|
| -genes.tsv | A TSV file with `AMRFinder+` results using nucleotide inputs |
| -proteins.tsv | A TSV file with `AMRFinder+` results using protein inputs |








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


### <i class="fa-xl fas fa-exclamation-circle"></i> AMRFinder+ 


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
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --amrfinder_db` | A custom AMRFinder+ database to use, either a tarball or a folder <br/>**Type:** `string` |

## Citations
If you use Bactopia and `amrfinderplus` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [AMRFinderPlus](https://github.com/ncbi/amr)  
    Feldgarden M, Brover V, Haft DH, Prasad AB, Slotta DJ, Tolstoy I, Tyson GH, Zhao S, Hsu C-H, McDermott PF, Tadesse DA, Morales C, Simmons M, Tillman G, Wasilenko J, Folster JP, Klimke W [Validating the NCBI AMRFinder Tool and Resistance Gene Database Using Antimicrobial Resistance Genotype-Phenotype Correlations in a Collection of NARMS Isolates](https://doi.org/10.1128/AAC.00483-19). _Antimicrob. Agents Chemother._ (2019)
  
- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
