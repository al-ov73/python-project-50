from gendiff import generate_diff
import pytest


test_cases_stylish = [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
     'tests/fixtures/right.json'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml',
     'tests/fixtures/right.json'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
     'tests/fixtures/right.json'),
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json',
     'tests/fixtures/right_2.json'),
    ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml',
     'tests/fixtures/right_2.json'),
]

test_cases_plain = [
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json',
     'tests/fixtures/right_plain.json'),
]

test_cases_json = [
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json',
     'tests/fixtures/right_json.json'),
]


@pytest.mark.parametrize('x, y, out', test_cases_stylish)
def test_generate_diff_stylish(x, y, out):
    expected = open(out).read()
    assert generate_diff(x, y, 'stylish') == expected


@pytest.mark.parametrize('x, y, out', test_cases_plain)
def test_generate_diff_plain(x, y, out):
    expected = open(out).read()
    assert generate_diff(x, y, 'plain') == expected


@pytest.mark.parametrize('x, y, out', test_cases_json)
def test_generate_diff_json(x, y, out):
    expected = open(out).read()
    assert generate_diff(x, y, 'json') == expected
