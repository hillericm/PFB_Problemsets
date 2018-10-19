#!/usr/bin/env python

import re

seqs = {} 
seq = []

with open('Python_07_ApoI.fasta', 'r') as dna:	
	for line in dna:
		seq.append(line)
		finalstring = ''.join(seq)
		print(finalstring)	
	print(finalstring)
	print(type(finalstring))
	for entry in re.finditer(r'(^\>\S+)([^>].+)', finalstring):
		ID = entry.group(1)
		seq.append((entry.group(2)).rstrip())
		sequence = ''.join(seq)

		seqs[ID] = sequence

print(ID)
print(finalstring)
#print(sequence)
#print(seqs)
