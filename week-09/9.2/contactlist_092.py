#!/usr/bin/env python3

class Contact(object):

  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

  def __str__(self):
    return "{} {} {}".format(self.name, self.phone, self.email)

class Contactlist(object):

  def __init__(self):
    self.d = {}

  def add(self, c):
    self.d[c.name] = c

  def get(self, name):
    if name in self.d:
      return self.d[name]
    else:
      return None

  def remove(self, name):
    if name in self.d:
      self.d.pop(name)
    else:
      return None

  def __str__(self):
    lines = []
    lines.append("Contact list")
    lines.append("------------")
    for k, v in sorted(self.d.items()):
      lines.append("{}".format(v))
    return "\n".join(lines)

