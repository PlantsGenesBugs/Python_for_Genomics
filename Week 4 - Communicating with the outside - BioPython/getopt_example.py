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


o,a = getopt.getopt(sys.argv[1:], "l:h") #o = optional and a = required args; can ignore name (first thing in list). When : used = option expects a value.

#set up dictionary that contains argument name and value put in by user

opts = {}
seqlen_o=;

for k, v in o:
	opts[k] = v
if "-h" in opts.keys():		#-h brings up help; if it's there, and the user calls it, print help message
	usage(); sys.exit()
if len(a) <1:
	usage();sys.exit("input fasta file is missing")
if "-l" in opts.keys():
	if int(opts["l"])<0:
		print("Length of sequence should be positive"); sys.exit(0)
	seqlen=opts["-l"]
