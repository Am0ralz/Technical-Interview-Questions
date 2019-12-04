# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X

class UnionFindRegion:
    """
    Class that implements the union-find structure with
    union by rank and find with path compression
    """

    def __init__(self, n):
        row = len(n)
        col = len(n[0])
        self.parent = {x * col + y: x * col + y for x in range(row) for y in range(col) if n[x][y] == "O"}
        self.parent[row * col] = row * col

    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot != yRoot:
            self.parent[xRoot] = yRoot


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return 0
        row = len(board)
        col = len(board[0])
        ufr = UnionFindRegion(board)

        for x in range(row):
            for y in range(col):
                if board[x][y] == 'O':
                    if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                        ufr.union(x * col + y, row * col)
                        continue

                    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 'O':
                            ufr.union(x * col + y, nx * col + ny)

        for x in range(row):
            for y in range(col):
                if board[x][y] == 'O' and ufr.find(x * col + y) != ufr.find(row * col):
                    board[x][y] = 'X'