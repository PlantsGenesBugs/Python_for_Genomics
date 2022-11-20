# BioPython
# See http://www.biopython.org
# Includes parsers for various bioinformatics file formats, access to online services, and interfaces to programmes like BLAST, ClustalOmega etc

# Check if Biopython is installed
import Bio
print(Bio.__version__)
#1.79

# If Biopython isn't installed, the import Bio command will fail - in that case, install Biopython from website
# http://biopython.org/wiki/Download

# Example Usage 1: Find out from what species an unkown DNA sequence came from
# We are going to use the BLAST tool from NCBI to compare our sequence to a database of sequences

from Bio.Blast import NCBIWWW
fasta_string = open("myseq.txt").read()       # open file and read sequence into variable
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)    # call NCBIWWW method qblast - returns a handle to get out the result; use blastn, nt database, var)

# for more information: >>>help(NCBIWWW.qblast)
# default output format is XML

# Looking at the BLAST record: import NCBIXML to look at the produced XML file
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)  # visualise XML file

# The BLAST results contain:
# 1. descriptions - a list. Each element will have a title, score, e-value, num_alignments
# 2. alignments - a list. Each element will have a title, length and hsps (High Scoring Pairs) - a list. HSP: score, bits, expect, num_alignments etc etc
# 3. multiple_alignment

# Parsing BLAST output in a human-readable way
len(blast_record.alignments)
# 50 (items in list; BLAST limits to 50 so probably more)

# Select the matches that gave a signifcant hit (set threshold at 0.01 -- 1% or less of a chance match)
E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)  # query sequence
            print(hsp.match)  # bar that shows match
            print(hsp.sbjct)  # subject sequence


# Returns several sequences identified as Zaire ebolavirus strains isolated from H. sapiens

# Further study:
# BioPython Tutorial and Cookbook: http://biopython.org/DIST/docs/tutorial/Tutorial.html
# BioPython FAQ: http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc5







