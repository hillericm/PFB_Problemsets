#!/usr/bin/env python3

from Bio import SeqIO


for entry in SeqIO.parse('four_reads.fastq', 'fastq'):
	fastq_entry = entry.letter_annotations['phred_quality']

	QC30 = 0
	for value in fastq_entry:
		if value >= 30:
			QC30 += 1
		
	print(entry.id)
	print(QC30)




for entry in SeqIO.parse('four_reads.fastq', 'fastq'):
	fastq_entry = entry.letter_annotations['phred_quality']
	trim_seq = entry.seq[5::]
	trim_qual = fastq_entry[5::]
	
	print(entry.id)
	print(fastq_entry)
	print(trim_qual)	
	

#	print('ID', entry,'seq',fastq_entry)
#	print(fast_dict)
#for entry in fasta_dict:
#	print(fasta_dict[entry].id, fasta_dict[entry].qual)

#openfile = open('four_reads.fastq', 'r')
	
#fastq_entry_as_list = []
#fastq_list = []
#count = 0
#for line in range(openfile:
#		fastq_entry_as_list.append(line)
#		print(fastq_entry_as_list)
#	count +=1
