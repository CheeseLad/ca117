#!/usr/bin/env python3

import sys

lines = []

for line in sys.stdin:
  lines.append(line.strip())


for word in lines:
  print("h"+ "e" * word.count("e") * 2 +"y")
