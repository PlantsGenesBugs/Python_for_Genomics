# Usage of the while loop. While the condition remains true, keep on running the loop

# Example: Given a DNA seq find the positions of all canonical donor splice site candidates in the sequence
# See file "find_donor.py"

#!/usr/bin/env python3

dna = input("Enter DNA sequence:")

#splice sites always start "gt"

pos = dna.find("gt", 0) #position of donor splice site starting from 0 index (first letter in sequence)

while pos>-1:        #or while pos>=0; keeps on running for each letter in the sequence until finished/condition is breached/the position is -1
    print("Donor splice site candidate at position %d" %pos)
    pos=dna.find("gt", pos+1)

    
# Usage of the for loop. Iterates over the items of a sequence in the order that they appear in the sequence

# Creat list of DNA motifs
motifs=["attccgt", "agggggtttttcg", "gtagc"]
for m in motifs:      #for each element in this list
    print(m, len(m))  #print out the value for that element and its length

#attccgt 7
#agggggtttttcg 13
#gtagc 5    


# To iterate over a sequence of numbers can use the range() function

for i in range(4):
     print(i) 
#0
#1
#2
#3

for i in range(1, 10, 2):   #starts at 1, ends at 10 (excludes 10), moves up 2 after each loop. If started at 0, would print 0, 2, 4, 6, 8
     print(i)
#1
#3
#5
#7
#9


# Examples: Find all characters in a protein sequence that are valid amino acids

# Pseudocode: for each character in protein sequence:
    #if character is NOT amino acid:
        #print invalid character and its position in protein

protein = "SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWFRSCRA"
for i in range(len(protein)):
    if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
        print("Protein contains invalid amino acid %s at position %d" % (protein[i], i))

#Protein contains invalid amino acid U at position 8
#Protein contains invalid amino acid U at position 9
#Protein contains invalid amino acid J at position 20

# Example: Determine if a protein sequence is valid (not interested in position of invalid amino acid) - files available "protein_valid.py" and "protein_valid2.py"
protein = "SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWFRSCRA"
for i in range(len(protein)):
    if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
        print("This is not a valid protein sequence")   # Just running these three lines will spit out the invalid sequence message 3 times
        break                                           # Prevents the loop from running again after the first invalid aa is found
    
    
# The continue statement causes the program to continue with the next iteration of the nearest enclosing loop, skipping the rest of the code in the loop

# Example: delete all invalid amino acid characters from a protein sequence - file available "protein_valid3.py"
protein = "SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWFRSCRA"
corrected_protein=""                                    #Initialise corrected protein with an empty string
for i in range(len(protein)):
    if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
        continue
    corrected_protein=corrected_protein+protein[i]      #If the previous step returns a FALSE (i.e. the aa IS a valid aa and appears in the reference string)

print("Corrected protein sequence is: %s" % corrected_protein)
#Corrected protein sequence is: SDVIHRYKPAKSHGWYVCRSRFTWMVWWFRSCRA


# Using continue statment can improve readability of code:
for i in range(n):
    if condition_1:
        function_1(i)
        if condition_2:
            function_2(i)
            if condition_3:
                function_3(i)
                ...

# Tidy this up with continue statement
for i in range(n):
    if not condition_1:
        continue
    function_1(i)
    if not condition_2:
        continue
    function_2(i)
    if not condition_3:
        continue
    function_3(i)
    ...

# Else statements (usually used with if) can be used with for and while loops in Python
# If used with for loop, the else statement is executed when the loop has exhausted iterating the list
# If used with while loop, the else statement is executed when the condition becomes false
# else statement not executed if loop terminated with break statement

# Example: find all prime numbers smaller than a given integer
N=10
for y in range(2,N):
    for x in range(2, y):
        if y % x == 0:
            print(y, "equals", x, "*", y//x)
            break
    else:
        print(y, "is a prime number")

        #2 is a prime number
#3 is a prime number
#4 equals 2 * 2
#5 is a prime number
#6 equals 2 * 3
#7 is a prime number
#8 equals 2 * 4
#9 equals 3 * 3     
        
# For the first loop, y = 2, and so the inner loop y is 2 so the range is (2,1) and the loop stops at the break command
# For the second loop, y = 3 and so the inner loop y is 3 which is the second round and range is (2,2), but 3%2 != 0 and 3 is a prime
# For the third loop, y = 4 and the inner loop range is (2,3) but 4%2 == 0 therefore the description 4 equals 2*2 is printed


# The pass statement is a placeholder (does nothing)

# Example: when a statement is required syntactically but you do not want any command or code to execute
if motif not in dna:
    pass
else:
    some_function_here(motif, dna)

# Can also use pass statement when you haven't yet written code for a particular situation but you need the placeholder for code to work


    
    
    
