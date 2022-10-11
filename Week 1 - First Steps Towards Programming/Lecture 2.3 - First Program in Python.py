# We will write a program to count the %GC in a dna sequence supplied by a user

# Strategy:
# Read Sequence from User
# Count number of Cs
# Count number of Gs
# Determine length of sequence
# Divide C+G by length of sequence and * 100 
# Print out GC content

dna = "acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag"
no_c = dna.count("c")
no_g = dna.count("g")
seq_len = len(dna)
gc_percent = (no_c+no_g)/seq_len*100 #100.0 in Python2
print(gc_percent)
# 53.06122448979592

# Lines 11 to 16 can be saved as a .py file for execution from the Terminal (e.g. gc.py). To run, go to the directory with the file in it:
#> cd Documents/Python 
#> python gc.py
# 53.06122448979592

# Adding #!/usr/bin/env python3
# as the top line means you don't have to specify python in the terminal to execute a .py file. You just have to list './gc.py' in the appropriate directory.
# Might require adding executable flag: chmod a+x gc.py
# Find where Python interpreter is located by running... which, e.g. 
#> which python
# /Users/myname/opt/anaconda3/bin/python

# Remember to ADD COMMENTS to your coding and make the variable names logical. Multi-line comments can be added between triple quotes.

