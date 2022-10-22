# Usage of the while loop. While the condition remains true, keep on running the loop

# Example: Given a DNA seq find the positions of all canonical donor splice site candidates in the sequence
# See file "find_donor.py"

#!/usr/bin/env python3

dna = input("Enter DNA sequence:")

#splice sites always start "gt"

pos = dna.find("gt", 0) #position of donor splice site starting from 0 index (first letter in sequence)

while pos>-1:   #or while pos>=0; keeps on running for each letter in the sequence until finished/condition is breached/the position is -1
    print("Donor splice site candidate at position %d" %pos)
    pos=dna.find("gt", pos+1)

    
# Usage of the for loop. Iterates over the items of a sequence in the order that they appear in the sequence

