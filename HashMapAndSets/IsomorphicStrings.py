# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
a = "aba"
b = "baa"


# Output: false
# Example 3:
#
# a = "paper"
# b = "title"


# Output: true

class Solution(object):
    def isIsomorphic(self, s, t):
        dct = {}
        for i in range(0, len(s)):
            if s[i] in dct:
                if dct[s[i]] != t[i]:
                    return False
            elif t[i] in dct.values():
                return False
            else:
                dct[s[i]] = t[i]

        return True

