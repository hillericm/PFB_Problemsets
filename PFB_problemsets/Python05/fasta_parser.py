#!/usr/bin/env python

fasta_count_dict = {} 
fasta_dict = {}

with open('Python_07.fasta', 'r') as dna:	
	for line in dna:
		line = line.rstrip()
		if line.startswith('>'):
			header = line[1::].split()
			gene_ID = header[0]
			fasta_dict[gene_ID] = ''	
		else: 
			fasta_dict[gene_ID] += line

for entry in fasta_dict:
	fasta_count_dict[gene_ID] = {'sequence': fasta_dict[gene_ID]}
	fasta_count_dict[gene_ID]['A'] = fasta_count_dict[gene_ID]['sequence'].count('A') 
	fasta_count_dict[gene_ID]['C'] = fasta_count_dict[gene_ID]['sequence'].count('C') 
	fasta_count_dict[gene_ID]['G'] = fasta_count_dict[gene_ID]['sequence'].count('G') 
	fasta_count_dict[gene_ID]['T'] = fasta_count_dict[gene_ID]['sequence'].count('T') 
	print(fasta_count_dict)
print(fasta_dict)
print(fasta_count_dict)
