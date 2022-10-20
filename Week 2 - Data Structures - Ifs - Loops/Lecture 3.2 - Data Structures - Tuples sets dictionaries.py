# Tuple = A number of values separated by commas; immutable (elements can't be changed)
 
t = 1, 2, 3
print(t)
#(1, 2, 3)

t=(1,2,3) #gives the same thing

# You can index and slice tuples like lists, but they are immutable (in contrast to lists) and usually contain a heterogenous sequence of elements

t[1]
#2


# Set = An unordered collection with no duplicate elements. Support mathematical operations (union, intersection, difference). Unordered = NO INDEX.

brca1 = {"DNA repair", "zinc ion binding", "DNA binding", "Ubiquitin-protein transferase activity", "protein ubiquitination"}
brca1
#{'protein ubiquitination', 'DNA repair', 'Ubiquitin-protein transferase activity', 'DNA binding', 'zinc ion binding'}
brca1[1]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'set' object is not subscriptable

brca1 = {"DNA repair", "zinc ion binding", "DNA binding", "Ubiquitin-protein transferase activity", "protein ubiquitination", "DNA repair"}
brca1
#{'protein ubiquitination', 'DNA repair', 'Ubiquitin-protein transferase activity', 'DNA binding', 'zinc ion binding'}
# duplicate entry NOT RETURNED

# Join two sets; Find elements present in two sets
brca2 = {"protein binding", "H4 histone acetyltransferase activity", "nucleoplasm", "DNA repair", "double-strand break repair"}

# Union
brca1 | brca2
#{'protein binding', 'protein ubiquitination', 'DNA repair', 'Ubiquitin-protein transferase activity', 'DNA binding', 'nucleoplasm', 'double-strand break repair', 'H4 histone acetyltransferase activity', 'zinc ion binding'}

# Intersection
brca1 & brca2
#{'DNA repair'}


# Difference
brca1 - brca2
#{'Ubiquitin-protein transferase activity', 'zinc ion binding', 'protein ubiquitination', 'DNA binding'}


# Dictionary = Data structure where you can store a pair of values - a key and a value associated with it, e.g. a word and its definition
# E.g. a TF motif name and its associated DNA sequence
# Keys can be strings or numbers; values can be any type
# Define a library as below (library = {key:value, key2:value2, key3:value3})

TF_motif = {"SP1": "gggcgg", "C/EBP":"attgcgcaat", "ATF":"tgacgtca", "c-Myc":"cacgtg", "Oct-1":"atgcaaat"}

# To access values in a library, use its key within square brackets
TF_motif["ATF"]
#'tgacgtca'

# Combine with % operator for clearer printing
print("The recognition sequence for the ATF transcription is %s." % TF_motif["ATF"])
#The recognition sequence for the ATF transcription is tgacgtca.

# To check if a key is present in a library, use the "in" function as learned before, e.g.
"NF-1" in TF_motif
#False

"ATF" in TF_motif
#True

# Update a dictionary by adding new values - add a new key:value pair as below
TF_motif["AP-1"]="tgagtca"
TF_motif
#{'SP1': 'gggcgg', 'C/EBP': 'attgcgcaat', 'ATF': 'tgacgtca', 'c-Myc': 'cacgtg', 'Oct-1': 'atgcaaat', 'AP-1': 'tgagtca'}

# Modify an existing entry by redefining it
TF_motif["AP-1"]="tga(g/c)tca"
TF_motif
#{'SP1': 'gggcgg', 'C/EBP': 'attgcgcaat', 'ATF': 'tgacgtca', 'c-Myc': 'cacgtg', 'Oct-1': 'atgcaaat', 'AP-1': 'tga(g/c)tca'}

# Delete an entry by using the del function
del TF_motif["SP1"]
TF_motif
#{'C/EBP': 'attgcgcaat', 'ATF': 'tgacgtca', 'c-Myc': 'cacgtg', 'Oct-1': 'atgcaaat', 'AP-1': 'tga(g/c)tca'}

# Add more than one entry/another dictionary to an existing one by using the .update method
# If a key:value pair already exists, it isn't entered twice into the library
TF_motif.update({"SP1":"gggcgg", "C/EBP":"attgcgcaat", "Oct-1":"atgcaa"})
TF_motif
#{'C/EBP': 'attgcgcaat', 'ATF': 'tgacgtca', 'c-Myc': 'cacgtg', 'Oct-1': 'atgcaa', 'AP-1': 'tga(g/c)tca', 'SP1': 'gggcgg'}

# If the key already exists, but you give it a different value, the new value will replace the original one
TF_motif.update({"SP1":"gggcggt", "TFN":"gcttatc"})
TF_motif
#{'C/EBP': 'attgcgcaat', 'ATF': 'tgacgtca', 'c-Myc': 'cacgtg', 'Oct-1': 'atgcaa', 'AP-1': 'tga(g/c)tca', 'SP1': 'gggcggt', 'TFN': 'gcttatc'}

# To find out how big a dictionary is, use len() function
len(TF_motif)
#7

# To get a list of the keys in a dictionary, use list function and keys method
list(TF_motif.keys())
#['C/EBP', 'ATF', 'c-Myc', 'Oct-1', 'AP-1', 'SP1', 'TFN']

# To get a list of all the values in a dictionary, use list function and values method
list(TF_motif.values())
#['attgcgcaat', 'tgacgtca', 'cacgtg', 'atgcaa', 'tga(g/c)tca', 'gggcggt', 'gcttatc']

# Display in alphabetical order using sorted function
sorted(TF_motif.keys())
#['AP-1', 'ATF', 'C/EBP', 'Oct-1', 'SP1', 'TFN', 'c-Myc'] #Upper case letters appear before lower case




