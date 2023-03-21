#!/usr/bin/env python3

class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def midpoint(self, other):
    x_point = (self.x + other.x) / 2
    y_point = (self.y + other.y) / 2
    return Point(x_point, y_point)

  def __str__(self):
    return f"({self.x:.1f}, {self.y:.1f})"

class Circle(object):
  def __init__(self, centre=None, radius=1):
    self.radius = radius
    if centre == None:
      self.centre = Point(0, 0)
    else:
      self.centre = centre

  def __str__(self):
    return f"Centre: {self.centre}\nRadius: {self.radius}"

