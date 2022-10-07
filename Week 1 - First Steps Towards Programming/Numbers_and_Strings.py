#!/usr/bin/python

'''
The first line is the "shebang" line. It specifies how to run a script - in this instance, using python.
For more info, see http://stanford.edu/~jainr/basics.py 
'''

# Numbers
# Use Python as calculator

5+5
# 10

10.5-2*3
# 4.5

10**2
# Used to calculate powers so 100 in this case

17.0//3
# Floor division - discards fractional part, so 5.0 in this case

17%3
# Modulo operator - returns remainder after division


# Types of Numbers
type(5)
# type 'int'

# Integers, float (decimal point present), complex (e.g. 3+2j)
# Note, in Python 2 something like 12/5 = 2, because you have to specify that 12 is a float in order to obtain a float result
# So 12.0/5 = 2.4



# Strings
# Especially NB in genomics - strings of letters surrounded by quotes

"atg"
# 'atg'

"This is a codon"
# 'This is a codon' (string as single object)

# You can use the backslash to escape something Python would otherwise try to interpret
"To print something, use the instruction \"print\" "
# 'To print something, use the instruction "print" '


# Strings can span multiple lines. We can use triple quotes to break a long line into several lines, but these aren't interpreted as individual strings
"""ATGCCCGTCAT
TCGGTAGTC
ATGCTAAAGTGCGATATA
ATAGTGGGCAAT
"""
# 'ATGCCCGTCAT\nTCGGTAGTC\nATGCTAAAGTGCGATATA\nATAGTGGGCAAT\n'

# This is also a good way to add (very long) comments to your code
# without having to put a hash at the start of each line :)

# \n is shown in the above string to indicate line breaks
# These can be added to a string to add a line break; \t inserts a tab space, \\ inserts a backslash, \" inserts a quote

print("A\tGGG")
# A       GGG

# Can also remove escape characters in the above string by using print() function

 print("""\ATGCCCGTCAT
... TCGGTAGTC
... ATGCTAAAGTGCGATATA
... ATAGTGGGCAAT
... """)

# ATGCCCGTCAT
# TCGGTAGTC
# ATGCTAAAGTGCGATATA
# ATAGTGGGCAAT

# Basic string operators: + (concatenate), * (copy string/replicate),
# in (membership - true if first string exists inside second string given),
# not in (non-membership - true if first string does not exist in second string)


"atg" + "aattgtgct"
# 'atgaattgtgct'

"atg"*3
# 'atgatgatg'

"atg" in "cgtagtatgccc"
# True





