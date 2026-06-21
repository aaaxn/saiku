.PHONY: install test format

install:
	uv sync

test:
	uv run pytest

format:
	uvx ruff format .
