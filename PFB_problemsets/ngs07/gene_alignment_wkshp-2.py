#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = SeqIO.to_dict(SeqIO.parse('pacbio-0_5.fasta', 'fasta'))

print(fasta_dict)
print(type(fasta_dict))
print(type(fasta_dict['tig00000001'].seq))
