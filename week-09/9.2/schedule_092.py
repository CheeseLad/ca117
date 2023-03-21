#!/usr/bin/env python3

class Meeting(object):

  def __init__(self, hour, minute, duration):
    self.hour = hour
    self.minute = minute
    self.duration = duration

  def __str__(self):
    return "{:02d}:{:02d} ({} minutes)".format(self.hour, self.minute, self.duration)

class Schedule(object):

  def __init__(self):
    self.l = []

  def add(self, m):
    self.l.append(str(m))

  def __str__(self):
    lines = []
    lines.append("Schedule")
    lines.append("--------")
    for line in sorted(self.l):
      lines.append(line)
    lines.append("Meetings today: {}".format(len(self.l)))
    return "\n".join(lines)
