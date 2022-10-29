#!/usr/bin/env python3

try:
	f=open("myfasta.txt")
except IOError:
	print("File does not exist")

seqs = {}

for line in f:
	line = line.rstrip().lstrip()
	if line.startswith(">"):
		words=line.split()
		name=words[0][1:]
		seqs[name]=""
	else:
		seqs[name] = seqs[name]+line

print(list(seqs.keys()))