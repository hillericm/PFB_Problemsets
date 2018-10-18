#!/usr/bin/env python3


with open('Python_06.fastq','r') as r_obj:

	lineCount = 0
	TotalChar = 0
	for line in r_obj:
		line = str(line)
		charCount = len(line)
		lineCount += 1
		TotalChar += charCount

	print('Line Count:', lineCount)	
	print('Total Characters:', TotalChar)
	print('Average Line Length:', TotalChar/lineCount) 
