# How to retrieve data from a dictionary that you built:

# Remember the .keys() and .values() methods from lecture 3.2
# Can also retrieve key + value using .items() method and looping through the whole dictionary

for name, seq in seqs.items():
    print(name, seq)            # Because my example file has large sequences, this comes out as a very big block of data!

# To run a python programme ("processfasta.py") on a specific file ("myfile.fa") from the terminal
>python processfasta.py myfile.fa

# The arguments of the above command are stored in the sys module's argv attributes as a list:
import sys
print(sys.argv)

# import sys at the top of your programme file. You can print out the arguments at any point in the program code by using print(sys.argv)
#Example code:

#!/usr/bin/env python3
"""
processfasta.py builds a dictionary with all sequences from a FASTA file
"""

import sys
filename = sys.argv[1]		#sys.argv[0] will be processfasta.py; [1] is the file we give it

try:
	f = open(filename)
except IOError:
	print("File %s does not exist" % filename)		# Note usage of % operator

    
# When using a function where some arguments are required and others are optional: the getopt module can help with arguments of sys.argv; note this is for running code/files from the COMMAND LINE

# Example: process FASTA sequences but only add those longer than 250 bp to the dictionary
>processing.py -l 250 myfile.fa
















