from gendiff import generate_diff

def test_generate_diff():   
    x = 'tests/fixtures/file1.json'
    y = 'tests/fixtures/file2.json'
    expected = open('tests/fixtures/right.json')
    assert print(generate_diff(x, y)) == print(expected)
