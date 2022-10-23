# Boolean Functions

# Example: Write a program that checks if a DNA sequence has an in-frame stop codon
# Stop codons are: TAG, TAA, TGA; frame read can start at pos 0, 1 or 2
# Available as separate file (dna_has_stop.py)

#!/usr/bin/env python3

'''   
Overall plan:
dna = input("Enter DNA sequence:")
if(has_stop_codon(dna)):
    print("Input sequence has an in-frame stop codon.")
else:
    print("Input sequence doesn't have an in-frame stop codon.")
'''

dna = input("Enter DNA sequence:")

def has_stop_codon(dna, frame=0):                           # default start position of search is 0; can customise
    "This function will check for in-frame stop codons"
    stop_codon_found=False
    stop_codons = ["tga", "tag", "taa"]                     # input sequence will have to be in lower case; include lower() method
    for i in range(frame, len(dna),3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found


