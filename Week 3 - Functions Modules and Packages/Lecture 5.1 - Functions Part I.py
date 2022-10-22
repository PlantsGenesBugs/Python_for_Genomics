# Functions used to perform calculations with input values and return a single result
# Built-in functions include print(), len(), type() etc
# Can create your own functions (user-defined)

# Some useful DNA sequence functions:
# 1. Computing GC content of DNA
# 2. Checking if a DNA sequence has an in-frame stop codon
# 3. Obtaining reverse-complement of a DNA sequence

# General syntax:
def function_name(input arguments):
  "string documenting function"
  function_code_block
  return output

# Example: computing the GC content of DNA

def gc(dna):
  "this function computes the GC percentage of a dna sequence"
  nbases = dna.count("n")+dna.count("N")
  gcpercent = float(dna.count("c")+dna.count("C")+dna.count("g")+dna.count("G"))*100.0/(len(dna)-nbases)
  return gcpercent

dna="aacttgtggcgcaatctctat"
gc(dna)
#42.85714285714285

gc("AACCGGTT")
#50.0


# Scope of Variable Declaration: if you declare a variable inside a function, it will only exist in that function (e.g. nbases is declared inside the function; this is a local variable to the gc function - not available outside of the function)
