#!/usr/bin/env python3

import sys

for line in sys.stdin:
  i = 0
  line = line.strip()
  while i < len(line) and line[i] != "m":
    i = i + 1
  if i < len(line):
    print(line[:i] + "M" + line[i + 1:])
  else:
    print(line)
