#!/usrbin/env python3

import sys
import string

data = []
processed = []
wordcount = []

for line in sys.stdin:
  line = line.strip()
  data.append(line)

data = str(" ".join(data))

for c in data:
  if c not in string.punctuation:
    processed.append(c.lower())

processed = "".join(processed)
processed = processed.split()

i = 0
while i < len(processed):
  if processed[i] not in wordcount:
    wordcount.append(processed[i])
  i = i + 1

print(len(wordcount))

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
