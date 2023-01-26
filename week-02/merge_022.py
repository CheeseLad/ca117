#!/usr/bin/env python3

import sys

lista = []
listb = []

with open(sys.argv[1], "r") as filea:
  fileain = filea.readlines()

for i in range(len(fileain)):
  lista.append(fileain[i].strip())

with open(sys.argv[2], "r") as fileb:
  filebin = fileb.readlines()

for i in range(len(filebin)):
  listb.append(filebin[i].strip())

for numbers in range(len(lista) + len(listb)):
  if numbers < len(lista):
    print(lista[numbers])
  if numbers < len(listb):
    print(listb[numbers])

