#!/usr/bin/env python3

import sys
import string

lines = []
dups = {}
dupewords = {}

for line in sys.stdin:
    words = line.strip().split()
    words.append("\n")
    for word in words:
      lines.append(word)

for word in lines:
   for char in string.punctuation:
      word = word.replace(char, "")
   
   if word.lower() not in dups:
      dups[word.lower()] = 1
   elif word.lower() in dups:
      dups[word.lower()] += 1

for word in dups:
   if dups[word.lower()] > 1:
      dupewords[word.lower()] = 0

final = []
for word in lines:
   oldword = word
   for char in string.punctuation:
      word = word.replace(char, "")
   if word.lower() in dupewords and word != "\n":
      if dupewords[word.lower()] == 0:
        final.append(oldword)
        dupewords[word.lower()] = 1
      else:
         final.append(".")
   else:
      final.append(oldword)

finallist = []
sentence = []
for word in final:
   if word != "\n":
     sentence.append(word)
   elif word == "\n":
      finallist.append(" ".join(sentence))
      sentence = []

for line in finallist:
  print(line)