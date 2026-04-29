## Summary

<!-- Brief description of what this PR does -->

## Type of Change

- [ ] Content update (new or modified documentation)
- [ ] Correction (typo, broken link, inaccurate information)
- [ ] Site infrastructure (config, styling, components, CI/CD)
- [ ] Auto-generation (templates, scripts, data files)

## Version Impact

- [ ] This change affects the current live version only (no snapshot needed)
- [ ] A version snapshot should be created before merging (new Bactopia release)
- [ ] A snapshot rebuild is needed after merging (fix to snapshotted content)

## Checklist

- [ ] Site builds without errors (`npm run build`)
- [ ] Changes verified in the dev server (`npm start`)
- [ ] `snapshots.json` updated (if adding/removing a version)
- [ ] LLM catalog regenerated (`make llms-catalog`) if pages were added/removed/renamed
