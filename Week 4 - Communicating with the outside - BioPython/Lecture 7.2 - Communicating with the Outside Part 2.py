# How to read and process FASTA files in Python
# Standard DNA sequence format; one or more sequences

# Example: Build a dictionary containing all the sequences from a FASTA file
# Create FASTA file by doing a BLAST search at NCBI, select sequences of interest and download as full FASTA format. The file I used is available in this repository.
# Build dictionary with gene ID as key and sequence itself as value

# Pseudocode:
#open file
#read in one line at a time
#ask if it is a header or not
#if header - get sequence name
#store sequence name as key
#if NOT header, then update sequence in dictionary (at current key spot)
#at end of sequence - are there any more lines? continue. If not, break.

try:
    f=open("myfasta.txt")
except IOError:
    print("File does not exist")
    
# Main loop of program:
# First set up empty dictionary
seqs = {}

# Go through line by line
# Discard the newline at the end (if any) (anything like returns or anything else)

for line in f:
  line = line.rstrip()

# Test the line for the presence of > which indicates a gene ID line
# If present (true), split the line into individual words, and look at the first element of that list [0] - that is the name. Then slice the > sign out [1:]
# Initialise a new entry for the dictionary with the name specified; fill the sequence in next

  if line.startswith(">"):
    words=line.split()
    name=words[0][1:]
    seqs[name]=""

# When not a header line, append the sequence on the current line to the entry just initiated; append to an existing entry
  else:
    seqs[name] = seqs[name]+line
#f.close()            Adding this to the loop gives a syntax error, so I have excluded it from my code; manually close the file "f"

# Note: if you have previously opened and read the file, make sure you return the current position to 0 by running f.seek(0)

# Check the length of the dictionary
len(seqs)
#6

# Check the keys of the dictionary
list(seqs.keys())
#['KY549441.1', 'MH598906.1', 'HF543599.2', 'KX752088.1', 'NC_046568.1', 'MF035968.1']


# Why am I getting an error?! 
# If you get an error message:
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
NameError: name 'name' is not defined
    
# It is likely your stream position (where python starts reading the file) is NOT at the start of the file
# To test where your stream position is, use:
f.tell()            #.tell() function: for more information look here https://docs.python.org/3/library/io.html

# To reset the position, use .seek(0):
f.seek(0)

# Another reason you could get the above error is if your file starts with anything other than a ">"
# Based on troubleshooting from Maciel Rodriguez (who did this course in 2018) the fix is to add the following code inside the for loop:
if not line or line[0]=="#":            # this works only if your file starts with a space/empty line or #. Other characters will have to be specified.
    continue

 # Another solution to space to the LEFT of your sequence would be to add the .lstrip() function to your for loop, as below:
for line in f:
	line = line.rstrip().lstrip()
	if line.startswith(">"):
		words=line.split()
		name=words[0][1:]
		seqs[name]=""
	else:
		seqs[name] = seqs[name]+line
  

# A copy of this code is available in this repository as "FastaLibrary.py"
        


















