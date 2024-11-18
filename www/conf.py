# -*- coding: utf-8 -*-
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import pathlib
import sys
import xarray
import datetime
import sphinx_autosummary_accessors

from contextlib import suppress
allowed_failures = set()

with suppress(ImportError):
    import matplotlib
    matplotlib.use('Agg')

autodoc_mock_imports = []
try:
    import cartopy  # noqa: F401
except ImportError:
    autodoc_mock_imports.append('cartopy')

# argopy_src = os.path.abspath('..')
# print("argopy loaded:", os.path.abspath('..'))
# sys.path.insert(0, os.path.abspath('..'))
root = pathlib.Path(__file__).absolute().parent.parent
os.environ["PYTHONPATH"] = str(root)
sys.path.insert(0, str(root))

import argopy  # noqa: E402
print("argopy: %s, %s" % (argopy.__version__, argopy.__file__))
# argopy.show_versions()
# argopy.show_options()

print("python exec:", sys.executable)
print("sys.path:", sys.path)

# -- General configuration ------------------------------------------------

ipython_warning_is_error = False

extensions = [
    # 'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram',
    'nbsphinx',
    'numpydoc',
    'sphinx_issues',
    'sphinx_autosummary_accessors',
    'sphinx_tabs.tabs',
    # 'sphinxcontrib.googleanalytics',
    'sphinxext.rediraffe',
    'sphinx_copybutton',
    'sphinx_design',
]

# sphinx_gallery_conf = {
#                        'expected_failing_examples': list(allowed_failures)
#                        }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', sphinx_autosummary_accessors.templates_path]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'argopy'
copyright = "2020-%s, Argopy Developers" % datetime.datetime.now().year
author = "Argopy Developers"
language = "en"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ".".join(argopy.__version__.split(".")[:2])
# The full version, including alpha/beta/rc tags.
release = argopy.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_templates',
                    '.ipynb_checkpoints', '_ext', '_src']

# Give *lots* of time for notebook cell execution!
# Note nbsphinx compiles *all* notebooks in docs unless excluded
nbsphinx_timeout = 60
nbsphinx_execute = "always"
# nbsphinx_prolog = """
# {% set docname = env.doc2path(env.docname, base=None) %}
# You can run this notebook in a `live session:
# <https://mybinder.org/v2/gh/euroargodev/argopy/docs/examples/master?urlpath=lab/tree/docs/{{ docname }}>`_ |Binder|
# or view it `on Github <https://github.com/euroargodev/argopy/blob/master-doc/docs/{{ docname }}>`_.
# .. |Binder| image:: https://mybinder.org/badge.svg
#    :target: https://mybinder.org/v2/gh/euroargodev/argopy/master-doc?urlpath=lab/tree/docs/{{ docname }}
# """

# sphinx-copybutton
copybutton_exclude = '.linenos, .gp, .go, .gh'


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'none'

# Create local pygments copies
# Previously used: https://github.com/richleland/pygments-css
# But do not want to depend on some random repository
from pygments.formatters import HtmlFormatter  # noqa: E402
from pygments.styles import get_all_styles  # noqa: E402
path = os.path.join('_static', 'pygments')
if not os.path.isdir(path):
    os.mkdir(path)
for style in get_all_styles():
    path = os.path.join('_static', 'pygments', style + '.css')
    if os.path.isfile(path):
        continue
    with open(path, 'w') as f:
        f.write(HtmlFormatter(style=style).get_style_defs('.highlight'))

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

autosummary_generate = True
numpydoc_class_members_toctree = True
numpydoc_show_class_members = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

html_context = {
    "github_user": "euroargodev",
    "github_repo": "argopy-5years",
    "github_version": "main",
    "doc_path": "www/_build/html",
    "default_mode": "light",
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    "custom.css"
]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/argopy_logo_5years.png"
html_favicon = '_static/argopy.ico'
html_title = "Celebrating argopy 5 years anniversary !"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sourcelink = False

# For sphinx_book_theme:
html_theme_options = {
    "repository_url": "https://www.github.com/euroargodev/argopy-5years",
    "collapse_navbar": False,
    "use_repository_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "use_download_button": False,
    "repository_branch": "main",
    "logo": {"image": html_logo,
             "alt_text": "argopy 5 years",
             },
    "show_nav_level": 2,  # https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/navigation.html#control-how-many-navigation-levels-are-shown-by-default
    'collapse_navigation': False,  # https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/navigation.html#remove-reveal-buttons-for-sidebar-items
    # "extra_footer": "<div>Hello world</div>",
}

# googleanalytics_id = 'G-C4MWDXYMXQ'
# googleanalytics_enabled = True

# Sometimes the savefig directory doesn't exist and needs to be created
# https://github.com/ipython/ipython/issues/8733
# becomes obsolete when we can pin ipython>=5.2; see doc/environment.yml
ipython_savefig_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   '_build', 'html', '_static')
if not os.path.exists(ipython_savefig_dir):
    os.makedirs(ipython_savefig_dir)

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'argopydoc'

# -- Options for Github ---------------------------------------
# GitHub repo
issues_github_path = "euroargodev/argopy-5years"

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'argopy', u'argopy Documentation',
     ["argopy Developers"], 1)
]

# ---------------------------------------
# configuration for sphinxext.opengraph
ogp_site_url = "https://github.com/euroargodev/argopy-5years"
ogp_image = "https://raw.githubusercontent.com/euroargodev/argopy/master/docs/_static/argopy_logo_long.png"

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'argopy', u'argopy Documentation',
     "argopy Developers", 'argopy', 'A python library for Argo data beginners and experts',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
#     'iris': ('https://scitools-iris.readthedocs.io/en/stable/', None),
#     'numpy': ('https://numpy.org/doc/stable/', None),
#     'numba': ('https://numba.readthedocs.io/en/stable/', None),
#     'matplotlib': ('https://matplotlib.org/stable/', None),
#     'xarray': ('https://docs.xarray.dev/en/stable/', None),
#     'dask': ('https://docs.dask.org/en/stable/', None),
#     'distributed': ('https://distributed.dask.org/en/stable/', None),
#     'dask_ml': ('https://ml.dask.org/', None),
#     'sklearn': ('https://scikit-learn.org/stable/', None),
#     'seaborn': ('https://seaborn.pydata.org/', None),
#     'fsspec': ('https://filesystem-spec.readthedocs.io/en/stable/', None),
#     'pyarrow': ('https://arrow.apache.org/docs/', None),
#     'IPython': ('https://ipython.readthedocs.io/en/stable/', None),
#     'virtualfleet': ('https://virtualfleet.readthedocs.io/en/latest/', None),
#     'boto3': ('https://boto3.amazonaws.com/v1/documentation/api/latest/', None),
#     's3fs': ('https://s3fs.readthedocs.io/en/latest/', None),
#     'kerchunk': ('https://fsspec.github.io/kerchunk/', None),
# }
