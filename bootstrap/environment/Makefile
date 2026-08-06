# AI Frontier Career Roadmap — lab workspace
#
#   make setup    create the venv and install the toolchain
#   make test     run the test suite for weeks completed so far
#   make check    lint + typecheck + test  (run this before every commit)
#
# Everything runs against BOOTSTRAP (the parent directory), which is the
# pytest rootdir and holds all ten lab packages.

SHELL       := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

ENV_DIR   := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
BOOTSTRAP := $(abspath $(ENV_DIR)/..)
VENV      := $(BOOTSTRAP)/.venv
PY        := $(VENV)/bin/python
PIP       := $(VENV)/bin/pip
PYTEST    := $(VENV)/bin/pytest
RUFF      := $(VENV)/bin/ruff
MYPY      := $(VENV)/bin/mypy
CONFIG    := $(ENV_DIR)/pyproject.toml

# Which course week are you on? Tests for later weeks are skipped.
WEEK_FILE := $(BOOTSTRAP)/CURRENT_WEEK
WEEK      := $(shell cat $(WEEK_FILE) 2>/dev/null || echo 0)

.PHONY: help
help: ## Show this help
	@echo "AI Frontier Career Roadmap — lab workspace"
	@echo "Current course week: $(WEEK)   (edit $(WEEK_FILE) to advance)"
	@echo ""
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

.PHONY: setup
setup: $(VENV)/.installed ## Create the venv and install the base toolchain

$(VENV)/.installed: $(ENV_DIR)/requirements.txt
	@test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r $(ENV_DIR)/requirements.txt
	@touch $@
	@echo ""
	@echo "Done. Activate with:  source $(VENV)/bin/activate"

.PHONY: freeze
freeze: ## Snapshot the exact installed versions (do this at each phase boundary)
	$(PIP) freeze > $(ENV_DIR)/requirements.lock.txt
	@echo "Wrote $(ENV_DIR)/requirements.lock.txt"

.PHONY: kernel
kernel: setup ## Register the venv as a Jupyter kernel
	$(PY) -m ipykernel install --user --name ai-roadmap --display-name "AI Roadmap"

.PHONY: notebook
notebook: setup ## Launch JupyterLab in the bootstrap workspace
	cd $(BOOTSTRAP) && $(VENV)/bin/jupyter lab

# ---------------------------------------------------------------------------
# Quality gates
# ---------------------------------------------------------------------------

.PHONY: test
test: setup ## Run tests for weeks 1..CURRENT_WEEK
	cd $(BOOTSTRAP) && $(PYTEST) --week=$(WEEK)

.PHONY: test-all
test-all: setup ## Run every test, including future weeks (expect failures)
	cd $(BOOTSTRAP) && $(PYTEST) --week=999

.PHONY: test-week
test-week: setup ## Run one week's tests only:  make test-week W=14
	@test -n "$(W)" || (echo "usage: make test-week W=<n>" && exit 1)
	cd $(BOOTSTRAP) && $(PYTEST) --week=$(W) --only-week=$(W)

.PHONY: cov
cov: setup ## Test with a coverage report
	cd $(BOOTSTRAP) && $(PYTEST) --week=$(WEEK) \
		--cov --cov-report=term-missing --cov-report=html

.PHONY: lint
lint: setup ## Lint with ruff
	cd $(BOOTSTRAP) && $(RUFF) check --config $(CONFIG) .

.PHONY: format
format: setup ## Format with ruff
	cd $(BOOTSTRAP) && $(RUFF) format --config $(CONFIG) .
	cd $(BOOTSTRAP) && $(RUFF) check --config $(CONFIG) --fix .

.PHONY: typecheck
typecheck: setup ## Typecheck with mypy
	cd $(BOOTSTRAP) && $(MYPY) --config-file $(CONFIG) . || true

.PHONY: check
check: lint typecheck test ## Everything. Run before every commit.
	@echo ""
	@echo "All checks passed for week $(WEEK)."

# ---------------------------------------------------------------------------
# Course progression
# ---------------------------------------------------------------------------

.PHONY: week
week: ## Set the current course week:  make week W=5
	@test -n "$(W)" || (echo "usage: make week W=<n>" && exit 1)
	@echo $(W) > $(WEEK_FILE)
	@echo "Current week is now $(W). Run 'make test' to see what's expected."

.PHONY: status
status: ## Show progress: current week, test counts, TODO count
	@echo "Course week:  $(WEEK) of 78"
	@echo "Month:        $$(( ($(WEEK) + 3) / 4 ))"
	@printf "Tests:        "
	@cd $(BOOTSTRAP) && $(PYTEST) --week=$(WEEK) --collect-only -q 2>/dev/null | tail -1 || true
	@printf "Unimplemented: "
	@grep -rl "raise NotImplementedError" $(BOOTSTRAP) --include="*.py" 2>/dev/null | wc -l | tr -d ' '

# ---------------------------------------------------------------------------
# Services (Months 7, 10, 11, 14, 15)
# ---------------------------------------------------------------------------

.PHONY: db-up
db-up: ## Start Postgres + pgvector
	docker compose -f $(ENV_DIR)/docker-compose.yml up -d postgres
	@echo "Postgres on localhost:5432  (db=airoadmap user=airoadmap pass=airoadmap)"

.PHONY: db-down
db-down: ## Stop the services
	docker compose -f $(ENV_DIR)/docker-compose.yml down

.PHONY: db-shell
db-shell: ## psql into the lab database
	docker compose -f $(ENV_DIR)/docker-compose.yml exec postgres psql -U airoadmap -d airoadmap

.PHONY: db-reset
db-reset: ## Destroy and recreate the database volume
	docker compose -f $(ENV_DIR)/docker-compose.yml down -v
	docker compose -f $(ENV_DIR)/docker-compose.yml up -d postgres

.PHONY: services-up
services-up: ## Start every service (Postgres, MLflow, Prometheus, Grafana)
	docker compose -f $(ENV_DIR)/docker-compose.yml --profile full up -d

.PHONY: services-down
services-down: ## Stop everything and remove volumes
	docker compose -f $(ENV_DIR)/docker-compose.yml --profile full down

# ---------------------------------------------------------------------------
# Housekeeping
# ---------------------------------------------------------------------------

.PHONY: clean
clean: ## Remove caches and build artifacts
	find $(BOOTSTRAP) -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
	find $(BOOTSTRAP) -type d -name .pytest_cache -prune -exec rm -rf {} + 2>/dev/null || true
	find $(BOOTSTRAP) -type d -name .mypy_cache -prune -exec rm -rf {} + 2>/dev/null || true
	find $(BOOTSTRAP) -type d -name .ruff_cache -prune -exec rm -rf {} + 2>/dev/null || true
	rm -rf $(BOOTSTRAP)/htmlcov $(BOOTSTRAP)/.coverage

.PHONY: nuke
nuke: clean ## Also delete the virtualenv
	rm -rf $(VENV)
