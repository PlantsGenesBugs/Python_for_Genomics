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

# "import sys" has to appear at the top of your programme file ("processfasta.py" in this instance). You can print out the arguments at any point in the program code by using print(sys.argv)
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

# To test if this works, you can edit the above code by adding "print(filename)" at the end. Then run the Python programme from the terminal as shown below and check that the output is "fasta.txt". The file fasta.txt is available in this repository

> python processfasta.py fasta.txt
#fasta.txt

# Also test that the IOError statement will work
> python processfasta.py smaug.txt
# File smaug.txt does not exist

    
# When using a function where some arguments are required and others are optional: the getopt module can help with arguments of sys.argv; note this is for running code/files from the COMMAND LINE

# Example: process FASTA sequences but only add those longer than 250 bp to the dictionary
>python processfasta.py -l 250 myfile.fa		# Running the programme "processing.py" on the file "myfile.fa" specifying a length argument of 250



















