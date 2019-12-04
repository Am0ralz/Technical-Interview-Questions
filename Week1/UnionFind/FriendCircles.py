# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in
# nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of
# C. And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1,
# then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total
# number of friend circles among all the students.

# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
#
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

class UnionFind:
    """
    Class that implements the union-find structure with
    union by rank and find with path compression
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]

    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1

    def printParent(self):
        print("index: ", list(range(9)))
        print("parent: ", self.parent)


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(len(M[0]))

        for i in range(len(M[0])):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    uf.union(i, j)
        for k in range(len(M[0])):
            uf.find(k)
        return len(set(uf.parent))


