---
title: meta.docs.meta.title
description: meta.docs.meta.description
tags:
---



# Bactopia Tool - `snippy`
The `snippy` subworkflow allows you to call SNPs and InDels against a reference with
[Snippy](https://github.com/tseemann/snippy). With the called SNPs/InDels, [snippy-core](https://github.com/tseemann/snippy#core-snp-phylogeny) 
a core-SNP alignment is created.

A phylogeny, based on the core-SNP alignment, will be created by [IQ-Tree](https://github.com/Cibiv/IQ-TREE). Optionally
a recombination-masked core-SNP alignment can be created with [Gubbins](https://github.com/nickjcroucher/gubbins).

Finally, the pair-wise SNP distance for each sample is also calculated with 
[snp-dists](https://github.com/tseemann/snp-dists).


## Example Usage
```
bactopia --wf snippy \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `snippy` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
snippy/
├── gubbins
│   ├── core-snp.branch_base_reconstruction.embl.gz
│   ├── core-snp.filtered_polymorphic_sites.fasta.gz
│   ├── core-snp.filtered_polymorphic_sites.phylip
│   ├── core-snp.final_tree.tre
│   ├── core-snp.node_labelled.final_tree.tre
│   ├── core-snp.per_branch_statistics.csv
│   ├── core-snp.recombination_predictions.embl.gz
│   ├── core-snp.recombination_predictions.gff.gz
│   └── core-snp.summary_of_snp_distribution.vcf.gz
├── iqtree
│   ├── core-snp.alninfo
│   ├── core-snp.bionj
│   ├── core-snp.ckp.gz
│   ├── core-snp.contree
│   ├── core-snp.mldist
│   ├── core-snp.splits.nex
│   ├── core-snp.treefile
│   └── core-snp.ufboot
├── logs
│   ├── gubbins
│   │   ├── core-snp.log
│   │   ├── nf-gubbins.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   ├── iqtree
│   │   ├── core-snp.log
│   │   ├── nf-iqtree.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   ├── snippy-core
│   │   ├── nf-snippy-core.{begin,err,log,out,run,sh,trace}
│   │   └── versions.yml
│   └── snpdists
│       ├── nf-snpdists.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── snippy-dag.dot
│   ├── snippy-report.html
│   ├── snippy-timeline.html
│   └── snippy-trace.txt
├── snippy
│   └── <SAMPLE_NAME>
│       ├── logs
│       │   └── snippy
│       │       ├── nf-snippy.{begin,err,log,out,run,sh,trace}
│       │       ├── <SAMPLE_NAME>.log
│       │       └── versions.yml
│       ├── <SAMPLE_NAME>.aligned.fa.gz
│       ├── <SAMPLE_NAME>.annotated.vcf.gz
│       ├── <SAMPLE_NAME>.bam
│       ├── <SAMPLE_NAME>.bam.bai
│       ├── <SAMPLE_NAME>.bed.gz
│       ├── <SAMPLE_NAME>.consensus.fa.gz
│       ├── <SAMPLE_NAME>.consensus.subs.fa.gz
│       ├── <SAMPLE_NAME>.consensus.subs.masked.fa.gz
│       ├── <SAMPLE_NAME>.coverage.txt.gz
│       ├── <SAMPLE_NAME>.csv.gz
│       ├── <SAMPLE_NAME>.filt.vcf.gz
│       ├── <SAMPLE_NAME>.gff.gz
│       ├── <SAMPLE_NAME>.html
│       ├── <SAMPLE_NAME>.raw.vcf.gz
│       ├── <SAMPLE_NAME>.subs.vcf.gz
│       ├── <SAMPLE_NAME>.tab
│       ├── <SAMPLE_NAME>.txt
│       └── <SAMPLE_NAME>.vcf.gz
├── snippy-core
│   ├── core-snp.aln.gz
│   ├── core-snp.tab.gz
│   ├── core-snp.txt
│   └── core-snp.vcf.gz
├── core-snp-clean.full.aln.gz
├── core-snp.distance.tsv
├── core-snp.full.aln.gz
├── core-snp.iqtree
└── core-snp.masked.aln.gz

```



### Results

#### Top Level

Below are results that are in the base directory.


| Filename                   | Description                                                              |
|----------------------------|--------------------------------------------------------------------------|
| core-snp-clean.full.aln.gz | Same as `core-snp.full.aln.gz` with unusual characters replaced with `N` |
| core-snp.distance.tsv      | Core genome Pair-wise SNP distance for each sample                       |
| core-snp.full.aln.gz       | A whole genome SNP alignment (includes invariant sites)                  |
| core-genome.iqtree         | Full result of the IQ-TREE core genome phylogeny                         |
| core-genome.masked.aln.gz  | A core-SNP alignment with the recomination masked                        |


#### Gubbins

Below is a description of the [Gubbins](https://github.com/nickjcroucher/gubbins) results. For more details about
Gubbins outputs see [Gubbins - Outputs](https://github.com/nickjcroucher/gubbins/blob/master/docs/gubbins_manual.md#output-files).


| Filename                                     | Description                                                                            |
|----------------------------------------------|----------------------------------------------------------------------------------------|
| core-snp.branch_base_reconstruction.embl.gz  | Base substitution reconstruction in EMBL format                                        |
| core-snp.filtered_polymorphic_sites.fasta.gz | FASTA format alignment of filtered polymorphic sites                                   |
| core-snp.filtered_polymorphic_sites.phylip   | Phylip format alignment of filtered polymorphic sites                                  |
| core-snp.final_tree.tre                      | Final phylogeny in Newick format (_branch lengths are in point mutations_)             |
| core-snp.node_labelled.final_tree.tre        | Final phylogeny in Newick format but with internal node labels                         |
| core-snp.per_branch_statistics.csv           | Per-branch reporting of the base substitutions inside and outside recombination events |
| core-snp.recombination_predictions.embl.gz   | Recombination predictions in EMBL file format                                          |
| core-snp.recombination_predictions.gff.gz    | Recombination predictions in GFF file format                                           |
| core-snp.summary_of_snp_distribution.vcf.gz  | VCF file summarising the distribution of point mutations                               |


#### IQ-TREE

Below is a description of the [IQ-TREE](http://www.iqtree.org/) results. If ClonalFrameML is executed, a fast tree
is created and given the prefix `start-tree`, the final tree has the prefix `core-genome`. For more details about
IQ-TREE outputs see [IQ-TREE - Outputs](https://github.com/Cibiv/IQ-TREE/wiki/Web-Server-Tutorial#analysis-results).


| Filename            | Description                                                                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| core-snp.alninfo    | Alignment site statistics                                                                                                                             |
| core-snp.bionj      | A neighbor joining tree produced by BIONJ                                                                                                             |
| core-snp.ckp.gz     | IQ-TREE writes a checkpoint file                                                                                                                      |
| core-snp.contree    | Consensus tree with assigned branch supports where branch lengths are optimized on the original alignment; printed if Ultrafast Bootstrap is selected |
| core-snp.mldist     | Contains the likelihood distances                                                                                                                     |
| core-snp.splits.nex | Support values in percentage for all splits (bipartitions), computed as the occurence frequencies in the bootstrap trees                              |
| core-snp.treefile   | Maximum likelihood tree in NEWICK format, can be visualized with treeviewer programs                                                                  |
| core-snp.ufboot     | Trees created during the bootstrap steps                                                                                                              |


#### Snippy

Below is a description of the per-sample [Snippy]([Snippy](https://github.com/tseemann/snippy)) results. For more details about
Snippy outputs see [Snippy - Outputs](https://github.com/tseemann/snippy#output-files).


| Filename                                        | Description                                                                                                                        |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| &lt;SAMPLE_NAME&gt;.aligned.fa.gz               | A version of the reference but with `-` at position with `depth=0` and `N` for `0 < depth < --mincov` (**does not have variants**) | 
| &lt;SAMPLE_NAME&gt;.annotated.vcf.gz            | The final variant calls with additional annotations from Reference genome's GenBank file                                           | 
| &lt;SAMPLE_NAME&gt;.bam                         | The alignments in [BAM](http://en.wikipedia.org/wiki/SAMtools) format. Includes unmapped, multimapping reads. Excludes duplicates  | 
| &lt;SAMPLE_NAME&gt;.bam.bai                     | Index for the .bam file                                                                                                            | 
| &lt;SAMPLE_NAME&gt;.bed.gz                      | The variants in [BED](http://genome.ucsc.edu/FAQ/FAQformat.html#format1) format                                                    | 
| &lt;SAMPLE_NAME&gt;.consensus.fa.gz             | A version of the reference genome with *all* variants instantiated                                                                 | 
| &lt;SAMPLE_NAME&gt;.consensus.subs.fa.gz        | A version of the reference genome with *only substitution* variants instantiated                                                   | 
| &lt;SAMPLE_NAME&gt;.consensus.subs.masked.fa.gz | A version of the reference genome with *only substitution* variants instantiated and low-coverage regions masked                   | 
| &lt;SAMPLE_NAME&gt;.coverage.txt.gz             | The per-base coverage of each position in the reference genome                                                                     | 
| &lt;SAMPLE_NAME&gt;.csv.gz                      | A [comma-separated](http://en.wikipedia.org/wiki/Comma-separated_values) version of the .tab file                                  | 
| &lt;SAMPLE_NAME&gt;.filt.vcf.gz                 | The filtered variant calls from Freebayes                                                                                          | 
| &lt;SAMPLE_NAME&gt;.gff.gz                      | The variants in [GFF3](http://www.sequenceontology.org/gff3.shtml) format                                                          | 
| &lt;SAMPLE_NAME&gt;.html                        | A [HTML](http://en.wikipedia.org/wiki/HTML) version of the .tab file                                                               | 
| &lt;SAMPLE_NAME&gt;.raw.vcf.gz                  | The unfiltered variant calls from Freebayes                                                                                        | 
| &lt;SAMPLE_NAME&gt;.subs.vcf.gz                 | *Only substitution* variants from the final annotated variants                                                                     | 
| &lt;SAMPLE_NAME&gt;.tab                         | A simple [tab-separated](http://en.wikipedia.org/wiki/Tab-separated_values) summary of all the variants                            | 
| &lt;SAMPLE_NAME&gt;.txt                         | A summary of the Snippy run                                                                                                        | 
| &lt;SAMPLE_NAME&gt;.vcf.gz                      | The final annotated variants in [VCF](http://en.wikipedia.org/wiki/Variant_Call_Format) format                                     | 


#### Snippy-Core

Below is a description of the [Snippy-Core]([Snippy](https://github.com/tseemann/snippy)) results. For more details about
Snippy-Core outputs see [Snippy-Core - Outputs](https://github.com/tseemann/snippy#output-files-1).


| Filename        | Description                                                                       |
|-----------------|-----------------------------------------------------------------------------------|
| core-snp.aln.gz | A core SNP alignment in FASTA format                                              | 
| core-snp.tab.gz | Tab-separated columnar list of core SNP sites with alleles but **NO** annotations | 
| core-snp.txt    | Tab-separated columnar list of alignment/core-size statistics                     | 
| core-snp.vcf.gz | Multi-sample VCF file with genotype GT tags for all discovered alleles            |                                                                                                     | 





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
| snippy-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| snippy-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| snippy-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| snippy-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### Snippy Parameters


| Parameter | Description | Default |
|---|---|---|
| `--reference` | Reference genome in GenBank format |  |
| `--mapqual` | Minimum read mapping quality to consider | 60 |
| `--basequal` | Minimum base quality to consider | 13 |
| `--mincov` | Minimum site depth to for calling alleles | 10 |
| `--minfrac` | Minimum proportion for variant evidence (0=AUTO) | 0 |
| `--minqual` | Minimum QUALITY in VCF column 6 | 100 |
| `--maxsoft` | Maximum soft clipping to allow | 10 |
| `--bwaopt` | Extra BWA MEM options, eg. -x pacbio |  |
| `--fbopt` | Extra Freebayes options, eg. --theta 1E-6 --read-snp-limit 2 |  |

### Snippy-Core Parameters


| Parameter | Description | Default |
|---|---|---|
| `--maxhap` | Largest haplotype to decompose | 100 |

### Gubbins Parameters


| Parameter | Description | Default |
|---|---|---|
| `--iterations` | Maximum number of iterations | 5 |
| `--min_snps` | Min SNPs to identify a recombination block | 3 |
| `--min_window_size` | Minimum window size | 100 |
| `--max_window_size` | Maximum window size | 10000 |
| `--filter_percentage` | Filter out taxa with more than this percentage of gaps | 25.0 |
| `--remove_identical_sequences` | Remove identical sequences | False |
| `--gubbin_opts` | Extra Gubbins options in quotes |  |
| `--skip_recombination` | Skip Gubbins execution in subworkflows | False |

### IQ-TREE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--iqtree_model` | Substitution model name | HKY |
| `--bb` | Ultrafast bootstrap replicates | 1000 |
| `--alrt` | SH-like approximate likelihood ratio test replicates | 1000 |
| `--asr` | Ancestral state reconstruction by empirical Bayes | False |
| `--iqtree_opts` | Extra IQ-TREE options in quotes. |  |
| `--skip_phylogeny` | Skip IQ-TREE execution in subworkflows | False |

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
If you use Bactopia and `snippy` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [Gubbins](https://github.com/nickjcroucher/gubbins)  
    Croucher NJ, Page AJ, Connor TR, Delaney AJ, Keane JA, Bentley SD, Parkhill J, Harris SR [Rapid phylogenetic analysis of large samples of recombinant bacterial whole genome sequences using Gubbins.](https://doi.org/10.1093/nar/gku1196) _Nucleic Acids Research_ 43(3), e15. (2015)
  
- [IQ-TREE](https://github.com/Cibiv/IQ-TREE)  
    Nguyen L-T, Schmidt HA, von Haeseler A, Minh BQ [IQ-TREE: A fast and effective stochastic algorithm for estimating maximum likelihood phylogenies.](https://doi.org/10.1093/molbev/msu300) _Mol. Biol. Evol._ 32:268-274 (2015)
  
- [ModelFinder](https://github.com/Cibiv/IQ-TREE)  
    Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS [ModelFinder - Fast model selection for accurate phylogenetic estimates.](https://doi.org/10.1038/nmeth.4285) _Nat. Methods_ 14:587-589 (2017)
  
- [UFBoot2](https://github.com/Cibiv/IQ-TREE)  
    Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS [UFBoot2: Improving the ultrafast bootstrap approximation.](https://doi.org/10.1093/molbev/msx281) _Mol. Biol. Evol._ 35:518–522 (2018)
  
- [Snippy](https://github.com/tseemann/snippy)  
    Seemann T [Snippy: fast bacterial variant calling from NGS reads](https://github.com/tseemann/snippy) (GitHub)
  
- [snp-dists](https://github.com/tseemann/snp-dists)  
    Seemann T [snp-dists - Pairwise SNP distance matrix from a FASTA sequence alignment.](https://github.com/tseemann/snp-dists) (GitHub)
  
