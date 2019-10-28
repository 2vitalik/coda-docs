import yaml


def read_yaml(filename):
    yaml.load(open(filename), Loader=yaml.BaseLoader)
