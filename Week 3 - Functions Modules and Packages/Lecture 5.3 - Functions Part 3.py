# More user defined functions

# A function to complement a DNA sequence

def reversecomp(seq):
  """Return the reverse complement of the DNA string."""
  seq = reverse_string(seq)
  seq = complement(seq)
  return seq

# First how to reverse a string
dna = "AGTGTGGGGCG"
dna[0:3]                # regular slice
#'AGT'
dna[0:3:2]              # extended slice, from 0 to 3 step along by 2 instead of 1
#'AT'
dna[::-1]               # the whole string, but in reverse order (step backwards 1 at a time)
#'GCGGGGTGTGA'

def reverse_string(seq):
  return seq[::-1]


# Second how to complement a string
# Will use a dictionary to do this, where the key is the existing base and the value is the complementary base
# Final complement function:

def complement(dna):
  """Return the complementary sequence string"""
  basecomplement = {"A":"T", "C":"G", "G":"C", "T":"A", "N":"N", "a":"t", "c":"g", "g":"c", "t":"a", "n":"n"}
  letters = list(dna)     # turns dna string into a list so that it can be used in the dictionary; each letter in the sequence is now an individual object
  letters = [basecomplement[base] for base in letters]    # block brackets means you are creating a list; this is a List Comprehension - see below
  return "".join(letters)


# Further clarification on List Comprehensions: provides a concise way to create lists; in the new list each element is the result of some operation(s) applied to each member of another sequence, OR it is a subsequence of those elements that satisfy a certain condition

# Syntax is: 
new_list = [operation(i) for i in old_list if filter(i)]    # i comes from the old list with perhaps some test/method applied to it

# alternative explanation of above syntax/equivalent longer description:
new_list = []
for i in old_list:
  if filter(i):
    new_list.append(operation(i))
    
    
# Test steps individually:
dna = "AGTGTGGGGCG"
basecomplement = {"A":"T", "C":"G", "G":"C", "T":"A", "N":"N", "a":"t", "c":"g", "g":"c", "t":"a", "n":"n"}
letters = list(dna) 
letters = [basecomplement[base] for base in letters]
letters
#['T', 'C', 'A', 'C', 'A', 'C', 'C', 'C', 'C', 'G', 'C']
"".join(letters)
#'TCACACCCCGC'

# Split and join methods = methods of STRINGS

# Split() returns a list of all the words in a string
sentence = "enzymes and other proteins come in many shapes"
sentence.split()
# ['enzymes', 'and', 'other', 'proteins', 'come', 'in', 'many', 'shapes']   # Splits on white space; can specify separator in argument
sentence.split("and")
#['enzymes ', ' other proteins come in many shapes']                        # Splits on "and" and removes "and"


# Join() returns a string in which the string elements were joined from a list. Separator string that joins the elemenst is the one upon which the function is called:
"-".join(["enzymes", "and", "other", "proteins", "come", "in", "many", "shapes"])
#'enzymes-and-other-proteins-come-in-many-shapes'
" ".join(["enzymes", "and", "other", "proteins", "come", "in", "many", "shapes"])
#'enzymes and other proteins come in many shapes'


# Final function to reverse and complement.... define the internal functions, then create this one and run it! (Easiest in Jupyter Notebook)
def reversecomp(seq):
  """Return the reverse complement of the DNA string."""
  seq = reverse_string(seq)
  seq = complement(seq)
  return seq

dna = "AGTGTGGGGCG"
reversecomp(dna)
#'CGCCCCACACT'



# Variable Number of Functions and Arguments
def myfunction(first, second, third):
  #do something with the 3 variables
  ...

def newfunction(first, second, third, *therest):
  print("First: %s" % first)
  print("Second: %s" % second)
  print("Third: %s" % third)
  print("And all the rest...", the rest)
  return

newfunction(1, 2, 3, 4, 5)
#First: 1
#Second: 2
#Third: 3
#And all the rest... (4, 5)

