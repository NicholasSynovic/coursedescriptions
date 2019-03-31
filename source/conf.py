# -*- coding: utf-8 -*-
#
# LUC LUC CS Loyola Chicago CS Academic Programs build configuration file, created by
# sphinx-quickstart on Sat Feb  2 23:37:32 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# Additional definitions

rst_epilog = """

.. |math100| replace:: `MATH 100: Intermediate Algebra <http://luc.edu/math/academics/courses/math100/index.shtml>`__

.. |math117| replace:: `MATH 117: College Algebra <http://luc.edu/math/academics/courses/math117/index.shtml>`__

.. |math118| replace:: `MATH 118: Precalculus <http://luc.edu/math/academics/courses/math118/index.shtml>`__

.. |math131| replace:: `MATH 131: Applied Calculus I <http://luc.edu/math/academics/courses/math131/index.shtml>`__

.. |math132| replace:: `MATH 132: Applied Calculus II <http://luc.edu/math/academics/courses/math132/index.shtml>`__

.. |math161| replace:: `MATH 161: Calculus I <http://luc.edu/math/academics/courses/math161/index.shtml>`__

.. |math162| replace:: `MATH 162: Calculus II <http://luc.edu/math/academics/courses/math162/index.shtml>`__

.. |math201| replace:: `MATH 201: Elementary Number Theory <http://luc.edu/math/academics/courses/math201/index.shtml>`__

.. |math212| replace:: `MATH 212: Linear Algebra <http://luc.edu/math/academics/courses/math212/index.shtml>`__

.. |math215| replace:: `MATH 215: Object Oriented Math Programming <http://luc.edu/math/academics/courses/math215/index.shtml>`__

.. |math263| replace:: `MATH 263: Multivariable Calculus <http://luc.edu/math/academics/courses/math263/index.shtml>`__

.. |math264| replace:: `MATH 264: Ordinary Differential Equations <http://luc.edu/math/academics/courses/math264/index.shtml>`__

.. |math304| replace:: `MATH 304: Probability and Statistics I <http://luc.edu/math/academics/courses/math304/index.shtml>`__

.. |math309| replace:: `MATH 309: Numerical Methods <http://luc.edu/math/academics/courses/math309/index.shtml>`__

.. |math313| replace:: `MATH 313: Abstract Algebra <http://luc.edu/math/academics/courses/math313/index.shtml>`__

.. |math314| replace:: `MATH 314: Advanced Topics in Abstract Algebra <http://luc.edu/math/academics/courses/math314/index.shtml>`__

.. |math315| replace:: `MATH 315: Advanced Topics in Linear Algebra <http://luc.edu/math/academics/courses/math315/index.shtml>`__

.. |math328| replace:: `MATH 328: Algebraic Coding Theory <http://luc.edu/math/academics/courses/math328/index.shtml>`__

.. |math331| replace:: `MATH 331: Cryptography <http://luc.edu/math/academics/courses/math331/index.shtml>`__

.. |math351| replace:: `MATH 351: Introduction to Real Analysis I <http://luc.edu/math/academics/courses/math351/index.shtml>`__

.. |math352| replace:: `MATH 352: Introduction to Real Analysis II <http://luc.edu/math/academics/courses/math352/index.shtml>`__

.. |math353| replace:: `MATH 353: Introductory Complex Analysis <http://luc.edu/math/academics/courses/math353/index.shtml>`__

.. |math409| replace:: `MATH 409: Advanced Numerical Anaylsis <http://luc.edu/math/academics/courses/math409/index.shtml>`__

.. |math428| replace:: `MATH 428: Algebraic Coding Theory <http://luc.edu/math/academics/courses/math428/index.shtml>`__

.. |stat103| replace:: `STAT 103: Fundamentals of Statistics <http://www.luc.edu/math/academics/courses/stat103/>`__

.. |stat203| replace:: `STAT 203: Statistics <http://luc.edu/math/academics/courses/stat203/index.shtml>`__

.. |stat304| replace:: `STAT 304: Probability and Statistics I <http://luc.edu/math/academics/courses/stat304/index.shtml>`__

.. |phil120| replace:: `PHIL 120 <http://luc.edu/philosophy/coursedescriptions.shtml>`__

.. |phys112| replace:: `PHYS 112: College Physics II <http://www.luc.edu/physics/courses.shtml#112>`__

.. |phys125| replace:: `PHYS 125: General Physics I <http://www.luc.edu/physics/courses.shtml#125>`__

.. |phys126| replace:: `PHYS 126: General Physics II <http://www.luc.edu/physics/courses.shtml#126>`__

.. |phys135| replace:: `PHYS 135: General Physics Lab I <http://www.luc.edu/physics/courses.shtml#135>`__

.. |phys136| replace:: `PHYS 136: General Physics Lab II <http://www.luc.edu/physics/courses.shtml#136>`__

.. |phys235| replace:: `PHYS 235: Modern Physics <http://www.luc.edu/physics/courses.shtml#235>`__

.. |phys237| replace:: `PHYS 237: Modern Physics Lab <http://www.luc.edu/physics/courses.shtml#237>`__

.. |phys266| replace:: `PHYS 266: Digital Electronics Laboratory <http://www.luc.edu/physics/courses.shtml#266>`__

.. |phys303| replace:: `PHYS 303: Electronics I <http://www.luc.edu/physics/courses.shtml#303>`__

.. |phys310| replace:: `PHYS 310: Optics <http://www.luc.edu/physics/courses.shtml#310>`__

.. |phys314| replace:: `PHYS 314: Theoretical Mechanics I <http://www.luc.edu/physics/courses.shtml#314>`__

.. |phys328| replace:: `PHYS 328: Thermal Physics & Statistical Mechanics <http://www.luc.edu/physics/courses.shtml#328>`__

.. |phys351| replace:: `PHYS 351: Electricity & Magnetism I <http://www.luc.edu/physics/courses.shtml#351>`__

.. |biol101| replace:: `BIOL 101: General Biology I <http://luc.edu/biology/bsinbiology/courseofferings/>`__

.. |biol282| replace:: `BIOL 282: Genetics <http://luc.edu/biology/bsinbiology/courseofferings/>`__

.. |biol388| replace:: `BIOL 388: Bioinformatics <http://luc.edu/biology/bsinbiology/courseofferings/>`__

.. |engl210| replace:: `ENGL 210: Business Writing <http://luc.edu/english/courses.shtml/>`__

.. |isscm241| replace:: `ISSCM 241: Business Statistics <http://www.luc.edu/quinlan/undergraduate/informationsystems/information_systems_courses.shtml>`__

.. |psyc101| replace:: `PSYC 101: General Psychology <http://www.luc.edu/psychology/course_offerings.shtml#d.en.76692>`__

.. |psyc304| replace:: `PSYC 304: Statistics <http://www.luc.edu/psychology/course_offerings.shtml#d.en.76692>`__

.. |cjc102| replace:: `CJC 101: The Criminal Justice System <http://www.luc.edu/criminaljustice/undergradcourses.shtml>`__

.. |cjc322| replace:: `CJC 322: Criminal Courts and Law <http://www.luc.edu/criminaljustice/undergradcourses.shtml>`__

.. |cjc323| replace:: `CJC 323: Criminal Procedure <http://www.luc.edu/criminaljustice/undergradcourses.shtml>`__

"""

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.mathjax']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Loyola Chicago CS Academic Programs'
copyright = u'2018, CS Department'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = os.environ.get("BOOK_VERSION", "beta")
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_context = {
            'css_files': [
                    '_static/theme_overrides.css',  # override wide tables in RTD theme
            ],
}



# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['../../themes']
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "LUC CS Loyola Chicago CS Academic Programs"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'LoyolaComputerScienceAcademicProgramsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'LoyolaComputerScienceAcademicPrograms.tex', u'LUC CS Loyola Chicago CS Academic Programs',
   u'CS Department', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'loyolauniversitychicagocomputerscience-Coursehandbook', u'LUC CS Loyola Chicago CS Academic Programs',
     [u'CS Department'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'LoyolaComputerScienceAcademicPrograms', u'LUC CS Loyola Chicago CS Academic Programs',
   u'CS Department', 'LoyolaComputerScienceAcademicPrograms', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'LUC CS Loyola Chicago CS Academic Programs'
epub_author = u'CS Department'
epub_publisher = u'CS Department'
epub_copyright = u'2018, CS Department'
epub_basename = 'LoyolaComputerScienceAcademicPrograms'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True
