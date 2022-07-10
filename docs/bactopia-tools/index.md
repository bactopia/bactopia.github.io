# Overview
After you've run your samples through Bactopia, you are probably going to want to
investigate them some more, or conduct some comparative analyses. That's where
Bactopia Tools come into play!

Bactopia Tools are a set of predifined workflows such as pan-genome contruction,
serotyping, and phylogenies. A main benefit of using Bactopia Tools, is they make
use of the predictable output structure of Bactopia to automate analyses. This saves
you valuable time by allowing you to make further use of the 
[many output files](output-overview/) to extend your analyses.

### Available Bactopia Tools
There are currently 44 Bactopia Tools that you can make use of.
Below are a list of available Bactopia Tools, grouped as __Subworkflows__ and __Modules__. 

#### Subworkflows (8)
Subworkflows string together 
tools to create an complete pipeline.  

| Subworkflow | Description |
|-------------|-------------|
| [ariba](/bactopia-tools/ariba/) | Gene identification through local assemblies |
    | [bakta](/bactopia-tools/bakta/) | Rapid annotation of bacterial genomes and plasmids |
    | [eggnog](/bactopia-tools/eggnog/) | Functional annotation of proteins using orthologous groups and phylogenies |
    | [gtdb](/bactopia-tools/gtdb/) | Identify marker genes and assign taxonomic classifications |
    | [merlin](/bactopia-tools/merlin/) | MinmER assisted species-specific bactopia tool seLectIoN |
    | [pangenome](/bactopia-tools/pangenome/) | Pangenome analysis with optional core-genome phylogeny |
    | [snippy](/bactopia-tools/snippy/) | Rapid variant calling from Illumina sequence reads with optional core-SNP phylogeny |
    | [staphtyper](/bactopia-tools/staphtyper/) | Determine the agr, spa and SCCmec types for _Staphylococcus aureus_ genomes |
    

#### Modules  (36)
Modules are workflows consisting of only one tool.

| Module | Description |
|-------------|-------------|
| [abricate](/bactopia-tools/abricate/) | Mass screening of contigs for antimicrobial and virulence genes |
    | [agrvate](/bactopia-tools/agrvate/) | Rapid identification of Staphylococcus aureus agr locus type and agr operon variants. |
    | [amrfinderplus](/bactopia-tools/amrfinderplus/) | Identify antimicrobial resistance in genes or proteins |
    | [busco](/bactopia-tools/busco/) | Assembly completeness based on evolutionarily informed expectations |
    | [checkm](/bactopia-tools/checkm/) | Assess the assembly quality of your samples |
    | [ectyper](/bactopia-tools/ectyper/) | In-silico prediction of _Escherichia coli_ serotype |
    | [emmtyper](/bactopia-tools/emmtyper/) | emm-typing of _Streptococcus pyogenes_ assemblies |
    | [fastani](/bactopia-tools/fastani/) | fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI) |
    | [gamma](/bactopia-tools/gamma/) | Identification, classification, and annotation of translated gene matches |
    | [genotyphi](/bactopia-tools/genotyphi/) | Salmonella Typhi genotyping with Mykrobe outputs |
    | [hicap](/bactopia-tools/hicap/) | Identify cap locus serotype and structure in your _Haemophilus influenzae_ assemblies |
    | [hpsuissero](/bactopia-tools/hpsuissero/) | Serotype prediction of _Haemophilus parasuis_ assemblies |
    | [ismapper](/bactopia-tools/ismapper/) | Identify insertion sites positions in bacterial genomes |
    | [kleborate](/bactopia-tools/kleborate/) | Screening Klebsiella genome assemblies for MLST, sub-species, and other related genes of interest |
    | [kraken](/bactopia-tools/kraken/) | Taxonomic classifications of sequence reads |
    | [legsta](/bactopia-tools/legsta/) | Typing of Legionella pneumophila assemblies |
    | [lissero](/bactopia-tools/lissero/) | Serogroup typing prediction for _Listeria monocytogenes_ |
    | [mashdist](/bactopia-tools/mashdist/) | Calculate Mash distances between sequences |
    | [mashtree](/bactopia-tools/mashtree/) | Quickly create a tree using Mash distances |
    | [mcroni](/bactopia-tools/mcroni/) | Sequence variation in mcr-1 genes (mobilized colistin resistance) |
    | [meningotype](/bactopia-tools/meningotype/) | Serotyping of Neisseria meningitidis |
    | [mlst](/bactopia-tools/mlst/) | Automatic MLST calling from assembled contigs |
    | [mobsuite](/bactopia-tools/mobsuite/) | Reconstruct and annotate plasmids in bacterial assemblies |
    | [mykrobe](/bactopia-tools/mykrobe/) | Antimicrobial resistance detection for specific species |
    | [ngmaster](/bactopia-tools/ngmaster/) | Multi-antigen sequence typing for _Neisseria gonorrhoeae_ |
    | [plasmidfinder](/bactopia-tools/plasmidfinder/) | Plasmid identification from assemblies |
    | [prokka](/bactopia-tools/prokka/) | Whole genome annotation of small genomes (bacterial, archeal, viral) |
    | [rgi](/bactopia-tools/rgi/) | Predict antibiotic resistance from assemblies |
    | [seqsero2](/bactopia-tools/seqsero2/) | Salmonella serotype prediction from reads or assemblies |
    | [seroba](/bactopia-tools/seroba/) | Serotyping of Streptococcus pneumoniae from sequence reads |
    | [shigatyper](/bactopia-tools/shigatyper/) | Shigella serotype from Illumina or Oxford Nanopore reads |
    | [sistr](/bactopia-tools/sistr/) | Serovar prediction of Salmonella assemblies |
    | [spatyper](/bactopia-tools/spatyper/) | Computational method for finding spa types in _Staphylococcus aureus_ |
    | [ssuissero](/bactopia-tools/ssuissero/) | Serotype prediction of _Streptococcus suis_ assemblies |
    | [staphopiasccmec](/bactopia-tools/staphopiasccmec/) | Primer based SCCmec typing of _Staphylococcus aureus_ genomes |
    | [tbprofiler](/bactopia-tools/tbprofiler/) | Detect resistance and lineages of _Mycobacterium tuberculosis_ genomes |
    

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
What `--exclude` allows is for you to give a text file with a list of samples that 
*should probably* be excluded from further analyses. While you can produce this list
yourself, the `summary` tool will produce a list of samples that do not pass certain 
thresholds. These thresholds are based on read lengths, sequence quality, coverage 
and assembly quality. You can adjust these thresholds to meet your needs.

#### `--include`
Similarly, `--include` allows you to give a text file with a list of samples to be 
included in the analysis. This allows you to target your anlyses on a specific subset
of samples. An example of this may be to use the `fastani` tool to determine samples
with >95% ANI to a reference, then create a pan-genome with the `roary` tool using 
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