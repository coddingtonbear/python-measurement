"""Sphinx configuration file."""
from pkg_resources import get_distribution

project = 'python-measurement'
copyright = '2013, Adam Coddington'
release = get_distribution('measurement').version
version = '.'.join(release.split('.')[:2])

master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
