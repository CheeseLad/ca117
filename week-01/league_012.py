#!/usr/bin/env python3

import sys

clubs = []
remain = []

for line in sys.stdin:
  line = line.strip()
  i = 0
  while i < len(line) and not line[i].isalpha():
    i = i + 1
  j = i
  while j < len(line) and (line[j].isalpha() or line[j] == " " or line[j] == "&"):
    j = j + 1
  clubs.append(line[i:j])
  remain.append(line[j:])

clublen = len(max(clubs, key=len))

print("POS CLUB" + " " * (clublen - 3) + "P   W   D   L  GF  GA  GD PTS")
pos = 1

for i in range(len(clubs)):
  tokens = remain[i].split()
  print(f"{pos:3d}" + " " + f"{clubs[i]:{clublen}s}" + f"{tokens[0]:3s} " + f"{tokens[1]:>2s}  " + f"{tokens[2]:>2s}  " + f"{tokens[3]:>2s}  " + f"{tokens[4]:>2s}  " + f"{tokens[5]:>2s} " + f"{tokens[6]:>3s} " + f"{tokens[7]:>3s}")
  pos = pos + 1

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
