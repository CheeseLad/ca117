#!/usr/bin/env python3

import sys

numbers = input()
numbers = numbers.split()
letters = input()

oldnums = numbers
i = 0
while i < len(numbers):
  numbers[i] = int(numbers[i])
  i = i + 1
numbers.sort()
final = []

for c in letters:
  if c == "A":
    final.append(str(min(oldnums)))
  elif c == "B":
    final.append(str(numbers[1]))
  elif c == "C":
    final.append(str(max(oldnums)))

print(" ".join(final))
