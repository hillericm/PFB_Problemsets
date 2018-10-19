#!/usr/bin/env python

import re

seqs = {} 
seq = []

with open('Python_07_ApoI.fasta', 'r') as dna:	
	for line in dna:
		seq.append(line)
		finalstring = ''.join(seq)
	for entry in re.finditer(r'(^\>\S+)', finalstring):
		ID = entry.group(1)
		sequence = entry.group(0).replace(entry.group(1), '')

print(ID)
print(sequence)
#	for entry in re.finditer(r'([^(^\>\S+?)])', finalstring):
#		sequence = entry.group(1)
#		finalstring
#		print(sequence)
#	''.join(entry.split('\n'))


#		seqs[ID] = sequence

#print(sequence)
#print(seqs)
