from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      m, n = len(grid), len(grid[0])
      dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
      
      def dfs(x, y):
        grid[x][y] = 0
        
        size = 1
        for i in range(4):
          newx, newy = x + dx[i], y + dy[i]
          if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] == 0:
            continue
          size += dfs(newx, newy)

        return size
  

      max_area = 0
      for i in range(m):
        for j in range(n):
          if grid[i][j] == 1:
            max_area = max(max_area, dfs(i, j))
      
      return max_area
