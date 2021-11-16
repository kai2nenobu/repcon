MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -e -o pipefail -c
.DEFAULT_GOAL := help

# Variables
GIT_DESCRIBE = $(shell git describe --dirty=+)

# If SHLVL is empty (means shell is not sh-like), use bash of Git for Windows
ifeq ($(SHLVL),)
    SHELL := C:\Program Files\Git\bin\bash.exe
endif

# all targets are phony
.PHONY: $(grep -oE ^[a-zA-Z0-9_-]+: $(MAKEFILE_LIST) | sed 's/://')

help: ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "    \033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

lint: lint-flake8 lint-mypy lint-black lint-isort ## Lint all

lint-flake8: ## Lint python files by flake8
	poetry run flake8 .

lint-mypy: ## Lint python files by mypy
	poetry run mypy --no-error-summary --pretty .

lint-black: ## Check the format of python files by black
	poetry run black --quiet --check --diff --color .

lint-isort: ## Lint import orders in python files by isort
	poetry run isort --quiet --check --diff --color .

format: format-black format-isort ## Format all files

format-black: ## Format python files by black
	poetry run black .

format-isort: ## Sort import orders in python files by isort
	poetry run isort .

test: junit.xml ## Unit test by pytest

junit.xml:
	poetry run pytest -v

# Convert a JUnit test report into Sonar Generic Execution report
sonar_report.xml: junit.xml
	poetry run repcon junit.xml sonar_report.xml

scan: sonar_report.xml  ## Scan by sonar-scanner
	sonar-scanner -Dsonar.projectVersion=$(GIT_DESCRIBE)

clean: ## Clean up generated files
	@$(RM) -r coverage.xml .pytest_cache .scannerwork
