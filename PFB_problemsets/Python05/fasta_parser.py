#!/usr/bin/env python

seq = []
seqs = {}

with open('test.fasta', 'r') as dna:	
	for line in dna:
		line = line.rstrip()
		if line.startswith('>'):
			ID = line[1::]
		else: 
			line = line.rstrip()
			seq.append(line)
			finalstring = ''.join(seq)

			seqs = {ID :{'sequence': finalstring}}

for entry in seqs:
	countA = seqs[ID]['sequence'].count('A')
		
	print(seqs)
	print(type(seqs))
	print(countA)		
