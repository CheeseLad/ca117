#!/usr/bin/env python3

import sys

from math import pi

for line in sys.stdin:
  line = line.strip()
  line = int(line)
  print(f"{pi:.{line:d}f}")

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
