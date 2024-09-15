# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'slides'
copyright = '2024, Sousuke NAKAMURA'
author = 'Sousuke NAKAMURA'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx_revealjs'
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['custom.css',]   

revealjs_static_path = ["_static"]

revealjs_script_conf = {
    'revealjs_use_index': True,
}
revealjs_style_theme = 'solarized'

revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
]
revealjs_css_files = [
    'custom.css',
    'revealjs/plugin/highlight/zenburn.css',
    # 'https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/style.css',
]
# budoux_targets = ["h1", "h2", "h3"]
