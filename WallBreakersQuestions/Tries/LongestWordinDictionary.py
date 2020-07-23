from collections import defaultdict


# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built
# one character at a time by other words in words. If there is more than one possible answer, return the longest word
# with the smallest lexicographical order. If there is no answer, return the empty string.

# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
#
# Example 2: Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"] Output: "apple" Explanation: Both
# "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller
# than "apply".

from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie():

    def __init__(self):
        self.root = self.get_node()
        self.word = ""

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def set_word(self, w):
        self.word = w

    def insert(self, word):

        root = self.root
        len1 = len(word)
        count = 0
        for i in range(len1):
            index = self.get_index(word[i])
            if index not in root.children and len1 - i == 1:
                root.children[index] = self.get_node()
                count += 1
            elif index not in root.children:
                break

            root = root.children.get(index)
            root.terminating = True
        if count == 1 and len(word) > len(self.word) or (
                count == 1 and len(word) == len(self.word) and word < self.word):
            self.set_word(word)


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        t = Trie()
        words.sort(key=len)
        for word in words:
            t.insert(word)
        return (t.word)