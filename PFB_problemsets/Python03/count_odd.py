#!/usr/bin/env python3
import sys

startNumb = int(sys.argv[1])
endNumb = 1+(int(sys.argv[2]))

for x in range(startNumb,endNumb):
	if x % 2 == 1:
		print(x)
 
