protein = "SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWFRSCRA"
for i in range(len(protein)):
    if protein[i] not in "ABCDEFGHIKLMNPQRSTVWXYZ":
        print("Protein contains invalid amino acid %s at position %d" % (protein[i], i))