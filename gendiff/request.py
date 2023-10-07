import requests


def request_data(path_to_file):
    if path_to_file[:4] == 'http':
        r = requests.get(path_to_file)
        return r.text, 'url'
    elif path_to_file.split('.')[-1] == 'json':
        return path_to_file, 'json'
    elif (
        path_to_file.split('.')[-1] == 'yaml'
        or path_to_file.split('.')[-1] == 'yml'
    ):
        return path_to_file, 'yaml'
