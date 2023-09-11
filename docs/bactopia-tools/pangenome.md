---
title: pangenome
description: A Bactopia Tool which creates a pangenome, then a core-genome phylogeny with multiple different tools.
---
# Bactopia Tool - `pangenome`
The `pangenome` subworkflow allows you to create a pan-genome with [PIRATE](https://github.com/SionBayliss/PIRATE),
[Panaroo](https://github.com/gtonkinhill/panaroo), or [Roary](https://github.com/sanger-pathogens/Roary)) of your samples.

You can further supplement your pan-genome by including completed genomes. This is possible using the `--species` 
or `--accessions` parameters. If used, [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) will 
download available completed genomes available from RefSeq. Any downloaded genomes will be annotated with 
[Prokka](https://github.com/tseemann/prokka) to create compatible GFF3 files.

A phylogeny, based on the core-genome alignment, will be created by [IQ-Tree](https://github.com/Cibiv/IQ-TREE). Optionally
a recombination-masked core-genome alignment can be created with [ClonalFrameML](https://github.com/xavierdidelot/ClonalFrameML)
and [maskrc-svg](https://github.com/kwongj/maskrc-svg).

Finally, the core genome pair-wise SNP distance for each sample is also calculated with 
[snp-dists](https://github.com/tseemann/snp-dists) and additional pan-genome wide association studies can be conducted 
using [Scoary](https://github.com/AdmiralenOla/Scoary).


## Example Usage
```
bactopia --wf pangenome \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `pangenome` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
<BACTOPIA_DIR>
└── bactopia-runs
    └── pangenome-<TIMESTAMP>
        ├── clonalframeml
        │   ├── core-genome.ML_sequence.fasta
        │   ├── core-genome.em.txt
        │   ├── core-genome.emsim.txt
        │   ├── core-genome.importation_status.txt
        │   ├── core-genome.labelled_tree.newick
        │   ├── core-genome.position_cross_reference.txt
        │   └── logs
        │       ├── nf-clonalframeml.{begin,err,log,out,run,sh,trace}
        │       └── versions.yml
        ├── core-genome.aln.gz
        ├── core-genome.distance.tsv
        ├── core-genome.iqtree
        ├── core-genome.masked.aln.gz
        ├── iqtree
        │   ├── core-genome.alninfo
        │   ├── core-genome.bionj
        │   ├── core-genome.ckp.gz
        │   ├── core-genome.contree
        │   ├── core-genome.mldist
        │   ├── core-genome.splits.nex
        │   ├── core-genome.treefile
        │   ├── core-genome.ufboot
        │   └── logs
        │       ├── core-genome.log
        │       ├── nf-iqtree.{begin,err,log,out,run,sh,trace}
        │       └── versions.yml
        ├── iqtree-fast
        │   ├── logs
        │   │   ├── nf-iqtree-fast.{begin,err,log,out,run,sh,trace}
        │   │   ├── start-tree.log
        │   │   └── versions.yml
        │   ├── start-tree.bionj
        │   ├── start-tree.ckp.gz
        │   ├── start-tree.iqtree
        │   ├── start-tree.mldist
        │   ├── start-tree.model.gz
        │   └── start-tree.treefile
        ├── nf-reports
        │   ├── pangenome-dag.dot
        │   ├── pangenome-report.html
        │   ├── pangenome-timeline.html
        │   └── pangenome-trace.txt
        ├── panaroo
        │   ├── aligned_gene_sequences
        │   ├── alignment_entropy.csv
        │   ├── combined_DNA_CDS.fasta
        │   ├── combined_protein_CDS.fasta
        │   ├── combined_protein_cdhit_out.txt
        │   ├── combined_protein_cdhit_out.txt.clstr
        │   ├── core_alignment_filtered_header.embl
        │   ├── core_alignment_header.embl
        │   ├── core_gene_alignment_filtered.aln
        │   ├── final_graph.gml
        │   ├── gene_data.csv
        │   ├── gene_presence_absence.Rtab
        │   ├── gene_presence_absence.csv
        │   ├── gene_presence_absence_roary.csv
        │   ├── logs
        │   │   ├── nf-panaroo.{begin,err,log,out,run,sh,trace}
        │   │   └── versions.yml
        │   ├── pan_genome_reference.fa
        │   ├── pre_filt_graph.gml
        │   ├── struct_presence_absence.Rtab
        │   └── summary_statistics.txt
        ├── pirate
        │   ├── PIRATE.gene_families.ordered.tsv
        │   ├── PIRATE.gene_families.tsv
        │   ├── PIRATE.genomes_per_allele.tsv
        │   ├── PIRATE.pangenome_summary.txt
        │   ├── PIRATE.unique_alleles.tsv
        │   ├── binary_presence_absence.fasta.gz
        │   ├── binary_presence_absence.nwk
        │   ├── cluster_alleles.tab
        │   ├── co-ords
        │   │   └── <SAMPLE_NAME>.co-ords.tab
        │   ├── core_alignment.fasta.gz
        │   ├── core_alignment.gff
        │   ├── feature_sequences
        │   │   └── <GENE_FAMILY>.{aa|nucleotide|.fasta.gz
        │   ├── gene_presence_absence.csv
        │   ├── genome2loci.tab
        │   ├── genome_list.txt
        │   ├── loci_list.tab
        │   ├── loci_paralog_categories.tab
        │   ├── logs
        │   │   ├── nf-pirate.{begin,err,log,out,run,sh,trace}
        │   │   ├── results
        │   │   │   ├── PIRATE.log
        │   │   │   ├── link_clusters.log
        │   │   │   └── split_groups.log
        │   │   └── versions.yml
        │   ├── modified_gffs
        │   ├── pan_sequences.fasta.gz
        │   ├── pangenome.connected_blocks.tsv
        │   ├── pangenome.edges
        │   ├── pangenome.gfa
        │   ├── pangenome.order.tsv
        │   ├── pangenome.reversed.tsv
        │   ├── pangenome.syntenic_blocks.tsv
        │   ├── pangenome.temp
        │   ├── pangenome_alignment.fasta.gz
        │   ├── pangenome_alignment.gff
        │   ├── pangenome_iterations
        │   │   ├── pan_sequences.{50|60|70|80|90|95|98}.reclustered.reinflated
        │   │   ├── pan_sequences.blast.output
        │   │   ├── pan_sequences.cdhit_clusters
        │   │   ├── pan_sequences.core_clusters.tab
        │   │   ├── pan_sequences.mcl_log.txt
        │   │   └── pan_sequences.representative.fasta.gz
        │   ├── pangenome_log.txt
        │   ├── paralog_clusters.tab
        │   ├── representative_sequences.faa
        │   └── representative_sequences.ffn
        ├── roary
        │   ├── accessory.header.embl
        │   ├── accessory.tab
        │   ├── accessory_binary_genes.fa.gz
        │   ├── accessory_binary_genes.fa.newick
        │   ├── accessory_graph.dot
        │   ├── blast_identity_frequency.Rtab
        │   ├── clustered_proteins
        │   ├── core_accessory.header.embl
        │   ├── core_accessory.tab
        │   ├── core_accessory_graph.dot
        │   ├── core_alignment_header.embl
        │   ├── gene_presence_absence.Rtab
        │   ├── gene_presence_absence.csv
        │   ├── logs
        │   │   ├── nf-roary.{begin,err,log,out,run,sh,trace}
        │   │   └── versions.yml
        │   ├── number_of_conserved_genes.Rtab
        │   ├── number_of_genes_in_pan_genome.Rtab
        │   ├── number_of_new_genes.Rtab
        │   ├── number_of_unique_genes.Rtab
        │   ├── pan_genome_reference.fa.gz
        │   └── summary_statistics.txt
        └── snpdists
            └── logs
                ├── nf-snpdists.{begin,err,log,out,run,sh,trace}
                └── versions.yml

```



### Results

#### Main Results

Below are main results of the `pangenome` Bactopia Tool.


| Filename                      | Description |
|-------------------------------|-------------|
| core-genome.aln.gz | A multiple sequence alignment FASTA of the core genome |
| core-genome.distance.tsv | Core genome pair-wise SNP distance for each sample |
| core-genome.iqtree | Full result of the IQ-TREE core genome phylogeny |
| core-genome.masked.aln.gz | A core-genome alignment with the recombination masked |


#### ClonalFrameML

Below is a description of the [ClonalFrameML](https://github.com/xavierdidelot/ClonalFrameML) results. For more details about
ClonalFrameML outputs see [ClonalFrameML - Outputs](https://github.com/xavierdidelot/clonalframeml/wiki#output).


| Filename                      | Description |
|-------------------------------|-------------|
| core-genome.ML_sequence.fasta | The sequence reconstructed by maximum likelihood for all internal nodes of the phylogeny, as well as for all missing data in the input sequences |
| core-genome.em.txt | The point estimates for R/theta, nu, delta and the branch lengths |
| core-genome.emsim.txt | The bootstrapped values for the three parameters R/theta, nu and delta |
| core-genome.importation_status.txt | The list of reconstructed recombination events |
| core-genome.labelled_tree.newick | The output tree with all nodes labelled so that they can be referred to in other files |
| core-genome.position_cross_reference.txt | A vector of comma-separated values indicating for each location in the input sequence file the corresponding position in the sequences in the output *ML_sequence.fasta* file |


#### IQ-TREE

Below is a description of the [IQ-TREE](http://www.iqtree.org/) results. If ClonalFrameML is executed, a fast tree
is created and given the prefix `start-tree`, the final tree has the prefix `core-genome`. For more details about
IQ-TREE outputs see [IQ-TREE - Outputs](https://github.com/Cibiv/IQ-TREE/wiki/Web-Server-Tutorial#analysis-results).


| Filename                      | Description |
|-------------------------------|-------------|
| core-genome.alninfo | Alignment site statistics |
| {core-genome,start-tree}.bionj | A neighbor joining tree produced by BIONJ |
| {core-genome,start-tree}.ckp.gz | IQ-TREE writes a checkpoint file |
| core-genome.contree | Consensus tree with assigned branch supports where branch lengths are optimized on the original alignment; printed if Ultrafast Bootstrap is selected |
| {core-genome,start-tree}.mldist | Contains the likelihood distances |
| {core-genome,start-tree}.model.gz | Information about all models tested |
| core-genome.splits.nex | Support values in percentage for all splits (bipartitions), computed as the occurence frequencies in the bootstrap trees |
| {core-genome,start-tree}.treefile | Maximum likelihood tree in NEWICK format, can be visualized with treeviewer programs |
| core-genome.ufboot | Trees created during the bootstrap steps |


#### PIRATE

Below is a description of the [PIRATE](https://github.com/SionBayliss/PIRATE) results. For more details about
PIRATE outputs see [PIRATE - Output files](https://github.com/SionBayliss/PIRATE#output-files).

!!! note "Available by default"

    By default PIRATE is used to create the pan-genome. If `--use_panaroo` or `--use_roary` are given, `pirate` outputs will
    not be available only Panaroo or Roary outputs.


| Filename                      | Description |
|-------------------------------|-------------|
| PIRATE.gene_families.ordered.tsv | Tabular summary of all gene families ordered on syntenic regions in the pangenome graph |
| PIRATE.gene_families.tsv | Tabular summary of all gene families |
| PIRATE.genomes_per_allele.tsv | A list of genomes associated with each allele |
| PIRATE.pangenome_summary.txt | Short summary of the number and frequency of genes in the pangenome |
| PIRATE.unique_alleles.tsv | Tabular summary of all unique alleles of each gene family |
| binary_presence_absence.{fasta.gz,nwk} | A tree (.nwk) generated by fasttree from binary gene_family presence-absence data and the fasta file used to create it |
| cluster_alleles.tab | List of alleles in paralogous clusters |
| co-ords/${SAMPLE_NAME}.co-ords.tab | Gene feature co-ordinates for each sample |
| core_alignment.fasta.gz | Gene-by-gene nucleotide alignments of the core genome created using MAFFT |
| core_alignment.gff | Annotation containing the position of the gene family within the core genome alignment |
| feature_sequences/${GENE_FAMILY}.{aa|nucleotide}.fasta | Amino acid and nucleotide sequences for each gene family |
| gene_presence_absence.csv | Lists each gene and which samples it is present in |
| genome2loci.tab | List of loci for each genome |
| genome_list.txt | List of genomes in the analysis |
| loci_list.tab | List of loci and their associated genomes |
| loci_paralog_categories.tab | Concatenation of classified paralogs |
| modified_gffs/${SAMPLE_NAME}.gff | GFF3 files which have been standardised for PIRATE |
| pan_sequences.fasta.gz | All representative sequences in the pangenome |
| pangenome.connected_blocks.tsv | List of connected blocks in the pangenome graph |
| pangenome.edges | List of classified edges in the pangenome graph |
| pangenome.gfa | GFA network file representing all unique connections between gene families |
| pangenome.order.tsv | Sorted list gene_families file on pangenome graph |
| pangenome.reversed.tsv | List of reversed blocks in the pangenome graph |
| pangenome.syntenic_blocks.tsv | List of syntenic blocks in the pangenome graph |
| pangenome.temp | Temporary file used by PIRATE |
| pangenome_alignment.fasta.gz | Gene-by-gene nucleotide alignments of the full pangenome created using MAFFT |
| pangenome_alignment.gff | Annotation containing the position of the gene family within the pangenome alignment |
| pangenome_iterations/pan_sequences.{50|60|70|80|90|95|98}.reclustered.reinflated | List of clusters for each reinflation threshold |
| pangenome_iterations/pan_sequences.blast.output | BLAST output of sequences against representatives and self hits. |
| pangenome_iterations/pan_sequences.cdhit_clusters | A list of CDHIT representative clusters |
| pangenome_iterations/pan_sequences.core_clusters.tab | A list of core clusters. |
| pangenome_iterations/pan_sequences.mcl_log.txt | A log file from `mcxdeblast` and `mcl` |
| pangenome_iterations/pan_sequences.representative.fasta | FASTA file with sequences for each representative cluster |
| pangenome_log.txt | Log file from PIRATE |
| paralog_clusters.tab | List of paralogous clusters |
| representative_sequences.{faa,ffn} | Representative protein and gene sequences for each gene family |


#### Panaroo

Below is a description of the [Panaroo](https://github.com/gtonkinhill/panaroo) results. For more details about
Panaroo outputs see [Panaroo Documentation](https://gtonkinhill.github.io/panaroo/#/gettingstarted/output).

!!! note "Only available when `--use_panaroo` is given"

    By default PIRATE is used to create the pan-genome, unless `--use_panaroo` is given.


| Filename                      | Description |
|-------------------------------|-------------|
| aligned_gene_sequences | A directory of per-gene alignments |
| combined_DNA_CDS.fasta.gz | All nucleotide sequence for the annotated genes |
| combined_protein_CDS.fasta.gz | All protein sequence for the annotated proeteins |
| combined_protein_cdhit_out.txt | Log output from CD-HIT |
| combined_protein_cdhit_out.txt.clstr | Cluster information from CD-HIT |
| core_alignment_header.embl | The core/pan-genome alignment in EMBL format |
| core_gene_alignment.aln.gz | The core/pan-genome alignment in FASTA format |
| final_graph.gml | The final pan-genome graph generated by Panaroo |
| gene_data.csv | CSV linking each gene sequnece and annotation to the internal representations |
| gene_presence_absence.Rtab | A binary tab seperated version of the `gene_presence_absence.csv` |
| gene_presence_absence.csv | Lists each gene and which samples it is present in |
| gene_presence_absence_roary.csv | Lists each gene and which samples it is present in in the same format as Roary |
| pan_genome_reference.fa.gz | FASTA file which contains a single representative nucleotide sequence from each of the clusters in the pan genome (core and accessory) |
| pre_filt_graph.gml | An intermeadiate pan-genome graph generated by Panaroo |
| struct_presence_absence.Rtab | A csv file which lists the presence and abscence of different genomic rearrangement events |
| summary_statistics.txt | Number of genes in the core and accessory |


#### Roary

Below is a description of the [Roary](https://github.com/sanger-pathogens/Roary/) results. For more details about
Roary outputs see [Roary Documentation](http://sanger-pathogens.github.io/Roary/).

!!! note "Only available when `--use_roary` is given"

    By default PIRATE is used to create the pan-genome, unless `--use_roary` is given.


| Filename                      | Description |
|-------------------------------|-------------|
| accessory.header.embl | EMBL formatted file of accessory genes |
| accessory.tab | Tab-delimited formatted file of accessory genes |
| accessory_binary_genes.fa | A FASTA file with binary presence and absence of accessory genes |
| accessory_binary_genes.fa.newick | A tree created using the binary presence and absence of accessory genes |
| accessory_graph.dot | A graph in DOT format of how genes are linked together at the contig level in the accessory genome |
| blast_identity_frequency.Rtab | Blast results for percentage idenity graph |
| clustered_proteins | Groups file where each line lists the sequences in a cluster |
| core_accessory.header.embl | EMBL formatted file of core genes |
| core_accessory.tab | Tab-delimited formatted file of core genes |
| core_accessory_graph.dot | A graph in DOT format of how genes are linked together at the contig level in the pan genome |
| core_alignment_header.embl | EMBL formatted file of core genome alignment |
| gene_presence_absence.csv | Lists each gene and which samples it is present in |
| gene_presence_absence.Rtab | Tab delimited binary matrix with the presence and absence of each gene in each sample |
| number_of_conserved_genes.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| number_of_genes_in_pan_genome.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| number_of_new_genes.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| number_of_unique_genes.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| pan_genome_reference.fa.gz | FASTA file which contains a single representative nucleotide sequence from each of the clusters in the pan genome (core and accessory) |
| summary_statistics.txt | Number of genes in the core and accessory |





### Audit Trail

Below are files that can assist you in understanding which parameters and program versions were used.

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

#### Nextflow Reports

These Nextflow reports provide great a great summary of your run. These can be used to optimize
resource usage and estimate expected costs if using cloud platforms.

| Filename | Description |
|----------|-------------|
| pangenome-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| pangenome-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| pangenome-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| pangenome-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


#### Program Versions

At the end of each run, each of the `versions.yml` files are merged into the files below.

| Filename                  | Description |
|---------------------------|-------------|
| software_versions.yml     | A complete list of programs and versions used by each process | 
| software_versions_mqc.yml | A complete list of programs and versions formatted for [MultiQC](https://multiqc.info/) |

## Parameters


### <i class="fa-xl fas fa-terminal"></i> Required Parameters
Define where the pipeline should find input data and save output data.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-bacterium"></i>` --bactopia` | The path to bactopia results to use as inputs <br/>**Type:** `string` |

### <i class="fa-xl fa-solid fa-filter"></i> Filtering Parameters
Use these parameters to specify which samples to include or exclude.

| Parameter | Description |
|:---|---|
| <i class="fa-lg far fa-square-plus"></i>` --include` | A text file containing sample names (one per line) to include from the analysis <br/>**Type:** `string` |
| <i class="fa-lg far fa-square-minus"></i>` --exclude` | A text file containing sample names (one per line) to exclude from the analysis <br/>**Type:** `string` |


### <i class="fa-xl fas fa-exclamation-circle"></i> ClonalFrameML Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-hashtag"></i>` --emsim` | Number of simulations to estimate uncertainty in the EM results <br/>**Type:** `integer`, **Default:** `100` |
| <i class="fa-lg fas fa-italic"></i>` --clonal_opts` | Extra ClonalFrameML options in quotes <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_recombination` | Skip ClonalFrameML execution in subworkflows <br/>**Type:** `boolean` |

### <i class="fa-xl fas fa-exclamation-circle"></i> IQ-TREE Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-italic"></i>` --iqtree_model` | Substitution model name <br/>**Type:** `string`, **Default:** `HKY` |
| <i class="fa-lg fas fa-hashtag"></i>` --bb` | Ultrafast bootstrap replicates <br/>**Type:** `integer`, **Default:** `1000` |
| <i class="fa-lg fas fa-hashtag"></i>` --alrt` | SH-like approximate likelihood ratio test replicates <br/>**Type:** `integer`, **Default:** `1000` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --asr` | Ancestral state reconstruction by empirical Bayes <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --iqtree_opts` | Extra IQ-TREE options in quotes. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_phylogeny` | Skip IQ-TREE execution in subworkflows <br/>**Type:** `boolean` |

### <i class="fa-xl fas fa-exclamation-circle"></i> NCBI Genome Download Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-italic"></i>` --species` | Name of the species to download assemblies <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --accession` | An NCBI Assembly accession to be downloaded <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --accessions` | An file of NCBI Assembly accessions (one per line) to be downloaded <br/>**Type:** `string` |
| <i class="fa-lg fas fa-italic"></i>` --format` | Comma separated list of formats to download <br/>**Type:** `string`, **Default:** `fasta` |
| <i class="fa-lg fas fa-italic"></i>` --section` | NCBI section to download <br/>**Type:** `string`, **Default:** `refseq` |
| <i class="fa-lg fas fa-italic"></i>` --assembly_level` | Comma separated list of assembly levels to download <br/>**Type:** `string`, **Default:** `complete` |
| <i class="fa-lg fas fa-italic"></i>` --kingdom` | Comma separated list of formats to download <br/>**Type:** `string`, **Default:** `bacteria` |
| <i class="fa-lg fas fa-italic"></i>` --limit` | Limit the number of assemblies to download <br/>**Type:** `string` |

### <i class="fa-xl fas fa-exclamation-circle"></i> PIRATE Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-italic"></i>` --steps` | Percent identity thresholds to use for pangenome construction <br/>**Type:** `string`, **Default:** `50,60,70,80,90,95,98` |
| <i class="fa-lg fas fa-italic"></i>` --features` | Comma-delimited features to use for pangenome construction <br/>**Type:** `string`, **Default:** `CDS` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --para_off` | Switch off paralog identification <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --z` | Retain all PIRATE intermediate files <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-italic"></i>` --pan_opt` | Additional arguments to pass to pangenome contruction. <br/>**Type:** `string` |

### <i class="fa-xl fas fa-exclamation-circle"></i> Prokka Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-file-alt"></i>` --proteins` | FASTA file of trusted proteins to first annotate from <br/>**Type:** `string` |
| <i class="fa-lg fas fa-file-alt"></i>` --prodigal_tf` | Training file to use for Prodigal <br/>**Type:** `string` |
| <i class="fa-lg fas fa-check"></i>` --compliant` | Force Genbank/ENA/DDJB compliance <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-school"></i>` --centre` | Sequencing centre ID <br/>**Type:** `string`, **Default:** `Bactopia` |
| <i class="fa-lg fas fa-hashtag"></i>` --prokka_coverage` | Minimum coverage on query protein <br/>**Type:** `integer`, **Default:** `80` |
| <i class="fa-lg fas fa-italic"></i>` --prokka_evalue` | Similarity e-value cut-off <br/>**Type:** `string`, **Default:** `1e-09` |
| <i class="fa-lg fas fa-italic"></i>` --prokka_opts` | Extra Prokka options in quotes. <br/>**Type:** `string` |

### <i class="fa-xl fas fa-exclamation-circle"></i> Panaroo Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --use_panaroo` | Use Panaroo instead of PIRATE in the 'pangenome' subworkflow <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --panaroo_mode` | The stringency mode at which to run panaroo <br/>**Type:** `string`, **Default:** `strict` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --panaroo_alignment` | Output alignments of core genes or all genes <br/>**Type:** `string`, **Default:** `core` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --panaroo_aligner` | Aligner to use for core/pan genome alignment <br/>**Type:** `string`, **Default:** `mafft` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --panaroo_core_threshold` | Core-genome sample threshold <br/>**Type:** `number`, **Default:** `0.95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --panaroo_threshold` | Sequence identity threshold <br/>**Type:** `number`, **Default:** `0.98` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --panaroo_family_threshold` | Protein family sequence identity threshold <br/>**Type:** `number`, **Default:** `0.7` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --len_dif_percent` | Length difference cutoff <br/>**Type:** `number`, **Default:** `0.98` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --merge_paralogs` | Do not split paralogs <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --panaroo_opts` | Additional options to pass to panaroo <br/>**Type:** `string` |

### <i class="fa-xl fas fa-exclamation-circle"></i> Roary Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --use_prank` | Use PRANK instead of MAFFT for core gene <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --use_roary` | Use Roary instead of PIRATE in the 'pangenome' subworkflow <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --i` | Minimum percentage identity for blastp <br/>**Type:** `integer`, **Default:** `95` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --cd` | Percentage of isolates a gene must be in to be core <br/>**Type:** `integer`, **Default:** `99` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --g` | Maximum number of clusters <br/>**Type:** `integer`, **Default:** `50000` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --s` | Do not split paralogs <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --ap` | Allow paralogs in core alignment <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --iv` | MCL inflation value <br/>**Type:** `number`, **Default:** `1.5` |

### <i class="fa-xl fas fa-exclamation-circle"></i> Scoary Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --traits` | Input trait table (CSV) to test for associations <br/>**Type:** `string` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --p_value_cutoff` | For statistical tests, genes with higher p-values will not be reported <br/>**Type:** `number`, **Default:** `0.05` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --correction` | Apply the indicated filtration measure. <br/>**Type:** `string`, **Default:** `I` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --permute` | Perform N number of permutations of the significant results post-analysis <br/>**Type:** `integer` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --start_col` | On which column in the gene presence/absence file do individual strain info start <br/>**Type:** `integer`, **Default:** `15` |

### <i class="fa-xl fas fa-exclamation-circle"></i> SNP-Dists Parameters


| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --a` | Count all differences not just [AGTC] <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --b` | Keep top left corner cell <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --csv` | Output CSV instead of TSV <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --k` | Keep case, don't uppercase all letters <br/>**Type:** `boolean` |


### <i class="fa-xl fa-solid fa-gears"></i> Optional Parameters
These optional parameters can be useful in certain settings.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-folder"></i>` --outdir` | Base directory to write results to <br/>**Type:** `string`, **Default:** `./` |
| <i class="fa-lg fas fa-folder"></i>` --run_name` | Name of the directory to hold results <br/>**Type:** `string`, **Default:** `bactopia` |
| <i class="fa-lg fas fa-expand-arrows-alt"></i>` --skip_compression` | Ouput files will not be compressed <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-folder"></i>` --datasets` | The path to cache datasets to <br/>**Type:** `string` |
| <i class="fa-lg fas fa-trash-restore"></i>` --keep_all_files` | Keeps all analysis files created <br/>**Type:** `boolean` |

### <i class="fa-xl fa-solid fa-arrow-up-right-dots"></i> Max Job Request Parameters
Set the top limit for requested resources for any single job.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-redo"></i>` --max_retry` | Maximum times to retry a process before allowing it to fail. <br/>**Type:** `integer`, **Default:** `3` |
| <i class="fa-lg fas fa-microchip"></i>` --max_cpus` | Maximum number of CPUs that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `4` |
| <i class="fa-lg fas fa-memory"></i>` --max_memory` | Maximum amount of memory (in GB) that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `32` |
| <i class="fa-lg far fa-clock"></i>` --max_time` | Maximum amount of time (in minutes) that can be requested for any single job. <br/>**Type:** `integer`, **Default:** `120` |
| <i class="fa-lg fas fa-angle-double-up"></i>` --max_downloads` | Maximum number of samples to download at a time <br/>**Type:** `integer`, **Default:** `3` |

### <i class="fa-xl fa-solid fa-screwdriver-wrench"></i> Nextflow Configuration Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-cog"></i>` --nfconfig` | A Nextflow compatible config file for custom profiles, loaded last and will overwrite existing variables if set. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-copy"></i>` --publish_dir_mode` | Method used to save pipeline results to output directory. <br/>**Type:** `string`, **Default:** `copy` |
| <i class="fa-lg fas fa-cogs"></i>` --infodir` | Directory to keep pipeline Nextflow logs and reports. <br/>**Type:** `string`, **Default:** `${params.outdir}/pipeline_info` |
| <i class="fa-lg fas fa-recycle"></i>` --force` | Nextflow will overwrite existing output files. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-trash-alt"></i>` --cleanup_workdir` | After Bactopia is successfully executed, the `work` directory will be deleted. <br/>**Type:** `boolean` |

### <i class="fa-xl fa-regular fa-address-card"></i> Nextflow Profile Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-folder"></i>` --condadir` | Directory to Nextflow should use for Conda environments <br/>**Type:** `string` |
| <i class="fa-lg fas fa-box"></i>` --registry` | Docker registry to pull containers from. <br/>**Type:** `string`, **Default:** `dockerhub` |
| <i class="fa-lg fas fa-folder"></i>` --datasets_cache` | Directory where downloaded datasets should be stored. <br/>**Type:** `string`, **Default:** `<BACTOPIA_DIR>/data/datasets` |
| <i class="fa-lg fas fa-folder"></i>` --singularity_cache` | Directory where remote Singularity images are stored. <br/>**Type:** `string` |
| <i class="fa-lg fas fa-toolbox"></i>` --singularity_pull_docker_container` | Instead of directly downloading Singularity images for use with Singularity, force the workflow to pull and convert Docker containers instead. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-recycle"></i>` --force_rebuild` | Force overwrite of existing pre-built environments. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-clipboard-list"></i>` --queue` | Comma-separated name of the queue(s) to be used by a job scheduler (e.g. AWS Batch or SLURM) <br/>**Type:** `string`, **Default:** `general,high-memory` |
| <i class="fa-lg fas fa-clipboard-list"></i>` --cluster_opts` | Additional options to pass to the executor. (e.g. SLURM: '--account=my_acct_name' <br/>**Type:** `string` |
| <i class="fa-lg fas fa-toggle-off"></i>` --disable_scratch` | All intermediate files created on worker nodes of will be transferred to the head node. <br/>**Type:** `boolean` |

### <i class="fa-xl fa-solid fa-reply-all"></i> Helpful Parameters
Uncommonly used parameters that might be useful.

| Parameter | Description |
|:---|---|
| <i class="fa-lg fas fa-palette"></i>` --monochrome_logs` | Do not use coloured log outputs. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-remove-format"></i>` --nfdir` | Print directory Nextflow has pulled Bactopia to <br/>**Type:** `boolean` |
| <i class="fa-lg far fa-clock"></i>` --sleep_time` | The amount of time (seconds) Nextflow will wait after setting up datasets before execution. <br/>**Type:** `integer`, **Default:** `5` |
| <i class="fa-lg fas fa-tasks"></i>` --validate_params` | Boolean whether to validate parameters against the schema at runtime <br/>**Type:** `boolean`, **Default:** `True` |
| <i class="fa-lg fas fa-question-circle"></i>` --help` | Display help text. <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-bacteria"></i>` --wf` | Specify which workflow or Bactopia Tool to execute <br/>**Type:** `string`, **Default:** `bactopia` |
| <i class="fa-lg fas fa-list"></i>` --list_wfs` | List the available workflows and Bactopia Tools to use with '--wf' <br/>**Type:** `boolean` |
| <i class="fa-lg far fa-eye"></i>` --show_hidden_params` | Show all params when using `--help` <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-question-circle"></i>` --help_all` | An alias for --help --show_hidden_params <br/>**Type:** `boolean` |
| <i class="fa-lg fas fa-info"></i>` --version` | Display version text. <br/>**Type:** `boolean` |

## Citations
If you use Bactopia and `pangenome` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [ClonalFramML](https://github.com/xavierdidelot/ClonalFrameML)  
    Didelot X, Wilson DJ [ClonalFrameML: Efficient Inference of Recombination in Whole Bacterial Genomes.](https://doi.org/10.1371/journal.pcbi.1004041) _PLoS Comput Biol_ 11(2) e1004041 (2015)
  
- [IQ-TREE](https://github.com/Cibiv/IQ-TREE)  
    Nguyen L-T, Schmidt HA, von Haeseler A, Minh BQ [IQ-TREE: A fast and effective stochastic algorithm for estimating maximum likelihood phylogenies.](https://doi.org/10.1093/molbev/msu300) _Mol. Biol. Evol._ 32:268-274 (2015)
  
- [ModelFinder](https://github.com/Cibiv/IQ-TREE)  
    Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS [ModelFinder - Fast model selection for accurate phylogenetic estimates.](https://doi.org/10.1038/nmeth.4285) _Nat. Methods_ 14:587-589 (2017)
  
- [UFBoot2](https://github.com/Cibiv/IQ-TREE)  
    Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS [UFBoot2: Improving the ultrafast bootstrap approximation.](https://doi.org/10.1093/molbev/msx281) _Mol. Biol. Evol._ 35:518–522 (2018)
  
- [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)  
    Blin K [ncbi-genome-download: Scripts to download genomes from the NCBI FTP servers](https://github.com/kblin/ncbi-genome-download) (GitHub)
  
- [Panaroo](https://github.com/gtonkinhill/panaroo)  
    Tonkin-Hill G, MacAlasdair N, Ruis C, Weimann A, Horesh G, Lees JA, Gladstone RA, Lo S, Beaudoin C, Floto RA, Frost SDW, Corander J, Bentley SD, Parkhill J [Producing polished prokaryotic pangenomes with the Panaroo pipeline.](https://doi.org/10.1186/s13059-020-02090-4) _Genome Biology_ 21(1), 180. (2020)
  
- [PIRATE](http://github.com/SionBayliss/PIRATE)  
    Bayliss SC, Thorpe HA, Coyle NM, Sheppard SK, Feil EJ [PIRATE: A fast and scalable pangenomics toolbox for clustering diverged orthologues in bacteria.](https://doi.org/10.1093/gigascience/giz119) _Gigascience_ 8 (2019)
  
- [Prokka](https://github.com/tseemann/prokka)  
    Seemann T [Prokka: rapid prokaryotic genome annotation](http://dx.doi.org/10.1093/bioinformatics/btu153) _Bioinformatics_ 30, 2068–2069 (2014)
  
- [Roary](https://github.com/sanger-pathogens/Roary)  
    Page AJ, Cummins CA, Hunt M, Wong VK, Reuter S, Holden MTG, Fookes M, Falush D, Keane JA, Parkhill J [Roary: rapid large-scale prokaryote pan genome analysis.](https://doi.org/10.1093/bioinformatics/btv421) _Bioinformatics_ 31, 3691–3693 (2015)
  
- [Scoary](https://github.com/AdmiralenOla/Scoary)  
    Brynildsrud O, Bohlin J, Scheffer L, Eldholm V [Rapid scoring of genes in microbial pan-genome-wide association studies with Scoary.](https://doi.org/10.1186/s13059-016-1108-8) _Genome Biol._ 17:238 (2016)
  
- [snp-dists](https://github.com/tseemann/snp-dists)  
    Seemann T [snp-dists - Pairwise SNP distance matrix from a FASTA sequence alignment.](https://github.com/tseemann/snp-dists) (GitHub)
  
