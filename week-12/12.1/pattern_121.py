#!/usr/bin/env python3

import sys

pattern = sys.stdin.readline().strip()
words = []
words_original =[]
final = []
new = []
wordsplit = []

for line in sys.stdin.readlines():
    if len(line.strip()) == len(pattern):
      words.append(line.strip())
      words_original.append(line.strip())



for word in words:
  for i in range(len(pattern)):
     if pattern[i] == "-":
        wordsplit.append("-")
     else:
        wordsplit.append(word[i])
        #word = word.replace(word[i], "-", 1)
  wordsplit.append("\n")
  newword = "".join(wordsplit)
final.append(newword)

final = "".join(final)
final = final.split()

for i in range(len(final)):
   if final[i] == pattern:
      new.append(words_original[i])

if len(new) > 0:
  print(", ".join(new))