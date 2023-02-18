#!/usr/bin/env python3

import sys
import string

alphabet = "abcdefghijklmnopqrstuvwxyz"
lines = []

for line in sys.stdin:
  lines.append(line.strip())

for word in lines:
  list = []
  input = word.lower()

  for c in input:
    if c not in string.punctuation and c in alphabet:
      list.append(c)

  list = sorted(list)
  list = "".join(list)

  final = []
  for char in alphabet:
    if char not in list:
      final.append(char)

  if len(final) >= 1:
    print("missing " + "".join(final))
  else:
    print("pangram")
