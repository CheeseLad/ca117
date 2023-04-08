#!/usr/bin/env python3

class MP3Track(object):
    
    def __init__(self, title, duration, artists=None):
        self.title = title
        self.duration = duration
        if artists == None:
            self.artists = []
        else:
            self.artists = artists

    def __str__(self):
        r = []
        r.append("Title: {}".format(self.title))
        r.append("By: {}".format(", ".join(self.artists)))
        r.append("Duration: {:01}:{:02}".format((self.duration // 60), (self.duration % 60)))
        return "\n".join(r)