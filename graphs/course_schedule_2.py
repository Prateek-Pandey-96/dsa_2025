from typing import List
from collections import defaultdict, deque

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


    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        indegree = [0]*n
        result = []
        for u, v in pre:
            graph[v].append(u)
            indegree[u] += 1
        
        visited = [0]*n
        for i in range(n):
            if visited[i] == 0:
                if self.isCyclic(i, graph, visited):
                    return result


        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            size = len(queue)
            while size>0:
                curr = queue.popleft()
                result.append(curr)
                for child in graph[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)

                size -= 1

        return result
