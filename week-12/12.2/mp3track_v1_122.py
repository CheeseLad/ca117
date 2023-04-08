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