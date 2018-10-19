#!/usr/bin/env python

import re

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
apoI = re.sub(r'([GA])AATT([CT])', r'\1^AATT\2', finalstring)
print(apoI)

#for match in re.finditer(r'([GA]AATT[CT])',finalstring):
#	print(match.group(1), (match.start(1)+1)) 
