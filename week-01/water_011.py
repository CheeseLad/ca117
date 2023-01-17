#!/usr/bin/env python3

import sys

litres = sys.stdin.readline().rstrip()
capacity = sys.stdin.readline().rstrip()
buckets = capacity.split()
#print(litres)
#print(buckets)

total = 0
i = 0
while i < len(buckets):
  total = total + int(buckets[i])
  if total > int(litres):
    done = i
    i = len(buckets)
  elif total > len(buckets):
    done = len(buckets)
  i = i + 1

print(done)
