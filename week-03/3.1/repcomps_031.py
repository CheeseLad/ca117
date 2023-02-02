#!/usr/bin/env python3

import sys

inputlist = []

for line in sys.stdin:
  inputlist.append(int(line.strip()))

for n in inputlist:
  print("Non-multiples of 3 replaced: " + str([n if n % 3 == 0 else 0 for n in range(1, n + 1)]))
