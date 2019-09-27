# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# s = "anagram"
# t = "nagaram"


# Output: true
# Example 2:
#
# s = "aa"
# t = "a"


# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        return self.dict(s) == self.dict(t)

    def dict(self, a):
        di = {}
        for i in a:
            if i in di:
                di[i] = di[i] + 1
            else:
                di[i] = 1
        return di
