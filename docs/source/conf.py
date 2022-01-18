# .. hikari-expo documentation master file, created by
#   sphinx-quickstart on Tue Jan 18 11:57:30 2022.

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("..."))
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("./extensions"))


# -- Project information -----------------------------------------------------

project = "hikari-expo"
copyright = "2022, VincentRPS"
author = "VincentRPS"

# The full version, including alpha/beta/rc tags
release = "1.1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "resourcelinks",
]

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.\n\n
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

html_theme_options = {
    "sidebar_hide_name": True,
}
html_favicon = "_static/hikari-expo.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

resource_links = {
    "discord": "https://discord.gg/3kDAzaM36b",
    "issues": "https://github.com/VincentRPS/hikari-expo/issues",
    # "examples": f"https://github.com/VincentRPS/hikari-expo/tree/{branch}/examples",
}

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
}