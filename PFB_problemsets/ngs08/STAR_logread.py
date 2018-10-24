#!/usr/bin/env python3

import sys
import subprocess


inputfile_get = str(subprocess.check_output('cat Log.out | grep ^readFilesIn | grep D$', shell=True))
print(inputfile_get)
print(type(inputfile_get))

inputfile_split = inputfile_get.split()
inputfile_strip = inputfile_split.pop()
print(inputfile_split[1:])

for i in inputfile_split[1:]:
	print(str(i))
	


