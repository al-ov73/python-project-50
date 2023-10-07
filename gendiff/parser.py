import json
import yaml
from yaml import CLoader as Loader


def parse(data, format):
    if format == 'json':
        with open(data) as f:
            return json.load(f)
    elif format == 'yaml':
        with open(data) as f:
            return yaml.load(f, Loader=Loader)
    elif format == 'url':
        return json.loads(data)
