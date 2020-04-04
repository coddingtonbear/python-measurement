"""Sphinx configuration file."""
import inspect

from pkg_resources import get_distribution

from measurement.base import AbstractMeasure

project = "python-measurement"
copyright = "2020, Johannes Hoppe"
release = get_distribution("measurement").version
version = ".".join(release.split(".")[:2])
html_theme = "python_docs_theme"

master_doc = "index"

html_logo = "caliper.svg"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx.ext.inheritance_diagram",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

inheritance_graph_attrs = dict(rankdir="TB")

graphviz_output_format = "svg"

autodoc_member_order = "bysource"


def process_measures(app, what, name, obj, options, lines):
    if inspect.isclass(obj) and issubclass(obj, AbstractMeasure):
        lines.append("**Supported Units:**")
        lines.extend(
            f"    :{obj._attr_to_unit(name)}: {', '.join(value.symbols)}"
            for name, value in obj._org_units.items()
        )
    return lines


def setup(app):
    app.connect("autodoc-process-docstring", process_measures)
