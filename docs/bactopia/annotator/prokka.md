---
title: stecfinder
description: A Bactopia Tool which uses Prokka to rapidly provide annotations in a standardized fashion.
---

The `prokka` module uses [Prokka](https://github.com/tseemann/prokka) to rapidly annotate bacterial 
genomes in a standardized fashion.


## Output Overview

Below is the default output structure for the `prokka` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── main
│       └── annotator
│           └── prokka
│               ├── <SAMPLE_NAME>-blastdb.tar.gz
│               ├── <SAMPLE_NAME>.faa.gz
│               ├── <SAMPLE_NAME>.ffn.gz
│               ├── <SAMPLE_NAME>.fna.gz
│               ├── <SAMPLE_NAME>.fsa.gz
│               ├── <SAMPLE_NAME>.gbk.gz
│               ├── <SAMPLE_NAME>.gff.gz
│               ├── <SAMPLE_NAME>.sqn.gz
│               ├── <SAMPLE_NAME>.tbl.gz
│               ├── <SAMPLE_NAME>.tsv
│               ├── <SAMPLE_NAME>.txt
│               └── logs
│                   ├── <SAMPLE_NAME>.{err|log}
│                   ├── nf-prokka.{begin,err,log,out,run,sh,trace}
│                   └── versions.yml
└── bactopia-runs
    └── prokka-<TIMESTAMP>
        └── nf-reports
            ├── prokka-dag.dot
            ├── prokka-report.html
            ├── prokka-timeline.html
            └── prokka-trace.txt

```



### Results

#### Prokka

Below is a description of the _per-sample_ results from [Prokka](https://github.com/tseemann/prokka).


| Extension                     | Description |
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


### <i class="fa-xl fas fa-exclamation-circle"></i> Prokka 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-alt"></i>` --proteins` | FASTA file of trusted proteins to first annotate from <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --prodigal_tf` | Training file to use for Prodigal <br/>**Type:** `string` |
| <i class="fa-lg fas fa-check"></i>` --compliant` | Force Genbank/ENA/DDJB compliance <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-school"></i>` --centre` | Sequencing centre ID <br/>**Type:** `string`, **Default:** `Bactopia` |
| <i class="fa-lg fas fa-hashtag"></i>` --prokka_coverage` | Minimum coverage on query protein <br/>**Type:** `integer`, **Default:** `80` |
| <i class="fa-lg fas fa-italic"></i>` --prokka_evalue` | Similarity e-value cut-off <br/>**Type:** `string`, **Default:** `1e-09` |
| <i class="fa-lg fas fa-italic"></i>` --prokka_opts` | Extra Prokka options in quotes. <br/>**Type:** `string` |

## Citations
If you use Bactopia and `prokka` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Prokka](https://github.com/tseemann/prokka)  
    Seemann T [Prokka: rapid prokaryotic genome annotation](http://dx.doi.org/10.1093/bioinformatics/btu153) _Bioinformatics_ 30, 2068–2069 (2014)
  
