#!/usr/bin/env python3
import sys

inputseq = open('ps06_seq.txt','r')

for line in inputseq:
	line = line.rstrip()
	name,seq = line.split() 
	seq = seq.lower()	
	seq = seq.replace('c', 'G')
	seq = seq.replace('g', 'C')
	seq = seq.replace('a', 'T')
	seq = seq.replace('t', 'A')
	seq = seq[::-1]
	print('>'+name+' REVCOMP'+'\n'+seq)



inputseq.close()
