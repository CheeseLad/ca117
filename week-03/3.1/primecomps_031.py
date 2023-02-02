#!/usr/bin/env python3

import sys

def prime(num):
  not_prime = False
  for i in range(2, num):
    if num % i == 0:
      not_prime = True
      break
  if not_prime:
    return False
  else:
    return True

inputlist = []

for lines in sys.stdin:
  inputlist.append(int(lines.strip()))

for n in inputlist:
  print("Primes: " + str([y for y in range(2, n + 1) if prime(y)]))
