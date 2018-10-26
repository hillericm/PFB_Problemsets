#!/usr/bin/env python3

import sys
from Bio import SeqIO

kmer_length = int(sys.argv[1])
top_num_count = int(sys.argv[3])

kmer_dict = {}

for entry in SeqIO.parse(sys.argv[2], 'fastq'):
	seq = str(entry.seq)
	seq = seq.strip()
	for i in range(0, len(seq) - kmer_length + 1):
		kmer = seq[i:(i+kmer_length)]	
		if kmer not in kmer_dict.keys():
			kmer_dict[kmer] = 1
		else:
			kmer_dict[kmer] += 1

sorted_kmer_dict = sorted(kmer_dict, key=lambda x: kmer_dict[x], reverse=True)

for entry in sorted_kmer_dict[:top_num_count]:
	print('{}\t{}'.format(entry, kmer_dict[entry]))


#counter = 0
#if counter < top_num_counts:
#	print('{}\t{}'.format(
#print(kmer_dict)
#print(sorted_kmer_dict)
#
#	for kmer in range(0, len(seq)):
#		



