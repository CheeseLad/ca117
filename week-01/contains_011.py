#!/usr/bin/env python3

import sys

for string in sys.stdin:
  string = string.strip()
  strings = string.split()
  strings[0] = strings[0].upper()
  strings[1] = strings[1].upper()
  counted = []
  length = []
  seen = []
  i = 0
  count = 0
  while i < len(strings[0]):
    if strings[0][i] in strings[1] and strings[0][i] not in seen:
      count = count + 1
      if strings[0][i] not in seen:
        seen.append(strings[0][i])
    i = i + 1
  counted.append(count)
  length.append(len(strings[0]))
  i = 0
  while i < len(counted):
    print(counted[i] == length[i])
    i = i + 1

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
