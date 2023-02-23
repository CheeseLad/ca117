#!/usr/bin/env python3

import sys

capacity = int(input())
startcap = capacity

lines = []
denied = 0

for line in sys.stdin:
  lines.append(line.strip())

for lines2 in lines:
  tokens = lines2.split()
  if tokens[0] == "enter":
    if int(tokens[1]) > capacity:
      denied = denied + 1
    elif startcap > 0:
      capacity = capacity - int(tokens[1])
  elif tokens[0] == "leave" and startcap > 0:
    capacity = capacity + int(tokens[1])

print(denied)
