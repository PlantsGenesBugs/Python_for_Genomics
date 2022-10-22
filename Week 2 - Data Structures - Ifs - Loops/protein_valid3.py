protein = "SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWFRSCRA"
corrected_protein=""                                   

for i in range(len(protein)):
	if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
		continue
	corrected_protein=corrected_protein+protein[i]      

print("Corrected protein sequence is: %s" % corrected_protein)