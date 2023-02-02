#!/usr/bin/env python3

import sys

lines = []

for line in sys.stdin:
  lines.append(line.strip())

def qnou(inpt):
  inpt = inpt.replace("qu", "**")
  return inpt

print("Words with q but no u: " + str([word for word in lines if "q" in qnou(word.lower())]))
