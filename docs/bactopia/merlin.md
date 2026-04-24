---
title: merlin
description: A Bactopia Tool for the automatic selection and executions of  species-specific tools.
---

_MinmER assisted species-specific bactopia tool seLectIoN_, or Merlin, uses distances based
on the RefSeq sketch downloaded by `bactopia datasets` to automatically run species-specific tools.

Currently Merlin knows 16 spells for which cover the following:

| Genus/Species | Tools |
|---------------|-------|
| Escherichia / Shigella   | [ECTyper](../bactopia-tools/ectyper.md), [ShigaTyper](../bactopia-tools/shigatyper.md), [ShigEiFinder](../bactopia-tools/shigeifinder.md), [ShigaPass](../bactopia-tools/shigapass.md)  |
| Haemophilus   | [hicap](../bactopia-tools/hicap.md), [HpsuisSero](../bactopia-tools/ssuissero.md) |
| Klebsiella | [Kleborate](../bactopia-tools/kleborate.md) |
| Legionella | [legsta](../bactopia-tools/legsta.md) |
| Listeria | [LisSero](../bactopia-tools/lissero.md) |
| Mycobacterium | [TBProfiler](../bactopia-tools/tbprofiler.md) |
| Neisseria | [meningotype](../bactopia-tools/meningotype.md), [ngmaster](../bactopia-tools/ngmaster.md) |
| Pseudomonas | [pasty](../bactopia-tools/pasty.md) |
| Salmonella | [SeqSero2](../bactopia-tools/seqsero2.md), [SISTR](../bactopia-tools/sistr.md) |
| Staphylococcus | [AgrVATE](../bactopia-tools/agrvate.md), [spaTyper](../bactopia-tools/spatyper.md), [staphopia-sccmec](../bactopia-tools/staphopiasccmec.md) |
| Streptococcus | [emmtyper](../bactopia-tools/emmtyper.md), [pbptyper](../bactopia-tools/pbptyper.md), [SsuisSero](../bactopia-tools/ssuissero.md) |

Merlin is avialable as an independent Bactopia Tool, or in the Bactopia with the `--ask_merlin` parameter. Even better,
if you want to force Merlin to execute all species-specific tools (no matter the distance), you can use `--full_merlin`.
Then all the spells will be unleashed!


## Output Overview

Below is the default output structure for the `merlin` step in Bactopia. Where
possible the file descriptions below were modified from a tools description.

```bash
<BACTOPIA_DIR>
├── <SAMPLE_NAME>
│   └── tools
│       ├── agrvate
│       │   ├── <SAMPLE_NAME>-agr_gp.tab
│       │   ├── <SAMPLE_NAME>-blastn_log.txt
│       │   ├── <SAMPLE_NAME>-hmm-log.txt
│       │   ├── <SAMPLE_NAME>-hmm.tab
│       │   ├── <SAMPLE_NAME>-summary.tab
│       │   └── logs
│       │       ├── nf-agrvate.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── ectyper
│       │   ├── <SAMPLE_NAME>.tsv
│       │   ├── blast_output_alleles.txt
│       │   └── logs
│       │       ├── ectyper.log
│       │       ├── nf-ectyper.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── emmtyper
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-emmtyper.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── genotyphi
│       │   ├── <SAMPLE_NAME>.csv
│       │   ├── <SAMPLE_NAME>.json
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── genotyphi
│       │       │   ├── nf-genotyphi.{begin,err,log,out,run,sh,trace}
│       │       │   └── versions.yml
│       │       └── mykrobe
│       │           ├── nf-genotyphi.{begin,err,log,out,run,sh,trace}
│       │           └── versions.yml
│       ├── hicap
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-hicap.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── hpsuissero
│       │   ├── <SAMPLE_NAME>_serotyping_res.tsv
│       │   └── logs
│       │       ├── nf-hpsuissero.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── kleborate
│       │   ├── <SAMPLE_NAME>.results.txt
│       │   └── logs
│       │       ├── nf-kleborate.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── legsta
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-legsta.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── mashdist
│       │   └── merlin
│       │       ├── <SAMPLE_NAME>-dist.txt
│       │       └── logs
│       │           ├── nf-mashdist.{begin,err,log,out,run,sh,trace}
│       │           └── versions.yml
│       ├── meningotype
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-meningotype.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── ngmaster
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-ngmaster.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── pasty
│       │   ├── <SAMPLE_NAME>.blastn.tsv
│       │   ├── <SAMPLE_NAME>.details.tsv
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-pasty.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── pbptyper
│       │   ├── <SAMPLE_NAME>-1A.tblastn.tsv
│       │   ├── <SAMPLE_NAME>-2B.tblastn.tsv
│       │   ├── <SAMPLE_NAME>-2X.tblastn.tsv
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-pbptyper.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── seqsero2
│       │   ├── <SAMPLE_NAME>_log.txt
│       │   ├── <SAMPLE_NAME>_result.tsv
│       │   ├── <SAMPLE_NAME>_result.txt
│       │   └── logs
│       │       ├── nf-seqsero2.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── seroba
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-seroba.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── shigatyper
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-shigatyper.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── shigeifinder
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-shigeifinder.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── sistr
│       │   ├── <SAMPLE_NAME>-allele.fasta.gz
│       │   ├── <SAMPLE_NAME>-allele.json.gz
│       │   ├── <SAMPLE_NAME>-cgmlst.csv
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-sistr.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── spatyper
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-spatyper.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── ssuissero
│       │   ├── <SAMPLE_NAME>_serotyping_res.tsv
│       │   └── logs
│       │       ├── nf-ssuissero.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── staphopiasccmec
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-staphopiasccmec.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       ├── stecfinder
│       │   ├── <SAMPLE_NAME>.tsv
│       │   └── logs
│       │       ├── nf-stecfinder.{begin,err,log,out,run,sh,trace}
│       │       └── versions.yml
│       └── tbprofiler
│           ├── <SAMPLE_NAME>.results.csv
│           ├── <SAMPLE_NAME>.results.json
│           ├── <SAMPLE_NAME>.results.txt
│           ├── bam
│           │   └── <SAMPLE_NAME>.bam
│           ├── logs
│           │   ├── nf-tbprofiler.{begin,err,log,out,run,sh,trace}
│           │   └── versions.yml
│           └── vcf
│               └── <SAMPLE_NAME>.targets.csq.vcf.gz
└── bactopia-runs
    └── merlin-<TIMESTAMP>
        ├── merged-results
        │   ├── agrvate.tsv
        │   ├── ectyper.tsv
        │   ├── emmtyper.tsv
        │   ├── genotyphi.tsv
        │   ├── hicap.tsv
        │   ├── hpsuissero.tsv
        │   ├── kleborate.tsv
        │   ├── legsta.tsv
        │   ├── logs
        │   │   └── <BACTOPIA_TOOL>-concat
        │   │       ├── nf-merged-results.{begin,err,log,out,run,sh,trace}
        │   │       └── versions.yml
        │   ├── meningotype.tsv
        │   ├── ngmaster.tsv
        │   ├── pasty.tsv
        │   ├── pbptyper.tsv
        │   ├── seqsero2.tsv
        │   ├── seroba.tsv
        │   ├── shigatyper.tsv
        │   ├── shigeifinder.tsv
        │   ├── sistr.tsv
        │   ├── spatyper.tsv
        │   ├── ssuissero.tsv
        │   ├── staphopiasccmec.tsv
        │   └── stecfinder.tsv
        └── nf-reports
            ├── merlin-dag.dot
            ├── merlin-report.html
            ├── merlin-timeline.html
            └── merlin-trace.txt

```

:::info[Directory structure might be different]

Depending on the options used at runtime, the `merlin` directory structure might
be different, but the output descriptions below still apply.
:::



### Results

#### Merged Results

Below are results that are concatenated into a single file.


| Filename                      | Description |
|-------------------------------|-------------|
| agrvate.tsv | A merged TSV file with `AgrVATE` results from all samples |
| clermontyping.csv | A merged TSV file with `ClermonTyping` results from all samples |
| ectyper.tsv | A merged TSV file with `ECTyper` results from all samples |
| emmtyper.tsv | A merged TSV file with `emmtyper` results from all samples |
| genotyphi.tsv | A merged TSV file with `genotyphi` results from all samples |
| hicap.tsv | A merged TSV file with `hicap` results from all samples |
| hpsuissero.tsv | A merged TSV file with `HpsuisSero` results from all samples |
| kleborate.tsv | A merged TSV file with `Kleborate` results from all samples |
| legsta.tsv | A merged TSV file with `legsta` results from all samples |
| lissero.tsv | A merged TSV file with `LisSero` results from all samples |
| meningotype.tsv | A merged TSV file with `meningotype` results from all samples |
| ngmaster.tsv | A merged TSV file with `ngmaster` results from all samples |
| pasty.tsv | A merged TSV file with `pasty` results from all samples |
| pbptyper.tsv | A merged TSV file with `pbptyper` results from all samples |
| seqsero2.tsv | A merged TSV file with `seqsero2` results from all samples |
| seroba.tsv | A merged TSV file with `seroba` results from all samples |
| shigapass.csv | A merged CSV file with `ShigaPass` results from all samples |
| shigatyper.tsv | A merged TSV file with `ShigaTyper` results from all samples |
| shigeifinder.tsv | A merged TSV file with `ShigEiFinder` results from all samples |
| sistr.tsv | A merged TSV file with `SISTR` results from all samples |
| spatyper.tsv | A merged TSV file with `spaTyper` results from all samples |
| ssuissero.tsv | A merged TSV file with `SsuisSero` results from all samples |
| staphopiasccmec.tsv | A merged TSV file with `staphopia-sccmec` results from all samples |
| stecfinder.tsv | A merged TSV file with `stecfinder` results from all samples |






#### AgrVATE

Below is a description of the _per-sample_ results from [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE).


| Extension                     | Description |
|-------------------------------|-------------|
| -agr_gp.tab | A detailed report for _agr_ kmer matches |
| -blastn_log.txt | Log files from programs called by `AgrVATE` |
| -summary.tab | A final summary report for _agr_ typing |






#### ClermonTyping

Below is a description of the _per-sample_ results from [ClermonTyping](https://github.com/happykhan/ClermonTyping).


| Extension                     | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.blast.xml | A BLAST XML file with the results of the ClermonTyping analysis |
| &lt;SAMPLE_NAME&gt;.html | A HTML file with the results of the ClermonTyping analysis |
| &lt;SAMPLE_NAME&gt;.mash.tsv | A TSV file with the Mash distances |
| &lt;SAMPLE_NAME&gt;.phylogroups.txt | A TSV file with the final phylogroup assignments |






#### ECTyper

Below is a description of the _per-sample_ results from [ECTyper](https://github.com/phac-nml/ecoli_serotyping).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `ECTyper` result, see [ECTyper - Report format](https://github.com/phac-nml/ecoli_serotyping#report-format) for details |
| blast_output_alleles.txt | Allele report generated from BLAST results |






#### emmtyper

Below is a description of the _per-sample_ results from [emmtyper](https://github.com/MDU-PHL/emmtyper).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `emmtyper` result, see [emmtyper - Result format](https://github.com/MDU-PHL/emmtyper#result-format) for details |






#### hicap

Below is a description of the _per-sample_ results from [hicap](https://github.com/scwatts/hicap).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.gbk | GenBank file and cap locus annotations |
| &lt;SAMPLE_NAME&gt;.svg | Visualization of annotated cap locus |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `hicap` results |






#### HpsuisSero

Below is a description of the _per-sample_ results from [HpsuisSero](https://github.com/jimmyliu1326/HpsuisSero).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_serotyping_res.tsv | A tab-delimited file with `HpsuisSero` result |






#### GenoTyphi

Below is a description of the _per-sample_ results from [GenoTyphi](https://github.com/katholt/genotyphi). A
full description of the GenoTyphi output is available at [GenoTyphi - Output](https://github.com/katholt/genotyphi/blob/main/README.md#explanation-of-columns-in-the-output)


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_predictResults.tsv | A tab-delimited file with `GenoTyphi` results |
| &lt;SAMPLE_NAME&gt;.csv | The output of `mykrobe predict` in comma-separated format |
| &lt;SAMPLE_NAME&gt;.json | The output of `mykrobe predict` in JSON format |






#### Kleborate

Below is a description of the _per-sample_ results from [Kleborate](https://github.com/katholt/Kleborate).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.results.txt | A tab-delimited file with `Kleborate` result, see  [Kleborate - Example output](https://github.com/katholt/Kleborate/wiki/Tests-and-example-outputs#example-output) for more details. |






#### legsta

Below is a description of the _per-sample_ results from [legsta](https://github.com/tseemann/legsta).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `legsta` result, see [legsta - Output](https://github.com/tseemann/legsta#output) for more details |






#### LisSero

Below is a description of the _per-sample_ results from [LisSero](https://github.com/MDU-PHL/LisSero).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `LisSero` results |






#### Mash

Below is a description of the _per-sample_ results from [Mash](https://github.com/marbl/Mash).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-dist.txt | A tab-delimited file with `mash dist` results |






#### meningotype

Below is a description of the _per-sample_ results from [meningotype](https://github.com/MDU-PHL/meningotype) .


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `meningotype` result |






#### ngmaster

Below is a description of the _per-sample_ results from [ngmaster](https://github.com/MDU-PHL/ngmaster).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `ngmaster` results |






#### pasty

Below is a description of the _per-sample_ results from [pasty](https://github.com/rpetit3/pasty).


| Extension                     | Description |
|-------------------------------|-------------|
| .blastn.tsv | A tab-delimited file of all blast hits |
| .details.tsv | A tab-delimited file with details for each serogroup |
| .tsv | A tab-delimited file with the predicted serogroup |






#### pbptyper

Below is a description of the _per-sample_ results from [pbptyper](https://github.com/rpetit3/pbptyper).


| Extension                     | Description |
|-------------------------------|-------------|
| .tblastn.tsv | A tab-delimited file of all blast hits |
| .tsv | A tab-delimited file with the predicted PBP type |






#### SeqSero2

Below is a description of the _per-sample_ results from [SeqSero2](https://github.com/denglab/SeqSero2).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_result.tsv | A tab-delimited file with `SeqSero2` results |
| &lt;SAMPLE_NAME&gt;_result.txt | A text file with key-value pairs of `SeqSero2` results |






#### Seroba

Below is a description of the _per-sample_ results from [Seroba](https://github.com/sanger-pathogens/seroba).
More details about the outputs are available from [Seroba - Output](https://sanger-pathogens.github.io/seroba/#output).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with the predicted serotype |
| detailed_serogroup_info.txt | Detailed information about the predicted results |






#### ShigaPass

Below is a description of the _per-sample_ results from [ShigaPass](https://github.com/imanyass/ShigaPass).


| Extension                     | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.csv | A CSV file with the predicted Shigella or EIEC serotype |






#### ShigaTyper

Below is a description of the _per-sample_ results from [ShigaTyyper](https://github.com/CFSAN-Biostatistics/shigatyper).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-hits.tsv | Detailed statistics about each individual gene hit |
| &lt;SAMPLE_NAME&gt;.tsv | The final predicted serotype by `ShigaTyper` |






#### ShigEiFinder

Below is a description of the _per-sample_ results from [ShigEiFinder](https://github.com/LanLab/ShigEiFinder).


| Extension                     | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with the predicted Shigella or EIEC serotype |






#### SISTR

Below is a description of the _per-sample_ results from [SISTR](https://github.com/phac-nml/sistr_cmd).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;-allele.fasta.gz | A FASTA file of the cgMLST allele search results |
| &lt;SAMPLE_NAME&gt;-allele.json.gz | JSON formated cgMLST allele search results, see  [SISTR - cgMLST search results](https://github.com/phac-nml/sistr_cmd#cgmlst-allele-search-results) for more details |
| &lt;SAMPLE_NAME&gt;-cgmlst.csv | A comma-delimited summary of the cgMLST allele search results |
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `SISTR` results, see [SISTR - Primary results](https://github.com/phac-nml/sistr_cmd#primary-results-output--o-sistr-results) for more details |






#### spaTyper

Below is a description of the _per-sample_ results from [spaTyper](https://github.com/HCGB-IGTP/spaTyper).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `spaTyper` result |






#### SsuisSero

Below is a description of the _per-sample_ results from [SsuisSero](https://github.com/jimmyliu1326/SsuisSero).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;_serotyping_res.tsv | A tab-delimited file with `SsuisSero` results |






#### staphopia-sccmec

Below is a description of the _per-sample_ results from [staphopia-sccmec](https://github.com/staphopia/staphopia-sccmec).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.tsv | A tab-delimited file with `staphopia-sccmec` results |






#### TBProfiler

Below is a description of the _per-sample_ results from [TBProfiler](https://github.com/jodyphelan/TBProfiler).


| Filename                      | Description |
|-------------------------------|-------------|
| &lt;SAMPLE_NAME&gt;.results.csv | A CSV formated `TBProfiler` result file of resistance and strain type |
| &lt;SAMPLE_NAME&gt;.results.json | A JSON formated `TBProfiler` result file of resistance and strain type |
| &lt;SAMPLE_NAME&gt;.results.txt | A text file with `TBProfiler` results |
| &lt;SAMPLE_NAME&gt;.bam | BAM file with alignment details |
| &lt;SAMPLE_NAME&gt;.targets.csq.vcf.gz | VCF with variant info again reference genomes |








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


### mashdist 


| Parameter | Description |
|:---|---|
| ` --mash_sketch` | The reference sequence as a Mash Sketch (.msh file) <br/>**Type:** `string` |
| ` --mash_seed` | Seed to provide to the hash function <br/>**Type:** `integer`, **Default:** `42` |
| ` --mash_table` |  Table output (fields will be blank if they do not meet the p-value threshold) <br/>**Type:** `boolean` |
| ` --mash_m` | Minimum copies of each k-mer required to pass noise filter for reads <br/>**Type:** `integer`, **Default:** `1` |
| ` --mash_w` | Probability threshold for warning about low k-mer size. <br/>**Type:** `number`, **Default:** `0.01` |
| ` --max_p` | Maximum p-value to report. <br/>**Type:** `number`, **Default:** `1.0` |
| ` --max_dist` | Maximum distance to report. <br/>**Type:** `number`, **Default:** `1.0` |
| ` --merlin_dist` | Maximum distance to report when using Merlin . <br/>**Type:** `number`, **Default:** `0.1` |
| ` --full_merlin` | Go full Merlin and run all species-specific tools, no matter the Mash distance <br/>**Type:** `boolean` |
| ` --use_fastqs` | Query with FASTQs instead of the assemblies <br/>**Type:** `boolean` |

### AgrVATE 


| Parameter | Description |
|:---|---|
| ` --typing_only` | agr typing only. Skips agr operon extraction and frameshift detection <br/>**Type:** `boolean` |

### ClermonTyping 


| Parameter | Description |
|:---|---|
| ` --clermon_threshold` | Do not use contigs under this size <br/>**Type:** `number` |

### ECTyper 


| Parameter | Description |
|:---|---|
| ` --opid` | Percent identity required for an O antigen allele match <br/>**Type:** `integer`, **Default:** `90` |
| ` --opcov` | Minumum percent coverage required for an O antigen allele match <br/>**Type:** `integer`, **Default:** `90` |
| ` --hpid` | Percent identity required for an H antigen allele match <br/>**Type:** `integer`, **Default:** `95` |
| ` --hpcov` | Minumum percent coverage required for an H antigen allele match <br/>**Type:** `integer`, **Default:** `50` |
| ` --verify` | Enable E. coli species verification <br/>**Type:** `boolean` |
| ` --print_alleles` | Prints the allele sequences if enabled as the final column <br/>**Type:** `boolean` |

### emmtyper 


| Parameter | Description |
|:---|---|
| ` --emmtyper_wf` | Workflow for emmtyper to use. <br/>**Type:** `string`, **Default:** `blast` |
| ` --cluster_distance` | Distance between cluster of matches to consider as different clusters <br/>**Type:** `integer`, **Default:** `500` |
| ` --percid` | Minimal percent identity of sequence <br/>**Type:** `integer`, **Default:** `95` |
| ` --culling_limit` | Total hits to return in a position <br/>**Type:** `integer`, **Default:** `5` |
| ` --mismatch` | Threshold for number of mismatch to allow in BLAST hit <br/>**Type:** `integer`, **Default:** `5` |
| ` --align_diff` | Threshold for difference between alignment length and subject length in BLAST <br/>**Type:** `integer`, **Default:** `5` |
| ` --gap` | Threshold gap to allow in BLAST hit <br/>**Type:** `integer`, **Default:** `2` |
| ` --min_perfect` | Minimum size of perfect match at 3 primer end <br/>**Type:** `integer`, **Default:** `15` |
| ` --min_good` | Minimum size where there must be 2 matches for each mismatch <br/>**Type:** `integer`, **Default:** `15` |
| ` --max_size` | Maximum size of PCR product <br/>**Type:** `integer`, **Default:** `2000` |

### hicap 


| Parameter | Description |
|:---|---|
| ` --database_dir` | Directory containing locus database <br/>**Type:** `string` |
| ` --model_fp` | Path to prodigal model <br/>**Type:** `string` |
| ` --full_sequence` | Write the full input sequence out to the genbank file rather than just the region surrounding and including the locus <br/>**Type:** `boolean` |
| ` --hicap_debug` | hicap will print debug messages <br/>**Type:** `boolean` |
| ` --gene_coverage` | Minimum percentage coverage to consider a single gene complete <br/>**Type:** `number`, **Default:** `0.8` |
| ` --gene_identity` | Minimum percentage identity to consider a single gene complete <br/>**Type:** `number`, **Default:** `0.7` |
| ` --broken_gene_length` | Minimum length to consider a broken gene <br/>**Type:** `integer`, **Default:** `60` |
| ` --broken_gene_identity` | Minimum percentage identity to consider a broken gene <br/>**Type:** `number`, **Default:** `0.8` |

### GenoTyphi 


| Parameter | Description |
|:---|---|
| ` --kmer` | K-mer length <br/>**Type:** `integer`, **Default:** `21` |
| ` --min_depth` | Minimum depth <br/>**Type:** `integer`, **Default:** `1` |
| ` --model` | Genotype model used. <br/>**Type:** `string`, **Default:** `kmer_count` |
| ` --report_all_calls` | Report all calls <br/>**Type:** `boolean` |
| ` --mykrobe_opts` | Extra Mykrobe options in quotes <br/>**Type:** `string` |

### Kleborate 


| Parameter | Description |
|:---|---|
| ` --kleborate_preset` | Preset module to use for Kleborate <br/>**Type:** `string`, **Default:** `kpsc` |
| ` --kleborate_opts` | Extra options in quotes for Kleborate <br/>**Type:** `string` |

### legsta 


| Parameter | Description |
|:---|---|
| ` --noheader` | Don't print header row <br/>**Type:** `boolean` |

### LisSero 


| Parameter | Description |
|:---|---|
| ` --min_id` | Minimum percent identity to accept a match <br/>**Type:** `number`, **Default:** `95.0` |
| ` --min_cov` | Minimum coverage of the gene to accept a match <br/>**Type:** `number`, **Default:** `95.0` |

### meningotype 
You can use these parameters to fine-tune your meningotype analysis

| Parameter | Description |
|:---|---|
| ` --finetype` | perform porA and fetA fine typing <br/>**Type:** `boolean` |
| ` --porB` | perform porB sequence typing (NEIS2020) <br/>**Type:** `boolean` |
| ` --bast` | perform Bexsero antigen sequence typing (BAST) <br/>**Type:** `boolean` |
| ` --mlst` | perform MLST <br/>**Type:** `boolean` |
| ` --all` | perform MLST, porA, fetA, porB, BAST typing <br/>**Type:** `boolean` |

### ngmaster 


| Parameter | Description |
|:---|---|
| ` --csv` | output comma-separated format (CSV) rather than tab-separated <br/>**Type:** `boolean` |

### pasty 


| Parameter | Description |
|:---|---|
| ` --pasty_min_pident` | Minimum percent identity to count a hit <br/>**Type:** `integer`, **Default:** `95` |
| ` --pasty_min_coverage` | Minimum percent coverage to count a hit <br/>**Type:** `integer`, **Default:** `95` |

### pbptyper 


| Parameter | Description |
|:---|---|
| ` --pbptyper_min_pident` | Minimum percent identity to count a hit <br/>**Type:** `integer`, **Default:** `95` |
| ` --pbptyper_min_coverage` | Minimum percent coverage to count a hit <br/>**Type:** `integer`, **Default:** `95` |

### SeqSero2 


| Parameter | Description |
|:---|---|
| ` --run_mode` | Workflow to run. 'a' allele mode, or 'k' k-mer mode <br/>**Type:** `string`, **Default:** `k` |
| ` --input_type` | Input format to analyze. 'assembly' or 'fastq' <br/>**Type:** `string`, **Default:** `assembly` |
| ` --bwa_mode` | Algorithms for bwa mapping for allele mode <br/>**Type:** `string`, **Default:** `mem` |

### SISTR 


| Parameter | Description |
|:---|---|
| ` --full_cgmlst` |  Use the full set of cgMLST alleles which can include highly similar alleles <br/>**Type:** `boolean` |

### spaTyper 


| Parameter | Description |
|:---|---|
| ` --repeats` | List of spa repeats <br/>**Type:** `string` |
| ` --repeat_order` | List spa types and order of repeats <br/>**Type:** `string` |
| ` --do_enrich` | Do PCR product enrichment <br/>**Type:** `boolean` |

### staphopia-sccmec 


| Parameter | Description |
|:---|---|
| ` --hamming` | Report the results as hamming distances <br/>**Type:** `boolean` |

### TBProfiler Profile 


| Parameter | Description |
|:---|---|
| ` --call_whole_genome` | Call whole genome <br/>**Type:** `boolean` |
| ` --mapper` | Mapping tool to use. If you are using nanopore data it will default to minimap2 <br/>**Type:** `string`, **Default:** `bwa` |
| ` --caller` | Variant calling tool to use <br/>**Type:** `string`, **Default:** `freebayes` |
| ` --calling_params` | Extra variant caller options in quotes <br/>**Type:** `string` |
| ` --suspect` | Use the suspect suite of tools to add ML predictions <br/>**Type:** `boolean` |
| ` --no_flagstat` | Don't collect flagstats <br/>**Type:** `boolean` |
| ` --no_delly` | Don't run delly <br/>**Type:** `boolean` |
| ` --tbprofiler_opts` | Extra options in quotes for TBProfiler <br/>**Type:** `string` |

## Citations
If you use Bactopia and `merlin` in your analysis, please cite the following.

- [Bactopia](https://bactopia.github.io/)  
    Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
  

- [AgrVATE](https://github.com/VishnuRaghuram94/AgrVATE)  
    Raghuram V. [AgrVATE: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants.](https://github.com/VishnuRaghuram94/AgrVATE) (GitHub)
  
- [ClermontTyping](https://github.com/happykhan/ClermonTyping)  
    Beghain J, Bridier-Nahmias A, Le Nagard H, Denamur E, Clermont O. [ClermonTyping: an easy-to-use and accurate in silico method for Escherichia genus strain phylotyping.](https://doi.org/10.1099/mgen.0.000192) Microbial Genomics, 4(7), e000192. (2018)
  
- [csvtk](https://bioinf.shenwei.me/csvtk/)  
    Shen, W [csvtk: A cross-platform, efficient and practical CSV/TSV toolkit in Golang.](https://github.com/shenwei356/csvtk/) (GitHub)
  
- [ECTyper](https://github.com/phac-nml/ecoli_serotyping)  
    Laing C, Bessonov K, Sung S, La Rose C [ECTyper - In silico prediction of _Escherichia coli_ serotype](https://github.com/phac-nml/ecoli_serotyping) (GitHub)  
- [emmtyper](https://github.com/MDU-PHL/emmtyper)  
    Tan A, Seemann T, Lacey D, Davies M, Mcintyre L, Frost H, Williamson D, Gonçalves da Silva A [emmtyper - emm Automatic Isolate Labeller](https://github.com/MDU-PHL/emmtyper) (GitHub)
  
- [GenoTyphi](https://github.com/katholt/genotyphi)  
    Wong VK, Baker S, Connor TR, Pickard D, Page AJ, Dave J, Murphy N, Holliman R, Sefton A, Millar M, Dyson ZA, Dougan G, Holt KE, & International Typhoid Consortium. [An extended genotyping framework for Salmonella enterica serovar Typhi, the cause of human typhoid](https://doi.org/10.1038/ncomms12827) _Nature Communications_ 7, 12827. (2016)
  
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
  
- [Mykrobe](https://github.com/Mykrobe-tools/mykrobe)  
    Hunt M, Bradley P, Lapierre SG, Heys S, Thomsit M, Hall MB, Malone KM, Wintringer P, Walker TM, Cirillo DM, Comas I, Farhat MR, Fowler P, Gardy J, Ismail N, Kohl TA, Mathys V, Merker M, Niemann S, Omar SV, Sintchenko V, Smith G, Supply P, Tahseen S, Wilcox M, Arandjelovic I, Peto TEA, Crook, DW, Iqbal Z [Antibiotic resistance prediction for Mycobacterium tuberculosis from genome sequence data with Mykrobe](https://doi.org/10.12688/wellcomeopenres.15603.1) _Wellcome Open Research_ 4, 191. (2019)
  
- [ngmaster](https://github.com/MDU-PHL/ngmaster)  
    Kwong J, Gonçalves da Silva A, Schultz M, Seeman T [ngmaster - _In silico_ multi-antigen sequence typing for _Neisseria gonorrhoeae_ (NG-MAST)](https://github.com/MDU-PHL/ngmaster) (GitHub)
  
- [pasty](https://github.com/rpetit3/pasty)  
    Petit III RA [pasty: in silico serogrouping of _Pseudomonas aeruginosa_ isolates](https://github.com/rpetit3/pasty) (GitHub)
  
- [pbptyper](https://github.com/rpetit3/pbptyper)  
    Petit III RA [pbptyper: In silico Penicillin Binding Protein (PBP) typer for _Streptococcus pneumoniae_ assemblies](https://github.com/rpetit3/pbptyper) (GitHub)
  
- [SeqSero2](https://github.com/denglab/SeqSero2)  
    Zhang S, Den-Bakker HC, Li S, Dinsmore BA, Lane C, Lauer AC, Fields PI, Deng X. [SeqSero2: rapid and improved Salmonella serotype determination using whole genome sequencing data.](https://doi.org/10.1128/AEM.01746-19) _Appl Environ Microbiology_ 85(23):e01746-19 (2019)
  
- [shigapass](https://github.com/imanyass/ShigaPass)  
    Yassine I, Hansen EE, Lefèvre S, Ruckly C, Carle I, Lejay-Collin M, Fabre L, Rafei R, Pardos de la Gandara M, Daboussi F, Shahin A, Weill FX [ShigaPass: an in silico tool predicting Shigella serotypes from whole-genome sequencing assemblies.](https://doi.org/10.1099%2Fmgen.0.000961) _Microb Genomics_ 9(3) (2023)
  
- [ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper)  
    Wu Y, Lau HK, Lee T, Lau DK, Payne J [In Silico Serotyping Based on Whole-Genome Sequencing Improves the Accuracy of Shigella Identification.](https://doi.org/10.1128/AEM.00165-19) *Applied and Environmental Microbiology*, 85(7). (2019)
  
- [ShigEiFinder](https://github.com/LanLab/ShigEiFinder)  
    Zhang X, Payne M, Nguyen T, Kaur S, Lan R [Cluster-specific gene markers enhance Shigella and enteroinvasive Escherichia coli in silico serotyping.](https://doi.org/10.1099/mgen.0.000704) Microbial Genomics, 7(12). (2021)
  
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
  
