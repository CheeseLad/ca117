class DFSPaths(object):
    
    def __init__(self, g, s):
      self.g = g
      self.s = s
      self.visited = [False] * g.V
      self.parent = [-1] * g.v
      
      self.dfs(s)

    def dfs(self, v):
       self.visited[v] = True
       for w in self.g.adj[v]:
          if not self.visited[w]:
             self.parent[w] = v
             self.dfs[w]

    def hasPathTo(self, v):
       return self.visited[v]
    
    def pathTo(self, v):
       if not self.hasPathTo(v):
          return []
       
       path = [v]
       while v != self.s:
          v = self.parent[v]
          path.append(v)
      
       return path[::-1]