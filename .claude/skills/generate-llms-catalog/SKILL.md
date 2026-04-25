---
name: generate-llms-catalog
description: >-
  Generate llms.txt and catalog.json files for LLM consumption from the
  Bactopia docs site content. Run this skill whenever documentation content
  is added, removed, or updated, when the user asks to regenerate the LLM
  catalog, refresh llms.txt, update the LLM index, or sync the static LLM
  files with the current documentation.
---

# Generate LLMs Catalog

Regenerate `static/llms.txt` and `static/catalog.json` from all documentation
content files. These files provide machine-readable indexes of the Bactopia
documentation for LLM consumption.

- `llms.txt` follows the [llms.txt standard](https://llmstxt.org/)
- `catalog.json` provides structured metadata (title, description, tags, URL) per page

## Steps

### 1. Run the generator

```bash
python bin/generate-llms-catalog.py
```

Or via Make:

```bash
make llms-catalog
```

The script walks all 6 content areas (docs, bactopia-tools, bactopia-pipelines,
developers, impact, blog), parses YAML frontmatter from each `.md`/`.mdx` file,
and generates both output files.

Expected output:

```
Collecting Bactopia...
  7 pages
Collecting Bactopia Tools...
  68 pages
Collecting Bactopia Pipelines...
  4 pages
Collecting Developers...
  221 pages
Collecting Impact & Outreach...
  5 pages
Collecting Blog...
  2 pages

Wrote static/llms.txt
Wrote static/catalog.json

Total: 307 pages across 6 sections
```

### 2. Verify output

Check that both files were generated correctly:

- `static/llms.txt` -- should have `# Bactopia` heading, blockquote tagline,
  section headings matching the navbar, and one `- [Title](URL): description`
  entry per page
- `static/catalog.json` -- should be valid JSON with `site`, `generated`,
  `total_pages`, and `sections` array. Each section should have `pages` with
  `title`, `description`, `url`, `path`, `tags`, and `source_file`

### 3. Build check

Run `npm run build` to confirm the site builds with the new static files.
Both should be served at the site root:

- `https://bactopia.github.io/llms.txt`
- `https://bactopia.github.io/catalog.json`
