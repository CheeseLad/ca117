#!/usr/bin/env python3

import sys

l = "angel"

def anagram(l,r):
  if r != "angle":
    r = r.lower()
    l = l.lower()
    for c in l:
     if c in l:
       r = r.replace(c, "", 1)
    if len(r) == 0:
      return True
    else:
      return False
  else:
      return False

lines = []

for word in sys.stdin:
  lines.append(word.strip())

print("Words containing 17 letters: " + str([line for line in lines if len(line) == 17]))
print("Words containing 18+ letters: " + str([line for line in lines if len(line) >= 18]))
print("Words with 4 a's: " + str([line for line in lines if (line.count("a") + line.count("A") == 4)]))
print("Words with 2+ q's: " + str([line for line in lines if (line.count("q") + line.count("Q") >= 2)]))
print("Words containing cie: " + str([line for line in lines if "cie" in line]))
print("Anagrams of angle: " + str([line for line in lines if anagram(l, line) and len(line) == 5]))

