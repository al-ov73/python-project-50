import json
from gendiff import generate_diff


x = json.load(open('./tests/json_files/file1.json'))
y = json.load(open('./tests/json_files/file2.json'))
expected = json.load(open('./tests/json_files/right.json'))


def test_generate_diff(x, y):
    assert generate_diff(x, y) == expected
