# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Input = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            RowDict = {}
            ColDict = {}
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] in RowDict:
                        return False
                    else:
                        RowDict[board[i][j]] = 1

                if board[j][i] != ".":
                    if board[j][i] in ColDict:
                        return False
                    else:
                        ColDict[board[j][i]] = 1

                if j % 3 == 0 and i % 3 == 0:
                    matrix = {}
                    for k in range(0, 3):
                        for f in range(0, 3):
                            if board[k + i][j + f] != ".":
                                if board[i + k][j + f] in matrix:
                                    return False
                                else:
                                    matrix[board[i + k][j + f]] = 1
        return True

# def rowCheck(string):
#     row="".join(string).replace(".","")
#     return len(set(row))-len(row)
# def isValidSudoku(self, board):
#         table=zip(*board)
#         for i in range(0,9):
#             if rowCheck(board[i])!=0 or rowCheck(table[i])!=0:
#                 return False
#         i=0
#         while i<9:
#             j=0
#             while j<9:
#                 if rowCheck(board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3])!=0:
#                     return False
#                 j+=3
#             i+=3
#         return True


