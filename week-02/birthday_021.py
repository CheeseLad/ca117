#!/usr/bin/env python3

import sys
import calendar

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dayline = [" and Monday's child is fair of face.", " and Tuesday's child is full of grace.", "and Wednesday's child is full of woe.", " and Thursday's child has far to go.", " and Friday's child is loving and giving.", " and Saturday's child works hard for a living.", " and Sunday's child is fair and wise and good in every way."]

for line in sys.stdin:
  lines = line.strip().split()
  day = days[calendar.weekday(int(lines[2]), int(lines[1]), int(lines[0]))]
  daysay = dayline[calendar.weekday(int(lines[2]), int(lines[1]), int(lines[0]))]
  print("You were born on a " + day + daysay)

#CA117 Solution by CheeseLad (https://github.com/CheeseLad)
