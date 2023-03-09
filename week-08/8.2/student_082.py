#!/usr/bin/env python3

class Student(object):

  def __init__(self, sid, name, modlist=None):
    self.sid = sid
    self.name = name
    if modlist == None:
     self.modlist = []
    else:
      self.modlist = modlist

  def add_module(self, mod):
    if mod not in self.modlist:
      self.modlist.append(mod)

  def del_module(self, mod):
    if mod not in self.modlist:
      self.modlist.remove(mod)

  def __str__(self):
    sortedlist = sorted(self.modlist)
    return f"ID: {self.sid}\nName: {self.name}\nModules: {', '.join(sortedlist)}"
