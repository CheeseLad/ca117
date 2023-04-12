#!/usr/bin/env python3

class Patient(object):

  def __init__(self, name, age, doctor):
    self.name = name
    self.age = age
    self.doctor = doctor

  def __str__(self):
    r = []
    r.append("Name: {}".format(self.name))
    r.append("Age: {}".format(self.age))
    r.append("Doctor: {}".format(self.doctor))
    return "\n".join(r)

class Ward(object):

    def __init__(self, d=None):
        if d == None:
            self.d = {}
        else:
            self.d = d

    def add(self, p):
        self.d[p.name] = p

    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def lookup(self, name):
      if name in self.d:
        return self.d[name]
      else:
        return None