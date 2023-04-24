#!/usr/bin/env python3

chess = [2,2,4,4,4,16]
import sys

for line in sys.stdin:
    line = line.strip().split()
    line = [int(t) for t in line]
    final = []
    for i in range(len(line)):
        final.append(chess[i] - line[i])
    final = [str(t) for t in final]
    print(" ".join(final))