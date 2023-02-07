#!/usr/bin/env python3

import sys
import string

words = []
wordcount = {}

for line in sys.stdin:
  words.append(line.lower().strip())

words = "".join(words)

for char in words:
  if char in string.punctuation and char != "'":
    words = words.replace(char, " ", 1)

words = sorted(words.split())

for word in words:
  if word not in wordcount:
    wordcount[word] = 1
  else:
    wordcount[word] +=1

for word in wordcount:
  print(f"{word} : {wordcount[word]}")
