# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'netlify Sphinxデモ'
copyright = '2018, shimizukawa'
author = 'shimizukawa'
version = release = '1.0'


# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.coverage']
extensions.append('sphinx.ext.mathjax')
todo_include_todos = True

rst_prolog = """
.. meta::
   :viewport: width=device-width, initial-scale=1.0
"""

source_suffix = '.rst'
master_doc = 'index'
language = 'ja'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_logo = 'sphinx-logo.png'
html_theme_options = {
    #'logo': 'sphinx-logo.png',
    'github_user': 'shimizukawa',
    'github_repo': 'netlify-trying',
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

