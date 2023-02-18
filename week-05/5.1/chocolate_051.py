#!/usr/bin/env python3

import sys


for line in sys.stdin:
 chocs = [400]
 i = 400
 while i < int(line):
   i = i + 400
   chocs.append(i)

 if int(line) > 0:
   print(len(chocs))
 else:
   print("0")
