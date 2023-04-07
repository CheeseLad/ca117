#!/usr/bin/env python3

import sys

lines = []
words = {}
final = []

for line in sys.stdin:
    lines.append(line.strip())
    line = line.strip().split()
    for word in line:
      words[word] = 0

for line in lines:
      line = line.split()
      for word in line:
        if word in words:
           words[word] += 1

for word in words:
   if words[word] >= len(lines):
      final.append(word)

print(len(final))
if len(final) > 0:
  print("\n".join(sorted(final)))