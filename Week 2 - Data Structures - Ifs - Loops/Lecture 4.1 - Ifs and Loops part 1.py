# Ifs and loops - decision making and repetition

# Example of an if statement
dna = input("Enter DNA sequence:")
#Enter DNA sequence:
agcgcggtatatatatgcnccann

if "n" in dna:
  nbases = dna.count("n")
  print("DNA sequence has %d undefined bases" % nbases)
#DNA sequence has 3 undefined bases

