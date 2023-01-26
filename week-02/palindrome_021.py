#!/usr/bin/env python3

import sys
import string

for line in sys.stdin:
  word = []
  line = line.strip().lower()
  for i in range(len(line)):
    if line[i] not in string.punctuation and line[i] != " ":
      word.append(line[i])
  wordcomplete = "".join(word)
  print(wordcomplete == wordcomplete[::-1])
