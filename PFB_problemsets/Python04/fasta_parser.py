#!/usr/bin/env python

seqs = {} 
seq = []

with open('Python_07_ApoI.fasta', 'r') as dna:	
	for line in dna:
		line = line.rstrip()
		if line.startswith('>'):
			ID = line[1::]
			seqs[ID] = ''	
		else: 
			line = line.rstrip()
			seq.append(line)
			finalstring = ''.join(seq)

			seqs[ID] = finalstring

print(ID)
print(finalstring)
print(seqs)
