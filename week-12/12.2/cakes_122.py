#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = [int(t) for t in line.strip().split()]
    line = sorted(line, reverse=True)
    print(sum(line) - sum(line[2::3]))