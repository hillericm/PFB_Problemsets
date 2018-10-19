#!/usr/bin/env python3
import sys

def dnaview(input_file, printlength):

	fasta_count_dict = {} 
	fasta_dict = {}

	file = open('sys.argv[1]', 'r')
	printlength = int(sys.argv[2])

	with file as dna:	
		for line in dna:
			line = line.rstrip()
			if line.startswith('>'):
				header = line[1::].split()
				gene_ID = header[0]
				fasta_dict[gene_ID] = ''	
			else: 
				fasta_dict[gene_ID] += line

	
	for entry in fasta_dict:
		seq = fasta_dict[gene_ID]

	
		count = 0
		while count < len(seq)/(printlength):
			print(seq[(printlength)*count:(printlength)*(count+1):])
			count += 1


