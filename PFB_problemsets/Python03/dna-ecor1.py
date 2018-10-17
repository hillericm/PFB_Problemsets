#!/usr/bin/env python3
import sys

dna = sys.argv[1]
dna_fix = dna.lower()

ecor1 = 'gaattc'

replaceEcor1 = dna_fix.replace(ecor1,'XXXXXX') 

ecor1StartLoc = (replaceEcor1.find('XXXXXX')+1)
ecor1EndLoc = (replaceEcor1.find('XXXXXX')+6)

intro = 'The EcoR1 site starts at nucleotide {} and ends at nucleotide {}.'

answer = intro.format(ecor1StartLoc, ecor1EndLoc)

print(answer)
