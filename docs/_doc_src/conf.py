# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or classes to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import pydata_sphinx_theme
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
sys.path.append(os.path.abspath("./_doc_ext"))


with open("../../unifhy/version.py") as fv:
    exec(fv.read())

# -- Project information -----------------------------------------------------
project = "unifhy"
copyright = "2020-{}, UK Centre for Ecology & Hydrology".format(datetime.now().year)
author = "Thibault Hallouin; Matt Brown"

# The full version, including alpha/beta/rc tags
if os.getenv("VERSION_RELEASE"):
    release = f"v{__version__}"
    version = f"v{__version__}"
else:
    release = "latest"
    version = "latest"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx_panels",
    # internal extensions
    "autocomponent",
]

# Boolean indicating whether to scan all found documents for
# autosummary directives, and to generate stub pages for each
# (http://sphinx-doc.org/latest/ext/autosummary.html)
autosummary_generate = True

# Both the class’ and the __init__ method’s docstring are concatenated
# and inserted.
autoclass_content = "both"

# This value selects how automatically documented members are sorted
# (http://sphinx-doc.org/latest/ext/autodoc.html)
autodoc_member_order = "groupwise"

# This value is a list of autodoc directive flags that should be
# automatically applied to all autodoc
# directives. (http://sphinx-doc.org/latest/ext/autodoc.html)
autodoc_default_flags = ["members", "inherited-members", "show-inheritance"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["../_doc_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["Thumbs.db", ".DS_Store"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all
# description unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in
# the output. They are ignored by default.
show_authors = False

# The default language to highlight source code
highlight_language = "python"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../_doc_static", "../_doc_img"]

# Output file base name for HTML help builder.
htmlhelp_basename = "unifhydoc"

# Paths (filenames) here must be relative to (under) html_static_path as above:
html_css_files = ["custom.css", "my_pygments_light.css", "my_pygments_dark.css"]

# Custom sidebar templates, maps document names to template names.
html_sidebars = {}

html_baseurl = "https://unifhy-org.github.io/unifhy"

html_favicon = "../_doc_img/favicon.ico"

html_permalinks_icon = '<span class="fa fa-link">'

html_theme_options = {
    "logo": {
        "image_light": "logo_light.svg",
        "image_dark": "logo_dark.svg",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/unifhy-org/unifhy",
            "icon": "fab fa-github",
        }
    ],
    "show_prev_next": False,
    "navbar_align": "content",
    "navbar_start": ["navbar-logo", "version-switcher"],
    # "navbar_center": ["navbar-nav", "navbar-version"],  # Just for testing
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "left_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    # "footer_items": ["copyright", "sphinx-version", ""]
    "switcher": {
        "json_url": f"{html_baseurl}/_static/switcher.json",
        "version_match": version,
    },
}

# If not '', a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page
# names to template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

html_show_sourcelink = False

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://docs.scipy.org/doc/numpy", None),
    "cf": ("https://ncas-cms.github.io/cf-python", None),
    "cftime": ("https://unidata.github.io/cftime", None),
    "cfunits": ("https://ncas-cms.github.io/cfunits", None),
}

intersphinx_cache_limit = 5

# prolog is a string added to every RST file
# used here to define a Python role 'globally'
rst_prolog = """
.. role:: py(code)
   :language: python
   :class: highlight
"""

# -- Options for sphinx-panels extension -------------------------------------

panels_add_bootstrap_css = False
