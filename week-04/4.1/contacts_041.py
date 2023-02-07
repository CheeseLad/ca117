#!/usr/bin/env python3

import sys

phonebook = {}
names = []

file = sys.argv[1]

with open(file, "r") as f_in:
  readin = f_in.readlines()

for line in readin:
  line = line.strip().split()
  phonebook[line[0]] = line[1]

for line in sys.stdin:
  names.append(line.strip())

for name in names:
  print(f"Name: {name}")
  if name in phonebook:
    print(f"Phone: {phonebook[name]}")
  else:
    print("No such contact")
