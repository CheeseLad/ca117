#!/usr/bin/env python3

import sys

lines = []
words = {}

for line in sys.stdin:
    lines.append(line.strip())


for line in lines:
    words[line] = line.count("aa") + line.count("ee") + line.count("ii") + line.count("oo") + line.count("uu")


for word in words:
    if words[word] == max(words.values()):
        print(word)