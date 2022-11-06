# How to retrieve data from a dictionary that you built:

# Remember the .keys() and .values() methods from lecture 3.2
# Can also retrieve key + value using .items() method and looping through the whole dictionary

for name, seq in seqs.items():
    print(name, seq)            # Because my example file has large sequences, this comes out as a very big block of data!

# To run a python programme ("processfasta.py") on a specific file ("myfile.fa") from the terminal
# --> note this is for running code/files from the COMMAND LINE
>python processfasta.py myfile.fa

# The arguments of the above command are stored in the sys module's argv attributes as a list:
import sys
print(sys.argv)

# "import sys" has to appear at the top of your programme file ("processfasta.py" in this instance). You can print out the arguments at any point in the program
# code by using print(sys.argv). However, the POINT is to have a way for the programme to ACCESS the specified values in the arguments in order to allow it to run
# (e.g. which file to open, which values to assign to variables in the function)
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

# To test if this works, you can edit the above code by adding "print(filename)" at the end. Then run the Python programme from the terminal as shown below and
# check that the output is "fasta.txt". The file fasta.txt is available in this repository

print(filename)		# add this to above code and run as below

> python processfasta.py fasta.txt
#fasta.txt

# Also test that the IOError statement will work
> python processfasta.py smaug.txt
# File smaug.txt does not exist

    
# When using a function where some arguments are required and others are optional: the getopt module can help with arguments of sys.argv; 

# Example: process FASTA sequences but only add those longer than 250 bp to the dictionary
>python processfasta.py -l 250 myfile.fa		# Running the programme "processing.py" on the file "myfile.fa" specifying a length argument of 250, where
							# the length argument is optional

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
	print("""
processfasta.py: reads a FASTA file and builds a dictionary with all sequences bigger than a given length

processfasta.py [-h] [-l <length>] <filename> #square brackets for optional args

-h		print this message
-l <length>	filter all sequences with a length smaller than <length> (default <length>=0)

<filename>	the file has to be in FASTA format
		""")

o, a = getopt.getopt(sys.argv[1:], "l:h")			# assign values to lists o and a (where o will be optional and a compulsory arguments)
								# The first argument of getopt method is ALL of the arguments to the original function (but we use
								# sys.argv[1:] to list all of the arguments excluding the function/programme name you have called
								# The second argument of the getopt method is ALL of the arguments the user can supply with a - 							
								# command (optional)
								# colon after an argument shows that the foregoing argument requires a number parameter
			
# Initialise dictionary (where you will put all of the above listed arguments in a name: value structure)
opts={}
seqlen=0

for k,v in o:					# name of arg = k, value assigned to arg = v
	opts[k]=v				# add the value v to the k'th name in the opts dictionary
if "-h" in opts.keys():				# after creating the dictionaty, if the user has specified -h (which will be present as a key in the dictionary, then
	usage()				        # run the usage function defined earlier which prints out a description of the programme
	sys.exit()				# exit after printing help (quit programme without running anything else)
if len(a) < 1:					# if user has not specified anything after calling the programme	
	usage()					# initialise the usage function that will print out the message above; then close programme with message
	sys.exit("Input FASTA file is missing")
if "-l" in opts.keys():				# if the user has specified an optional length argument but it is shorter than 0, print out error and exit programme
	if int(opts["l"])<0:
		print("Length of sequence should be positive!")
		sys.exit(0)
	seqlen=opts["-l"]			# if the above returns a false value (sequence is longer than 0): assign the value next to the "-l" argument to the 						    
						# seqlen key	
		
# Note: the above code is available in a separate file in this repository for ease of use (getopt_example.py)	



# Using the System Environment

# When running a script/program in UNIX environment there are standard streams recognized by a computer program:
# - Standard input (stdin): stream data (e.g. text) going into a program. Unless redirected, stdin is expected from the keyboard which started the program
# - Standard outpout (stdout): stream where a program writes its output data. Unless redirected, stdout is the text terminal which initiated the program
# - Standard error (stderr): typically used by programs to output error messages or diagnostics. A stream independent of stdout and can provide error messages
#   even when stdout has been redirected. stderr can also be redirected separately: my_program | my_script.sh 1>program_output.txt 2>error_messages.txt

# The sys module provides file handles for stdin, stdout and stderr:
# import sys
# ask sys module to read a line from standard input
>>> sys.stdin.read()	# call the read method; Python waits for input from keyboard
a line
another line		# To show you are done with input, Ctrl+D

# Note that on MacOS (perhaps elsewhere) the read output is truncated to 6 characters of each line, and the line break is therefore not shown
# In order to repeat the sys.stdin.read() command, you first have to move the location of where the input will be read by running sys.stdin.seek(0)

# Interfacing with External Programs
# You can take output from a Python programme and pass it onto an external programme (which can be in any programming language potentially); e.g. pre-processing
# some sequences and then handing them over to an analysis programme (TopHat, Cufflinks)
# This is done by handing the output to the operating system of the computer, which in turn feeds it into the external programme. You specify this path
# in your script. You can also specify the return of the output from the external programme (although this was not covered in this lecture).
# You could further use the output from the external programme and pipe it back into your original programme for further processing OR
# get the output from the external programme and pass it onto another external programme for further processing.

# To pass output on/call external programmes, import the subprocess module (for more info see: https://docs.python.org/3/library/subprocess.html)
import subprocess
subprocess.call(["ls", "-l"])		# This calls the ls function from system, with "-l" as argument

# A more realistic example of this:
subprocess.call(["tophat", "genome_mouse_idx", "PE_reads_1.fq.gz", "PE_reads_2.fq.gz"]) 
# You are providing a list of arguments as the first argument to the call() function. By convention in the system environment, the first item is the 
# programme you are calling (executable name). The rest of the arguments in the list appear in the order in which tophat require them.
# In this case the argument "genome_mouse_idx" specifies the genome that should be used for sequence alignment. The other arguments are the sequences to be used.
# Tophat will be using sys.argv to get the arguments that you are providing.
# The point of this lecture is to explain how programs talk to each other via the standard streams provided by the operating system (i.e. communication outside
# of the specific program that you are using).




















