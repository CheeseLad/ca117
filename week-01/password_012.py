#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  upper, lower, numeric, other = 0, 0, 0, 0
  for c in line:
    if c.isupper():
      upper = 1
    elif c.islower():
      lower = 1
    elif c.isnumeric():
      numeric = 1
    else:
      other = 1
  print(upper + lower + numeric + other)

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
