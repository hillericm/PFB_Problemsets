#!/usr/bin/env python

import re


dna = open('Python_07_ApoI.fasta', 'r')

seq = []
for line in dna:
	line = line.rstrip()
	seq.append(line)
	seq2 = str(seq)

for match in re.finditer(r'([GA]AATT[CT])', seq2):
	print(match.group(1), match.start(1)) 
