import os
import re

import yaml.reader

root_dir = os.path.dirname(os.path.abspath(__file__))

# to enable emoji etc.
yaml.reader.Reader.NON_PRINTABLE = re.compile(
    '[^'
    '\x09\x0A\x0D\x20-\x7E\x85\xA0-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF'
    ']'
)


def read_yaml(filename):
    return yaml.load(open(filename, encoding='utf-8'), Loader=yaml.BaseLoader)


def write_yaml(filename, data):
    return yaml.dump(data, open(filename, 'w', encoding='utf-8'),
                     allow_unicode=True, sort_keys=False)
