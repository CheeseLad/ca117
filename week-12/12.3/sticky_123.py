#!/usr/bin/env python3

from re import findall
import sys

line1 = sys.stdin.readline().strip().split()
line2 = sys.stdin.readline().strip()
line2split = line2.split()


for line in line1:
    if line in line2split:
        line2 = line2.replace(line, "", 1)

p = r'\w{2}'

processed = findall(p, line2)

line2 = line2 + "??"

keys = []
for i in range(len(line2)):
    if line2[i] != "?":
     if line2[i] == line2[i + 1]:
          keys.append(line2[i] + line2[i + 1])

listkey = []
for w in keys:
    if w.count(w[0]) == 2 and w[0] not in listkey and w[0] != " ":
        listkey.append(w[0])

if len(listkey) > 0:
  print("".join(sorted(listkey)))