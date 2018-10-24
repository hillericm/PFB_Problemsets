#!/usr/bin/env python3

#I want to parse out information from column and then count the occurance of those columns. Because often many reads will be the "same" I'll use the set function

import sys

bam_input = open(sys.argv[1], 'r')

read_dict = {}
read_count_dict = {}

for line in bam_input:
	line = line.strip()
	line = line.split('\t')
	readID = line[0]
	isoform = line[2]
	geneID = isoform.split('^')[0]
	if geneID not in read_dict.keys():	
		read_dict[geneID] = {readID}

	if geneID in read_dict.keys():
		read_dict[geneID].add(readID)


for geneID in read_dict:
	read_count = len(read_dict[geneID])
	read_count_dict[geneID] = read_count


sorted_read_count = sorted(read_count_dict, key=lambda x: read_count_dict[x], reverse=True)

print(read_count_dict)

for entry in sorted_read_count:
	print('{}\t{}'.format(entry, read_count_dict[entry]))
