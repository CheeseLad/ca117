#!/usr/bin/env python3

import sys

x = []
y = []
for line in sys.stdin:
    line = line.strip().split()
    x.append(line[0])
    y.append(line[1])

for num in x:
    if x.count(num) == 1:
        x = num

for num in y:
    if y.count(num) == 1:
        y = num

print(x, y)