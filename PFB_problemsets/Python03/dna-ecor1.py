#!/usr/bin/env python3
import sys

dna = sys.argv[1]
dna_fix = dna.lower()

ecor1 = 'gaattc'

replaceEcor1 = dna_fix.replace(ecor1,'XXXXXX') 

ecor1StartLoc = (dna_fix.find(ecor1)+1)
ecor1EndLoc = (dna_fix.find(ecor1)+6)

intro = 'The EcoR1 site starts at nucleotide {} and ends at nucleotide {}.'

answer = intro.format(ecor1StartLoc, ecor1EndLoc)

print(answer)
