.PHONY: install lint format typecheck test all

install:
	uv pip install -r requirements.txt

lint:
	ruff check mentest/ --fix

format:
	black mentest/

typecheck:
	mypy mentest/

test:
	pytest -v tests/

all: format lint typecheck