#!/usr/bin/env python3

class MP3Track(object):
    
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        r = []
        r.append("Title: {}".format(self.title))
        r.append("Duration: {}".format(self.duration))
        return "\n".join(r)
    
class MP3Collection(object):
    
    def __init__(self, d=None):
        if d == None:
            self.d = {}
        else:
            self.d = d

    def add(self, mp3):
        self.d[mp3.title] = mp3
    
    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def lookup(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None