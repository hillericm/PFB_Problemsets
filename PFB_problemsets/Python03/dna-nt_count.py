#!/usr/bin/env python3
import sys

seq = sys.argv[1]

seq_fix = seq.lower()

intro = 'There are {} A, {} G, {} C, and {} T.'

countA = (seq_fix.count('a'))
countT = (seq_fix.count('t'))
countG = (seq_fix.count('g'))
countC = (seq_fix.count('c'))

answer = intro.format(countA, countG, countC, countT)

print(answer)
