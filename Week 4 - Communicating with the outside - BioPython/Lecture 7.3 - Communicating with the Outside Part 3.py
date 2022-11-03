# How to retrieve data from a dictionary that you built:

# Remember the .keys() and .values() methods from lecture 3.2
# Can also retrieve key + value using .items() method and looping through the whole dictionary

for name, seq in seqs.items():
    print(name, seq)            # Because my example file has large sequences, this comes out as a very big block of data!

# To run a python programme ("processfasta.py") on a specific file ("myfile.fa") from the terminal --> note this is for running code/files from the COMMAND LINE
>python processfasta.py myfile.fa

# The arguments of the above command are stored in the sys module's argv attributes as a list:
import sys
print(sys.argv)

# "import sys" has to appear at the top of your programme file ("processfasta.py" in this instance). You can print out the arguments at any point in the program code by using print(sys.argv). However, the POINT is to have a way for the programme to ACCESS the specified values in the arguments in order to allow it to run (e.g. which file to open, which values to assign to variables in the function)
#Example code:

#!/usr/bin/env python3
"""
processfasta.py builds a dictionary with all sequences from a FASTA file
"""

import sys
filename = sys.argv[1]		#sys.argv[0] will be processfasta.py; [1] is the file we give it. This assigns the file's name to the appropriate variable.

try:
	f = open(filename)
except IOError:
	print("File %s does not exist" % filename)		# Note usage of % operator

# To test if this works, you can edit the above code by adding "print(filename)" at the end. Then run the Python programme from the terminal as shown below and check that the output is "fasta.txt". The file fasta.txt is available in this repository

print(filename)		# add this to above code and run as below

> python processfasta.py fasta.txt
#fasta.txt

# Also test that the IOError statement will work
> python processfasta.py smaug.txt
# File smaug.txt does not exist

    
# When using a function where some arguments are required and others are optional: the getopt module can help with arguments of sys.argv; 

# Example: process FASTA sequences but only add those longer than 250 bp to the dictionary
>python processfasta.py -l 250 myfile.fa		# Running the programme "processing.py" on the file "myfile.fa" specifying a length argument of 250, where 							   # the length argument is optional

# First you have to tell the programme what to do with the arguments that will be specified when executing the programme from the command line:

def usage():						# define a usage function that tells the user what the function does
	print("""processfasta.py reads FASTA files and builds a dictionary
	with all sequences bigger than a given length
	
	processfasta.py [-h] [-l <length>] <filename>		#[] mark optional arguments
	-h		print this message
	-l <length>	filter all sequences with a length smaller than <length> (default <length>=0)
	<filename>	the file has to be in FASTA format
	""")
	

# Now add all the appropriate code to the original function

#!/usr/bin/env python3

import sys
import getopt
def usage():
	print	("""
processfasta.py: reads a FASTA file and builds a dictionary with all sequences bigger than a given length

processfasta.py [-h] [-l <length>] <filename> #square brackets for optional args

-h		print this message
-l <length>	filter all sequences with a length smaller than <length> (default <length>=0)

<filename>	the file has to be in FASTA format
		""")

o, a = getopt.getopt(sys.argv[1:], "l:h")			# assign values to lists o and a (where o will be optional and a compulsory arguments)
								# The first argument of getopt method is ALL of the arguments to the original function (but we use
								# sys.argv[1:] to list all of the arguments excluding the function/programme name you have called
								# The second argument of the getopt method is ALL of the arguments the user can supply with a - 								# command (optional)
								# colon after an argument shows that the foregoing argument requires a number parameter
			
# Initialise dictionary (where you will put all of the above listed arguments in a name: value structure)
opts={}
seqlen=0

for k,v in o:					# name of arg = k, value assigned to arg = v
	opts[k]=v				# add the value v to the k'th name in the opts dictionary
if "-h" in opts.keys():				# after creating the dictionaty, if the user has specified -h (which will be present as a key in the dictionary, then 	      usage()				      # run the usage function defined earlier which prints out a description of the programme
	sys.exit()				# exit after printing help (quit programme without running anything else)
if len(a) < 1:					# if user has not specified anything after calling the programme	
	usage()					# initialise the usage function that will print out the message above; then close programme with message
	sys.exit("Input FASTA file is missing")
if "-l" in opts.keys():				# if the user has specified an optional length argument but it is shorter than 0, print out error and exit programme
	if int(opts["l"])<0:
		print("Length of sequence should be positive!")
		sys.exit(0)
	seqlen=opts["-l"]			# if the above returns a false value (sequence is longer than 0): assign the value next to the "-l" argument to the 						    # seqlen key	
		
# Note: the above code is available in a separate file in this repository for ease of use (getopt_example.py)	




















