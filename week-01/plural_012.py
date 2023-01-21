#!/usr/bin/env python3

import sys

es = ["ch","sh","x","s","z"]
vowel = ["a","e","i","o","u"]

for line in sys.stdin:
  line = line.strip()
  if line[-2:] in es or line[-1:] in es:
    print(line + "es")
  elif line[-2:-1] not in vowel and line[-1:] == "y":
    print(line[:len(line) - 1] + "ies")
  elif line[-1:] == "o":
    print(line + "es")
  elif line[-2:] == "fe":
    print(line[:len(line) - 2] + "ves")
  elif line[-1:] == "f":
    print(line[:len(line) - 1] + "ves")
  elif line[-1:] == "o":
    print(line + "es")
  else:
    print(line + "s")
