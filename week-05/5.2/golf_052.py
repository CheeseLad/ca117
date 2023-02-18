#!/usr/bin/env python3

import sys

lines = []
dict = {}
disq = []

def tagger(item):
  return item[1]

for line in sys.stdin:
  lines.append(line.strip())

for liner in lines:
  liner = liner.split()
  card = []
  values = []
  card.append(" ".join(liner[:len(liner) - 3]))
  values.append(liner[len(liner) - 3])
  values.append(liner[len(liner) - 2])
  values.append(liner[len(liner) - 1])
  total = 0

  for num in values:
    try:
      if int(num) >= 0:
        total = total + int(num)
      else:
        disq.append(card[0])
        break
    except ValueError:
      disq.append(card[0])
      break

  dict[card[0]] = int(total)

dict = sorted(dict.items(), key=tagger)

for line in dict:
  if line[0] not in disq:
    print(line[0] + ": " + str(line[1]))

if len(disq) > 0:
  print("Disqualified: " + ", ".join(disq))
