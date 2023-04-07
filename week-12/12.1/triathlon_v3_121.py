#!/usr/bin/env python3

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
  
  def __eq__(self, other):
    return sum(self.times.values()) == sum(other.times.values())
  
  def __lt__(self, other):
    return sum(self.times.values()) < sum(other.times.values())
  

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
  
  def best(self):
    r = {}
    for t in self.d.values():
      r[sum(t.times.values())] = (t.name, t.tid, sum(t.times.values()))
    
    order = sorted(r)[0]
    ra = []
    ra.append("Name: {}".format(r[order][0]))
    ra.append("ID: {}".format(r[order][1]))
    ra.append("Race time: {}".format(r[order][2]))
    return "\n".join(ra)
  
  def worst(self):
    r = {}
    for t in self.d.values():
      r[sum(t.times.values())] = (t.name, t.tid, sum(t.times.values()))
    
    order = sorted(r, reverse=True)[0]
    ra = []
    ra.append("Name: {}".format(r[order][0]))
    ra.append("ID: {}".format(r[order][1]))
    ra.append("Race time: {}".format(r[order][2]))
    return "\n".join(ra)
