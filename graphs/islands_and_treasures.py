from typing import List
from collections import deque

class Solution:
  def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    m, n = len(grid), len(grid[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                queue.append((i, j))
    
    level = 0
    inf = 2147483647
    while queue:
        size = len(queue)
        level += 1
        while size > 0:
            x, y = queue.popleft()
            for i in range(4):
                newx, newy = x + dx[i], y + dy[i]
                if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] != inf:
                    continue
                grid[newx][newy] = level
                queue.append((newx, newy))
            size -= 1


