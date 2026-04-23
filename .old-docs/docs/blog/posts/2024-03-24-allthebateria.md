---
authors:
  - rpetit3
categories:
  - Community
  - Tutorial
date: 2024-03-24
draft: false
pin: true
links:
  - installation.md
slug: bactopia-allthebacteria-tutorial
description: Learn how to use Bactopia to analyze nearly 2,000,000 bacterial assemblies from the AllTheBacteria project.
---

# Using Bactopia with AllTheBacteria Assemblies

[AllTheBacteria](https://github.com/iqbal-lab-org/AllTheBacteria) (ATB) is a collection
of nearly 2,000,000 bacterial assemblies. In this post you'll learn how to use Bactopia to
seamlessly analyze these assemblies with the available [Bactopia Tools](../../bactopia-tools/index.md).

<!-- more -->

## AllTheBacteria

[Zamin Iqbal's Group](https://www.ebi.ac.uk/research/iqbal/), who brought us [661k bacterial assemblies](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001421),
has now taken it a step further with [AllTheBacteria](https://www.biorxiv.org/content/10.1101/2024.03.08.584059v1).
As someone once tasked with assembling "all the _Staphylococcus aureus_ genomes" (_although, it was only
about 700 samples in 2010!_), this is truly an impressive feat, and a valuable community resource!
With the latest assemblies, the collection is now nearly 2,000,000 bacterial assemblies! 🎉

Similar to their previous methods, the latest version of AllTheBacteria uses [Shovill](https://github.com/tseemann/shovill)
for assembly. In addition, each assembly has basic metrics calculated, undergoes taxonomic
abundance estimation, and has sketches made available. For more details about this project,
please see:

- Preprint: _[AllTheBacteria - all bacterial genomes assembled, available and searchable](https://www.biorxiv.org/content/10.1101/2024.03.08.584059v1)_
- GitHub: [AllTheBacteria](https://github.com/iqbal-lab-org/AllTheBacteria)

Since Zamin revealed the latest updates on AllTheBacteria, I've been wondering: _How could Bactopia
users take advantage these assemblies? Especially, through available [Bactopia Tools](../../bactopia-tools/index.md)?_

## Why Bactopia Tools?

The really nice thing about Bactopia Tools is they make it super easy to run [60 additional analyses](../../bactopia-tools/index.md)
on your genomes. It's really as simple as adding `--wf <tool>` to your Bactopia command, then Bactopia
will then handle the rest for you, including container selection and audit trails. 

Obviously, I'm a bit biased here, but utilizing Bactopia Tools in this situation would
greatly streamline a lot of downstream analyses of AllTheBacteria assemblies. I think this
would allow researchers to quickly get to the science behind these assemblies.

To give you an idea, there are currently 38 Bactopia Tools that use assemblies as inputs.
In other words, each of these tools would be easy to run on the 2,000,000 AllTheBacteria
assemblies.

??? tip "Expand to see the list of Bactopia Tools"

    Each of the tools listed below accepts a single assembly as input.

    | Tool | Description |
    |------|-------------|
    | [bakta](../../bactopia-tools/bakta.md) | Rapid annotation of bacterial genomes & plasmids |
    | [fastani](../../bactopia-tools/fastani.md) | Fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI) |
    | [gtdb](../../bactopia-tools/gtdb.md) | Identify marker genes and assign taxonomic classifications |
    | [mashtree](../../bactopia-tools/mashtree.md) | Create a trees using Mash distances |
    | [abricate](../../bactopia-tools/abricate.md) | Mass screening of contigs for antimicrobial and virulence genes |
    | [abritamr](../../bactopia-tools/abritamr.md) | A NATA accredited tool for reporting the presence of antimicrobial resistance genes |
    | [agrvate](../../bactopia-tools/agrvate.md) | Rapid identification of Staphylococcus aureus agr locus type and agr operon variants |
    | [amrfinderplus](../../bactopia-tools/amrfinderplus.md) | Identify antimicrobial resistance in genes or proteins |
    | [btyper3](../../bactopia-tools/btyper3.md) | Taxonomic classification of Bacillus cereus group isolates |
    | [busco](../../bactopia-tools/busco.md) | Assembly completeness based on evolutionarily informed expectations |
    | [checkm](../../bactopia-tools/checkm.md) | Assess the assembly quality of your microbial samples |
    | [ectyper](../../bactopia-tools/ectyper.md) | In-silico prediction of Escherichia coli serotype |
    | [emmtyper](../../bactopia-tools/emmtyper.md) | emm-typing of Streptococcus pyogenes assemblies |
    | [gamma](../../bactopia-tools/gamma.md) | Identification, classification, and annotation of translated gene matches |
    | [hicap](../../bactopia-tools/hicap.md) | Identify cap locus serotype and structure in your Haemophilus influenzae assemblies |
    | [hpsuissero](../../bactopia-tools/hpsuissero.md) | Rapid Haemophilus parasuis Serotyping of assemblies |
    | [kleborate](../../bactopia-tools/kleborate.md) | Screen for MLST, sub-species, and other Klebsiella related genes of interest |
    | [legsta](../../bactopia-tools/legsta.md) | Typing of Legionella pneumophila assemblies |
    | [lissero](../../bactopia-tools/lissero.md) | Serogroup typing prediction for Listeria monocytogenes |
    | [mashdist](../../bactopia-tools/mashdist.md) | Calculate Mash distances between sequences |
    | [mcroni](../../bactopia-tools/mcroni.md) | Sequence variation in mobilized colistin resistance (mcr-1) genes |
    | [meningotype](../../bactopia-tools/meningotype.md) | Serotyping of Neisseria meningitidis |
    | [mlst](../../bactopia-tools/mlst.md) | Scan contig files against PubMLST typing schemes |
    | [mobsuite](../../bactopia-tools/mobsuite.md) | Reconstruct and annotate plasmids in bacterial assemblies |
    | [pasty](../../bactopia-tools/pasty.md) | Serogrouping of Pseudomonas aeruginosa isolates |
    | [pbptyper](../../bactopia-tools/pbptyper.md) | Penicillin Binding Protein (PBP) typer for Streptococcus pneumoniae |
    | [phispy](../../bactopia-tools/phispy.md) | Predict prophages in bacterial genomes |
    | [plasmidfinder](../../bactopia-tools/plasmidfinder.md) | Plasmid identification from assemblies |
    | [prokka](../../bactopia-tools/prokka.md) | Whole genome annotation of small genomes (bacterial, archeal, viral) |
    | [quast](../../bactopia-tools/quast.md) | Assess the quality of assembled contigs |
    | [rgi](../../bactopia-tools/rgi.md) | Predict antibiotic resistance from assemblies |
    | [seqsero2](../../bactopia-tools/seqsero2.md) | Salmonella serotype prediction from reads or assemblies |
    | [shigeifinder](../../bactopia-tools/shigeifinder.md) | Shigella and EIEC serotyping from assemblies |
    | [sistr](../../bactopia-tools/sistr.md) | Serovar prediction of Salmonella assemblies |
    | [spatyper](../../bactopia-tools/spatyper.md) | Computational method for finding spa types in Staphylococcus aureus |
    | [staphopiasccmec](../../bactopia-tools/staphopiasccmec.md) | Primer based SCCmec typing of Staphylococcus aureus genomes |
    | [stecfinder](../../bactopia-tools/stecfinder.md) | Serotyping Shigella toxin producing Escherichia coli genomes |
    | [ssuissero](../../bactopia-tools/ssuissero.md) | Rapid Streptococcus suis Serotyping of assemblies |

!!! failure "Bactopia Tools require samples processed with Bactopia"

    One of the key features of Bactopia Tools, is they utilize Bactopia outputs to rapidly 
    identify and begin analysis. AllTheBacteria assemblies were not processed by Bactopia,
    so they aren't compatible with Bactopia Tools. But, no worries, with a little work we
    can make this a possibility!

## `bactopia atb-formatter`

Bactopia already allows assemblies as inputs, but I didn't want users to have to go through the
full Bactopia pipeline to use the Bactopia Tools. Instead, I wanted to make a quick and easy way
for users to go directly to using Bactopia Tools. To accomplish this, I created a new Bactopia 
command called [atb-formatter](https://github.com/bactopia/bactopia-py?tab=readme-ov-file#all-the-bacteria-atb)
(_AllTheBacteria Formatter_). With `atb-formatter`, the necessary Bactopia output directory
structure will be created from a directory of _AllTheBacteria assemblies.

!!! success "AllTheBacteria assemblies can be used with Bactopia Tools!"

That's cool and all, but let's actually demonstrate the usage of `atb-formatter` on some
_Legionella pneumophila_ assemblies from AllTheBacteria.

## Example Usage for _Legionella pneumophila_

To demonstrate the usage of `bactopia atb-formatter`, I will use assemblies for
_Legionella pneumophila_ from AllTheBacteria and run [legsta](https://github.com/tseemann/legsta),
 a typing tool for _L. pneumophila_ assemblies, written by [Torsten Seeman](https://www.doherty.edu.au/people/associate-professor-torsten-seemann),
To be specific, I will run legsta from the available [Bactopia Tool](https://bactopia.github.io/latest/bactopia-tools/legsta/).

### Getting Setup

Before we get started, you'll need to have Bactopia installed. If you haven't done this yet,
please see the [installation instructions](../../installation.md).

You will also want to make sure you are using at least version 3.0.1 of Bactopia, as this is
the first release to have the `atb-formatter` command.

``` { .bash .no-copy }
bactopia --version
bactopia 3.0.1
```

### Download the Assemblies

First I will download the _L. pneumophila_ assemblies from AllTheBacteria, then extract
them into a folder called `legionella-assemblies`. Easy enough!

``` { .bash .copy } 
mkdir atb-legionella
cd atb-legionella

# Download the assemblies
wget https://ftp.ebi.ac.uk/pub/databases/AllTheBacteria/Releases/0.1/assembly/legionella_pneumophila__01.asm.tar.xz
wget https://ftp.ebi.ac.uk/pub/databases/AllTheBacteria/Releases/0.1/assembly/legionella_pneumophila__02.asm.tar.xz

# Extract the assemblies
mkdir legionella-assemblies
tar -C legionella-assemblies -xJf legionella_pneumophila__01.asm.tar.xz
tar -C legionella-assemblies -xJf legionella_pneumophila__02.asm.tar.xz
```

At the time of writing this, there were 5,393 _L. pneumophila_ assemblies available from
AllTheBacteria. While its not _Salmonella enterica_ with it's hundreds of thousands of assemblies,
it's a great number to demonstrate the usage of `bactopia atb-formatter`.

### Create the Bactopia Directory Structure

With the assemblies extracted, now I need to create the required Bactopia directory to make
use of Bactopia Tools. For this, I used `bactopia atb-formatter`, which creates a sample folder
for each assembly that matches the BioSample accession.

``` { .bash .copy } 
# Create the Bactopia directory structure
bactopia atb-formatter --path legionella-assemblies --recursive
```

??? info "A few notes about `bactopia atb-formatter`"

    Please note the usage of `--recursive` here, this will traverse the `legionella-assemblies` directory
    to find all assemblies contained. At this point, the `bactopia` directory structure has been
    created for 5,393 assemblies and is ready for use with Bactopia Tools.

    Also, by default the assemblies are not copied into the Bactopia directory structure, but
    instead symbolic links are created. This is to save disk space, but if you would like to
    copy the assemblies, you can use the `--publish-mode` parameter to change this behavior

After running the above command, you should see something like the following:

``` { .bash .no-copy } 
2024-03-22 14:30:07:root:INFO - Setting up Bactopia directory structure (use --verbose to see more details)
2024-03-22 14:30:08:root:INFO - Bactopia directory structure created at bactopia
2024-03-22 14:30:08:root:INFO - Total assemblies processed: 5393
```

### Use Bactopia to run Legsta

Fancy! Now we have all the assemblies sym-linked into a Bactopia directory structure. It's
time to let Bactopia Tools shine! To do this, I will run the
[legsta Bactopia Tool](https://bactopia.github.io/latest/bactopia-tools/legsta/) and demonstrate
how seamless it is to type 5,393 assemblies.

With a simple addition of `--wf legsta` and pointing to the Bactopia directory, `legsta` will
be executed on all 5,393 assemblies! It really is that simple!

``` { .bash .copy } 
# Run legsta
bactopia --wf legsta -profile singularity
```

!!! tip "Please use Docker or Singularity for these analyses"

    I'm a big supporter of Conda, but for reproducibility, it is recommended to use Docker or
    Singularity with Bactopia Tools. Conda environments can change depending on when they are
    installed, however the containers will always be the same.

After some time, the `legsta` tool will complete for all 5,393 assemblies, and you should be
met with something like the following:

```{bash}
[5d/d04297] process > BACTOPIATOOLS:LEGSTA:LEGSTA_MODULE (SAMN29911258) [100%] 5393 of 5393 ✔
[71/c63bf7] process > BACTOPIATOOLS:LEGSTA:CSVTK_CONCAT (legsta)        [100%] 1 of 1 ✔
[16/833262] process > BACTOPIATOOLS:CUSTOM_DUMPSOFTWAREVERSIONS (1)     [100%] 1 of 1 ✔

    Bactopia Tools: `legsta Execution Summary
    ---------------------------
    Bactopia Version : 3.0.1
    Nextflow Version : 23.10.1
    Command Line     : nextflow run /home/rpetit3/bactopia/main.nf --wf legsta \
                                    --bactopia bactopia/ -profile singularity
    Resumed          : false
    Completed At     : 2024-03-22T15:09:54.959834620-06:00
    Duration         : 32m 51s
    Success          : true
    Exit Code        : 0
    Error Report     : -
    Launch Dir       : /home/rpetit3/test-legsta
```

This took about 30 minutes on my laptop, but it was incredibly simple to run `legsta` on 
all 5,393 _L. pneumophila_ assemblies.

### Results of Typing

Here's the fun part, typing results for all 5,393 _L. pneumophila_ assemblies! Another nice
thing about the Bactopia Tools in that in most cases it will merge all the results at the end
leaving you with just a single file to review.

To share the results of this analysis, I've uploaded the results to Google Drive and made 
them available from this link: <a href="https://docs.google.com/spreadsheets/d/1NjkXEstWq5PMP0CLmO392HTjC8UuW-JPQIXpqsZ30nU/edit?usp=sharing" target="_blank">Bactopia - Legsta Results from AllTheBacteria</a>

From this Google Sheet, you can make a copy or export the results as a CSV file.

## Conclusion

In this post, I demonstrated how in just a few steps you can make use of Bactopia Tools to
rapidly and seamlessly start analyzing the 2,000,000 bacterial assemblies from AllTheBacteria.
If you are planning to do your own downstream analyses on these assemblies, I hope this post
has convinced you that Bactopia can make this process much easier.

If you have any questions or ideas for additional Bactopia Tools, please feel free to reach
out to me! 

__🎉 Also! This the first ever blog post for Bactopia! 🎉__
