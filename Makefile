.PHONY: install lint format typecheck test all

install:
	uv pip install -r requirements.txt

lint:
	ruff check app/ --fix

format:
	black app/

typecheck:
	mypy app/

test:
	pytest -v tests/

all: format lint typecheck