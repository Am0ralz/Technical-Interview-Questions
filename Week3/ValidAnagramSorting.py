# Given two strings s and t , write a function to determine if t is an anagram of s.
# Example 1:
#
# s = "anagram"
# t = "nagaram"
#

# Output: true
# Example 2:
#
# Input:
s = "rat"
t = "car"
# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        s, t = sorted(s), sorted(t)
        return s == t


print(isAnagram(s, t))
