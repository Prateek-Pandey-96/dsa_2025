from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        queue = deque()
        queue.append(node)

        mp = {}
        mp[node] = Node(node.val)

        while queue:
            size = len(queue)

            while size > 0:
                curr = queue.popleft()
                
                for neighbor in curr.neighbors:
                    if neighbor not in mp:
                        mp[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    mp[curr].neighbors.append(mp[neighbor])
                size -= 1 

        return mp[node]
