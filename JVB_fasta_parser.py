#!/usr/bin/env python3

import sys

fasta_filename = sys.argv[1]

fasta_fileobj = open('fasta_filename','r')
output_file = sys.stdout

sequence_name = ''
sequence_desc = ''
sequence_string = ''

for line in fasta_fileobj:
	line = line.rstrip()
	if line.startswith('>'):
		if len(sequence_string) > 0:
			#do something cool with the sequence
			#such as write, alter with a function
			#done here must also be done outside
			#for loop
			sequence_string = ''
		line = line.lstrip('>')
		sequence_info = line.split(maxsplit=1)
		sequence_name = sequence_info[0]
		if len(sequence_info) > 1:
			sequence_desc = sequence_info[1]

	else:
		sequence_string += line

if len(sequence_string) > 0:
	#do something cool with the sequence
	# to insure it is done to final sequence
	sequence_string = ''
