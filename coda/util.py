import os

import yaml

root_dir = os.path.dirname(os.path.abspath(__file__))


def read_yaml(filename):
    return yaml.load(open(filename, encoding='utf-8'), Loader=yaml.BaseLoader)
