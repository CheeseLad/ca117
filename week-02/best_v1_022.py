#!/usr/bin/env python3

import sys
error = 0
try:
  with open(sys.argv[1], "r") as f:
    lines = f.readlines()
except FileNotFoundError:
  print(f"The file {sys.argv[1]} could not be opened.")
  error = 1

highestmark = 0
highestname = ""
if error == 0:
  for line in lines:
    tokens = line.strip().split()
    if int(tokens[0]) > highestmark:
      highestmark = int(tokens[0])
      highestname = " ".join(tokens[1:])

  print(f"Best student: {highestname}")
  print(f"Best mark: {highestmark}")

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
