---
name: generate-skills-docs
description: >-
  Generate the AI Skills reference page for the Bactopia docs site.
  Runs a Python parser to extract structured metadata from the bactopia repo's
  SKILL.md files, then generates developers/ai-skills/index.mdx with an overview
  table and per-skill entries. Use this skill whenever skills are added,
  removed, or updated in the bactopia repo, when the user asks to regenerate
  the skills docs page, refresh the skills reference, update the AI skills
  documentation, or sync the docs site with the current set of bactopia skills.
---

# Generate Skills Docs

Regenerate the AI Skills reference page (`developers/ai-skills/index.mdx`) from the
SKILL.md files in the bactopia repo. This skill combines a deterministic Python
parser for structured extraction with Claude's ability to synthesize
natural-language content (when-to-use bullets, examples, related skills).

## Steps

### 1. Run the parser

Run `bin/generate-skills.py` to extract structured metadata from all SKILL.md files:

```bash
python bin/generate-skills.py /home/rpetit3/repos/bactopia/bactopia/.claude/skills --json
```

If the user provides a different bactopia repo path, substitute it. The script outputs
JSON with this shape per skill:

```json
{
  "name": "skill-name",
  "description": "Full description from frontmatter",
  "first_sentence": "First sentence of description.",
  "summary": "First paragraph of the markdown body.",
  "category": "Scaffolding|Maintenance|Review & Quality|Testing|Project",
  "cli_command": "bactopia-*",
  "cli_page": "/developers/cli/bactopia-*"
}
```

### 2. Generate the MDX page

Using the JSON output, write `developers/ai-skills/index.mdx` with this structure:

#### Frontmatter

```yaml
---
title: AI Skills
description: Reference for AI skills that automate Bactopia development tasks
---
```

#### Page body

Follow this outline exactly:

```markdown
# AI Skills

[intro paragraph -- see below]

## Overview

[summary table of all skills]

## Scaffolding

[skills with add-* prefix]

## Maintenance

[skills with update-*/merge-* prefix]

## Review & Quality

[skills with review-* prefix]

## Testing

[skills with run-* prefix]

## Project

[skills with project-* prefix]
```

#### Intro paragraph

Write 2-3 sentences explaining:
- These skills automate common Bactopia development tasks through AI-assisted coding tools
- Each skill wraps one or more bactopia-py CLI commands with interactive guidance
- Skills live in the bactopia repo at `.claude/skills/` and are invoked with `/skill-name`

Include a link: `[View skills on GitHub](https://github.com/bactopia/bactopia/tree/main/.claude/skills)`

#### Overview table

```markdown
| Skill | Category | Description |
|-------|----------|-------------|
| [`/add-bactopia-tool`](#add-bactopia-tool) | Scaffolding | First sentence from description... |
```

Use the `first_sentence` field from the JSON. Link each skill name to its heading
anchor on the same page.

#### Per-skill entries

For each skill, write an entry under its category heading:

```markdown
### `/skill-name`

[summary -- first paragraph from the SKILL.md body]

**Wraps:** [`bactopia-command`](/developers/cli/bactopia-command)

**When to use:**
- [2-3 bullet points extracted from the description's trigger phrases]
- [Focus on the "Use when asked to..." patterns in the description]

**Examples:**
\`\`\`
/skill-name argument1
/skill-name argument2
\`\`\`

**Related skills:** [`/sibling`](#sibling), [`/other`](#other)
```

Guidelines for each field:

- **Summary**: Use the `summary` field from JSON (first paragraph of body).
  Keep it to 1-2 sentences. If the summary is too long, trim to the essential point.
- **Wraps**: Link to the CLI Reference page using the `cli_page` field.
- **When to use**: Extract from the `description` field. Look for phrases like
  "Use when asked to...", "Use this skill whenever...", or the comma-separated
  list of trigger contexts. Convert to 2-3 concise bullet points.
- **Examples**: Create 2-3 realistic invocation examples. For skills that take
  a component name (like `/run-tests` or `/update-module`), show examples with
  different component names. For skills with no arguments (like `/project-status`),
  show just the bare invocation.
- **Related skills**: Cross-reference skills that are commonly used together.
  Use these relationships:
  - `add-bactopia-tool` <-> `add-module`, `add-subworkflow`, `run-tests`, `update-catalog`
  - `add-module` <-> `add-bactopia-tool`, `add-subworkflow`
  - `add-subworkflow` <-> `add-bactopia-tool`, `add-module`
  - `update-module` <-> `merge-schemas`, `project-status`
  - `update-catalog` <-> `project-status`, `merge-schemas`
  - `merge-schemas` <-> `update-module`, `update-catalog`
  - `review-groovydoc` <-> `review-citations`, `review-docs`
  - `review-citations` <-> `review-groovydoc`, `review-docs`
  - `review-docs` <-> `review-groovydoc`, `review-citations`, `project-status`
  - `review-tests` <-> `run-tests`
  - `run-tests` <-> `review-tests`
  - `project-status` <-> `update-catalog`, `run-tests`

### 3. Verify sidebar and index

Check that `sidebars-developers.ts` includes `'ai-skills'` after
`'nf-bactopia/index'`. If not, add it.

Check that `developers/index.mdx` has an "AI Skills" section between
"nf-bactopia Plugin" and "Subworkflows". If not, add:

```markdown
## AI Skills

Automation skills that orchestrate Bactopia CLI commands through AI-assisted
coding tools for scaffolding, maintenance, review, and testing tasks.

[Browse AI Skills](/developers/ai-skills)
```

### 4. Build check

Run `npm run build` to confirm the page builds without errors. If there are
MDX parsing issues, fix them (common culprits: unescaped `<`, `>`, `{`, `}`
in descriptions).
