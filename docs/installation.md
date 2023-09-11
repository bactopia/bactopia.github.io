---
title: Installation
description: >-
    Learn how Bactopia install and get started using Bactopia for your genomic analyses.
---

Bactopia includes hundreds of tools in its workflow. As you can imagine installing these
tools can turn into a very frustrating process. With this in mind, from the onset Bactopia was
developed to only include programs that available from [Bioconda](https://bioconda.github.io/)
and [Conda-Forge](https://conda-forge.org/).

## *(Optional)* Install Conda via MambaForge

Conda is an open source package management system and environment management system that runs
on Windows, Mac OSX, and Linux. By using packages available from Conda, we can streamline the
installation process for the hundreds of tools that Bactopia uses.

If you do not have Conda installed I recommend installing
[MambaForge](https://github.com/conda-forge/miniforge#mambaforge), as it comes with Mamba
pre-installed. You'll want to follow the [MambaForge Install Instructions](https://github.com/conda-forge/miniforge#unix-like-platforms-mac-os--linux)
for this. This will take a few minutes, but once complete you'll be ready to install
Bactopia.

## Installation
Once you have Conda all set up, you are ready to create an environment for
Bactopia. To do so, you can use the following command:

```{bash}
mamba create -n bactopia -c conda-forge -c bioconda bactopia
```

After a few minutes you will have a new conda environment suitably named *bactopia*.
To activate this environment, you will can use the following command:

```{bash}
conda activate bactopia
```

And voilà, you are all set to get started processing your data!

## Windows and OSX Support

!!! warning "Windows is not supported, please use Windows Subsystem for Linux"
    Bactopia will never support Windows natively due to dependencies. To use Bactopia on a
    Windows machine, you will need to set up Windows Subsystem for Linux (WSL). This would
    allow you to run Bactopia inside the Linux subsystem. I have limited resources to test
    Bactopia in WSL, but if you give it a go and run into any issues please reach out!

!!! warning "OSX has limited support"
    I have developed Bactopia primarily for Linux, but I recognize it is useable on Mac OSX.
    Currently the support for OSX will be limited due to not having significant resources
    available for testing OSX extensively. Please keep this in mind when using Bactopia on
    OSX. I will still try to help out if you run into any issues!

!!! danger "Apple silicon (ARM) is not supported"
    Bactopia will not work on Apple silicon or other ARM processors. This is due to many of
    the tools used by Bactopia not having an ARM compatible build. It is planned in Bioconda's
    future, until then the best option is to use Docker to emulate linux/amd64 architecture.
    This can be done by using the `-profile arm` option when running Bactopia.

## Docker and Singularity

You can also use Bactopia with Docker or Singularity, but it is Nextflow that will be
handling this. This is done using the `-profile` option. For example, to use Docker you
would use `-profile docker`, and `-profile singularity` for Singularity.

When using these profiles, Nextflow will use Docker or Singularity for each process that
is executed. In other words, Nextflow will be using `docker run` or `singularity exec`
without the need for you to do anything else.

!!! tip "Always prefer containers over Conda"
    While I will be the first to admit that I love Conda, it is not perfect. Overtime tools
    can become broken or incompatible due to dependencies. Containers are a great way
    to avoid these issues. If you are using Bactopia, and have Docker or Singularity
    available I would recommend using them over Conda.

## Run from GitHub Repository

Alternatively, if you already have Nextflow installed, and you don't want to use
Conda to install Bactopia, you can run Bactopia directly from the GitHub repository.

```{bash}
nextflow run bactopia/bactopia
```

!!! info "Missing out on helper commands"
    The Conda install of Bactopia comes with a few helper commands that are not available
    when running directly with Nextflow. These include commands to help prepare sample sheets,
    search public databases, pre-build environments, among other helper tools.
