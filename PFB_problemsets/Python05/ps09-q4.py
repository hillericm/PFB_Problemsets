#!/usr/bin/env python3
import sys

def fasta_widthwrite(seq, linewidth):
        output = ''
        for nt in range(0,len(seq),linewidth):
                output += seq[nt:nt+linewidth]+'\n'
        return output


fasta_filename = sys.argv[1]

fasta_fileobj = open(fasta_filename, 'r')
output_file = sys.stdout

sequence_name = ''
sequence_desc = ''
sequence_string = ''

for line in fasta_fileobj:
	line = line.rstrip()
	if line.startswith('>'):
		if len(sequence_string) > 0:
			func_output = fasta_widthwrite(sequence_string, int(sys.argv[2]))
			output_file.write('>{}{}\n{}\n'.format(sequence_name, sequence_desc, func_output))			
			sequence_string = ''		
		line = line.lstrip('>')
		sequence_info = line.split(maxsplit=1)
		sequence_name = sequence_info[0]
		if len(sequence_info) > 1:
			sequence_desc = sequence_info[1]

	else:
		sequence_string += line

if len(sequence_string) > 0:
	func_output = fasta_widthwrite(sequence_string, int(sys.argv[2]))
	output_file.write('>{}{}\n{}\n'.format(sequence_name, sequence_desc, func_output))	
	sequence_string = ''	


#	fasta_count_dict = {} 
#	fasta_dict = {}
#
#	file = open('sys.argv[1]', 'r')
#	printlength = int(sys.argv[2])
#
#	with file as dna:	
#		for line in dna:
#			line = line.rstrip()
#			if line.startswith('>'):
#				header = line[1::].split()
#				gene_ID = header[0]
#				fasta_dict[gene_ID] = ''	
#			else: 
#				fasta_dict[gene_ID] += line
#
#	
#	for entry in fasta_dict:
#		seq = fasta_dict[gene_ID]
#
#	
#		count = 0
#		while count < len(seq)/(printlength):
#			print(seq[(printlength)*count:(printlength)*(count+1):])
#			count += 1
#
#
