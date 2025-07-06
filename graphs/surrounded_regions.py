from typing import List

class Solution:
    def dfs(self, x, y, board):
        board[x][y] = '#'
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        m, n = len(board), len(board[0])
 
        for i in range(4):
            newx, newy = x + dx[i], y + dy[i]
            if newx < 0 or newy < 0 or newx >= m or newy >= n:
                continue
            if board[newx][newy] != 'O':
                continue
            self.dfs(newx, newy, board)

    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][n-1] == 'O':
                self.dfs(i, n-1, board)


        for j in range(1, n):
            if board[0][j] == 'O':
                self.dfs(0, j, board)
            if board[m-1][j] == 'O':
                self.dfs(m-1, j, board)


        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
