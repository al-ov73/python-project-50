import json
import yaml
from yaml import CLoader


def parse(data, format):
    if format == 'json':
        print(data)
        return json.loads(data)
    elif format == 'yaml':
        return yaml.load(data, Loader=CLoader)
