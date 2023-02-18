#!/usr/bin/env python3

import sys

pos = int(sys.stdin.readline().rstrip())
moves = sys.stdin.readline().rstrip()

for char in moves:
  set = "contd"
  if char == "A":
    if pos == 1 and set != "done":
      pos = 2
      set = "done"
    elif pos == 2 and set != "done":
      pos = 1
      set = "done"
  elif char == "B" and set != "done":
    if pos == 2 and set != "done":
      pos = 3
      set = "done"
    elif pos == 3 and set != "done":
      pos = 2
      set = "done"
  elif char == "C" and set != "done":
    if pos == 3 and set != "done":
      pos = 1
      set = "done"
    elif pos == 1 and set != "done":
      pos = 3
      set = "done"

print(pos)
