#!/usr/bin/env python3

class Student(object):

  def __init__(self, name, id, module_mark):
    self.name = name
    self.id = id
    self.module_mark = module_mark

  def __str__(self):
    lines = []
    modules = []
    marks = []
    for line in self.module_mark:
      modules.append(line[0])
      marks.append(line[1])
    total = 0
    for num in marks:
      total = total + int(num)
    avg_mark = total / len(marks)
    modules = sorted(modules)
    lines.append("Name: {}".format(self.name))
    lines.append("ID: {}".format(self.id))
    lines.append("Modules: {}".format(", ".join(modules)))
    lines.append("Average mark: {:.0f}".format(avg_mark))
    return "\n".join(lines)

class Classlist(object):

  def __init__(self):
    self.l = []

  def add(self, other):
    self.l.append(str(other))

  def __str__(self):
    markcount = {}
    newline = []
    for line in self.l:
      tokens = line.split()
      markcount[line] = tokens[len(tokens) - 1]
    for k, v in sorted(markcount.items()):
      newline.append(k)
    return "\n".join(newline)
