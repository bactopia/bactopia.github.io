---
title: Quick Start
description: >-
    Get started using Bactopia in a few commands, no asking questions and no looking back!
---
# Quick Start

## Installation via Conda

This is as quick as it gets. The following commands will install Bactopia and run a test dataset.

```{bash}
# Install Bactopia using Mamba
mamba create -y -n bactopia -c conda-forge -c bioconda bactopia

# Test Bactopia
# First launch will set up environments (e.g. Conda, Docker, or Singularity)
conda activate bactopia
bactopia -profile test,standard
```

!!! note "Use `-profile` to change environment"
    The default profile for Bactopia is Conda. If you would like to test using Docker or
    Singularity, you can use the `-profile` option. For example, to use Docker you would use
    `-profile test,docker`, and `-profile test,singularity` for Singularity.

## Run from GitHub Repository

Alternatively, if you already have Nextflow installed, and you don't want to use
Conda to install Bactopia, you can run Bactopia directly from the GitHub repository.

```{bash}
nextflow run bactopia/bactopia -profile test,standard
```

!!! info "Missing out on helper commands"
    The Conda install of Bactopia comes with a few helper commands that are not available
    when running directly with Nextflow. These include commands to help prepare sample sheets,
    search public databases, pre-build environments, among other helper tools.
