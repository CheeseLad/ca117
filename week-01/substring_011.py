#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  substring = line.split()
  if substring[0].upper() in substring[1].upper():
    print("True")
  else:
    print("False")

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
