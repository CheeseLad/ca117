#!/usr/bin/env python3

import sys

f, s, g, u, d = [int(t) for t in sys.stdin.readline().strip().split()]

if g - s >= 0:
  buttons = []
  i = s
  while i < g:
      buttons.append(i)
      i = i + u
      if i > g and i != g:
         buttons.append(i)
         i = i - d

if g - s <= 0:
  buttons = []
  i = s
  while i < g:
      buttons.append(i)
      i = i - d

if i <= f:
  print(len(buttons))
else:
  print("Sorry Sheila!")