#!/usr/bin/env python3

import re

data = open('Python_07.fasta','r')

seq = data.read()

#geneHeaders = re.findall(r'\>.*\b', seq)


for match in re.finditer(r'\>(\S+)(.+[\n])', seq):
	ID = match.group(1)
	Description = match.group(2)
	print('ID:',ID,'Description:', Description)


