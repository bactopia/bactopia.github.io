---
title: Bactopia Tools
description: >-
    More than 60 additional workflows to allow you to easily
    dive further into your Bactopia results.
---
# Overview

After you've run your samples through Bactopia, you are probably going to want to
investigate them some more, or conduct some comparative analyses. That's where
Bactopia Tools come into play!

Bactopia Tools are a set of pre-defined workflows such as pan-genome contruction,
serotyping, and phylogenies. A main benefit of using Bactopia Tools, is they make
use of the predictable output structure of Bactopia to automate analyses. This saves
you valuable time by allowing you to make further use of the 
[many output files](../full-guide.md) to extend your analyses.

### Available Bactopia Tools
There are currently 60 Bactopia Tools that you can make use of.
Below are a list of available Bactopia Tools, grouped as __Subworkflows__ and __Modules__. 

#### Subworkflows (10)

Subworkflows string together tools to create an complete pipeline.  

| Subworkflow | Description |
|-------------|-------------|
| [ariba](ariba.md) | Gene identification through local assemblies |
    | [bakta](bakta.md) | Rapid annotation of bacterial genomes and plasmids |
    | [eggnog](eggnog.md) | Functional annotation of proteins using orthologous groups and phylogenies |
    | [gtdb](gtdb.md) | Identify marker genes and assign taxonomic classifications |
    | [mashtree](mashtree.md) | Quickly create a tree using Mash distances |
    | [merlin](merlin.md) | MinmER assisted species-specific bactopia tool seLectIoN |
    | [pangenome](pangenome.md) | Pangenome analysis with optional core-genome phylogeny |
    | [scrubber](scrubber.md) | Scrub human reads from FASTQ files |
    | [snippy](snippy.md) | Rapid variant calling from Illumina sequence reads with optional core-SNP phylogeny |
    | [staphtyper](staphtyper.md) | Determine the agr, spa and SCCmec types for _Staphylococcus aureus_ genomes |
    

#### Modules  (50)

Modules are workflows consisting of only one tool.

| Module | Description |
|-------------|-------------|
| [abricate](abricate.md) | Mass screening of contigs for antimicrobial and virulence genes |
        | [abritamr](abritamr.md) | A NATA accredited tool for reporting the presence of antimicrobial resistance genes |
        | [agrvate](agrvate.md) | Rapid identification of Staphylococcus aureus agr locus type and agr operon variants. |
        | [amrfinderplus](amrfinderplus.md) | Identify antimicrobial resistance in genes or proteins |
        | [blastn](blastn.md) | Search against nucleotide BLAST databases using nucleotide queries |
        | [blastp](blastp.md) | Search against protein BLAST databases using protein queries |
        | [blastx](blastx.md) | Search against protein BLAST databases using translated nucleotide queries |
        | [bracken](bracken.md) | Estimate taxonomic abundance of samples from Kraken2 results |
        | [btyper3](btyper3.md) | Taxonomic classification of Bacillus cereus group isolates |
        | [busco](busco.md) | Assembly completeness based on evolutionarily informed expectations |
        | [checkm](checkm.md) | Assess the assembly quality of your samples |
        | [ectyper](ectyper.md) | In-silico prediction of _Escherichia coli_ serotype |
        | [emmtyper](emmtyper.md) | emm-typing of _Streptococcus pyogenes_ assemblies |
        | [fastani](fastani.md) | fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI) |
        | [gamma](gamma.md) | Identification, classification, and annotation of translated gene matches |
        | [genotyphi](genotyphi.md) | Salmonella Typhi genotyping with Mykrobe outputs |
        | [hicap](hicap.md) | Identify cap locus serotype and structure in your _Haemophilus influenzae_ assemblies |
        | [hpsuissero](hpsuissero.md) | Serotype prediction of _Haemophilus parasuis_ assemblies |
        | [ismapper](ismapper.md) | Identify insertion sites positions in bacterial genomes |
        | [kleborate](kleborate.md) | Screening Klebsiella genome assemblies for MLST, sub-species, and other related genes of interest |
        | [kraken2](kraken2.md) | Taxonomic classifications of sequence reads |
    | [legsta](legsta.md) | Typing of Legionella pneumophila assemblies |
        | [lissero](lissero.md) | Serogroup typing prediction for _Listeria monocytogenes_ |
        | [mashdist](mashdist.md) | Calculate Mash distances between sequences |
        | [mcroni](mcroni.md) | Sequence variation in mcr-1 genes (mobilized colistin resistance) |
        | [meningotype](meningotype.md) | Serotyping of Neisseria meningitidis |
        | [midas](midas.md) | Estimate species abundances from FASTQ files |
        | [mlst](mlst.md) | Automatic MLST calling from assembled contigs |
        | [mobsuite](mobsuite.md) | Reconstruct and annotate plasmids in bacterial assemblies |
        | [mykrobe](mykrobe.md) | Antimicrobial resistance detection for specific species |
        | [ngmaster](ngmaster.md) | Multi-antigen sequence typing for _Neisseria gonorrhoeae_ |
        | [pasty](pasty.md) | in silico serogrouping of Pseudomonas aeruginosa isolates |
        | [pbptyper](pbptyper.md) | Penicillin Binding Protein (PBP) typer for Streptococcus pneumoniae |
        | [phispy](phispy.md) | Predict prophages in bacterial genomes |
        | [plasmidfinder](plasmidfinder.md) | Plasmid identification from assemblies |
        | [pneumocat](pneumocat.md) | Assign capsular type to Streptococcus pneumoniae from sequence reads |
        | [quast](quast.md) | A module for assessing the quality of assembled contigs |
        | [rgi](rgi.md) | Predict antibiotic resistance from assemblies |
        | [seqsero2](seqsero2.md) | Salmonella serotype prediction from reads or assemblies |
        | [seroba](seroba.md) | Serotyping of Streptococcus pneumoniae from sequence reads |
        | [shigatyper](shigatyper.md) | Shigella serotype from Illumina or Oxford Nanopore reads |
        | [shigeifinder](shigeifinder.md) | Shigella and EIEC serotyping from assemblies |
        | [sistr](sistr.md) | Serovar prediction of Salmonella assemblies |
        | [spatyper](spatyper.md) | Computational method for finding spa types in _Staphylococcus aureus_ |
        | [ssuissero](ssuissero.md) | Serotype prediction of _Streptococcus suis_ assemblies |
        | [staphopiasccmec](staphopiasccmec.md) | Primer based SCCmec typing of _Staphylococcus aureus_ genomes |
        | [stecfinder](stecfinder.md) | Serotype of Shigatoxin producing E. coli using Illumina reads or assemblies |
        | [tblastn](tblastn.md) | Search against translated nucleotide BLAST databases using protein queries |
        | [tblastx](tblastx.md) | Search against translated nucleotide databases using a translated nucleotide query |
        | [tbprofiler](tbprofiler.md) | Detect resistance and lineages of _Mycobacterium tuberculosis_ genomes |
        

### Common Inputs

With the exceptions of the `summary` tool, each Bactopia Tool will use the following 
input parameters:
```
    --bactopia STR          Directory containing Bactopia analysis results for all samples.

    --exclude STR           A text file containing sample names to exclude from the
                                analysis. The expected format is a single sample per line.

    --include STR           A text file containing sample names to include in the
                                analysis. The expected format is a single sample per line.
```

#### `--bactopia`

This parameter tells each tool where to find your Bactopia outputs from your project. 
Using this path, the tool will identify the required inputs and begin analysis. What 
this means is there is no need for you to wrangle up input files for comparative analyses.

#### `--exclude`

What `--exclude` allows is for you to give a text file with a list of samples to 
exclude from further analyses. While you can produce this list yourself, the
`summary` tool will produce a list of samples that do not pass certain thresholds.
These thresholds are based on read lengths, sequence quality, coverage and assembly
quality. You can adjust these thresholds to meet your needs.

#### `--include`

Similarly, `--include` allows you to give a text file with a list of samples to be 
included in the analysis. This allows you to target your analyses on a specific subset
of samples. An example of this may be to use the `fastani` tool to determine samples
with >95% ANI to a reference, then create a pan-genome with the `pangenome` tool using 
only the subset of samples.

### nf-core/modules Availabilty

Good news! All Bactopia Tools are also available through [nf-core/modules](https://github.com/nf-core/modules),
a repository of ready to use Nextflow DSL2 modules. This means you can leverage nf-core tools 
to rapidly string together your own workflows. 

Many of the above Bactopia Tools were submitted to [nf-core/modules](https://github.com/nf-core/modules) 
as part of [Bactopia V2](https://github.com/bactopia/bactopia/issues/233). The [nf-core Team](https://nf-co.re/about)
is a fun group to work with so expect many more Bactopia Tools to find their way to 
[nf-core/modules](https://github.com/nf-core/modules)!

_Thank you modules team!_

### Suggest A Tool

Do you have an idea or suggestion for an analysis that should be added to the set 
of Bactopia Tools? If so, please feel free to submit it to 
[Bactopia GitHub Issues](https://github.com/bactopia/bactopia/issues)!