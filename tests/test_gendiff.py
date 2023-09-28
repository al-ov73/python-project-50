from gendiff import generate_diff

def test_generate_diff():   
    x = 'tests/json_files/file1.json'
    y = 'tests/json_files/file2.json'
    expected = open('tests/json_files/right.json')
    assert print(generate_diff(x, y)) == print(expected)
