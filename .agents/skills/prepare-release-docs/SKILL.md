---
name: prepare-release-docs
description: >-
  Prepare the Bactopia docs site for a new bactopia release. Covers the full
  per-release workflow: regenerating auto-generated content from the new
  bactopia tag, registering new Bactopia Tools in the tools index, refreshing
  hand-written pages for changed behavior, updating the AI Skills page,
  regenerating the LLM catalog, bumping the version label, snapshotting the
  outgoing version locally, and pushing a branch for PR review (never merging
  to master). Use this skill whenever a new
  bactopia version is released or tagged, when the user asks to update the
  docs for a release, bump the docs version, prepare release docs, or publish
  docs for a new bactopia version.
---

# Prepare Release Docs

Update the bactopia.github.io docs site for a new bactopia release. The site
auto-generates most content from the bactopia source repo, so a release means:
regenerate from the new tag, fix the few hand-written pages, bump the version
label, snapshot the outgoing version locally, then push a branch and hand off
to a PR -- the skill never merges to master.

Inputs to collect from the user (or infer from context):

- `NEW_VERSION` -- the released tag, e.g. `v4.1.0`
- Release notes: https://github.com/bactopia/bactopia/releases/tag/<NEW_VERSION>

Work on a dedicated branch named `<NEW_VERSION>-docs`.

## Steps

### 1. Clone the release tag fresh

Do not rely on or modify any existing local bactopia checkout -- clone the
tag shallowly from GitHub into a scratch path:

```bash
git clone --branch <NEW_VERSION> --depth 1 https://github.com/bactopia/bactopia.git /tmp/bactopia-<NEW_VERSION>
```

Use `/tmp/bactopia-<NEW_VERSION>` as `BACTOPIA_REPO` everywhere below. If the
path already exists, `rm -rf` it first.

### 2. Read the release notes and extract what the docs must reflect

From the GitHub release page and the repo's `CHANGELOG.md`, list:

- New Bactopia Tools (`--wf <NAME>`) -> each needs a generated page AND an
  entry in `data/tool-categories.yml` (step 3)
- New/removed modules and subworkflows -> handled automatically by
  `make generate` (step 4)
- New skills in `.agents/skills/` -> AI Skills page (step 5)
- Removed or renamed CLI parameters and replaced tools -> hand-written page
  sweep (step 7)
- Behavior changes to defaults (e.g. a new default tool) -> hand-written page
  sweep (step 7)

### 3. Register new Bactopia Tools in `data/tool-categories.yml`

`bin/generate-tools-index.py` (run by `make generate`) fails the build if any
`bactopia-tools/*.mdx` is missing from this file. For each new tool, add its
name to the `tools:` list of the best-fit category (alphabetical). If unsure
of the category, ask the user -- the grouping is user-facing.

### 4. Regenerate auto-generated content

```bash
export PATH="$HOME/.conda/envs/bactopia-dev/bin:$PATH"
make generate BACTOPIA_REPO=<clone path>
```

This regenerates `data/bactopia.json`, `docs/changelog.md`, all
`bactopia-tools/`, `bactopia-pipelines/`, `developers/subworkflows/`,
`developers/modules/`, `developers/cli/`, the impact pages, and the grouped
`bactopia-tools/index.mdx`.

Spot-check: `data/bactopia.json` mentions the new tools, and `git status`
shows the expected new/changed pages. If new tools from the release notes are
missing, investigate `bin/parse-bactopia.py` before hand-writing anything --
generated pages must come from the generator.

### 5. Refresh the AI Skills page (only if skills changed)

Compare `.agents/skills/` in the fresh clone against the skills documented in
`developers/ai-skills/index.mdx`. If any were added, removed, or renamed,
follow the `generate-skills-docs` skill to regenerate the page.

### 6. Regenerate the LLM catalog

```bash
make llms-catalog
```

### 7. Sweep hand-written pages for stale content

Files under `docs/` (except `changelog.md`), `developers/index.mdx`, and the
section index pages are hand-written -- `make generate` does not touch them.
For every removed/renamed parameter and replaced tool from step 2, grep the
hand-written pages and update them:

```bash
grep -rn "<removed-param>\|<replaced-tool>" docs/ --include='*.md' --include='*.mdx'
```

Also bump captured CLI banners (e.g. `Bactopia Version : X.Y.Z` in
`docs/tutorial.md`) to the new version.

### 8. Bump the current-version label

In `docusaurus.config.ts`, set `versions.current.label` to `'<NEW_VERSION>'`.

### 9. Build and verify

```bash
npm run build
```

Then verify the new behavior landed (adapt greps to the release):

- New tool pages exist and appear in `bactopia-tools/index.mdx` under the
  right category headings
- Removed parameters are gone from both generated and hand-written pages
- `docs/changelog.md` has the new version section
- `static/llms.txt` / `static/catalog.json` include the new pages
- `npm start` and eyeball the new tool pages, the tools index, and the
  version dropdown showing the new label

### 10. Snapshot the outgoing version locally (while the PR is open)

The outgoing version's docs must be captured as a snapshot so they stay
available at `/<OUTGOING_VERSION>/` after the switch. A snapshot is just a
production build pushed to an orphan branch plus an entry in
`snapshots.json` -- do it locally, no GitHub Actions workflow needed.

Build the outgoing version from a clean worktree of master:

```bash
git worktree add /tmp/docs-snapshot master
cd /tmp/docs-snapshot
npm ci
export PATH="$HOME/.conda/envs/bactopia-dev/bin:$PATH"
git clone --branch <OUTGOING_VERSION> --depth 1 https://github.com/bactopia/bactopia.git /tmp/bactopia-<OUTGOING_VERSION>
make generate BACTOPIA_REPO=/tmp/bactopia-<OUTGOING_VERSION>
DOCS_VERSION=<OUTGOING_VERSION> npm run build
```

Push the build output to an orphan branch:

```bash
cd build
git init
git checkout --orphan snapshot/<OUTGOING_VERSION>
git add -A
git commit -m "Snapshot <OUTGOING_VERSION> ($(find . -type f | wc -l) files)"
git remote add origin git@github.com:bactopia/bactopia.github.io.git
git push origin snapshot/<OUTGOING_VERSION> --force
```

Back on the release branch, register the snapshot with the file count from
the build:

```bash
make snapshot-add VERSION=<OUTGOING_VERSION> FILES=<count>
git worktree remove /tmp/docs-snapshot --force
```

Timing is load-bearing: the snapshot must be built from master BEFORE the
release PR merges, or the "outgoing" snapshot would contain the new
version's content. Building it while the PR is open for review is the right
moment. Check the Cloudflare Pages file budget with `make snapshot-list`;
only deactivate old snapshots (`make snapshot-deactivate VERSION=vX.Y.Z`)
when approaching the 20,000-file limit.

### 11. Commit, push the branch, and hand off to a PR

```bash
git add -A
git commit -m "Update docs for bactopia <NEW_VERSION>"
git push -u origin <NEW_VERSION>-docs
```

Stop here -- the skill never merges to master. Tell the user the branch is
pushed and ready: they open the PR, review the Netlify deploy preview that
is automatically built and linked on the PR, and merge when satisfied. The
deploy workflow runs on the merge to master, serving the new version at `/`
and assembling the snapshot under `/<OUTGOING_VERSION>/`.

### 12. Post-deploy verification (after the user merges)

- `https://bactopia.io/` shows the new version label and changelog section
- `https://bactopia.io/<OUTGOING_VERSION>/` serves the snapshot with its
  version banner
- `https://bactopia.io/llms.txt` includes the new pages
