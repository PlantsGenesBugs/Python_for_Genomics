#!/usr/bin/env python3

"""
processfasta.py builds a dictionary with all sequences from a FASTA file
"""
import getopt
import sys
filename = sys.argv[1]		#sys.argv[0] will be processfasta.py; [1] is the file we give it

try:
	f = open(filename)
except IOError:
	print("File %s does not exist" % filename)		# Note usage of % operator

print(filename)