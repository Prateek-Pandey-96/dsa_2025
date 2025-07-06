from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, curr, graph, visited):
        visited[curr] = True
        
        for child in graph[curr]:
            if visited[child] == False:
                self.dfs(child, graph, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False]*n
        count = 0

        for i in range(n):
            if visited[i] == False:
                count += 1
                self.dfs(i, graph, visited)
        
        return count
