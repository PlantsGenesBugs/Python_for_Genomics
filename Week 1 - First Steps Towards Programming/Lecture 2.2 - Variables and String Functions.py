#!/usr/bin/python

# Variables
# Storage container for numbers, strings and other values

# Equal sign used to asign a value to a variable
`codon = "atg"`
`dna_sequence = "gtccgaatagtcccatagtacacatggc"`

# Give variables MEANINGFUL names
# Note there are restrictions to variable names - case sensitive, can only have letters, numbers (not first letter) and underscore

# Indexing and slicing
# [x] gives character at position x (note, first position is 0) 
# [x:y] slices a substring between positions x and y (excluding y)

`dna = "AATTGCGATGGGC"`
`dna[0] `
# 'A'

`dna[2:4]`
# 'TT’

`dna[-1]`
# 'C'

`dna[-3:-1]`
# 'GG'

'dna[:4]` # is the same as dna[0:4]; omitting the first defaults to zero; omitting the last defaults to the final position
# 'AATT'

# Useful String Functions
# Length of a string: len()

`len(dna)`
# 13

# Other functions include type() and print(); find help by using help() and putting function name in brackets (e.g. help(len))


# Strings as Objects
# Strings have variable names and values. They can also perform specific actions, called methods

`dna.count("G")` #counts the number of times "G" appears in the string called "dna"; "ask object dna to do method count"
# 5

# can also count substrings

 `dna.count("GC")`
  # 2
  





