gen-diff:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl
	gendiff file1.json file2.json

run:
	poetry run python -m gendiff.scripts.gendiff gendiff/json_files/file1.json gendiff/json_files/file2.json