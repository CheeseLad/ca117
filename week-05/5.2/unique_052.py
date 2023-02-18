#!/usr/bin/env python3

import sys
lines = []

for line in sys.stdin:
  lines.append(line.strip())

for nums in lines:
  digits = [int(n) for n in nums.strip().split()]
  uniques = [n for n in digits if digits.count(n) == 1]
  if len(uniques) != 0:
    print(max(uniques))
  else:
    print("none")
