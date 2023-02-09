#!/usr/bin/env python3

test = {"key" : "value", "key2" : "value2"}

def swap_keys_values(d):
  keys = list(d.keys())
  values = list(d.values())
  return dict(zip(values, keys))
