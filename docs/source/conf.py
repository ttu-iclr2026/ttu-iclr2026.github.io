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

import datetime
from typing import List

try:
    import render_papers
    render_papers.main()
except Exception:
    print("Did not update papers.rst")

try:
    import pkg_resources
    print("\nPackage versions:")
    with open("../requirements.txt") as f:
        requirements = [line.strip() for line in f if line.strip()]
        for package in requirements:
            try:
                version = pkg_resources.get_distribution(package).version
                print(f"{package}: {version}")
            except pkg_resources.DistributionNotFound:
                print(f"{package}: Not installed")
except Exception as e:
    print(f"Could not print package versions: {e}")



def get_years(start_year=2021):
    year = datetime.datetime.now().year
    if year > start_year:
        return f"{start_year} - {year}"
    else:
        return f"{year}"


# -- Project information -----------------------------------------------------

project = "2nd Workshop on Test-Time Adaptation: Putting Updates to the Test! (PUT)"
author = "The organizing team"
copyright = f"{get_years(2024)}, {author}"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "numpy": (" https://numpy.org/doc/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
    "torchvsion": ("https://pytorch.org/vision/stable/", None),
    "python": ("https://docs.python.org/3", None),
}

# ignore link checks for generic types/TypeVars
nitpick_ignore = [("py:class", "T")]

coverage_show_missing_items = True

# Config is documented here:
# https://sphinx-copybutton.readthedocs.io/en/latest/
copybutton_prompt_text = r">>> |\$ "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True
autodoc_member_order = "bysource"

typehints_defaults = "comma"
always_document_param_types = True
simplify_optional_unions = True


templates_path = ["_templates"]

exclude_patterns: List[str] = []

html_theme = "pydata_sphinx_theme"

# https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html
html_theme_options = {
    "logo": {
        "text": "PUT 2025",
       #  "image_light": "logo.png",
        # "image_dark": "_static/logo-dark.png",
    },
    "nosidebar": True,
    "icon_links": [
        {
            "name": "Contact us!",
            "url": "mailto:tta_icml25@googlegroups.com",
            "icon": "fas fa-envelope",
        },
    ],
    "external_links": [
    ],
    "collapse_navigation": False,
    "navigation_depth": 4,
    "navbar_align": "content",
    "show_prev_next": False,
}

# TODO(stes): Replace with workshop logo
#html_logo = "logo.png"

# Remove the search field for now
html_sidebars = {"**" : []}  # Empty dictionary to remove all sidebars

html_show_sourcelink = False

# Disable links for embedded images
html_scaled_image_link = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

add_function_parentheses = False
