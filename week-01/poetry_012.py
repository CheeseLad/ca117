#!/usr/bin/env python3

import sys

lines = []

for line in sys.stdin:
  lines.append(line.strip())

biggest = len(max(lines, key=len))

for line in lines:
  line = line.strip()
  print(f"{line:^{biggest:d}s}")
