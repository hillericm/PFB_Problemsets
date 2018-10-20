#!/usr/bin/env python3
def dnaview(seq, linewidth):
	seq = seq.replace('\n', '')
	output = ''
	for nt in range(0,len(seq),linewidth):
		output += seq[nt:nt+linewidth]+'\n'
	return output


#while count < len(seq)/(linewidth):
#        seq_fitted = seq([linewidth*count:(linewidth)*(count+1):])
#        seq_fitted_grown += seq_fitted
#        count += 1
#        return seq_fitted_grown




#	count = 0
#	while count < len(dna)/(printlength):
#		print(dna[(printlength)*count:(printlength)*(count+1):])
#		count += 1

dna2 = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

print(dnaview(dna2, 4)) 
