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

## Version Snapshots

The site uses 5 Docusaurus docs plugins, so native versioning (which only supports the default plugin) is not used. Instead, each release is preserved as a static build snapshot stored in an orphan git branch (`snapshot/vX.Y.Z`). The deploy workflow assembles active snapshots into the build output at deploy time.

- `/` -- always serves the current version
- `/vX.Y.Z/` -- serves active version snapshots (with an announcement banner linking to latest)
- `snapshots.json` -- registry of all versions; the `active` flag controls which are included in the deploy
- Cloudflare Pages free plan has a 20,000 file limit; each snapshot uses ~2,000 files

### Creating a snapshot (new Bactopia release)

1. Go to **Actions > Create Version Snapshot** and run the workflow
   - `version`: the version tag (e.g., `v4.0.0`)
   - `bactopia_ref`: the bactopia repo ref to build from (e.g., `v4.0.0`)
2. The workflow builds the site with a version banner, pushes an orphan branch `snapshot/vX.Y.Z`, and updates `snapshots.json` on master
3. The deploy workflow runs automatically, including the new snapshot

After creating the snapshot, update the version label in `docusaurus.config.ts` to the new version:

```typescript
versions: {
  current: {
    label: 'v4.1.0',  // update to new version
    ...
  },
},
```

### Rebuilding a snapshot

Re-run the **Create Version Snapshot** workflow with the same version. The orphan branch is force-pushed with the new build.

### Managing versions

```bash
make snapshot-list                       # show all versions and file budget
make snapshot-add VERSION=vX.Y.Z FILES=N # manually register a snapshot
make snapshot-deactivate VERSION=v2.1.0  # drop from active deploy
make snapshot-activate VERSION=v2.1.0    # restore to active deploy
```

Deactivated versions appear under "Archived Versions" in the dropdown, linking to the GitHub branch. Re-activate anytime with `make snapshot-activate`.

## Deployment

The site is deployed to [Cloudflare Pages](https://pages.cloudflare.com/) via GitHub Actions. Pushes to `master` trigger the deploy workflow (`.github/workflows/deploy.yml`), which:

1. Generates docs from the bactopia source repo
2. Builds the Docusaurus site
3. Fetches active version snapshots from their orphan branches
4. Deploys the assembled output to Cloudflare Pages
