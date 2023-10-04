from gendiff import generate_diff


def test_generate_diff_json():
    x = 'tests/fixtures/file1.json'
    y = 'tests/fixtures/file2.json'
    expected = open('tests/fixtures/right.json').read()
    assert generate_diff(x, y, 'stylish') == expected


def test_generate_diff_jml():
    x = 'tests/fixtures/file1.yml'
    y = 'tests/fixtures/file2.yml'
    expected = open('tests/fixtures/right.json').read()
    assert generate_diff(x, y, 'stylish') == expected


def test_generate_diff_jaml():
    x = 'tests/fixtures/file1.yaml'
    y = 'tests/fixtures/file2.yaml'
    expected = open('tests/fixtures/right.json').read()
    assert generate_diff(x, y, 'stylish') == expected


def test_generate_diff_jml_2():
    x = 'tests/fixtures/file3.yml'
    y = 'tests/fixtures/file4.yml'
    expected = open('tests/fixtures/right_2.json').read()
    assert generate_diff(x, y, 'stylish') == expected


def test_generate_diff_json_2():
    x = 'tests/fixtures/file3.json'
    y = 'tests/fixtures/file4.json'
    expected = open('tests/fixtures/right_2.json').read()
    assert generate_diff(x, y, 'stylish') == expected


def test_generate_diff_json_plain():
    x = 'tests/fixtures/file3.json'
    y = 'tests/fixtures/file4.json'
    expected = open('tests/fixtures/right_plain.json').read()
    assert generate_diff(x, y, 'plain') == expected


def test_generate_diff_json_json():
    x = 'tests/fixtures/file3.json'
    y = 'tests/fixtures/file4.json'
    expected = open('tests/fixtures/right_json.json').read()
    assert generate_diff(x, y, 'json') == expected
