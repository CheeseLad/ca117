#!/usr/bin/env python3

def get_divisors(n):
  divisors = []
  for i in range(1,n + 1):
    if n % i == 0:
      divisors.append(i)

  return divisors

def get_proper_divisors(n):
  storeddiv = get_divisors(n)
  storeddiv.pop(len(storeddiv) - 1)
  return storeddiv

def is_perfect(n):
  total = 0
  perfectlist = get_proper_divisors(n)
  for s in perfectlist:
    total = total + s

  if total == n:
    return True
  else:
    return False
