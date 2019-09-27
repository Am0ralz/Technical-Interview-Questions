# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
from typing import List, Any


# Input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

class Solution(object):
    def transpose(self, A):
        cols = len(A)
        rows = len(A[0])
        matrix = [[0 for col in range(cols)] for row in range(rows)]
        for i in range(cols):
            for j in range(rows):
                matrix[j][i] = A[i][j]
        return matrix


