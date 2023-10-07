import requests


def request_data(path_to_file):
    extension = path_to_file.split('.')[-1]
    # json url
    if path_to_file[:4] == 'http' and extension == 'json':
        return requests.get(path_to_file).text, 'json'
    # json local
    elif extension == 'json':
        with open(path_to_file, 'r') as data:
            return data.read(), 'json'
    #yaml, yml url
    elif (path_to_file[:4] == 'http' 
        and (extension == 'yml' or extension == 'yaml')):
        r = requests.get(path_to_file)
        return r.text, 'yaml'
    #yaml, yml local
    elif extension == 'yaml' or extension == 'yml':
        with open(path_to_file, 'r') as data:
            return data.read(), 'yaml'
