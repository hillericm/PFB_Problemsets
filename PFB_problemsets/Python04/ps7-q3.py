#!/usr/bin/env python3

import re

data = open('Python_07.fasta','r')

seq = data.read()

geneHeaders = re.findall(r'\>.*\b', seq)

print(geneHeaders)


