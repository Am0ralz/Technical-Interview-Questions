# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example:
#
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie():

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)

        root.terminating = True


class Solution(object):
    def findWords(self, board, words):
        t = Trie()
        root = t.root
        lstWrds = []
        for w in words:
            t.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, root, i, j, "", lstWrds)
        return lstWrds

    def dfs(self, board, root, i, j, path, lstWrds):
        if root.terminating:
            lstWrds.append(path)
            root.terminating = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        root = root.children.get(ord(tmp) - ord('a'))
        if not root:
            return
        board[i][j] = "#"
        self.dfs(board, root, i + 1, j, path + tmp, lstWrds)
        self.dfs(board, root, i - 1, j, path + tmp, lstWrds)
        self.dfs(board, root, i, j - 1, path + tmp, lstWrds)
        self.dfs(board, root, i, j + 1, path + tmp, lstWrds)
        board[i][j] = tmp