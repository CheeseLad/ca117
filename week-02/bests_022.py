#!/usr/bin/env python3

import sys
error = 0
try:
  with open(sys.argv[1], "r") as f:
    lines = f.readlines()
except FileNotFoundError:
  print(f"The file {sys.argv[1]} could not be opened.")
  error = 1

beststudents = []
highestmark = 0
highestname = ""

if error == 0:
  for line in lines:
    tokens = line.strip().split()
    if int(tokens[0]) > highestmark:
      highestmark = int(tokens[0])
      highestname = " ".join(tokens[1:])

if error == 0:
  for line in lines:
    tokens = line.strip().split()
    if int(tokens[0]) == highestmark:
      beststudents.append(" ".join(tokens[1:]))
  beststudents = ", ".join(beststudents)

  print(f"Best student(s): {beststudents}")
  print(f"Best mark: {highestmark}")
