#!/usr/bin/env python3
import sys

TestingNumber=float(sys.argv[1])

if TestingNumber > 0 :
  if TestingNumber < 50 :
    if TestingNumber % 2 == 0:
      print('Alright alright alright. A positive even number smaller than 50.')
    else:
      print('Close, but no one wants a small odd positive number')
  elif TestingNumber >50:
    if TestingNumber % 3 == 0:
      print('A really big positive number. And divisible by 3. Well done.')
    elif TestingNumber % 3 > 0:
      print('A large positive number indivisible by 3? Boring')
  else:
    print('Nifty Fifty')

elif TestingNumber < 0:
  print('No dice, compadre. That one is negative.')

else:
  print('You are a zero')
