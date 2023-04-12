#!/usr/bin/env python3

import sys

lines = []

for line in sys.stdin:
  lines.append(line.strip() + ":")

for test in lines:

  linesplit = []
  for char in test:
    linesplit.append(char)


  i = 0
  j = 0
  totals = []
  try:
    while i < len(test):
      i = j
      total = 0
      while test[i] == test[j]:
        j = j + 1
        total = total + 1

      totals.append(total)
      i = i + 1
  except IndexError:
    pass

  final = []
  count = 0
  for i in range(len(totals)):
    final.append(str(totals[i]) + str(linesplit[count]))
    count += totals[i]

  print("".join(final))
