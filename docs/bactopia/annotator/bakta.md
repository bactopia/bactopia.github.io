---
title: bakta
description: A Bactopia Tool which uses Bakta to rapidly provide extensive annotations (tRNA, tmRNA, rRNA, ncRNA, CRISPR, CDS, pseudogenes, and sORFs) in a standardized fashion.
---

The `bakta` module uses [Bakta](https://github.com/oschwengers/bakta) to rapidly annotate bacterial 
genomes and plasmids in a standardized fashion. Bakta makes use of a large database ([40+ GB](https://doi.org/10.5281/zenodo.4247252))
to provide extensive annotations including: tRNA, tmRNA, rRNA, ncRNA, CRISPR, CDS, and sORFs.


## Output Overview

Below is the default output structure for the `bakta` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── main
│       └── annotator
│           └── bakta
│               ├── <SAMPLE_NAME>-blastdb.tar.gz
│               ├── <SAMPLE_NAME>.embl.gz
│               ├── <SAMPLE_NAME>.faa.gz
│               ├── <SAMPLE_NAME>.ffn.gz
│               ├── <SAMPLE_NAME>.fna.gz
│               ├── <SAMPLE_NAME>.gbff.gz
│               ├── <SAMPLE_NAME>.gff3.gz
│               ├── <SAMPLE_NAME>.hypotheticals.faa.gz
│               ├── <SAMPLE_NAME>.hypotheticals.tsv
│               ├── <SAMPLE_NAME>.tsv
│               ├── <SAMPLE_NAME>.txt
│               └── logs
│                   ├── nf-bakta.{begin,err,log,out,run,sh,trace}
│                   └── versions.yml
└── bactopia-runs
    └── bakta-<TIMESTAMP>
        └── nf-reports
            ├── bakta-dag.dot
            ├── bakta-report.html
            ├── bakta-timeline.html
            └── bakta-trace.txt

```



### Results

#### Bakta

Below is a description of the _per-sample_ results from [Bakta](https://github.com/oschwengers/bakta).


| Extension                     | Description |
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


### <i class="fa-xl fas fa-exclamation-circle"></i> Bakta Download 


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-alt"></i>` --bakta_db` | Tarball or path to the Bakta database <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --bakta_db_type` | Which Bakta DB to download 'full' (~30GB) or 'light' (~2GB) <br/>**Type:** `string`, **Default:** `full` |
| <i class="fa-lg fas fa-file-alt"></i>` --bakta_save_as_tarball` | Save the Bakta database as a tarball <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --download_bakta` | Download the Bakta database to the path given by --bakta_db <br/>**Type:** `boolean` |

### <i class="fa-xl fas fa-exclamation-circle"></i> Bakta 


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

## Citations
If you use Bactopia and `bakta` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Bakta](https://github.com/oschwengers/bakta)  
    Schwengers O, Jelonek L, Dieckmann MA, Beyvers S, Blom J, Goesmann A [Bakta - rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.](https://doi.org/10.1099/mgen.0.000685) _Microbial Genomics_ 7(11) (2021)
  
