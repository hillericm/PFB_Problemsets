#!/usr/bin/env python3
import re

r_obj = open('Python_07.txt','r')

poem = r_obj.read()

newpoem = re.sub(r'Nobody', 'Gus', poem)

print(newpoem)


#for match in re.finditer(r'(Nobody)', poem):
#	print(match.group(1), (match.start(1)+1))

