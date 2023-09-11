---
title: assembler
description: A Bactopia Tool which uses a variety of assembly tools to create an assembly of Illumina and Oxford Nanopore reads.

---

The `assembler` module uses a variety of assembly tools to create an assembly of
Illumina and Oxford Nanopore reads. The tools used are:

| Tool | Description |
|------|-------------|
| [Dragonflye](https://github.com/rpetit3/dragonflye) | Assembly of Oxford Nanopore reads, as well as hybrid assembly with short-read polishing |
| [Shovill](https://github.com/tseemann/shovill) | Assembly of Illumina paired-end reads |
| [Shovill-SE](https://github.com/rpetit/shovill) | Assembly of Illumina single-end reads |
| [Unicycler](https://github.com/rrwick/Unicycler) | Hybrid assembly, using short-reads first then long-reads |

Summary statistics for each assembly are generated using [assembly-scan](https://github.com/rpetit3/assembly-scan).


## Output Overview

Below is the default output structure for the `assembler` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── main
│       └── assembler
│           ├── flash.{hist|histogram}
|           |   flye.info
│           ├── logs
│           │   ├── {dragonflye|shovill|unicycler}.log
│           │   ├── nf-assembler.{begin,err,log,out,run,sh,trace}
│           │   └── versions.yml
│           ├── <SAMPLE_NAME>.fna.gz
│           ├── <SAMPLE_NAME>.tsv
│           ├── <SAMPLE_NAME>-assembly-error.txt
│           ├── shovill.corrections
│           ├── {flye|miniasm|raven|unicycler}-unpolished.fasta.gz
│           └── {flye|megahit|miniasm|raven|spades|unicycler|velvet}-unpolished.gfa.gz
└── bactopia-runs
    └── bactopia-<TIMESTAMP>
        ├── merged-results
        │   ├── assembly-scan.tsv
        │   └── logs
        │       └── assembly-scan-concat
        │           ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │           └── versions.yml
        └── nf-reports
            ├── bactopia-dag.dot
            ├── bactopia-report.html
            ├── bactopia-timeline.html
            └── bactopia-trace.txt

```

!!! info "Directory structure might be different"

    Depending on the options used at runtime, the `assembler` directory structure might
    be different, but the output descriptions below still apply.



### Results

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


| Extension                     | Description |
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


### <i class="fa-xl fas fa-exclamation-circle"></i> Assembler 


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

## Citations
If you use Bactopia and `assembler` in your analysis, please cite the following.

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
  
