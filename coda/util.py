import os

import yaml

root_dir = os.path.dirname(os.path.abspath(__file__))


def read_yaml(filename):
    yaml.load(open(filename), Loader=yaml.BaseLoader)
