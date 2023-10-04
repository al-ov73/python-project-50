gendiff-install:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff-stylish1:
	gendiff -f stylish tests/fixtures/file1.json tests/fixtures/file2.json

gendiff-stylish2:
	gendiff -f stylish tests/fixtures/file3.json tests/fixtures/file4.json

gendiff-yml:
	gendiff -f stylish tests/fixtures/file1.yml tests/fixtures/file2.yml

gendiff-yml2:
	gendiff -f stylish tests/fixtures/file3.yml tests/fixtures/file4.yml

gendiff-plain1:
	gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json

gendiff-plain2:
	gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.json

gendiff-json1:
	gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json

gendiff-json2:
	gendiff -f json tests/fixtures/file3.json tests/fixtures/file4.json

run-json:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json

run-json2:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file3.json tests/fixtures/file4.json

run-json3:
	poetry run python -m gendiff.scripts.gendiff -f json tests/fixtures/file3.json tests/fixtures/file4.json

run-plain:
	poetry run python -m gendiff.scripts.gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.json

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
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml