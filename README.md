# bactopia.github.io

Documentation for [Bactopia](https://github.com/bactopia/bactopia), built with [Docusaurus 3](https://docusaurus.io/).

## Prerequisites

- **Node.js** >= 18
- **Conda** environment `bactopia-dev` from the [bactopia repo](https://github.com/bactopia/bactopia) (provides Node.js, Python, and all shared dependencies)

```bash
# Create the environment (from the bactopia repo)
cd /path/to/bactopia
conda env create -f environment.yml -n bactopia-dev
conda activate bactopia-dev
```

## Development Setup

```bash
git clone git@github.com:bactopia/bactopia.github.io.git
cd bactopia.github.io
npm install
npm start
```

The dev server runs at `http://0.0.0.0:8000` with hot reload.

## Available Scripts

| Script              | Description                          |
| ------------------- | ------------------------------------ |
| `npm start`         | Start the dev server with hot reload |
| `npm run build`     | Production build to `build/`         |
| `npm run serve`     | Serve the production build locally   |
| `npm run clear`     | Clear the Docusaurus cache           |
| `npm run typecheck` | Run TypeScript type checking         |

## Generating Docs from Bactopia Source

Most documentation under `bactopia-tools/`, `bactopia-pipelines/`, `developers/`, and `impact/` is auto-generated from the [bactopia](https://github.com/bactopia/bactopia) source repo using Python scripts in `bin/`.

```bash
# Generate all docs (requires bactopia repo path)
make generate BACTOPIA_REPO=/path/to/bactopia
```

Individual targets are also available:

| Target                       | Description                                       |
| ---------------------------- | ------------------------------------------------- |
| `parse`                      | Parse the bactopia repo into `data/bactopia.json` |
| `generate-workflows`         | Generate tool and pipeline docs                   |
| `generate-subworkflows`      | Generate subworkflow docs                         |
| `generate-modules`           | Generate module docs                              |
| `generate-citations`         | Generate citations page                           |
| `generate-acknowledgements`  | Generate acknowledgements page                    |
| `generate-enhancements`      | Generate enhancements page                        |
| `parse-cli`                  | Parse bactopia-py CLI into `data/cli.json`        |
| `generate-cli`               | Generate CLI reference docs                       |
| `update-citations`           | Refresh `data/citations.yml` from source          |
| `clean-generated`            | Remove all generated files                        |

By default, `parse-cli` uses the Python from `bactopia-dev`. Override with:

```bash
make parse-cli BACTOPIA_DEV_PYTHON=/path/to/python
```

## Project Structure

```text
docs/                  Main Bactopia documentation
bactopia-tools/        Auto-generated tool docs
bactopia-pipelines/    Auto-generated pipeline docs
developers/            Developer guides, subworkflows, modules, CLI reference
impact/                Impact & outreach content
blog/                  Blog posts
data/                  JSON/YAML data files (citations, CLI, bactopia metadata)
src/                   React components, custom CSS, pages
bin/                   Python doc-generation scripts
templates/             Jinja2 templates for doc generation
static/                Static assets (images, logos)
```

## Versioning

When a new Bactopia release ships, a version snapshot is created so users can access docs for prior releases via the version dropdown in the navbar.

## Deployment

The site is deployed to GitHub Pages on the `gh-pages` branch.

```bash
npm run build    # build the production site
npm run deploy   # deploy to GitHub Pages
```
