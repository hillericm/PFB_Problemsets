#!/usr/bin/env python3

list10 = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tuplist = [(len(x),x) for x in list10]

for x in tuplist:
	print(x[0],'\t', x[1], '\n')
