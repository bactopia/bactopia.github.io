BACTOPIA_REPO ?=

BACTOPIA_DEV_PYTHON ?= /home/rpetit3/.conda/envs/bactopia-dev/bin/python

.PHONY: generate parse copy-changelog generate-workflows generate-subworkflows generate-modules generate-citations generate-acknowledgements generate-enhancements parse-cli generate-cli generate-tools-index update-citations generate-llms-catalog llms-catalog clean-generated snapshot-list snapshot-add snapshot-deactivate snapshot-activate

generate: parse copy-changelog generate-workflows generate-subworkflows generate-modules generate-citations generate-acknowledgements generate-enhancements parse-cli generate-cli generate-tools-index

parse:
	@test -n "$(BACTOPIA_REPO)" || (echo "Error: BACTOPIA_REPO is not set. Pass it explicitly, for example: make generate BACTOPIA_REPO=../bactopia" >&2; exit 1)
	python bin/parse-bactopia.py $(BACTOPIA_REPO) --output data/bactopia.json

copy-changelog:
	@test -n "$(BACTOPIA_REPO)" || (echo "Error: BACTOPIA_REPO is not set." >&2; exit 1)
	cp $(BACTOPIA_REPO)/CHANGELOG.md docs/changelog.md

generate-workflows:
	python bin/generate-workflows.py data/bactopia.json --tools-dir bactopia-tools/ --pipelines-dir bactopia-pipelines/ --docs-dir docs/

generate-subworkflows:
	python bin/generate-subworkflows.py data/bactopia.json --output-dir developers/subworkflows/

generate-modules:
	python bin/generate-modules.py data/bactopia.json --output-dir developers/modules/

generate-citations:
	python bin/generate-citations.py data/citations.yml --output impact/citations.md

generate-acknowledgements:
	python bin/generate-acknowledgements.py data/bactopia.json --output impact/acknowledgements.md

generate-enhancements:
	python bin/generate-enhancements.py data/contributions.yml --output impact/enhancements.md

parse-cli:
	$(BACTOPIA_DEV_PYTHON) bin/parse-cli.py --output data/cli.json

generate-cli:
	python bin/generate-cli.py data/cli.json --output-dir developers/cli/

generate-tools-index:
	python bin/generate-tools-index.py data/tool-categories.yml --tools-dir bactopia-tools/ --output bactopia-tools/index.mdx

update-citations:
	python bin/update-citations.py --output data/citations.yml

generate-llms-catalog:
	python bin/generate-llms-catalog.py

llms-catalog: generate-llms-catalog

clean-generated:
	rm -rf data/bactopia.json data/cli.json bactopia-tools/*.mdx bactopia-pipelines/*.mdx developers/subworkflows/*.mdx developers/modules/*.mdx developers/cli/*.mdx impact/citations.md impact/acknowledgements.md impact/enhancements.md static/llms.txt static/catalog.json docs/changelog.md

# --- Version Snapshot Management ---

snapshot-list:
	@python3 -c "\
	import json; \
	d = json.load(open('snapshots.json')); \
	active = [s for s in d['snapshots'] if s['active']]; \
	archived = [s for s in d['snapshots'] if not s['active']]; \
	active_files = sum(s['files'] for s in active); \
	main = 2000; \
	print('Active versions:'); \
	[print(f'  {s[\"version\"]:>10}  {s[\"files\"]:>5} files') for s in active]; \
	print(f'\nArchived versions:'); \
	([print(f'  {s[\"version\"]:>10}  {s[\"files\"]:>5} files') for s in archived] if archived else [print('  (none)')]); \
	print(f'\nEstimated deploy: ~{main} (main) + {active_files} (snapshots) = {main + active_files} / 20000'); \
	print(f'Remaining budget: ~{20000 - main - active_files} files (~{(20000 - main - active_files) // main} more snapshots)')"

snapshot-add:
	@test -n "$(VERSION)" || (echo "Error: VERSION is required. Usage: make snapshot-add VERSION=v4.0.0 FILES=1839" >&2; exit 1)
	@python3 -c "\
	import json, sys; \
	f = 'snapshots.json'; d = json.load(open(f)); \
	v = '$(VERSION)'; n = int('$(FILES)' or '0'); \
	exists = [s for s in d['snapshots'] if s['version'] == v]; \
	(print(f'Error: {v} already exists', file=sys.stderr) or sys.exit(1)) if exists else None; \
	d['snapshots'].insert(0, {'version': v, 'branch': f'snapshot/{v}', 'files': n, 'active': True}); \
	json.dump(d, open(f, 'w'), indent=2); \
	print(f'Added {v} (files={n}, active=true)')"

snapshot-deactivate:
	@test -n "$(VERSION)" || (echo "Error: VERSION is required. Usage: make snapshot-deactivate VERSION=v2.1.0" >&2; exit 1)
	@python3 -c "\
	import json, sys; \
	f = 'snapshots.json'; d = json.load(open(f)); \
	v = '$(VERSION)'; \
	matched = [s for s in d['snapshots'] if s['version'] == v]; \
	(print(f'Error: {v} not found', file=sys.stderr) or sys.exit(1)) if not matched else None; \
	[s.update({'active': False}) for s in d['snapshots'] if s['version'] == v]; \
	json.dump(d, open(f, 'w'), indent=2); \
	print(f'Deactivated {v} (will not be included in deploy)')"

snapshot-activate:
	@test -n "$(VERSION)" || (echo "Error: VERSION is required. Usage: make snapshot-activate VERSION=v2.1.0" >&2; exit 1)
	@python3 -c "\
	import json, sys; \
	f = 'snapshots.json'; d = json.load(open(f)); \
	v = '$(VERSION)'; \
	matched = [s for s in d['snapshots'] if s['version'] == v]; \
	(print(f'Error: {v} not found', file=sys.stderr) or sys.exit(1)) if not matched else None; \
	[s.update({'active': True}) for s in d['snapshots'] if s['version'] == v]; \
	json.dump(d, open(f, 'w'), indent=2); \
	print(f'Activated {v} (will be included in deploy)')"
