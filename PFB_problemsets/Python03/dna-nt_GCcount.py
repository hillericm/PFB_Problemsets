#!/usr/bin/env python3
import sys

seq = sys.argv[1]

seq_fix = seq.lower()

intro = 'The GC content of the submitted sequence is {}.'

countG = (seq_fix.count('g'))
countC = (seq_fix.count('c'))
totalNT = len(seq_fix)

GC = (int(countG)+int(countC))/(int(totalNT))
percentGC = GC*100

answer = intro.format(percentGC)

print(answer)
