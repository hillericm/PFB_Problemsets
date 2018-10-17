#!/usr/bin/env python3
import sys

seq = sys.argv[1]

seq_fix = seq.lower()


compC = seq_fix.replace('c', 'G')
compG = compC.replace('g', 'C')
compA = compG.replace('a', 'T')
compT = compA.replace('t', 'A')

revcomp = compT[::-1]
print(revcomp)



