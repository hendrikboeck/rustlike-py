import os
import sys

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rusttypes'
copyright = '2024, Hendrik Böck <hendrikboeck.dev@protonmail.com>'
author = 'Hendrik Böck <hendrikboeck.dev@protonmail.com>'
release = '0.1.0'
html_title = f"{project} {release}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'qiskit_sphinx_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'qiskit-ecosystem'
html_static_path = ['_static']

html_theme_options = {
    "disable_ecosystem_logo": True,
}
