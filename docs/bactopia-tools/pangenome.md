---
tags:
---



# Bactopia Tool - `pangenome`
The `pangenome` subworkflow allows you to create a pan-genome with [PIRATE](https://github.com/SionBayliss/PIRATE)
(or [Roary](https://github.com/sanger-pathogens/Roary)) of your samples.

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
pangenome/
├── clonalframeml
│   ├── core-genome.ML_sequence.fasta
│   ├── core-genome.em.txt
│   ├── core-genome.emsim.txt
│   ├── core-genome.importation_status.txt
│   ├── core-genome.labelled_tree.newick
│   └── core-genome.position_cross_reference.txt
├── {iqtree,iqtree-fast}
│   ├── core-genome.alninfo
│   ├── {core-genome,start-tree}.bionj
│   ├── {core-genome,start-tree}.ckp.gz
│   ├── core-genome.contree
│   ├── {core-genome,start-tree}.mldist
│   ├── {core-genome,start-tree}.model.gz
│   ├── core-genome.splits.nex
│   ├── {core-genome,start-tree}.treefile
│   └── core-genome.ufboot
├── logs
│   ├── clonalframeml
│   │   ├── nf-clonalframeml.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   ├── custom_dumpsoftwareversions
│   │   ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   ├── {iqtree,iqtree-fast}
│   │   ├── core-genome.log
│   │   ├── nf-iqtree.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   ├── pirate
│   │   ├── nf-pirate.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   ├── roary
│   │   ├── nf-roary.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   └── snpdists
│       ├── nf-snpdists.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── pangenome-dag.dot
│   ├── pangenome-report.html
│   ├── pangenome-timeline.html
│   └── pangenome-trace.txt
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
│   │   └── <GENE_FAMILY>.{aa|nucleotide|.fasta
│   ├── gene_presence_absence.csv
│   ├── genome2loci.tab
│   ├── genome_list.txt
│   ├── loci_list.tab
│   ├── loci_paralog_categories.tab
│   ├── modified_gffs
│   │   └── <SAMPLE_NAME>.gff
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
│   │   └── pan_sequences.representative.fasta
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
│   ├── number_of_conserved_genes.Rtab
│   ├── number_of_genes_in_pan_genome.Rtab
│   ├── number_of_new_genes.Rtab
│   ├── number_of_unique_genes.Rtab
│   ├── pan_genome_reference.fa.gz
│   └── summary_statistics.txt
├── core-genome.aln.gz
├── core-genome.distance.tsv
├── core-genome.iqtree
├── core-genome.masked.aln.gz
├── software_versions.yml
└── software_versions_mqc.yml

```



### Results

#### Top Level

Below are results that are in the base directory.


| Filename    | Description |
|-------------|-------------|
| core-genome.aln.gz        | A multiple sequence alignment FASTA of the core genome |
| core-genome.distance.tsv  | Core genome Pair-wise SNP distance for each sample |
| core-genome.iqtree        | Full result of the IQ-TREE core genome phylogeny |
| core-genome.masked.aln.gz | A core-genome alignment with the recomination masked |


#### ClonalFrameML

Below is a description of the [ClonalFrameML](https://github.com/xavierdidelot/ClonalFrameML) results. For more details about
ClonalFrameML outputs see [ClonalFrameML - Outputs](https://github.com/xavierdidelot/clonalframeml/wiki#output).


| Filename | Description |
|----------|-------------|
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


| Filename    | Description |
|-------------|-------------|
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
Roary outputs see [PIRATE - Output files](https://github.com/SionBayliss/PIRATE#output-files).

!!! note "Available by default"

    By default PIRATE is used to create the pan-genome. If `--use_roary` is given, `pirate` outputs will
    not be available only the `roary` outputs.


| Filename | Description |
|----------|-------------|
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
| feature_sequences/${GENE_FAMILY}.{aa\|nucleotide}.fasta | Amino acid and nucleotide sequences for each gene family |
| gene_presence_absence.csv | Lists each gene and which samples it is present in |
| genome2loci.tab | List of loci for each genome |
| genome_list.txt | List of genomes in the analysis |
| loci_list.tab | List of loci and their associated genomes |
| loci_paralog_categories.tab | Concatenation of classified paralogs |
| modified_gffs/${SAMPLE_NAME}.gff | GFF3 files which have been standardised for PIRATE |
| pan_sequences.fasta.gz | All representative sequences in the pangenome  |
| pangenome.connected_blocks.tsv | List of connected blocks in the pangenome graph |
| pangenome.edges | List of classified edges in the pangenome graph |
| pangenome.gfa | GFA network file representing all unique connections between gene families |
| pangenome.order.tsv | Sorted list gene_families file on pangenome graph |
| pangenome.reversed.tsv | List of reversed blocks in the pangenome graph |
| pangenome.syntenic_blocks.tsv | List of syntenic blocks in the pangenome graph |
| pangenome_alignment.fasta.gz | Gene-by-gene nucleotide alignments of the full pangenome created using MAFFT |
| pangenome_alignment.gff | Annotation containing the position of the gene family within the pangenome alignment |
| pangenome_iterations/pan_sequences.{50\|60\|70\|80\|90\|95\|98}.reclustered.reinflated | List of clusters for each reinflation threshold  |
| pangenome_iterations/pan_sequences.blast.output | BLAST output of sequences against representatives and self hits. |
| pangenome_iterations/pan_sequences.cdhit_clusters | A list of CDHIT representative clusters |
| pangenome_iterations/pan_sequences.core_clusters.tab | A list of core clusters. |
| pangenome_iterations/pan_sequences.mcl_log.txt | A log file from `mcxdeblast` and `mcl` |
| pangenome_iterations/pan_sequences.representative.fasta | FASTA file with sequences for each representative cluster |
| paralog_clusters.tab | List of paralogous clusters |
| representative_sequences.faa | Representative protein sequences for each gene family |
| representative_sequences.ffn | Representative gene sequences for each gene family |


#### Roary

Below is a description of the [Roary](https://github.com/sanger-pathogens/Roary/) results. For more details about
Roary outputs see [Roary Documentation](http://sanger-pathogens.github.io/Roary/).

!!! note "Only available when `--use_roary` is given"

    By default PIRATE is used to create the pan-genome, unless `--use_roary` is given. So, you will either
    have a `roary` folder or a `pirate` folder.


| Filename | Description |
|----------|-------------|
| accessory.header.embl | Tab/EMBL formatted file of accessory genes |
| accessory.tab | Tab/EMBL formatted file of accessory genes |
| accessory_binary_genes.fa | A FASTA file with binary presence and absence of accessory genes |
| accessory_binary_genes.fa.newick | A tree created using the binary presence and absence of accessory genes |
| accessory_graph.dot | A graph in DOT format of how genes are linked together at the contig level in the accessory genome |
| blast_identity_frequency.Rtab | Blast results for percentage idenity graph |
| clustered_proteins | Groups file where each line lists the sequences in a cluster |
| core_accessory.header.embl | Tab/EMBL formatted file of core genes |
| core_accessory.tab | Tab/EMBL formatted file of core genes |
| core_accessory_graph.dot | A graph in DOT format of how genes are linked together at the contig level in the pan genome |
| core_alignment_header.embl | Tab/EMBL formatted file of core genome alignment |
| gene_presence_absence.csv | Lists each gene and which samples it is present in |
| gene_presence_absence.Rtab | Tab delimited binary matrix with the presence and absence of each gene in each sample |
| number_of_conserved_genes.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| number_of_genes_in_pan_genome.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| number_of_new_genes.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| number_of_unique_genes.Rtab | Graphs on how the pan genome varies as genomes are added (in random orders) |
| pan_genome_reference.f.gz | FASTA file which contains a single representative nucleotide sequence from each of the clusters in the pan genome (core and accessory) |
| summary_statistics.txt | Number of genes in the core and accessory |





### Audit Trail

Below are files that can assist you in understanding which parameters and program versions were used.

#### Logs 

Each process that is executed will have a `logs` folder containing helpful files for you to review
if the need ever arises.

| Filename                      | Description |
|-------------------------------|-------------|
| nf-&lt;PROCESS_NAME&gt;.begin | An empty file used to designate the process started |
| nf-&lt;PROCESS_NAME&gt;.err   | Contains STDERR outputs from the process |
| nf-&lt;PROCESS_NAME&gt;.log   | Contains both STDERR and STDOUT outputs from the process |
| nf-&lt;PROCESS_NAME&gt;.out   | Contains STDOUT outputs from the process |
| nf-&lt;PROCESS_NAME&gt;.run   | The script Nextflow uses to stage/unstage files and queue processes based on given profile |
| nf-&lt;PROCESS_NAME&gt;.sh    | The script executed by bash for the process  |
| nf-&lt;PROCESS_NAME&gt;.trace | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report for the process |
| versions.yml                  | A YAML formatted file with program versions |

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


### Required Parameters
Define where the pipeline should find input data and save output data.

| Parameter | Description | Default |
|---|---|---|
| `--bactopia` | The path to bactopia results to use as inputs |  |

### Filtering Parameters
Use these parameters to specify which samples to include or exclude.

| Parameter | Description | Default |
|---|---|---|
| `--include` | A text file containing sample names (one per line) to include from the analysis |  |
| `--exclude` | A text file containing sample names (one per line) to exclude from the analysis |  |


### ClonalFrameML Parameters


| Parameter | Description | Default |
|---|---|---|
| `--emsim` | Number of simulations to estimate uncertainty in the EM results | 100 |
| `--clonal_opts` | Extra ClonalFrameML options in quotes |  |
| `--skip_recombination` | Skip ClonalFrameML execution in subworkflows | False |

### IQ-TREE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--m` | Substitution model name | MFP |
| `--bb` | Ultrafast bootstrap replicates | 1000 |
| `--alrt` | SH-like approximate likelihood ratio test replicates | 1000 |
| `--asr` | Ancestral state reconstruction by empirical Bayes | False |
| `--iqtree_opts` | Extra IQ-TREE options in quotes. |  |
| `--skip_phylogeny` | Skip IQ-TREE execution in subworkflows | False |

### NCBI Genome Download Parameters


| Parameter | Description | Default |
|---|---|---|
| `--species` | Name of the species to download assemblies |  |
| `--accession` | An NCBI Assembly accession to be downloaded |  |
| `--accessions` | An file of NCBI Assembly accessions (one per line) to be downloaded |  |
| `--format` | Comma separated list of formats to download | fasta |
| `--section` | NCBI section to download | refseq |
| `--assembly_level` | Comma separated list of assembly levels to download | complete |
| `--kingdom` | Comma separated list of formats to download | bacteria |
| `--limit` | Limit the number of assemblies to download |  |

### PIRATE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--steps` | Percent identity thresholds to use for pangenome construction | 50,60,70,80,90,95,98 |
| `--features` | Comma-delimited features to use for pangenome construction | CDS |
| `--para_off` | Switch off paralog identification | False |
| `--z` | Retain all PIRATE intermediate files | False |
| `--pan_opt` | Additional arguments to pass to pangenome contruction. |  |

### Prokka Parameters


| Parameter | Description | Default |
|---|---|---|
| `--proteins` | FASTA file of trusted proteins to first annotate from |  |
| `--prodigal_tf` | Training file to use for Prodigal |  |
| `--prokka_coverage` | Minimum coverage on query protein | 80 |
| `--prokka_evalue` | Similarity e-value cut-off | 1e-09 |
| `--prokka_opts` | Extra Prokka options in quotes. |  |

### Roary Parameters


| Parameter | Description | Default |
|---|---|---|
| `--use_prank` | Use PRANK instead of MAFFT for core gene | False |
| `--use_roary` | Use Roary instead of PIRATE in the 'pangenome' subworkflow | False |
| `--i` | Minimum percentage identity for blastp | 95 |
| `--cd` | Percentage of isolates a gene must be in to be core | 99 |
| `--g` | Maximum number of clusters | 50000 |
| `--s` | Do not split paralogs | False |
| `--ap` | Allow paralogs in core alignment | False |
| `--iv` | MCL inflation value | 1.5 |

### Scoary Parameters


| Parameter | Description | Default |
|---|---|---|
| `--traits` | Input trait table (CSV) to test for associations |  |
| `--p_value_cutoff` | For statistical tests, genes with higher p-values will not be reported | 0.05 |
| `--correction` | Apply the indicated filtration measure. | I |
| `--permute` | Perform N number of permutations of the significant results post-analysis | 0 |
| `--start_col` | On which column in the gene presence/absence file do individual strain info start | 15 |

### SNP-Dists Parameters


| Parameter | Description | Default |
|---|---|---|
| `--a` | Count all differences not just [AGTC] | False |
| `--b` | Keep top left corner cell | False |
| `--csv` | Output CSV instead of TSV | False |
| `--k` | Keep case, don't uppercase all letters | False |


### Optional Parameters
These optional parameters can be useful in certain settings.

| Parameter | Description | Default |
|---|---|---|
| `--outdir` | Base directory to write results to | ./ |
| `--run_name` | Name of the directory to hold results | bactopia |
| `--skip_compression` | Ouput files will not be compressed | False |
| `--keep_all_files` | Keeps all analysis files created | False |

### Max Job Request Parameters
Set the top limit for requested resources for any single job.

| Parameter | Description | Default |
|---|---|---|
| `--max_retry` | Maximum times to retry a process before allowing it to fail. | 3 |
| `--max_cpus` | Maximum number of CPUs that can be requested for any single job. | 4 |
| `--max_memory` | Maximum amount of memory (in GB) that can be requested for any single job. | 32 |
| `--max_time` | Maximum amount of time (in minutes) that can be requested for any single job. | 120 |
| `--max_downloads` | Maximum number of samples to download at a time | 3 |

### Nextflow Configuration Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description | Default |
|---|---|---|
| `--nfconfig` | A Nextflow compatible config file for custom profiles, loaded last and will overwrite existing variables if set. |  |
| `--publish_dir_mode` | Method used to save pipeline results to output directory. | copy |
| `--infodir` | Directory to keep pipeline Nextflow logs and reports. | ${params.outdir}/pipeline_info |
| `--force` | Nextflow will overwrite existing output files. | False |
| `--cleanup_workdir` | After Bactopia is successfully executed, the `work` directory will be deleted. | False |

### Nextflow Profile Parameters
Parameters to fine-tune your Nextflow setup.

| Parameter | Description | Default |
|---|---|---|
| `--condadir` | Directory to Nextflow should use for Conda environments |  |
| `--registry` | Docker registry to pull containers from. | dockerhub |
| `--singularity_cache` | Directory where remote Singularity images are stored. |  |
| `--singularity_pull_docker_container` | Instead of directly downloading Singularity images for use with Singularity, force the workflow to pull and convert Docker containers instead. |  |
| `--force_rebuild` | Force overwrite of existing pre-built environments. | False |
| `--queue` | Comma-separated name of the queue(s) to be used by a job scheduler (e.g. AWS Batch or SLURM) | general,high-memory |
| `--cluster_opts` | Additional options to pass to the executor. (e.g. SLURM: '--account=my_acct_name' |  |
| `--disable_scratch` | All intermediate files created on worker nodes of will be transferred to the head node. | False |

### Helpful Parameters
Uncommonly used parameters that might be useful.

| Parameter | Description | Default |
|---|---|---|
| `--monochrome_logs` | Do not use coloured log outputs. |  |
| `--nfdir` | Print directory Nextflow has pulled Bactopia to |  |
| `--sleep_time` | The amount of time (seconds) Nextflow will wait after setting up datasets before execution. | 5 |
| `--validate_params` | Boolean whether to validate parameters against the schema at runtime | True |
| `--help` | Display help text. |  |
| `--wf` | Specify which workflow or Bactopia Tool to execute | bactopia |
| `--list_wfs` | List the available workflows and Bactopia Tools to use with '--wf' |  |
| `--show_hidden_params` | Show all params when using `--help` |  |
| `--help_all` | An alias for --help --show_hidden_params |  |
| `--version` | Display version text. |  |

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
  
