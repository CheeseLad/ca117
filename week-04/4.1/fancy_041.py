#!/usr/bin/env python3

import sys

file = sys.argv[1]
phonebook = {}
names = []

with open(file, "r") as f_in:
  details = f_in.readlines()


for line in details:
  line = line.strip().split()
  phonebook[line[0]] = [line[1], line[2]]


for name in sys.stdin:
  names.append(name.strip())

for word in names:
  print(f"Name: {word}")
  if word in phonebook:
    print(f"Phone: {phonebook[word][0]}")
    print(f"Email: {phonebook[word][1]}")
  else:
    print("No such contact")
