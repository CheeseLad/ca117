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
