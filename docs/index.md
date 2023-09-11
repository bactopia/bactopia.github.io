![Bactopia Logo](assets/bactopia-logo.png)

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in minutes__

    ---

    Install `bactopia` from [Bioconda](https://bioconda.github.io/) and start processing
    genomes in minutes

    [:octicons-arrow-right-24: Installation](installation.md)

-   :material-bacteria:{ .lg .middle } __Effortless bacterial genomics__

    ---

    Streamlined pipeline for efficient and complete analysis of bacterial genomes

    [:octicons-arrow-right-24: Beginner's Guide](beginners-guide.md)

-   :material-lightbulb-on:{ .lg .middle } __Seamlessly expand analyses__

    ---

    Rapidly extend studies with a variety of supplementary, ready-made, workflows

    [:octicons-arrow-right-24: Bactopia Tools](bactopia-tools/index.md)

-   :material-star:{ .lg .middle } __Making an impact__

    ---

    A free and open-source tool that regularly contributes back to the community

    [:octicons-arrow-right-24: Impact and Outreach](impact-and-outreach/index.md)

</div>

## Overview

Bactopia is a flexible pipeline for complete analysis of bacterial genomes. The goal of
Bactopia is process your data with a broad set of tools, so that you can get to the fun
part of analyses quicker!

Bactopia was inspired by [Staphopia](https://staphopia.github.io/), a workflow we (Tim Read
and myself) released that is targeted towards *Staphylococcus aureus* genomes. Using what we
learned from Staphopia and user feedback, Bactopia was developed from scratch with usability,
portability, and speed in mind from the start.

Bactopia uses [Nextflow](https://www.nextflow.io/) to manage the workflow, allowing for support
of many types of environments (e.g. cluster or cloud). Bactopia allows for the usage of many
public datasets as well as your own datasets to further enhance the analysis of your sequencing.
Bactopia only uses software packages available from [Bioconda](https://bioconda.github.io/)
and [Conda-Forge](https://conda-forge.org/) to make installation as simple as possible for
*all* users.

To highlight the use of [Bactopia Datasets](datasets.md), [Bactopia](workflow-overview.md),
and [Bactopia Tools](bactopia-tools/index.md), we performed an analysis of 1,664 public
*Lactobacillus* genomes, focusing on *Lactobacillus crispatus*, a species that is a common
part of the human vaginal microbiome. The results from this analysis are published in mSystems
under the title:
*[Bactopia: a flexible pipeline for complete analysis of bacterial genomes](https://doi.org/10.1128/mSystems.00190-20)*

<a class="zoom" href="/assets/bactopia-workflow.png">
![Bactopia Workflow](/assets/bactopia-workflow.png)
</a>

## Documentation Overview
[Quick Start](quick-start.md)  
Straight the point details for getting started with Bactopia.  

[Installation](installation.md)  
More detailed information for getting Bactopia set up on your system.

[Beginner's Guide](beginners-guide.md)  
A guide to essential parameters for getting started with Bactopia

[Workflow Steps](bactopia/gather.md)  
A step-by-step walkthrough of the Bactopia workflow

[Full Guide](full-guide.md)  
A complete guide to all steps in Bactopia

[Changelog Usage](changelog.md)  
The full set of parameters that users can tweak in Bactopia.

[Acknowledgements](impact-and-outreach/acknowledgements.md)  
A list of datasets and software (and many thanks!) used by Bactopia.

## Funding

Support for this project came (in part) from an Emory Public Health Bioinformatics Fellowship
funded by the [CDC Emerging Infections Program (U50CK000485) PPHF/ACA: Enhancing Epidemiology and Laboratory Capacity](https://dph.georgia.gov/EIP),
the [Wyoming Public Health Division](https://health.wyo.gov/publichealth/), and
the [Center for Applied Pathogen Epidemiology and Outbreak Control (CAPE)](https://www.linkedin.com/company/center-for-applied-pathogen-epidemiology-and-outbreak-control/).

<a href="https://dph.georgia.gov/EIP">
![Georgia Emerging Infections Program](assets/gaeip-banner.png){ width="22%" }
</a>
<a href="https://health.wyo.gov/publichealth/">
![Wyoming Public Health Division](assets/wyphd-banner.jpg){ width="44%" }
</a>
<a href="https://www.linkedin.com/company/center-for-applied-pathogen-epidemiology-and-outbreak-control/">
![Center for Applied 
Pathogen Epidemiology and Outbreak Control](assets/cape-banner.png){ width="29%" }
</a>

## Citing Bactopia

If you use Bactopia in your analysis, please cite the following.

Petit III RA, Read TD [Bactopia - a flexible pipeline for complete analysis of bacterial genomes.](https://doi.org/10.1128/mSystems.00190-20) _mSystems_ 5 (2020)
