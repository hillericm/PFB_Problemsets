#!/usr/bin/env python3
import sys

TestingNumber=int(sys.argv[1])

if TestingNumber > 0 :
  if TestingNumber < 50 :
    print('Alright alright alright. A positive number. But still smaller than 50.')
  else:
    print('A big positive number.')

elif TestingNumber < 0:
  print('No dice, compadre. That one is negative.')

else:
  print('You are a zero')
