---
title: meta.docs.meta.title
description: meta.docs.meta.description
tags:
---



# Bactopia Tool - `merlin`
_MinmER assisted species-specific bactopia tool seLectIoN_, or Merlin, uses distances based
on the RefSeq sketch downloaded by `bactopia datasets` to automatically run species-specific tools.

Currently Merlin knows 16 spells for which cover the following:

| Genus/Species | Tools |
|---------------|-------|
| Escherichia   | [ECTyper](/bactopia-tools/ectyper/)  |
| Haemophilus   | [hicap](/bactopia-tools/hicap/), [HpsuisSero](/bactopia-tools/ssuissero/) |
| Klebsiella | [Kleborate](/bactopia-tools/kleborate/) |
| Legionella | [legsta](/bactopia-tools/legsta/) |
| Listeria | [LisSero](/bactopia-tools/lissero/) |
| Mycobacterium | [TBProfiler](/bactopia-tools/tbprofiler/) |
| Neisseria | [meningotype](/bactopia-tools/meningotype/), [ngmaster](/bactopia-tools/ngmaster/) |
| Salmonella | [SeqSero2](/bactopia-tools/seqsero2/), [SISTR](/bactopia-tools/sistr/) |
| Staphylococcus | [AgrVATE](/bactopia-tools/agrvate/), [spaTyper](/bactopia-tools/spatyper/), [staphopia-sccmec](/bactopia-tools/staphopiasccmec/) |
| Streptococcus | [emmtyper](/bactopia-tools/emmtyper/), [SsuisSero](/bactopia-tools/ssuissero/) |

Merlin is avialable as an independent Bactopia Tool, or in the Bactopia with the `--ask_merlin` parameter. Even better,
if you want to force Merlin to execute all species-specific tools (no matter the distance), you can use `--full_merlin`.
Then all the spells will be unleashed!


## Example Usage
```
bactopia --wf merlin \
  --bactopia /path/to/your/bactopia/results \ 
  --include includes.txt  
```

## Output Overview

Below is the default output structure for the `merlin` tool. Where possible the 
file descriptions below were modified from a tools description.

```{bash}
merlin/
├── <SAMPLE_NAME>
│   ├── agrvate
│   │   ├── <SAMPLE_NAME>-agr_gp.tab
│   │   ├── <SAMPLE_NAME>-blastn_log.txt
│   │   └── <SAMPLE_NAME>-summary.tab
│   ├── ectyper
│   │   ├── <SAMPLE_NAME>.tsv
│   │   └── blast_output_alleles.txt
│   ├── emmtyper
│   │   └── <SAMPLE_NAME>.tsv
│   ├── hicap
│   │   └── <SAMPLE_NAME>.tsv
│   ├── hpsuissero
│   │   └── <SAMPLE_NAME>_serotyping_res.tsv
│   ├── kleborate
│   │   └── <SAMPLE_NAME>.results.txt
│   ├── legsta
│   │   └── <SAMPLE_NAME>.tsv
│   ├── lissero
│   │   └── <SAMPLE_NAME>.tsv
│   ├── logs
│   │   └── <BACTOPIA_TOOL>
│   │       ├── nf-<BACTOPIA_TOOL>.{begin,err,log,out,run,sh,trace}
│   │       └── versions.yml
│   ├── mashdist
│   │   └── <SAMPLE_NAME>-dist.txt
│   ├── meningotype
│   │   └── <SAMPLE_NAME>.tsv
│   ├── ngmaster
│   │   └── <SAMPLE_NAME>.tsv
│   ├── seqsero2
│   │   ├── <SAMPLE_NAME>_log.txt
│   │   ├── <SAMPLE_NAME>_result.tsv
│   │   └── <SAMPLE_NAME>_result.txt
│   ├── sistr
│   │   ├── <SAMPLE_NAME>-allele.fasta.gz
│   │   ├── <SAMPLE_NAME>-allele.json.gz
│   │   ├── <SAMPLE_NAME>-cgmlst.csv
│   │   └── <SAMPLE_NAME>.tsv
│   ├── spatyper
│   │   └── <SAMPLE_NAME>.tsv
│   ├── ssuissero
│   │   └── <SAMPLE_NAME>_serotyping_res.tsv
│   ├── staphopiasccmec
│   │   └── <SAMPLE_NAME>.tsv
│   └── tbprofiler
│       ├── <SAMPLE_NAME>.results.csv
│       ├── <SAMPLE_NAME>.results.json
│       ├── <SAMPLE_NAME>.results.txt
│       ├── bam
│       │   └── <SAMPLE_NAME>.bam
│       └── vcf
│           └── <SAMPLE_NAME>.targets.csq.vcf.gz
├── logs
│   ├── csvtk_concat
│   │   └── <BACTOPIA_TOOL>
│   │       ├── nf-csvtk_concat.{begin,err,log,out,run,sh,trace}
│   │       └── versions.yml
│   └── custom_dumpsoftwareversions
│       ├── nf-custom_dumpsoftwareversions.{begin,err,log,out,run,sh,trace}
│       └── versions.yml
├── nf-reports
│   ├── merlin-dag.dot
│   ├── merlin-report.html
│   ├── merlin-timeline.html
│   └── merlin-trace.txt
├── agrvate.tsv
├── ectyper.tsv
├── emmtyper.tsv
├── hicap.tsv
├── hpsuissero.tsv
├── kleborate.tsv
├── legsta.tsv
├── lissero.tsv
├── meningotype.tsv
├── ngmaster.tsv
├── seqsero2.tsv
├── sistr.tsv
├── software_versions.yml
├── software_versions_mqc.yml
├── spatyper.tsv
├── ssuissero.tsv
└── staphopiasccmec.tsv

```

!!! info "Directory structure might be different"

    `merlin` is available as a standalone Bactopia Tool, as well as from
    the main Bactopia workflow (e.g. through Staphopia or Merlin). If executed 
    from Bactopia, the `merlin` directory structure might be different, but the
    output descriptions below still apply.



### Results

#### Top Level

Below are results that are in the base directory.


| Filename    | Description |
|-------------|-------------|
| agrvate.tsv | A merged TSV file with `AgrVATE` results from all samples |
| ectyper.tsv | A merged TSV file with `ECTyper` results from all samples |
| emmtyper.tsv | A merged TSV file with `emmtyper` results from all samples |
| hicap.tsv  | A merged TSV file with `hicap` results from all samples |
| hpsuissero.tsv | A merged TSV file with `HpsuisSero` results from all samples |
| kleborate.tsv | A merged TSV file with `Kleborate` results from all samples |
| legsta.tsv  | A merged TSV file with `legsta` results from all samples |
| lissero.tsv  | A merged TSV file with `LisSero` results from all samples |
| meningotype.tsv  | A merged TSV file with `meningotype` results from all samples |
| ngmaster.tsv  | A merged TSV file with `ngmaster` results from all samples |
| seqsero2.tsv  | A merged TSV file with `seqsero2` results from all samples |
| sistr.tsv  | A merged TSV file with `SISTR` results from all samples |
| spatyper.tsv  | A merged TSV file with `spaTyper` results from all samples |
| ssuissero.tsv  | A merged TSV file with `SsuisSero` results from all samples |
| staphopiasccmec.tsv  | A merged TSV file with `staphopia-sccmec` results from all samples |


#### AgrVATE

Below is a description of the _per-sample_ results from [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE).


| Extension       | Description |
|-----------------|-------------|
| -agr_gp.tab     | Detailed report for _agr_ kmer matches |
| -blastn_log.txt | Log files from programs called by `AgrVATE` |
| -summary.tab    | A final summary report for _agr_ typing |


#### ECTyper

Below is a description of the _per-sample_ results from [ECTyper](https://github.com/phac-nml/ecoli_serotyping).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `ECTyper` result, see [ECTyper - Report format](https://github.com/phac-nml/ecoli_serotyping#report-format) for details  |
| blast_output_alleles.txt | Allele report generated from BLAST results |


#### emmtyper

Below is a description of the _per-sample_ results from [emmtyper](https://github.com/MDU-PHL/emmtyper).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `emmtyper` result, see [emmtyper - Result format](https://github.com/MDU-PHL/emmtyper#result-format) for details  |


#### hicap

Below is a description of the _per-sample_ results from [hicap](https://github.com/scwatts/hicap).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.gbk  | GenBank file and cap locus annotations |
| &lt;SAMPLE_NAME&gt;.svg  | Visualization of annotated cap locus |
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `hicap` results |


#### HpsuisSero

Below is a description of the _per-sample_ results from [HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_serotyping_res.tsv  | A tab-delimited file with `HpsuisSero` result |


#### Kleborate

Below is a description of the _per-sample_ results from [Kleborate](https://github.com/katholt/Kleborate).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.results.tsv  | A tab-delimited file with `Kleborate` result, see [Kleborate - Example output](https://github.com/katholt/Kleborate/wiki/Tests-and-example-outputs#example-output) for more details |


#### legsta

Below is a description of the _per-sample_ results from [legsta](https://github.com/tseemann/legsta).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `legsta` result, see [legsta - Output](https://github.com/tseemann/legsta#output) for more details |


#### LisSero

Below is a description of the _per-sample_ results from [LisSero](https://github.com/MDU-PHL/LisSero).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `LisSero` results |


#### Mash

Below is a description of the _per-sample_ results from [Mash](https://github.com/marbl/Mash).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-dist.txt  | A tab-delimited file with `mash dist` results |


#### meningotype

Below is a description of the _per-sample_ results from [meningotype](https://github.com/MDU-PHL/meningotype) .


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `meningotype` result |


#### ngmaster

Below is a description of the _per-sample_ results from [ngmaster](https://github.com/MDU-PHL/ngmaster).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `ngmaster` results |


#### SeqSero2

Below is a description of the _per-sample_ results from [SeqSero2](https://github.com/denglab/SeqSero2).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `SeqSero2` results |
| &lt;SAMPLE_NAME&gt;.txt  | A text file with key-value pairs of `SeqSero2` results |


#### SISTR

Below is a description of the _per-sample_ results from [SISTR](https://github.com/phac-nml/sistr_cmd).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-allele.fasta.gz  | A FASTA file of the cgMLST allele search results  |
| &lt;SAMPLE_NAME&gt;-allele.json.gz  | JSON formated cgMLST allele search results, see [SISTR - cgMLST search results](https://github.com/phac-nml/sistr_cmd#cgmlst-allele-search-results) for more details |
| &lt;SAMPLE_NAME&gt;-cgmlst.csv  | A comma-delimited summary of the cgMLST allele search results |
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `SISTR` results, see [SISTR - Primary results](https://github.com/phac-nml/sistr_cmd#primary-results-output--o-sistr-results) for more details |


#### spaTyper

Below is a description of the _per-sample_ results from [spaTyper](https://github.com/HCGB-IGTP/spaTyper).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `spaTyper` results |


#### SsuisSero

Below is a description of the _per-sample_ results from [SsuisSero](https://github.com/jimmyliu1326/SsuisSero).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_serotyping_res.tsv  | A tab-delimited file with `SsuisSero` results |


#### staphopia-sccmec

Below is a description of the _per-sample_ results from [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv  | A tab-delimited file with `staphopia-sccmec` results |


#### TBProfiler

Below is a description of the _per-sample_ results from [TBProfiler](https://github.com/jodyphelan/TBProfiler).


| Filename                 | Description |
|--------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.results.csv  | A CSV formated `TBProfiler` result file of resistance and strain type |
| &lt;SAMPLE_NAME&gt;.results.json  | A JSON formated `TBProfiler` result file of resistance and strain type |
| &lt;SAMPLE_NAME&gt;.results.txt  | A text file with `TBProfiler` results |
| &lt;SAMPLE_NAME&gt;.bam  |BAM file with alignment details |
| &lt;SAMPLE_NAME&gt;.targets.csq.vcf.gz | VCF with variant info again refernce genomes |





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
| merlin-dag.dot | The Nextflow [DAG visualisation](https://www.nextflow.io/docs/latest/tracing.html#dag-visualisation) |
| merlin-report.html | The Nextflow [Execution Report](https://www.nextflow.io/docs/latest/tracing.html#execution-report) |
| merlin-timeline.html | The Nextflow [Timeline Report](https://www.nextflow.io/docs/latest/tracing.html#timeline-report) |
| merlin-trace.txt | The Nextflow [Trace](https://www.nextflow.io/docs/latest/tracing.html#trace-report) report |


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


### mashdist Parameters


| Parameter | Description | Default |
|---|---|---|
| `--mash_sketch` | The reference sequence as a Mash Sketch (.msh file) |  |
| `--mash_seed` | Seed to provide to the hash function | 42 |
| `--mash_table` |  Table output (fields will be blank if they do not meet the p-value threshold) | False |
| `--mash_m` | Minimum copies of each k-mer required to pass noise filter for reads | 1 |
| `--mash_w` | Probability threshold for warning about low k-mer size. | 0.01 |
| `--max_p` | Maximum p-value to report. | 1.0 |
| `--max_dist` | Maximum distance to report. | 1.0 |
| `--merlin_dist` | Maximum distance to report when using Merlin . | 0.1 |
| `--full_merlin` | Go full Merlin and run all species-specific tools, no matter the Mash distance | False |
| `--use_fastqs` | Query with FASTQs instead of the assemblies | False |

### AgrVATE Parameters


| Parameter | Description | Default |
|---|---|---|
| `--typing_only` | agr typing only. Skips agr operon extraction and frameshift detection | False |

### ECTyper Parameters


| Parameter | Description | Default |
|---|---|---|
| `--opid` | Percent identity required for an O antigen allele match | 90 |
| `--opcov` | Minumum percent coverage required for an O antigen allele match | 90 |
| `--hpid` | Percent identity required for an H antigen allele match | 95 |
| `--hpcov` | Minumum percent coverage required for an H antigen allele match | 50 |
| `--verify` | Enable E. coli species verification | False |
| `--print_alleles` | Prints the allele sequences if enabled as the final column | False |

### emmtyper Parameters


| Parameter | Description | Default |
|---|---|---|
| `--emmtyper_wf` | Workflow for emmtyper to use. | blast |
| `--cluster_distance` | Distance between cluster of matches to consider as different clusters | 500 |
| `--percid` | Minimal percent identity of sequence | 95 |
| `--culling_limit` | Total hits to return in a position | 5 |
| `--mismatch` | Threshold for number of mismatch to allow in BLAST hit | 5 |
| `--align_diff` | Threshold for difference between alignment length and subject length in BLAST | 5 |
| `--gap` | Threshold gap to allow in BLAST hit | 2 |
| `--min_perfect` | Minimum size of perfect match at 3 primer end | 15 |
| `--min_good` | Minimum size where there must be 2 matches for each mismatch | 15 |
| `--max_size` | Maximum size of PCR product | 2000 |

### hicap Parameters


| Parameter | Description | Default |
|---|---|---|
| `--database_dir` | Directory containing locus database |  |
| `--model_fp` | Path to prodigal model |  |
| `--full_sequence` | Write the full input sequence out to the genbank file rather than just the region surrounding and including the locus | False |
| `--hicap_debug` | hicap will print debug messages | False |
| `--gene_coverage` | Minimum percentage coverage to consider a single gene complete | 0.8 |
| `--gene_identity` | Minimum percentage identity to consider a single gene complete | 0.7 |
| `--broken_gene_length` | Minimum length to consider a broken gene | 60 |
| `--broken_gene_identity` | Minimum percentage identity to consider a broken gene | 0.8 |

### HpsuisSero Parameters


| Parameter | Description | Default |
|---|---|---|

### Kleborate Parameters


| Parameter | Description | Default |
|---|---|---|
| `--skip_resistance` | Turn off resistance genes screening | False |
| `--skip_kaptive` | Turn off Kaptive screening of K and O loci | False |
| `--min_identity` | Minimum alignment percent identity for main results | 90.0 |
| `--kleborate_min_coverage` | Minimum alignment percent coverage for main results | 80.0 |
| `--min_spurious_identity` | Minimum alignment percent identity for spurious results | 80.0 |
| `--min_spurious_coverage` | Minimum alignment percent coverage for spurious results | 40.0 |
| `--min_kaptive_confidence` | Minimum Kaptive confidence to call K/O loci - confidence levels below this will be reported as unknown | Good |
| `--force_index` | Rebuild the BLAST index at the start of execution | False |

### legsta Parameters


| Parameter | Description | Default |
|---|---|---|
| `--noheader` | Don't print header row | False |

### LisSero Parameters


| Parameter | Description | Default |
|---|---|---|
| `--min_id` | Minimum percent identity to accept a match | 95.0 |
| `--min_cov` | Minimum coverage of the gene to accept a match | 95.0 |

### meningotype Parameters
You can use these parameters to fine-tune your meningotype analysis

| Parameter | Description | Default |
|---|---|---|
| `--finetype` | perform porA and fetA fine typing | False |
| `--porB` | perform porB sequence typing (NEIS2020) | False |
| `--bast` | perform Bexsero antigen sequence typing (BAST) | False |
| `--mlst` | perform MLST | False |
| `--all` | perform MLST, porA, fetA, porB, BAST typing | False |

### ngmaster Parameters


| Parameter | Description | Default |
|---|---|---|
| `--csv` | output comma-separated format (CSV) rather than tab-separated | False |

### SeqSero2 Parameters


| Parameter | Description | Default |
|---|---|---|
| `--run_mode` | Workflow to run. 'a' allele mode, or 'k' k-mer mode | k |
| `--input_type` | Input format to analyze. 'assembly' or 'fastq' | assembly |
| `--bwa_mode` | Algorithms for bwa mapping for allele mode | mem |

### SISTR Parameters


| Parameter | Description | Default |
|---|---|---|
| `--full_cgmlst` |  Use the full set of cgMLST alleles which can include highly similar alleles | False |

### spaTyper Parameters


| Parameter | Description | Default |
|---|---|---|
| `--repeats` | List of spa repeats |  |
| `--repeat_order` | List spa types and order of repeats |  |
| `--do_enrich` | Do PCR product enrichment | False |

### staphopia-sccmec Parameters


| Parameter | Description | Default |
|---|---|---|
| `--hamming` | Report the results as hamming distances | False |

### SsuisSero Parameters


| Parameter | Description | Default |
|---|---|---|

### TBProfiler Parameters


| Parameter | Description | Default |
|---|---|---|
| `--call_whole_genome` | Call whole genome | False |
| `--mapper` | Mapping tool to use. If you are using nanopore data it will default to minimap2 | bwa |
| `--caller` | Variant calling tool to use | freebayes |
| `--calling_params` | Extra variant caller options in quotes |  |
| `--tb_min_depth` | Minimum depth required to call variant | 10 |
| `--tb_af` | Minimum allele frequency to call variants | 0.1 |
| `--tb_reporting_af` | Minimum allele frequency to use variants for prediction | 0.1 |
| `--coverage_fraction_threshold` | Cutoff used to calculate fraction of region covered by <= this value | 0 |
| `--suspect` | Use the suspect suite of tools to add ML predictions | False |
| `--no_flagstat` | Don't collect flagstats | False |
| `--no_delly` | Don't run delly | False |


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
If you use Bactopia and `merlin` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE)  
    Raghuram V. [AgrVATE: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.](https://github.com/VishnuRaghuram94/AgrVATE) (GitHub)
  
- [ECTyper](https://github.com/phac-nml/ecoli_serotyping)  
    Laing C, Bessonov K, Sung S, La Rose C [ECTyper - In silico prediction of _Escherichia coli_ serotype](https://github.com/phac-nml/ecoli_serotyping) (GitHub)  
- [emmtyper](https://github.com/MDU-PHL/emmtyper)  
    Tan A, Seemann T, Lacey D, Davies M, Mcintyre L, Frost H, Williamson D, Gonçalves da Silva A [emmtyper - emm Automatic Isolate Labeller](https://github.com/MDU-PHL/emmtyper) (GitHub)
  
- [hicap](https://github.com/scwatts/hicap)  
    Watts SC, Holt KE [hicap: in silico serotyping of the Haemophilus influenzae capsule locus.](https://doi.org/10.1128/JCM.00190-19) _Journal of Clinical Microbiology_ JCM.00190-19 (2019)
  
- [HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero)  
    Lui J [HpsuisSero: Rapid _Haemophilus parasuis_ serotyping](https://github.com/jimmyliu1326/HpsuisSero) (GitHub)
  
- [Kleborate](https://github.com/katholt/Kleborate)  
    Lam MMC, Wick RR, Watts, SC, Cerdeira LT, Wyres KL, Holt KE [A genomic surveillance framework and genotyping tool for Klebsiella pneumoniae and its related species complex.](https://doi.org/10.1038/s41467-021-24448-3) _Nat Commun_ 12, 4188 (2021)
  
- [legsta](https://github.com/tseemann/legsta)  
    Seemann T [legsta: In silico Legionella pneumophila Sequence Based Typing](https://github.com/tseemann/legsta) (GitHub)
  
- [LisSero](https://github.com/MDU-PHL/LisSero)  
    Kwong J, Zhang J, Seeman T, Horan, K, Gonçalves da Silva A [LisSero - _In silico_ serotype prediction for _Listeria monocytogenes_](https://github.com/MDU-PHL/LisSero) (GitHub)
  
- [Mash](https://github.com/marbl/Mash)  
    Ondov BD, Treangen TJ, Melsted P, Mallonee AB, Bergman NH, Koren S, Phillippy AM [Mash: fast genome and metagenome distance estimation using MinHash](http://dx.doi.org/10.1186/s13059-016-0997-x). _Genome Biol_ 17, 132 (2016)
  
- [meningotype](https://github.com/MDU-PHL/meningotype)  
    Kwong JC, Gonçalves da Silva A, Stinear TP, Howden BP, & Seemann T [meningotype: in silico typing for _Neisseria meningitidis_.](https://github.com/MDU-PHL/meningotype) (GitHub)
  
- [ngmaster](https://github.com/MDU-PHL/ngmaster)  
    Kwong J, Gonçalves da Silva A, Schultz M, Seeman T [ngmaster - _In silico_ multi-antigen sequence typing for _Neisseria gonorrhoeae_ (NG-MAST)](https://github.com/MDU-PHL/ngmaster) (GitHub)
  
- [SeqSero2](https://github.com/denglab/SeqSero2)  
    Zhang S, Den-Bakker HC, Li S, Dinsmore BA, Lane C, Lauer AC, Fields PI, Deng X. [SeqSero2: rapid and improved Salmonella serotype determination using whole genome sequencing data.](https://doi.org/10.1128/AEM.01746-19) _Appl Environ Microbiology_ 85(23):e01746-19 (2019)
  
- [SISTR](https://github.com/phac-nml/sistr_cmd)  
    Yoshida CE, Kruczkiewicz P, Laing CR, Lingohr EJ, Gannon VPJ, Nash JHE, Taboada EN [The Salmonella In Silico Typing Resource (SISTR): An Open Web-Accessible Tool for Rapidly Typing and Subtyping Draft Salmonella Genome Assemblies.](https://doi.org/10.1371/journal.pone.0147101) _PloS One_, 11(1), e0147101. (2016)
  
- [spaTyper](https://github.com/HCGB-IGTP/spaTyper)  
    Sanchez-Herrero JF, and Sullivan M [spaTyper: Staphylococcal protein A (spa) characterization pipeline](http://doi.org/10.5281/zenodo.4063625). Zenodo. (2020)
  
- [SsuisSero](https://github.com/jimmyliu1326/SsuisSero)  
    Lui J [SsuisSero: Rapid _Streptococcus suis_ serotyping](https://github.com/jimmyliu1326/SsuisSero) (GitHub)
  
- [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec)  
    Petit III RA, Read TD [_Staphylococcus aureus_ viewed from the perspective of 40,000+ genomes.](http://dx.doi.org/10.7717/peerj.5261) _PeerJ_ 6, e5261 (2018)
  
- [TBProfiler](https://github.com/jodyphelan/TBProfiler)  
    Phelan JE, O’Sullivan DM, Machado D, Ramos J, Oppong YEA, Campino S, O’Grady J, McNerney R, Hibberd ML, Viveiros M, Huggett JF, Clark TG [Integrating informatics tools and portable sequencing technology for rapid detection of resistance to anti-tuberculous drugs.](https://doi.org/10.1186/s13073-019-0650-x) _Genome Med_ 11, 41 (2019)
  
