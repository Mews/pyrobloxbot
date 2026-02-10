import importlib.metadata

metadata = importlib.metadata.metadata("pyrobloxbot")

project = "pyrobloxbot"
copyright = "2026, Mews"
author = "Mews"
release = metadata["Version"]

extensions = ["myst_parser", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns = []  # type: ignore[var-annotated]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
}
