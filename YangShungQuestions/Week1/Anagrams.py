# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
a = "anagram"
b = "nagaram"
# Output: true
# Example 2:
#
c = "rat"
d = "car"


# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s, t = sorted(s), sorted(t)
    return s == t
