from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        
        def dfs(x: int, y: int):
            grid[x][y] = "0"

            for idx in range(4):
                newx, newy = x + dx[idx], y + dy[idx]
                if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy]=="0":
                    continue
                dfs(newx, newy)
            

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count
