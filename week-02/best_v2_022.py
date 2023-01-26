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
    if error == 0:
      tokens = line.strip().split()
      try:
        int(tokens[0])
        if int(tokens[0]) > highestmark and error == 0:
          highestmark = int(tokens[0])
          highestname = " ".join(tokens[1:])
      except ValueError:
        print(f"Invalid mark {tokens[0]} encountered. Exiting.")
        error = 1
  if error == 0:
    print(f"Best student: {highestname}")
    print(f"Best mark: {highestmark}")
