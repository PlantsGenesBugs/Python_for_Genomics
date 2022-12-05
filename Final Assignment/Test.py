# Have to answer following questions about multi-sequence FASTA file:
# 1. number of records in file (a new record starts with >)
# 2. lengths of sequences in file? longest? shortest? more than one longest? seq identifiers?
# 3. identify ORFs in forward strand - which one is longest? identifier? for each identifier, which is longest ORF in that seq? starting position? 
# note: ORFs must have both start and stop codons
# 4. given length n, how many repeats of length n are present in all sequences in the FASTA file. Which is most frequent repeat of a given length?

# Plan:
# Create dictionary from file of FASTA sequences (see Lecture 3.2, Lecture 7.2 and FastLibrary.py)
# Count number of keys (len(library));(alternate, if object is a list, can do object.count(">"))
# Loop through dictionary to retrieve sequence lengths
# Return longest, shortest and identifiers (keys)
# Loop: Search for start codon in string/sequence (ATG), once found, progress in groups of three and search for stop codon (TAA, TAG, TGA). Save result.
# For above see Lecture 2.2 (dna.find("ATG") followed by dna.find("ATG", 1) and dna.find("ATG", 2) will find all starts, but you MUST add the stop codon in search)
# Combine above with if statement (see Lecture 4.1): if ATG is found, then look for stop codon by progressing in 3s. If not found, stop processing and carry on.
# For more useful code examples see Lecture 4.2, e.g. pos = dna.find("gt", 0) - position of "gt" starting from 0 index.
# Another useful bit of code in Lecture 5.2: searching a DNA sequence for in-frame stop codons.
