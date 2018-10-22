#!/usr/bin/env python3

import sys

class nucComp(object):
	def __init__(self, sequence_1, sequence_2, match_score, mismatch_score):
		self.sequence_1 = sequence_1 
		self.sequence_2 = sequence_2
		self.match_score = match_score
		self.mismatch_score = mismatch_score
		seq1_list = [self.sequence_1]
		seq2_list = [self.sequence_2]

	def rev_comp(self):
		input1 = self.sequence_2.lower()
		input2 = input1.replace('a', 'T')
		input3 = input2.replace('c', 'G')
		input4 = input3.replace('g', 'C')
		input5 = input4.replace('t', 'A')
		revcomp = input5[::-1]
		return [revcomp]

	def compare_1_2(self):
		score_1_2 = 0
		for nt in range(0, len(seq1_list)):
			if seq1_list[nt] == seq2_list[nt]:
				score_1_2 += int(self.match_score) 
			if not seq1_list[nt] == seq2_list[nt]:
				score_1_2 += int(self.mismatch_score)
			return score_1_2 

#	def compare_2_1(self):
#		score_2_1 = 0
#		for nt in range(0,len(str(self.sequence_2))):
#			if str(self.sequence_2)[nt] == str(self.sequence_1)[nt]:
#				score_2_1 += int(self.match_score) 
#			if not str(self.sequence_2)[nt] == str(self.sequence_1)[nt]:
#				score_2_1 += int(self.mismatch_score)
#			return score_2_1
#	
#	def compare_r1_2(self):
#		score_r1_2 = 0
#		for nt in range(0,len(rev_comp(self.sequence_1):
#			if rev_comp(self.sequence_1)[nt] == str(self.sequence_2)[nt]:
#				score_r1_2 += int(self.match_score) 
#			if not revcomp1[nt] == str(self.sequence_2)[nt]:
#				score_r1_2 += int(self.mismatch_score)
#			return score_r1_2
#	
#	def compare_r2-1(self):
#		score_r2-1 = 0
#		for nt in range(0,revcomp2):
#			if revcomp2[nt] == str(self.sequence_1)[nt]:
#				score_r2-1 += int(self.match_score) 
#			if not revcomp2[nt] == str(self.sequence_1)[nt]:
#				score_r2_1 += int(self.mismatch_score)
#			return score_r2_1
#
#	def compare_r1_r2(self):
#		score_r1_r2 = 0
#		for nt in range(0,revcomp1):
#			if revcomp1[nt] == revcopm2[nt]:
#				score_r1_r2 += int(self.match_score) 
#			if not revcomp1[nt] == revcomp2[nt]:
#				score_r1_r2 += int(self.mismatch_score)
#			return score_r1_r2 
#

attempt1 = nucComp('agtctgtca','gatctctcgc', 1, -1)

print(attempt1)

