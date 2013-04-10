import sys, os

# -- General configuration -----------------------------------------------------

sys.path.append(os.path.abspath('../_sphinx/exts'))
extensions = ['sphinx.ext.todo', 'includecode']
templates_path = ['_templates']

source_suffix = '.rst'
source_encoding = 'utf-8'
master_doc = 'index'
exclude_patterns = []

project = u'Eventsourced'
copyright = u'2012-2013 Eventsourced'
version = '@version@'
release = '@version@'

highlight_language = 'scala'

pygments_style = 'simple'
add_function_parentheses = False
show_authors = True

# -- Options for HTML output ---------------------------------------------------

html_theme = 'eventsourced'
html_theme_path = ['../_sphinx/themes']
html_title = u'Eventsourced'
html_favicon = None
html_static_path = ['../_sphinx/static']

html_last_updated_fmt = '%b %d, %Y'
html_use_smartypants = False
html_add_permalinks = None
html_copy_source = False

todo_include_todos = True

html_domain_indices = False
html_use_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
#htmlhelp_basename = 'Akkadoc'