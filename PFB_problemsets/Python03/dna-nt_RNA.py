#!/usr/bin/env python3
import sys

seq = sys.argv[1]

seq_fix = seq.lower()


RNA = seq_fix.replace('t', 'u')

print(RNA)
