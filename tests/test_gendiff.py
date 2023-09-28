from gendiff import generate_diff

def test_generate_diff_json():   
    x = 'tests/fixtures/file1.json'
    y = 'tests/fixtures/file2.json'
    expected = open('tests/fixtures/right.json')
    assert print(generate_diff(x, y)) == print(expected)

def test_generate_diff_jml():   
    x = 'tests/fixtures/file1.jml'
    y = 'tests/fixtures/file2.jml'
    expected = open('tests/fixtures/right.json')
    assert print(generate_diff(x, y)) == print(expected)
