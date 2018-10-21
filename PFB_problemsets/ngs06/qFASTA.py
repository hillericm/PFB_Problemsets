#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = SeqIO.to_dict(SeqIO.parse('human_cds.fasta', 'fasta'))

for fasta_entry in fasta_dict:
	entry_sequence = str(fasta_dict[fasta_entry].seq)
	countA = entry_sequence.count('A')
	countC = entry_sequence.count('C')
	countG = entry_sequence.count('G')
	countT = entry_sequence.count('T')
	nuCompA = countA/(len(entry_sequence))
	nuCompC = countC/(len(entry_sequence))
	nuCompG = countG/(len(entry_sequence))
	nuCompT = countT/(len(entry_sequence))
	GCcontent = ((countG + countC)/len(entry_sequence))
	#print('ID', fasta_dict[fasta_entry].id, '%A:', countA , '%C:', countC, '%G:', countG, '%T:', countT, 'len:', len(entry_sequence))
	#print('ID', fasta_dict[fasta_entry].id, '%A:', nuCompA*100, '%C:', nuCompC*100, '%G:', nuCompG*100, '%T:', nuCompT*100, '%Total:', (nuCompA+nuCompC+nuCompG+nuCompT)*100)
	print('ID', fasta_dict[fasta_entry].id,'\t', GCcontent)
	
	
