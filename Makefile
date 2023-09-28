gen-diff:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl
	gendiff tests/json_files/file1.json tests/json_files/file2.json

run:
	poetry run python -m gendiff.scripts.gendiff tests/json_files/file1.json tests/json_files/file2.json

lint:
	poetry run flake8 gendiff

report:
	./gradlew jacocoTestReport