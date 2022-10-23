#!/usr/bin/env python3

'''   
Overall plan:
dna = input("Enter DNA sequence:")
if(has_stop_codon(dna)):
    print("Input sequence has an in-frame stop codon.")
else:
    print("Input sequence doesn't have an in-frame stop codon.")
'''


def has_stop_codon(dna, frame=0):
    "This function will check for in-frame stop codons"
    stop_codon_found=False
    stop_codons = ["tga", "tag", "taa"]
    for i in range(frame, len(dna),3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found


            
            

    
    