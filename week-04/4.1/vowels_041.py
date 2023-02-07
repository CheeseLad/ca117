#!/usr/bin/env python3

import sys

lines = []

vowels = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}

for line in sys.stdin:
  lines.append(line.strip().lower())

lines = "".join(lines)

for char in lines:
  if char in vowels:
    vowels[char] += 1

sortvowels = sorted(vowels.values(), reverse=True)
width = len(str(max(sortvowels)))

for number in sortvowels:
  if vowels["a"] == number:
    print(f"a : {number:{width}d}")
  if vowels["e"] == number:
    print(f"e : {number:{width}d}")
  if vowels["i"] == number:
    print(f"i : {number:{width}d}")
  if vowels["o"] == number:
    print(f"o : {number:{width}d}")
  if vowels["u"] == number:
    print(f"u : {number:{width}d}")
