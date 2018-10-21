#!/usr/bin/env python3

from Bio import SeqIO


for fasta_entry in SeqIO.parse('Python_08.fasta', 'fasta'):
	print('ID', fasta_entry.id)
	print('len {}'.format(len(fasta_entry)))
