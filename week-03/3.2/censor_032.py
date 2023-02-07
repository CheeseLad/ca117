#!/usr/bin/env python3

import sys

filename = sys.argv[1]
inputs = []

with open(filename, "r") as f_in:
  inputs = f_in.readlines()

lines = []
modline = []

for line in sys.stdin:
  lines.append(line.strip())

for i in range(len(lines)):
  for item in inputs:
    lines[i] = lines[i].replace(item.strip(), "@" * len(item.strip()))

print("\n".join(lines))
