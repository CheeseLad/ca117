#!/usr/bin/env python3

import sys

test = sys.stdin.readline().strip()
final = []

i = 0
while int(test) not in range(1,10):
  for char in test:
    if char != "0":
      final.append(char)
      total = 1
  for nums in final:
    total = total * int(nums)
  final = []
  test = str(total)
  i = i + 1


if int(test) in range(1,10):
  print(test)
else:
  print(total)
