# Defining modules and packages
# Modules - a way to put functions together in a file (.py); related code is grouped into a module

# Example: put the reverse-complement function created in Lecture 5.3 into a module called dnautil.py
# To use the module, import it using the import statement

import dnautil
dnautil.reversecomp("GTAC")
#"GTAC"


# module has to be in the working directory (or provide a path)
# Use sys.path variable from the sys built-in module to check list of all directories where Python looks for files

import sys
sys.path

# Extending the Search Path (if the sys.path variable doesn't point to the directory where your module is saved)
sys.path.append("/Users/myname/Courses/Python")

#To use a function in a module, you have to specify WHERE that function is by calling the module as well
# When working from terminal, first go to the directory that holds the module
# Then run Python
import dnautil
dna = "aatggc"
dnautil.reversecomp(dna)
#'gccatt'

# You don't have to use the module name if you use the from statement; specify a function or use * to import all
from dnautil import *
reversecomp(dna)
#'gccatt'

# Specify one or more functions to avoid importing the same function more than once when it is included in several modules


# Packages are groups of modules
# Packages use dotted module names, e.g. module A.B refers to submodule B in package A
# Each package in Python is a directory that MUST contain a special file called __init__.py
# __init__.py can be empty - it simply indicates that the directory it contains is a Python package so it can be imported like a module

# Example
# dnautil.py is a file containing dna related functions
# rnautil.py is a file containing rna related functions
# proetinutil.py is a file containing protein related functions
# You want to group them together in a package called bioseq which processes all types of biological data

# Possible structure for the above package:

bioseq/
  __init__.py
  dnautil.py
  rnautil.py
  proteinutil.py
  ...

# Can also have submodules
# To load packages
import bioseq.dnautil                     # must use bioseq.dnautil.reversecomp(dna)
from bioseq import dnautil                # must use dnautil.reversecomp(dna)
from bioseq.dnautil import reversecomp    # must use reversecomp(dna)


