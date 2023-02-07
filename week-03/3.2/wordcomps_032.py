#!/usr/bin/env python3

import sys

lines  = []
eletter = []

for line in sys.stdin:
  lines.append(line.strip())

def isVowels(str):
  chara, chare, chari, charo, charu = 0,0,0,0,0
  for char in str:
    if char == "a":
      chara = 1
    elif char == "e":
      chare = 1
    elif char == "i":
      chari = 1
    elif char == "o":
      charo = 1
    elif char == "u":
      charu = 1
  if chara + chare + chari + charo + charu == 5:
    return True

for word in lines:
  eletter.append(word.count("e"))

maxe = max(eletter)

print("Shortest word containing all vowels: " + str(min([word for word in lines if isVowels(word)], key=len)))
print("Words ending in iary: " + str(len([word for word in lines if word.endswith("iary")])))
print("Words with most e's: " + str([word for word in lines if word.count("e") == maxe]))
