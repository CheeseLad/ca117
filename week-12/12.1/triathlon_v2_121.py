#!/usr/bin/env python3

class Triathlete(object):
    
  def __init__(self, name, tid):
    self.name = name
    self.tid = tid

  def __str__(self):
    r = []
    r.append("Name: {}".format(self.name))
    r.append("ID: {}".format(self.tid))
    return "\n".join(r)
  
class Triathlon(object):

  def __init__(self, d=None):
    if d == None:
      self.d = {}
    else:
      self.d = d

  def add(self, t):
    self.d[t.tid] = t

  def remove(self, t):
    if t in self.d:
      del(self.d[t])

  def lookup(self, t):
    if t in self.d:
      return self.d[t]
    else:
      return None
    
  def __str__(self):
    r = {}
    for t in self.d.values():
      r[t.name] = t.tid

    order = sorted(r.keys())
    ra = []
    for name in order:
      ra.append("Name: {}".format(name))
      ra.append("ID: {}".format(r[name]))
    return "\n".join(ra)
