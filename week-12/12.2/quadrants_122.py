#!/usr/bin/env python3

import sys

for line in sys.stdin:
    x, y = line.strip().split()
    x, y = int(x), int(y)
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x < 0 and y > 0:
        print(4)