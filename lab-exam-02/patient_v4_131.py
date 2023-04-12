#!/usr/bin/env python3

class Patient(object):

  def __init__(self, name, age, doctor, vitals=None):
    self.name = name
    self.age = age
    self.doctor = doctor
    if vitals == None:
      self.vitals = {}
    else:
      self.vitals = vitals

  def __str__(self):
    r = []
    r.append("Name: {}".format(self.name))
    r.append("Age: {}".format(self.age))
    r.append("Doctor: {}".format(self.doctor))
    return "\n".join(r)

  def record_vital(self, typ, num):
    self.vitals[typ] = num

  def get_vital(self, typ):
    if typ in self.vitals:
      return self.vitals[typ]
    else:
      return "N/A"
