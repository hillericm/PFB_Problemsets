#!/usr/bin/env python3

w_obj = open('tompetty_uc.txt','w')
r_obj = open('tompetty.txt','r') 
for line in r_obj:
	line = line.rstrip()
	lineUpper = line.upper()
	w_obj.write(lineUpper + '\n')
w_obj.close()
r_obj.close()		

print('Wrote', 'tompetty_uc.txt')



