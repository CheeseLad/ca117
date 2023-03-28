#!/usr/bin/env python3

import sys
names = []

for line in sys.stdin:
    names.append(line.strip())

left = []
right = []

for i in range(len(names)):
  if i % 2 != 0:
     left.append(names[i])
  elif i % 2 == 0:
     right.append(names[i])

for person in left[::-1]:
   right.append(person)

for word in right:
   print(word)