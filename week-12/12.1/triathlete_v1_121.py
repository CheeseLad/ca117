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