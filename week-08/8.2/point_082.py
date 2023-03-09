#!/usr/bin/env python3

from math import sqrt
class Point(object):

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def distance(p1, p2):
    return sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2))

  def __str__(self):
    return "({:.1f}, {:.1f})".format(self.x, self.y)
