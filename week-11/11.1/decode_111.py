#!/usr/bin/env python3

import sys
lines = []

for inputs in sys.stdin:
  lines.append(inputs.strip())

for word in lines:
    if "apa" in word:
      word = word.replace("apa", "a")
    if "epe" in word:
      word = word.replace("epe", "e")
    if "ipi" in word:
      word = word.replace("ipi", "i")
    if "opo" in word:
      word = word.replace("opo", "o")
    if "upu" in word:
      word = word.replace("upu", "u")
    
    print(word)