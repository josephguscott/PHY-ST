import os

from Bio import SeqIO
from Bio import AlignIO


# get MSA input information (name)
inputAlignmentName = str(input("Enter your MSA name: \n>> "))

# read in MSA
inputSeq = open(inputAlignmentName, "r")
outputSeq = open("output.fas", "w")

alignments = AlignIO.parse(inputSeq, "phylip")
AlignIO.write(alignments, outputSeq, "fasta")

outputSeq.close()
inputSeq.close()