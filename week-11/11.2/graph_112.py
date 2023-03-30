#!/usr/bin/env python3

class Graph(object):
    
    def __init__(self, V):
        self.V = V
        self.adj = {}
        for i in range(self.V):
            self.adj[i] = [] * V

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])
    
    def maxDegree(self):
        return max([len(n) for n in self.adj.values()])
    
    def avgDegree(self):
        averages = []
        [averages.append(len(n)) for n in self.adj.values()]
        total = 0
        for n in averages:
            total = total + int(n)
        return float(total / len(averages))