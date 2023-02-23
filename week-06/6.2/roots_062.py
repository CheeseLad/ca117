#!/usr/bin/env python3

from math import sqrt

import sys

lines = []

for line in sys.stdin:
  lines.append(line.strip())

for numinput in lines:

  list = numinput.split()
  a = int(list[0])
  b = int(list[1])
  c = int(list[2])
  if (b ** 2) - 4 * (a * c) >= 0:
    pos_root = float(((b * -1) + sqrt((b ** 2) - 4 * (a * c))) / (2 * a))
    neg_root = float(((b * -1) - sqrt((b ** 2) - 4 * (a * c))) / (2 * a))
    print(f"{neg_root:.1f}, {pos_root:.1f}")
  else:
    print("None")
