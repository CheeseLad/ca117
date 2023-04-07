#!/usr/bin/env python3

class Triathlete(object):
    
  def __init__(self, name, tid, times=None):
    if times == None:
      self.times = {}
    else:
      self.times = times
    self.name = name
    self.tid = tid

  def __str__(self):
    r = []
    r.append("Name: {}".format(self.name))
    r.append("ID: {}".format(self.tid))
    r.append("Race time: {}".format(sum(self.times.values())))
    return "\n".join(r)
  
  def add_time(self, item, time):
    self.times[item] = time

  def get_time(self, item):
    return self.times[item]