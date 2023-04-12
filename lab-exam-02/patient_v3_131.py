#!/usr/bin/env python3

class Patient(object):

  def __init__(self, name, age, doctor, medication=None):
    self.name = name
    self.age = age
    self.doctor = doctor
    if medication == None:
      self.medication = []
    
    self.medication = medication

  def add_medication(self, med):
    if self.medication == None:
      self.medication = []
    self.medication.append(med)
    

  def __str__(self):
    r = []
    r.append("Name: {}".format(self.name))
    r.append("Age: {}".format(self.age))
 #   if len(self.medication) > 0:
    if self.medication == None:
      self.medication = []
    r.append("Medications: {}".format(", ".join(self.medication)))
 #   else:
 #     r.append("Medications: ")
    r.append("Doctor: {}".format(self.doctor))
    return "\n".join(r)
