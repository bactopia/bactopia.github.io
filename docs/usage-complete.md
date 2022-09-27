---
title: Bactopia - Complete Usage
description: >
    A complete list and description of each and every parameter you can change in Bactopia.
---
# Runtime Parameters

Bactopia includes numerous (180+) configurable parameters. Now that doesn't mean you need to go in there and start changing them, but there will be times when you might have to. By exposing all these parameters, you can easily change them to fit your needs. In the following sections, these parameters are grouped by which Nextflow process they are applicable to. The description and default values for these parameters were taken from the program to which they apply.

!!! note "Not all of the available parameters for each and every program are available"
    If you see a tool in which a parameter has not been made available, please make a suggestion!

## Required Parameters
The required parameters depends on how many samples are to be proccessed. You can learn more about which approach to take at [Specifying Input FASTQs](usage-basic.md#fastq-inputs).
```{bash}
---------------------------------------------
   _                _              _
  | |__   __ _  ___| |_ ___  _ __ (_) __ _
  | '_ \ / _` |/ __| __/ _ \| '_ \| |/ _` |
  | |_) | (_| | (__| || (_) | |_) | | (_| |
  |_.__/ \__,_|\___|\__\___/| .__/|_|\__,_|
                            |_|
  bactopia v2.x.x
  Bactopia is a flexible pipeline for complete analysis of bacterial genomes.
---------------------------------------------
Typical pipeline command:

  bactopia --samples samples.txt --datasets datasets/ --species 'Staphylococcus aureus'

Required Parameters
  ### For Procesessing Multiple Samples
  --samples                     [string]  A FOFN with sample names and paths to 
                                            FASTQ/FASTAs to process

  ### For Processing A Single Sample
  --R1                          [string]  First set of compressed (gzip) paired-end
                                            FASTQ reads (requires --R2 and --sample)
  --R2                          [string]  Second set of compressed (gzip) paired-end
                                            FASTQ reads (requires --R1 and --sample)
  --SE                          [string]  Compressed (gzip) single-end FASTQ reads 
                                            (requires --sample)
  --ont                         [boolean] Treat `--SE` as long reads for analysis.
                                            (requires --sample)
  --hybrid                      [boolean] Treat `--SE` as long reads for hybrid assembly. 
                                            (requires --R1, --R2, --SE and --sample)
  --sample                      [string]  Sample name to use for the input sequences

  ### For Downloading from SRA/ENA or NCBI Assembly
  **Note: Downloaded assemblies will have error free Illumina reads simulated for processing.**
  --accessions                  [string]  A file containing ENA/SRA Experiment accessions
                                            or NCBI Assembly accessions to processed
  --accession                   [string]  Sample name to use for the input sequences

  ### For Processing an Assembly
  **Note: Assemblies will have error free Illumina reads simulated for processing.**
  --assembly                    [string]  A assembled genome in compressed FASTA format.
                                            (requires --sample)
```

## Dataset Parameters
If you followed the steps in [Build Datasets](datasets.md), you can use the following parameters to point Bactopia to you datasets.

```{bash}
Dataset Parameters
  --datasets                    [string]  The path to datasets that have already been set up
  --species                     [string]  Name of species for species-specific dataset to use
  --ask_merlin                  [boolean] Ask Merlin to execute species specific Bactopia
                                            Tools based on Mash distances
  --coverage                    [integer] Reduce samples to a given coverage [default: 100]
  --genome_size                 [string]  Expected genome size (bp) for all samples, a
                                            value of '0' will disable read error
                                            correction and read subsampling, otherwise
                                            estimate with Mash [default: 0]
  --available_datasets          [boolean] Print a list of available datasets found based
                                            on location given by `--datasets`
```

### `--genome_size`
Throughout the Bactopia workflow a genome size is used for various tasks. By default, a genome size is estimated using Mash. However, users can provide their own value for genome size, use values based on [Species Specific Datasets](/datasets/#species-specific), or completely disable it.

| Value   | Result                                                                        |
|---------|-------------------------------------------------------------------------------|
| *empty* | Mash is used to estimate the genome size                                      |
| integer | Uses the genome size (e.g. `--genome_size 2800000`) provided by the user      |
| 0       | Read error correct and read subsampling will be disabled.                     |
| min     | Requires `--species`, the minimum completed genome size for a species is used |
| median  | Requires `--species`, the median completed genome size for a species is used  |
| mean    | Requires `--species`, the mean completed genome size for a species is used    |
| max     | Requires `--species`, the maximum completed genome size for a species is used |

!!! error "Mash may not be the most accurate estimate"
    Mash is very convenient to quickly estimate a genome size, but it may not be the most accurate in all cases and will differ between samples. It is recommended that when possible a known genome size or one based off completed genomes should be used. 

## Gather Samples Parameters
```{bash}
  --skip_fastq_check            [boolean] Skip minimum requirement checks for input FASTQs
  --min_basepairs               [integer] The minimum amount of basepairs required to continue
                                            downstream analyses. [default: 2241820]
  --min_reads                   [integer] The minimum amount of reads required to continue
                                            downstream analyses. [default: 7472]
  --min_coverage                [integer] The minimum amount of coverage required to continue
                                            downstream analyses. [default: 10]
  --min_proportion              [number]  The minimum proportion of basepairs for paired-end
                                            reads to continue downstream analyses.
                                            [default: 0.5]
  --min_genome_size             [integer] The minimum estimated genome size allowed for the
                                            input sequence to continue downstream analyses.
                                            [default: 100000]
  --max_genome_size             [integer] The maximum estimated genome size allowed for the
                                            input sequence to continue downstream analyses.
                                            [default: 18040666]
  --attempts                    [integer] Maximum times to attempt downloads [default: 3]
  --use_ena                     [boolean] Download FASTQs from ENA
  --no_cache                    [boolean] Skip caching the assembly summary file from
                                            ncbi-genome-download
```

## QC Reads Parameters
```{bash}
QC Reads Parameters
  --skip_qc                     [boolean] The QC step will be skipped and it will be assumed
                                            the inputs sequences have already been QCed.
  --skip_qc_plots               [boolean] QC Plot creation by FastQC or Nanoplot will be
                                            skipped
  --skip_error_correction       [boolean] FLASH error correction of reads will be skipped.
  --adapters                    [string]  A FASTA file containing adapters to remove
  --adapter_k                   [integer] Kmer length used for finding adapters. [default: 23]
  --phix                        [string]  phiX174 reference genome to remove
  --phix_k                      [integer] Kmer length used for finding phiX174. [default: 31]
  --ktrim                       [string]  Trim reads to remove bases matching reference kmers
                                            [default: r]
  --mink                        [integer] Look for shorter kmers at read tips down to this
                                            length, when k-trimming or masking. [default: 11]
  --hdist                       [integer] Maximum Hamming distance for ref kmers (subs only)
                                            [default: 1]
  --tpe                         [string]  When kmer right-trimming, trim both reads to the
                                            minimum length of either [default: t]
  --tbo                         [string]  Trim adapters based on where paired reads overlap
                                            [default: t]
  --qtrim                       [string]  Trim read ends to remove bases with quality below
                                            trimq. [default: rl]
  --trimq                       [integer] Regions with average quality BELOW this will be
                                            trimmed if qtrim is set to something other than
                                            f [default: 6]
  --maq                         [integer] Reads with average quality (after trimming) below
                                            this will be discarded [default: 10]
  --minlength                   [integer] Reads shorter than this after trimming will be
                                            discarded [default: 35]
  --ftm                         [integer] If positive, right-trim length to be equal to zero,
                                            modulo this number [default: 5]
  --tossjunk                    [string]  Discard reads with invalid characters as bases
                                            [default: t]
  --qout                        [string]  PHRED offset to use for output FASTQs [default: 33]
  --maxcor                      [integer] Max number of corrections within a 20bp window
                                            [default: 1]
  --sampleseed                  [integer] Set to a positive number to use as the random number
                                            generator seed for sampling [default: 42]
  --ont_minlength               [integer] ONT Reads shorter than this will be discarded
                                            [default: 1000]
  --ont_minqual                 [integer] Minimum average read quality filter of ONT reads
  --porechop_opts               [integer] Extra Porechop options in quotes
  --nanoplot_opts               [integer] Extra NanoPlot options in quotes
  --bbduk_opts                  [integer] Extra BBDuk options in quotes
```

## Assembly Parameters
```{bash}
Assemble Genome Parameters
  --shovill_assembler           [string]  Assembler to be used by Shovill [default: skesa]
  --dragonflye_assembler        [string]  Assembler to be used by Dragonflye [default: flye]
  --use_unicycler               [boolean] Use unicycler for paired end assembly
  --min_contig_len              [integer] Minimum contig length <0=AUTO> [default: 500]
  --min_contig_cov              [integer] Minimum contig coverage <0=AUTO> [default: 2]
  --contig_namefmt              [string]  Format of contig FASTA IDs in 'printf' style
  --shovill_opts                [string]  Extra assembler options in quotes
  --shovill_kmers               [string]  K-mers to use <blank=AUTO>
  --trim                        [boolean] Enable adaptor trimming
  --no_stitch                   [boolean] Disable read stitching for paired-end reads
  --no_corr                     [boolean] Disable post-assembly correction
  --unicycler_mode              [string]  Bridging mode used by Unicycler [default: normal]
  --min_polish_size             [integer] Contigs shorter than this value (bp) will not be
                                            polished using Pilon [default: 10000]
  --min_component_size          [integer] Graph dead ends smaller than this size (bp) will
                                            be removed from the final graph [default: 1000]
  --min_dead_end_size           [integer] Graph dead ends smaller than this size (bp) will
                                            be removed from the final graph [default: 1000]
  --medaka_model                [string]  The model to use for Medaka polishing
  --medaka_steps                [integer] The number of Medaka polishing steps to conduct
  --racon_steps                 [integer] The number of Racon polishing steps to conduct
                                            [default: 1]
  --no_polish                   [boolean] Skip the assembly polishing step
  --no_miniasm                  [boolean] Skip miniasm+Racon bridging
  --no_rotate                   [boolean] Do not rotate completed replicons to start at a
                                             standard gene
  --reassemble                  [boolean] If reads were simulated, they will be used to
                                            create a new assembly.
```

## Assembly QC Parameters
```{bash}
Assembly QC Parameters
  --run_checkm                  [boolean] Run CheckM in the assembly QC step
  --checkm_unique               [integer] Minimum number of unique phylogenetic markers
                                            required to use lineage-specific marker set.
                                            [default: 10]
  --checkm_multi                [integer] Maximum number of multi-copy phylogenetic markers
                                            before defaulting to domain-level marker set.
                                            [default: 10]
  --aai_strain                  [number]  AAI threshold used to identify strain heterogeneity
                                            [default: 0.9]
  --checkm_length               [number]  Percent overlap between target and query
                                            [default: 0.7]
  --full_tree                   [boolean] Use the full tree (requires ~40GB of memory) for
                                            determining lineage of each bin.
  --skip_pseudogene_correction  [boolean] Skip identification and filtering of pseudogene
  --ignore_thresholds           [boolean] Ignore model-specific score thresholds
  --checkm_ali                  [boolean] Generate HMMER alignment file for each bin
  --checkm_nt                   [boolean] Generate nucleotide gene sequences for each bin
  --force_domain                [boolean] Use domain-level sets for all bins
  --no_refinement               [boolean] Do not perform lineage-specific marker set refinement
  --individual_markers          [boolean] Treat marker as independent
  --skip_adj_correction         [boolean] Do not exclude adjacent marker genes when estimating
                                            contamination
  --contig_thresholds           [string]  Comma-separated list of contig length thresholds
                                            [default: 0,1000,10000,100000,250000,1000000]
  --plots_format                [string]  Save plots in specified format [default: pdf]
```

## Annotate Genome Parameters
```{bash}
Annotate Genome Parameters
  --compliant                   [boolean] Force Genbank/ENA/DDJB compliance
  --centre                      [string]  Sequencing centre ID [default: Bactopia]
  --addmrna                     [boolean] Add 'mRNA' features for each 'CDS' feature
  --rawproduct                  [boolean] Do not clean up /product annotation
  --cdsrnaolap                  [boolean] Allow [tr]RNA to overlap CDS
  --prokka_evalue               [string]  Similarity e-value cut-off [default: 1e-09]
  --prokka_coverage             [integer] Minimum coverage on query protein [default: 80]
  --nogenes                     [boolean] Do not add 'gene' features for each 'CDS' feature
  --norrna                      [boolean] Don't run rRNA search
  --notrna                      [boolean] Don't run tRNA search
  --rnammer                     [boolean] Prefer RNAmmer over Barrnap for rRNA prediction
  --rfam                        [boolean] Enable searching for ncRNAs with Infernal+Rfam
  --skip_prodigal_tf            [boolean] If a Prodigal training file was found, it will not
                                            be used
```

## Minmer Sketch Parameters
```{bash}
Minmer Sketch Parameters
  --count_31mers                [boolean] Enable 31-mer counting with McCortex
  --keep_singletons             [boolean] Keep all counted 31-mers
  --sketch_size                 [integer] Sketch size. Each sketch will have at most this many
                                            non-redundant min-hashes. [default: 10000]
  --sourmash_scale              [integer] Choose number of hashes as 1 in FRACTION of input
                                            k-mers [default: 10000]
```

## Minmer Query Parameters
```{bash}
Minmer Query Parameters
  --no_winner_take_all          [boolean] Disable winner-takes-all strategy for identity
                                            estimates
  --screen_i                    [number]  Minimum identity to report. [default: 0.8]
```

## Antimicrobial Resistance Parameters
```{bash}
Antimicrobial Resistance Parameters
  --skip_amr                    [boolean] Skip running AMRFinder+.
  --amr_plus                    [boolean] Add the plus genes to the report
  --amr_report_common           [boolean] Suppress proteins common to a taxonomy group
  --amr_organism                [string]  Taxonomy group: Campylobacter, Escherichia,
                                            Klebsiella, Salmonella, Staphylococcus, Vibrio
  --amr_ident_min               [integer] Minimum identity for nucleotide hit (0..1). -1 means
                                            use a curated threshold if it exists and 0.9
                                            otherwise [default: -1]
  --amr_coverage_min            [number]  Minimum coverage of the reference protein
                                            [default: 0.5]
  --amr_translation_table       [integer] NCBI genetic code for translated BLAST [default: 11]
```

## BLAST Parameters
```{bash}
Blast Parameters
  --perc_identity               [integer] Percent identity [default: 50]
  --qcov_hsp_perc               [integer] Percent query coverage per hsp [default: 50]
  --max_target_seqs             [integer] Maximum number of aligned sequences to keep
                                            [default: 2000]
```

## Call Variant Parameters
```{bash}
Call Variants Parameters
  --mapqual                     [integer] Minimum read mapping quality to consider
                                            [default: 60]
  --basequal                    [integer] Minimum base quality to consider [default: 13]
  --mincov                      [integer] Minimum site depth to for calling alleles
                                            [default: 10]
  --minfrac                     [integer] Minimum proportion for variant evidence (0=AUTO)
  --minqual                     [integer] Minimum QUALITY in VCF column 6 [default: 100]
  --maxsoft                     [integer] Maximum soft clipping to allow [default: 10]
  --bwaopt                      [string]  Extra BWA MEM options, eg. -x pacbio
  --fbopt                       [string]  Extra Freebayes options, eg. --read-snp-limit 2
  --random_tie_break            [boolean] On references with matching distances, randomly 
                                            select one.
  --disable_auto_variants       [boolean] Disable automatic selection of reference genome
                                            based on Mash distances
```

## Mapping Parameters
```{bash}
Mapping Query Parameters
  --keep_unmapped_reads         [boolean] Keep unmapped reads, this does not affect variant
                                            calling.
  --bwa_mem_opts                [string]  Extra BWA MEM options
  --bwa_aln_opts                [string]  Extra BWA ALN options
  --bwa_samse_opts              [string]  Extra BWA SAMSE options
  --bwa_sampe_opts              [string]  Extra BWA SAMPE options
  --bwa_n                       [integer] Maximum number of alignments to output in the XA
                                            tag for reads paired properly. [default: 9999]
```

## Sequence Type Parameters
```{bash}
Sequence Type Parameters
  --mlst_nucmer_min_id          [integer] Minimum alignment identity (delta-filter -i)
                                            [default: 90]
  --mlst_nucmer_min_len         [integer] Minimum alignment identity (delta-filter -i)
                                            [default: 20]
  --mlst_nucmer_breaklen        [integer] Value to use for -breaklen when running nucmer
                                            [default: 200]
  --mlst_assembly_cov           [integer] Target read coverage when sampling reads for assembly
                                            [default: 50]
  --mlst_min_scaff_depth        [integer] Minimum number of read pairs needed as evidence for
                                            scaffold link between two contigs [default: 10]
  --mlst_spades_options         [string]  Extra options to pass to Spades assembler
  --mlst_assembled_threshold    [number]  If proportion of gene assembled (regardless of into
                                            how many contigs) is at least this value then the
                                            flag gene_assembled is set [default: 0.95]
  --mlst_gene_nt_extend         [integer] Max number of nucleotides to extend ends of gene
                                            matches to look for start/stop codons [default: 30]
  --mlst_unique_threshold       [number]  If proportion of bases in gene assembled more than
                                            once is <= this value, then the flag unique_contig
                                            is set [default: 0.03]
  --mlst_ariba_no_clean         [boolean] Do not clean up intermediate files created by Ariba.
```

## Optional Parameters
```{bash}
Optional Parameters
  --outdir                      [string]  Base directory to write results to [default: ./]
  --run_name                    [string]  Name of the directory to hold results 
                                            [default: bactopia]
  --skip_compression            [boolean] Ouput files will not be compressed
  --keep_all_files              [boolean] Keeps all analysis files created
```

### `--keep_all_files`
In some processes, Bactopia will delete large intermediate files (e.g. multiple uncompressed FASTQs) **only** after a process successfully completes. Since this a per-process function, it does not affect Nextflow's ability to resume (`-resume`)a workflow. You can deactivate this feature using `--keep_all_files`. Please, keep in mind the *work* directory is already large, this will make it 2-3 times larger.


## Max Job Request Parameters
```{bash}
Max Job Request Parameters
  --max_retry                   [integer] Maximum times to retry a process before allowing it
                                            to fail. [default: 3]
  --max_cpus                    [integer] Maximum number of CPUs that can be requested for any
                                            single job. [default: 4]
  --max_memory                  [integer] Maximum amount of memory (in GB) that can be
                                            requested for any single job. [default: 32]
  --max_time                    [integer] Maximum amount of time (in minutes) that can be
                                            requested for any single job. [default: 120]
  --max_downloads               [integer] Maximum number of samples to download at a time
                                            [default: 3]
```

### `--max_cpus`
At execution, Nextflow creates a queue and the number of slots in the queue is determined by the total number of cores on the system. So if you have a 24-core system, that means Nextflow will have a queue with 24-slots available. This feature kind of makes `--max_cpus` a little misleading. Typically when you give `--max_cpus` you are saying *"use this amount of cpus"*. But that is not the case for Nextflow and Bactopia. When you use `--max_cpus` what you are actually saying is *"for any particular task, use this amount of slots"*. Commands within a task processors will use the amount specified by `--max_cpus`.

!!! error "`--max_cpus` can have a significant effect on the efficiency of Bactopia"
    So for example if you have a system with 24-cores.

    This command, `bactopia ... --max_cpus 24`, says *for any particular task, use 24 slots*. Nextflow will give tasks in Bactopia 24 slots out of 24 available (24-core machine). In other words the queue can one have one task running at once because each task occupies 24 slots.

    On the other hand, `bactopia ... --max_cpus 4` says *for any particular task, use 4 slots*. Now, for Nextflow will give each task 4 slots out of 24 slots. Which means 6 tasks can be running at once. This can lead to much better efficiency because less jobs are stuck waiting in line. 

    There are some tasks in Bactopia that will only ever use a single slot because they are single-core tasks. But for example the `annotation` step will always use the number of slots specified by `--max_cpus`. If the `--max_cpus` is too high, the `annotation` will get bogged down, which causes tasks dependent on `annotation` to also get bogged down.

!!! info "When in doubt `--max_cpus 4` is a safe value."
    This is also the default value for Bactopia.

### `-qs`
The `-qs` parameter is short for *queue size*. As described above for `--max_cpus`, the default value for `-qs` is set to the total number of cores on the system. This parameter allows you to adjust the maximum number of cores Nextflow can use at any given moment.

!!! error "`-qs` allows you to play nicely on shared resources"
    From the example above, if you have a system with 24-cores. The default queue size if 24 slots.

    `bactopia ... --max_cpus 4` says *for any particular task, use a maximum of 4 slots*. Nextflow will give each task 4 slots out of 24 slots. But there might be other people also using the server.

    `bactopia ... --max_cpus 4 -qs 12` says *for any particular task, use a maximum of 4 slots, but don't use more than 12 slots*. Nextflow will give each task 4 slots out of 12 slots. Now instead of using all the cores on the server, the maximum that can be used in 12.

!!! info "`-qs` might need adjusting for job schedulers."
    The default value for `-qs` is set to 100 when using a job scheduler (e.g. SLURM, AWS Batch). There may be times when you need adjust this to meet your needs. For example, if using AWS Batch you might want to increase the value to have more jobs processed at once (e.g. 100 vs 500).

## Nextflow Configuration Parameters
```{bash}
Nextflow Configuration Parameters
  --nfconfig                    [string]  A Nextflow compatible config file for custom
                                            profiles, loaded last and will overwrite existing
                                            variables if set.
  --publish_dir_mode            [string]  Method used to save pipeline results to output
                                            directory. [default: copy]
  --infodir                     [string]  Directory to keep pipeline Nextflow logs and reports.
                                            [default: ${params.outdir}/pipeline_info]
  --force                       [boolean] Nextflow will overwrite existing output files.
  --cleanup_workdir             [boolean] After Bactopia is successfully executed, the `work`
                                            directory will be deleted.
```

### `--nfconfig`
A key feature of Nextflow is you can provide your own config files. What this boils down to you can easily set Bactopia to run on your environment. With `--nfconfig` you can tell Bactopia to import your config file. 

`--nfconfig` has been set up so that it is the last config file to be loaded by Nextflow. This means that if your config file contains variables (e.g. params or profiles) already set they will be overwritten by your values.

[Nextflow goes into great details on how to create configuration files.](https://www.nextflow.io/docs/latest/config.html) Please check the following links for adjustsments you be interested in making.

| Scope   | Description |
|---------|-------------|
| [env](https://www.nextflow.io/docs/latest/config.html#scope-env)     | Set any environment variables that might be required |
| [params](https://www.nextflow.io/docs/latest/config.html#scope-params)  | Change the default values of command line arguments  |
| [process](https://www.nextflow.io/docs/latest/config.html#scope-process) | Adjust perprocess configurations such as containers, conda envs, or resource usage |
| [profile](https://www.nextflow.io/docs/latest/config.html#config-profiles) | Create predefined profiles for your [Executor](https://www.nextflow.io/docs/latest/operator.html#filtering-operators) |

There are [many other scopes](https://www.nextflow.io/docs/latest/config.html#config-scopes) that you might be interested in checking out.

You are most like going to want to create a custom profile. By doing so you can specify it at runtime (`-profile myProfile`) and Nextflow will be excuted based on that profile. Often times your custom profile will include information on the executor (queues, allocations, apths, etc...).

If you need help please [reach out](https://github.com/bactopia/bactopia/issues/new/choose)!

*If you're using the standard profile (did not specify -profile 'xyz') this might not be necessary.*

### `--cleanup_workdir`
After you run Bactopia, you will notice a directory called `work`. This directory is where Nextflow runs all the processes and stores the intermediate files. After a process completes successfully, the appropriate results are pulled out and placed in the sample's result folder. The `work` directory can grow very large very quickly! Please keep this in mind when using Bactopia. To help prevent the build up of the `work` directory you can use `--cleanup_workdir` to delete intermediate files after a successful execution of Bactopia.

!!! info "Bactopia and Bactopia Tools use separate `work` directories"
    Inside the `work` directory there will be separate subfolders that correspond to a Bactopia run or a specific Bactopia Tool run. This allows you to more easily identify which are ok to delete. The `work` directory is always ok to delete after a successful run.

### `-resume`
Bactopia relies on [Nextflow's Resume Feature](https://www.nextflow.io/docs/latest/getstarted.html#modify-and-resume) to resume runs. You can tell Bactopia to resume by adding `-resume` to your command line. When `-resume` is used, Nextflow will review the cache and determine if the previous run is resumable. If the previous run is not resumable, execution will
start at the beginning.


## Nextflow Profile Parameters
```{bash}
Nextflow Profile Parameters
  --condadir                    [string]  Directory to Nextflow should use for Conda
                                            environments
  --use_mamba                   [boolean] Uses mamba instead of conda for building 
                                            environments [default: false]
  --registry                    [string]  Docker registry to pull containers from. 
                                            [default: dockerhub]
  --singularity_cache           [string]  Directory where remote Singularity images are stored.
  --singularity_pull_docker_container 
                                [boolean] Instead of directly downloading Singularity images
                                            for use with Singularity, force the workflow to
                                            pull and convert Docker containers instead.
  --force_rebuild               [boolean] Force overwrite of existing pre-built environments.
  --queue                       [string]  Comma-separated name of the queue(s) to be used by a
                                            job scheduler (e.g. AWS Batch or SLURM)
                                            [default: general,high-memory]
  --cluster_opts                [string]  Additional options to pass to the executor.
                                            (e.g. SLURM: '--account=my_acct_name'
  --disable_scratch             [boolean] All intermediate files created on worker nodes of
                                            will be transferred to the head node.
```

## Helpful Parameters
```{bash}
Helpful Parameters
  --monochrome_logs             [boolean] Do not use coloured log outputs.
  --nfdir                       [boolean] Print directory Nextflow has pulled Bactopia to
  --sleep_time                  [integer] The amount of time (seconds) Nextflow will wait after
                                            setting up datasets before execution. [default: 5]
  --validate_params             [boolean] Boolean whether to validate parameters against the
                                            schema at runtime [default: true]
  --help                        [boolean] Display help text.
  --wf                          [string]  Specify which workflow or Bactopia Tool to execute
                                            [default: bactopia]
  --list_wfs                    [boolean] List the available workflows and Bactopia Tools to
                                            use with '--wf'
  --show_hidden_params          [boolean] Show all params when using `--help`
  --help_all                    [boolean] An alias for --help --show_hidden_params
  --version                     [boolean] Display version text.
```
