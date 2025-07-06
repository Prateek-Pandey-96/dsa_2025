from typing import List
from collections import defaultdict

class Solution:
  def dfs(self, curr, par, graph, visited) -> bool:
      visited[curr] = True

      for child in graph[curr]:
          if visited[child] == False:
              if (self.dfs(child, curr, graph, visited)):
                  return True
          elif child != par:
              return True
      return False
          

  def validTree(self, n: int, edges: List[List[int]]) -> bool:
      # there should be n-1 edges
      ln = len(edges)
      if ln != n-1:
          return False

      # there should be no cycles
      graph = defaultdict(list)
      for u,v in edges:
          graph[u].append(v)
          graph[v].append(u)

      visited = [False] * n

      cyclic = self.dfs(0, -1, graph, visited)
      if cyclic:
          return False

      # there should be no unvisited node
      for i in range(n):
          if visited[i] == False:
              return False

      return True


        
