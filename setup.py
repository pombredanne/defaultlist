"""collections.defaultdict equivalent implementation of list."""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path


def _read_metainfo(filepath):
    import re
    pat = re.compile(r"__(?P<name>[a-z_]+)__ = (?P<expr>.*)")
    metainfo = {}
    with open(filepath) as fh:
        for line in fh:
            match = pat.match(line)
            if match:
                metainfo[match.group("name")] = eval(match.group("expr"))
    return metainfo


config = _read_metainfo("defaultlist.py")
config['license'] = 'Apache 2.0'
config['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]
config['keywords'] = 'defaultlist list defaultdict collections'
config['py_modules'] = ['defaultlist']
config['extras_require'] = {
    'dev': ['check-manifest'],
    'test': ['coverage'],
}
config['test_suite'] = 'nose.collector'


# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    config['long_description'] = f.read()

setup(**config)
