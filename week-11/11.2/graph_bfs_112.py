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

class BFSPaths(object):
    
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = [False] * g.V
        self.parent = [False] * g.V
        self.bfs(s)

    def bfs(self, s):

        queue = [s]
        self.marked[s] = True
        while len(queue) > 0:
            item = queue[0]
            parent = queue.pop(0)
            for w in self.g.adj[item]:
                if self.marked[w] == False:
                  self.parent[w] = parent
                  queue.append(w)
                  self.marked[w] = True

    def hasPathTo(self, v):
        return self.marked[v]
    
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return []
        
        path = [v]
        while v != self.s:
             v = self.parent[v]
             path.append(v)

        return path[::-1]