# Ifs and loops - decision making and repetition


# Example of an if statement

dna = input("Enter DNA sequence:")
#Enter DNA sequence:
agcgcggtatatatatgcnccann

if "n" in dna:
  nbases = dna.count("n")
  print("DNA sequence has %d undefined bases" % nbases)
#DNA sequence has 3 undefined bases

# Condition in if statement is Boolean (True/False)(operators - equal ==, not equal !=, less than and greater than <>, less/greater or equal as well
0>1
#False
1>0
#True
len("agtcgt")>=10
#False
"GT"!="AT"
#True
10+1==11
#True

# Membership Operators: in = true if variable in the specified sequence (false otherwise); not in = true if it does not find a variable in the specified sequence
motif="gtccc"
dna="atatattgtcccattt"
motif in dna
#True

# Identity Operators: is = true if the variabes on either side of operator point to the same object (false otherwise); is not = false if the variable on either side of the operator point to the same object 
alphabet=["a", "c", "g", "t"] # create a list
newalphabet = alphabet[:] # slice the list
alphabet == newalphabet # compare 
#True
alphabet is newalphabet
# False (they are not the same object)

# Alternative Execution (separate file available in this repository folder, check_dna.py)
# To count number of undefined bases (either lower case n or upper case N - not both in the instruction below)

#!/usr/bin/env python3

dna = input("Enter DNA sequence:")

if "n" in dna:
    nbases = dna.count("n")
    print("DNA sequence has %d undefined bases" % nbases)
elif "N" in dna:
    nbases = dna.count("N")
    print("DNA sequence has %d undefined bases" % nbases)

else:        #position of else is critical here! must be in line with if
    print("DNA sequence has no undefined bases")


    
# If both lower and upper case n/N are present, will have to use logical operators (and, or, not) (see file check_dna2.py)

#!/usr/bin/env python3

dna = input("Enter DNA sequence:")

if "n" in dna or "N" in dna:
    nbases = dna.count("n") + dna.count("N")
    print("DNA sequence has %d undefined bases" % nbases)

else:      #position of else is critical here! must be in line with if
    print("DNA sequence has no undefined bases")

