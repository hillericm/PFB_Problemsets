#!/usr/bin/env python3

import sys
from Bio import SeqIO

seq_list = []

for entry in SeqIO.parse('reads.fq', 'fastq'):
	seq = str(entry.seq)
	seq_list.append(seq)

for entry in seq_list:
	kmer = entry[]
	print(kmer)
#	for kmer in range(0, len(seq)):
#		



