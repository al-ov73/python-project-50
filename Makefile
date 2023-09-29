gen-diff-json:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl
	gendiff tests/fixtures/file1.json tests/fixtures/file2.json

gen-diff-yaml:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl
	gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

run-json:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json

run-yaml:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml

lint:
	poetry run flake8 gendiff

install:
	poetry install

check: selfcheck test lint

selfcheck:
	poetry check

test:
	poetry run pytest -v

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml