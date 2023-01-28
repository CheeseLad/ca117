#!/usr/bin/env python3

import sys

digits = []

i = 0
while i < 10:
  digits.append(i)
  i = i + 1

#print(digits)

for email in sys.stdin:
  email = email.strip()
  names = email.split(".")
  second = names[1].split("@")
  i = 0
  while i < len(second[0]) and (second[0][i] < "0" or second[0][i] > "9"):
    i = i + 1
  print(names[0].capitalize() + " " + second[0][:i].capitalize())

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
