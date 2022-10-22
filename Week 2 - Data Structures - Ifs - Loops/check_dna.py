#!/usr/bin/env python3

dna = input("Enter DNA sequence:")

if "n" in dna:
    nbases = dna.count("n")
    print("DNA sequence has %d undefined bases" % nbases)
elif "N" in dna:
    nbases = dna.count("N")
    print("DNA sequence has %d undefined bases" % nbases)

else: #position of else is critical here! must be in line with if
    print("DNA sequence has no undefined bases")