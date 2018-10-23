#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = SeqIO.to_dict(SeqIO.parse('pacbio-0_5.fasta', 'fasta'))

fasta_length_list = []

for entry in fasta_dict:
#	fasta_length_list.append([fasta_dict[entry].id, len(str(fasta_dict[entry].seq))])	
	fasta_length_list.append(len(str(fasta_dict[entry].seq)))

sorted_length_list = sorted(fasta_length_list)[::-1]
#print(sorted_length_list)

genome_size = 4600000
sorted_for_N50 = []
for entry in sorted_length_list:
	if genome_size >= 2300000:
		genome_size -= entry
		sorted_for_N50.append(entry)

n50 = sorted_for_N50[-1]

#print(sorted_length_list)
#print(sorted_for_N50)
print('Total Contig Number', len(fasta_length_list))
print('Max Contig Length:', max(fasta_length_list))
print('Min Contig Length:', min(fasta_length_list))
print('L50:', len(sorted_for_N50))
print('N50:', n50)
#print(type(n50))
#print(max(fasta_length_list))
#print(min(fasta_length_list))
#print(type(fasta_length_list))
#fasta_dict_keys = fasta_dict.keys()
#print(fasta_length_list)
#print(fasta_dict)
#print(fasta_dict_keys)
#print(len(fasta_dict))
#print(len(fasta_dict.keys()))
	
