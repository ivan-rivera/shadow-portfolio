.PHONY: install
install:
	uv sync --all-groups

.PHONY: lint
lint:
	uv run pre-commit run --all-files

.PHONY: test
test:
	uv run pytest tests/ -v --cov=portfolio --cov-report=term-missing

.PHONY: coverage
coverage:
	uv run coverage run -m pytest tests/ -v --cov=portfolio --cov-report=html

.PHONY: version-check
version-check:
	uv run cz bump --dry-run
