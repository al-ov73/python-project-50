from gendiff import generate_diff

def test_generate_diff_json():   
    x = 'tests/fixtures/file1.json'
    y = 'tests/fixtures/file2.json'
    expected = open('tests/fixtures/right.json')
    assert print(generate_diff(x, y)) == print(expected)

def test_generate_diff_jml():   
    x = 'tests/fixtures/file1.yml'
    y = 'tests/fixtures/file2.yml'
    expected = open('tests/fixtures/right.json')
    assert print(generate_diff(x, y)) == print(expected)
    
def test_generate_diff_json_2():   
    x = 'tests/fixtures/file3.json'
    y = 'tests/fixtures/file4.json'
    expected = open('tests/fixtures/right_2.json')
    assert print(generate_diff(x, y)) == print(expected)
