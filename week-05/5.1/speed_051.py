#!/usr/bin/env python3

import sys

values = []
speeds = []

for line in sys.stdin:
  values.append(line.strip().split())

pt, pd = values[0][0], values[0][1]

for i in range(1,len(values)):
  ct, cd = values[i][0], values[i][1]
  speeds.append((int(cd) - int(pd)) // (int(ct) - int(pt)))
  pt, pd = ct, cd

print(max(speeds))
