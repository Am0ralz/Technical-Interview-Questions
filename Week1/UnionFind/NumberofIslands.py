# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
# and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.

# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

class UnionFindGrid:

    def __init__(self, n):
        row = len(n)
        col = len(n[0])
        self.count = sum(n[i][j] == '1' for i in range(row) for j in range(col))
        self.parent = [i for i in range(row * col)]

    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot: return
        self.parent[xRoot] = yRoot
        self.count -= 1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        ufg = UnionFindGrid(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i * col + j
                if j < col - 1 and grid[i][j + 1] == '1':
                    ufg.union(index, index + 1)
                if i < row - 1 and grid[i + 1][j] == '1':
                    ufg.union(index, index + col)
        return ufg.count
