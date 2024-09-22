---
title: mlst
description: A Bactopia Tool which uses mlst scan assemblies and determine the sequence type based on PubMLST schemas.
---

The `mlst` module uses [mlst](https://github.com/tseemann/mlst) scan assemblies and determine the sequence type.
It makes use of [PubMLST](https://pubmlst.org/) schemes and by default automatically scans each schema. To specify
a specific scheme to scan, you can provide it with `--scheme`.


## Output Overview

Below is the default output structure for the `mlst` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       └── mlst
│           ├── <SAMPLE_NAME>.tsv
│           └── logs
│               ├── nf-mlst.{begin,err,log,out,run,sh,trace}
│               └── versions.yml
└── bactopia-runs
    └── mlst-<TIMESTAMP>
        ├── merged-results
        │   ├── logs
        │   │   └── mlst-concat
        │   │       ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │   │       └── versions.yml
        │   └── mlst.tsv
        └── nf-reports
            ├── mlst-dag.dot
            ├── mlst-report.html
            ├── mlst-timeline.html
            └── mlst-trace.txt

```



### Results

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


### <i class="fa-xl fas fa-exclamation-circle"></i> MLST 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --scheme` | Don't autodetect, force this scheme on all inputs <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --minid` | Minimum DNA percent identity of full allelle to consider 'similar' <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mincov` | Minimum DNA percent coverage to report partial allele at all <br/>**Type:** `integer`, **Default:** `10` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --minscore` | Minimum score out of 100 to match a scheme <br/>**Type:** `integer`, **Default:** `50` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --nopath` | Strip filename paths from FILE column <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --mlst_db` | A custom MLST database to use, either a tarball or a directory <br/>**Type:** `string` |

## Citations
If you use Bactopia and `mlst` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [mlst](https://github.com/tseemann/mlst)  
    Seemann T [mlst: scan contig files against PubMLST typing schemes](https://github.com/tseemann/mlst) (GitHub)
  
- [PubMLST.org](https://pubmlst.org/)  
    Jolley KA, Bray JE, Maiden MCJ [Open-access bacterial population genomics: BIGSdb software, the PubMLST.org website and their applications.](http://dx.doi.org/10.12688/wellcomeopenres.14826.1) _Wellcome Open Res_ 3, 124 (2018)
  
