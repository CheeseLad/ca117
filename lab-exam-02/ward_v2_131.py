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

  def add_medication(self, med):
    medication.append(med)

  def __str__(self):
    r = []
    r.append("Name: {}".format(self.name))
    r.append("Age: {}".format(self.age))
    r.append("Medications: {}".format(", ".join(self.medication)))
    r.append("Doctor: {}".format(self.doctor))
    return "\n".join(r)

class Ward(object):

    def __init__(self, d=None, medd=None):
        if d == None:
            self.d = {}
        else:
            self.d = d
        if medd == None:
            self.medd = {}
        else:
            self.medd = medd

    def add(self, p):
        self.d[p.name] = p
        self.medd[p.name] = p.medication

    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def lookup(self, name):
      if name in self.d:
        return self.d[name]
      else:
        return None

    def get_patients_by_med(self, medtype):
      newlst = []
      for w in self.d:
        newlst.append((w, self.d[w].medication))
      final = []
      for w in newlst:
        if medtype in w[1]:
          final.append(self.d[w[0]])

      return final