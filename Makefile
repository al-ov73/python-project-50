gen-diff:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl
	gendiff tests/fixtures/file1.json tests/fixtures/file2.json

run:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json

lint:
	poetry run flake8 gendiff

install:
	poetry install

check: selfcheck test lint

selfcheck:
	poetry check

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml