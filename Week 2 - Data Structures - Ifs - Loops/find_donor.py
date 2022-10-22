#!/usr/bin/env python3

dna = input("Enter DNA sequence:")

#splice sites always start "gt"

pos = dna.find("gt", 0) #position of donor splice site -first

while pos>-1:
    print("Donor splice site candidate at position %d" %pos)
    pos=dna.find("gt", pos+1)