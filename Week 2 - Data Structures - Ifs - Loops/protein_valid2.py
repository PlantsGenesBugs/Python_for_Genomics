protein = input("Please enter protein sequence:")

for i in range(len(protein)):
	if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
		print("This is not a valid protein sequence")   
		break