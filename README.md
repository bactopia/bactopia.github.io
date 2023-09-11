# bactopia.github.io
Bactopia Documentation


## Local Install

```{bash}
# Create a MkDocs environment
mamba create -n bactopia-docs -c conda-forge -c bioconda mkdocs pip setuptools
conda activate bactopia-docs

# Install mkdocs-material 
pip install mkdocs-material
# Or, insiders edition
pip install git+https://${GH_TOKEN}@github.com/squidfunk/mkdocs-material-insiders.git

# Clone the repo
git clone git@github.com:bactopia/bactopia.github.io.git
cd bactopia.github.io

# Serve the docs
mkdocs serve -a 0.0.0.0:8000
```
