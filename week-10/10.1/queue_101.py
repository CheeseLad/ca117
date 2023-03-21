#!/usr/bin/env python3

class Queue(object):
    def __init__(self):
        self.l = []

    def enqueue(self, e):
        self.l.append(e)
    
    def dequeue(self):
        index = self.l[0]
        self.l.pop(0)
        return index
    
    def first(self):
        return self.l[0]
    
    def is_empty(self):
        return len(self.l) == 0
    
    def __len__(self):
        return len(self.l)