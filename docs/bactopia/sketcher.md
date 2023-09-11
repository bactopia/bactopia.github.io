---
title: sketcher
description: A Bactopia Tool which uses Mash and Sourmash to create sketches and query RefSeq and GTDB.

---

The `sketcher` module uses [Mash](https://github.com/marbl/Mash) and
[Sourmash](https://github.com/dib-lab/sourmash) to create sketches and query
[RefSeq](https://www.ncbi.nlm.nih.gov/refseq/) and [GTDB](https://gtdb.ecogenomic.org/).


## Output Overview

Below is the default output structure for the `sketcher` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── main
│       └── sketcher
│           ├── logs
│           │   ├── nf-sketcher.{begin,err,log,out,run,sh,trace}
│           │   └── versions.yml
│           ├── <SAMPLE_NAME>-k{21|31}.msh
│           ├── <SAMPLE_NAME>-mash-refseq88-k21.txt
│           ├── <SAMPLE_NAME>-sourmash-gtdb-rs207-k31.txt
│           └── <SAMPLE_NAME>.sig
└── bactopia-runs
    └── bactopia-<TIMESTAMP>
        └── nf-reports
            ├── bactopia-dag.dot
            ├── bactopia-report.html
            ├── bactopia-timeline.html
            └── bactopia-trace.txt

```



### Results

#### sketcher

Below is a description of the _per-sample_ results from the `sketcher` subworkflow.


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-k{21\|31}.msh | A Mash sketch of the input assembly for k=21 and k=31 |
| &lt;SAMPLE_NAME&gt;-mash-refseq88-k21.txt | The results of querying the Mash sketch against RefSeq88 |
| &lt;SAMPLE_NAME&gt;-sourmash-gtdb-rs207-k31.txt | The results of querying the Sourmash sketch against GTDB-rs207 |
| &lt;SAMPLE_NAME&gt;.sig | A Sourmash sketch of the input assembly for k=21, k=31, and k=51 |








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


### <i class="fa-xl fas fa-exclamation-circle"></i> Sketcher 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-hashtag"></i>` --sketch_size` | Sketch size. Each sketch will have at most this many non-redundant min-hashes. <br/>**Type:** `integer`, **Default:** `10000` |
| <i class="fa-lg fas fa-hashtag"></i>` --sourmash_scale` | Choose number of hashes as 1 in FRACTION of input k-mers <br/>**Type:** `integer`, **Default:** `10000` |
| <i class="fa-lg fas fa-fast-forward"></i>` --no_winner_take_all` | Disable winner-takes-all strategy for identity estimates <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-hashtag"></i>` --screen_i` | Minimum identity to report. <br/>**Type:** `number`, **Default:** `0.8` |

## Citations
If you use Bactopia and `sketcher` in your analysis, please cite the following.

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
  
