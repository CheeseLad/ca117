#!/usr/bin/env python3

import sys

for line in sys.stdin:
  linestrip = line.strip()
  linesstart = linestrip[0].capitalize()
  linesend = linestrip[len(linestrip) - 1].capitalize()
  print(linesstart + linestrip[1:len(linestrip) - 1] + linesend)
