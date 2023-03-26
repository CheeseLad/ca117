#!/usr/bin/env python3

def collatz(n):
    print(n)
    if n != 1:
      if n % 2 == 0:
         n = n //2
      elif n % 2 != 0:
        n = (n * 3) + 1

      return collatz(n)