#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

i = 0
while i < len(words):
  words[i] = words[i].rstrip()
  i = i + 1

#print(words)

i = 0
while i < len(words):
  if len(words[i]) >= 3:
    print(words[i][1:len(words[i]) - 1])
  i = i + 1

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
