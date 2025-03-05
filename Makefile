uv run gendiff -h:
	uv run python -m gendiff.scripts.gendiff -h

lint:
	uv run ruff check
