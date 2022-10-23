# Defining modules and packages
# Modules - a way to put functions together in a file (.py); related code is grouped into a module

# Example: put the reverse-complement function created in Lecture 5.3 into a module called dnautil.py
# To use the module, import it using the import statement

import dnautil

# module has to be in the working directory (or provide a path)
# Use sys.path variable from the sys built-in module to check list of all directories where Python looks for files

import sys
sys.path

# Extending the Search Path


