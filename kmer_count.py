#!/usr/bin/python

# This script is a simple kmer counter.
# See Moeckel et al. (2024) "A survey of k-mer methods and applications in bioinformatics"

# Input: FASTA file with a command line argument setting the k-value
# Output: Stdout, displaying the canonical kmer and number of times it appears in the file separated by a tab.

# import libraries
import sys

# declare variables
kmers = dict()
contigs = dict()

# open given fasta file
inFile = open(sys.argv[1], "r")
# read in given k-value
k = int(sys.argv[2])
# for each header line:
for line in inFile:
    line = line.strip()
    if ">" in line:
        header = line
        contigs[header] = ""
        continue
    else:
        contigs[header] += line

for header in list(contigs.keys()):
    for i in range(len(contigs[header]) - k + 1):
        kmer = contigs[header][i:i+k]
        # this if statement checks if the kmer is canonical (alphabetically first to its reverse complement) - if not, it is reversed
        if kmer > kmer[::-1]:
            kmer = kmer[::-1]
        if kmer in kmers:
            kmers[kmer] = kmers[kmer] + 1
        else:
            kmers[kmer] = 1

for key in list(kmers.keys()):
   print(key + "\t" + str(kmers[key]))

# close fasta file
inFile.close()