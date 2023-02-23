#!/usr/bin/env python3

import sys

lines = []
counts = {}

def tagger(item):
  return item[1]

for line in sys.stdin:
  lines.append(line.strip())

for lines2 in lines:
  words = lines2.split()
  for word in words:
    if word in counts:
      counts[word] +=1
    elif word not in counts:
      counts[word] = 1

csort = sorted(counts.items(), key=tagger, reverse=True)
ind = int(csort[0][1])
total = 0

for items in csort:
  if items[1] == ind:
    total = total + 1

print(total)
for items in csort:
  if items[1] == ind:
    print(items[0])
