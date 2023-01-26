#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip().split()
  linea, lineb = line[0], line[1]
  lineao, linebo = line[0], line[1]
  for char in max(line, key=len):
    if char in linea:
      lineb = lineb.replace(char, "", 1)
  if len(lineb) < 1 and len(lineao) == len(linebo):
    print("True")
  else:
    print("False")
