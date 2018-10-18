#!/usr/bin/env python3
import sys


count = 1
fact = 1

while count < 1001:
	fact *= count
	count += 1
print(fact)
