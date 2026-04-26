BACTOPIA_REPO ?=

BACTOPIA_DEV_PYTHON ?= /home/rpetit3/.conda/envs/bactopia-dev/bin/python

.PHONY: generate parse generate-workflows generate-subworkflows generate-modules generate-citations generate-acknowledgements generate-enhancements parse-cli generate-cli generate-tools-index update-citations generate-llms-catalog llms-catalog clean-generated

generate: parse generate-workflows generate-subworkflows generate-modules generate-citations generate-acknowledgements generate-enhancements parse-cli generate-cli generate-tools-index

parse:
	@test -n "$(BACTOPIA_REPO)" || (echo "Error: BACTOPIA_REPO is not set. Pass it explicitly, for example: make generate BACTOPIA_REPO=../bactopia" >&2; exit 1)
	python bin/parse-bactopia.py $(BACTOPIA_REPO) --output data/bactopia.json

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
	rm -rf data/bactopia.json data/cli.json bactopia-tools/*.mdx bactopia-pipelines/*.mdx developers/subworkflows/*.mdx developers/modules/*.mdx developers/cli/*.mdx impact/citations.md impact/acknowledgements.md impact/enhancements.md static/llms.txt static/catalog.json
