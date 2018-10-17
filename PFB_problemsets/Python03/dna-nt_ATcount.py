#!/usr/bin/env python3
import sys

seq = sys.argv[1]

seq_fix = seq.lower()

intro = 'The AT content of the submitted sequence is {}.'

countA = (seq_fix.count('a'))
countT = (seq_fix.count('t'))
totalNT = len(seq_fix)

AT = (int(countA)+int(countT))/(int(totalNT))
percentAT = AT*100

answer = intro.format(percentAT)

print(answer)
