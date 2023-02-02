#!/usr/bin/env python3

import sys

inputlist = []

for lines in sys.stdin:
  inputlist.append(int(lines.strip()))

for n in inputlist:
  lst = list(range(1, n + 1))
  print("Multiples of 3: " + str([n for n in lst if n % 3 == 0]))
  print("Multiples of 3 squared: " + str([n * n for n in lst if n % 3 == 0]))
  print("Multiples of 4 doubled: " + str([n * 2 for n in lst if n % 4 == 0]))
  print("Multiples of 3 or 4: " + str([n for n in lst if n % 3 == 0 or n % 4 == 0]))
  print("Multiples of 3 and 4: " + str([n for n in lst if n % 3 == 0 and n % 4 == 0]))
