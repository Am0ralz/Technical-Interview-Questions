# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.


def isvalid(board, num, position):
    for i in range(len(board[0])):

        if board[position[0]][i] == str(num) and position[1] != i:
            return False

    for i in range(len(board)):
        if board[i][position[1]] == str(num) and position[0] != i:
            return False

    XBox = position[1] // 3
    YBox = position[0] // 3

    for i in range(YBox * 3, YBox * 3 + 3):

        for j in range(XBox * 3, XBox * 3 + 3):

            if board[i][j] == str(num) and (i, j) != position:
                return False

    return True


def checkEmpty(board):
    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j] == '.':
                return i, j

    return None


class Solution(object):
    def solveSudoku(self, board):
        checked = checkEmpty(board)
        if not checked:
            return True
        else:
            row, col = checked

        for i in range(1, 10):

            if isvalid(board, i, (row, col)):
                board[row][col] = str(i)

                if self.solveSudoku(board):
                    return True

                board[row][col] = "."

        return False
