from typing import List
from collections import defaultdict

class Solution:
    def isCyclic(self, src: int, graph, visited: List[int]) -> bool:
        visited[src] = 1
        visited[src] = 2

        for child in graph[src]:
            if visited[child] == 0:
                exists = self.isCyclic(child, graph, visited)
                if exists:
                    return True
            elif visited[child] == 2:
                return True

        visited[src] = 1
        return False

    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in pre:
            graph[v].append(u)
        visited = [0]*n

        for i in range(n):
            if visited[i] == 0:
                if self.isCyclic(i, graph, visited):
                    return False

        return True
