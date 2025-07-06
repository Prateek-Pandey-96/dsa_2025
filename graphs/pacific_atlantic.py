from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        queue = deque()

        pacific = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            queue.append((i, 0))
            pacific[i][0] = 1
        for j in range(1, n):
            queue.append((0, j))
            pacific[0][j] = 1

        
        while queue:
            x, y = queue.popleft()
            curr = heights[x][y]

            for i in range(4):
                newx, newy = x + dx[i], y + dy[i]
                
                if newx < 0 or newy < 0 or newx >= m or newy >= n or heights[newx][newy] < curr:
                    continue
                if pacific[newx][newy] != 0:
                    continue
                queue.append((newx, newy))
                pacific[newx][newy] = 1

        
        atlantic = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            queue.append((i, n-1))
            atlantic[i][n-1] = 1
        for j in range(n-1):
            queue.append((m-1, j))
            atlantic[m-1][j] = 1


        while queue:
            x, y = queue.popleft()
            curr = heights[x][y]

            for i in range(4):
                newx, newy = x + dx[i], y + dy[i]
                
                if newx < 0 or newy < 0 or newx >= m or newy >= n or heights[newx][newy] < curr:
                    continue
                if atlantic[newx][newy] != 0:
                    continue
                queue.append((newx, newy))
                atlantic[newx][newy] = 1


        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    result.append([i, j])

        return result


