#!/usr/bin/env python3

class Patient(object):

  def __init__(self, name, age, doctor, medication=None):
    self.name = name
    self.age = age
    self.doctor = doctor
    if medication == None:
      self.medication = []
    else:
      self.medication = medication

  def add_meedication(self, med):
    medication.append(med)

  def __str__(self):
    r = []
    r.append("Name: {}".format(self.name))
    r.append("Age: {}".format(self.age))
    r.append("Medications: {}".format(", ".join(self.medication)))
    r.append("Doctor: {}".format(self.doctor))
    return "\n".join(r)
