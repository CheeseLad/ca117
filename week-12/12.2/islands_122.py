#!/usr/bin/env python3

import sys

class Graph(object):

   def __init__(self, V):
      self.V = V
      self.adj = {}
      for v in range(V):
         self.adj[v] = []

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

def search(v, visited, adj):
   visited[v] = True
   for w in adj[v]:
      if not visited[w]:
         search(w, visited, adj)

V = int(sys.stdin.readline().strip())

g = Graph(V)

for line in sys.stdin.readlines():
   v, w = [int(t) for t in line.strip().split()]
   g.addEdge(v, w)

islands = 0
visited = [False] * V
for v in range(V):
   if not visited[v]:
      islands += 1
      search(v, visited, g.adj)


print(islands)