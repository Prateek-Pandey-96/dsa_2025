from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        queue = deque()
        
        rotten = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    grid[i][j] = 0
                elif grid[i][j] == 1:
                    rotten += 1
        
        if len(queue) == 0 and rotten != 0:
            return -1
        elif len(queue) == 0 and rotten == 0:
            return 0

        time = -1
        while queue:
            size = len(queue)
            while size > 0:
                x, y = queue.popleft()
                for i in range(4):
                    newx, newy = x + dx[i], y + dy[i]
                    if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy]==0:
                        continue
                    queue.append((newx, newy))
                    grid[newx][newy] = 0
                size -= 1
            time += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return time
