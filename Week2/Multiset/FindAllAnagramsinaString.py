# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
# Example 1:
#
# Input:
a = "cbaebabacd"
b = "abc"
#
# Output:
# [0, 6]
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#

from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        indexs = []
        l = len(p)
        cp = Counter(p)
        cs = None
        i = 0
        while i + l <= len(s):
            if i == 0:
                cs = Counter(s[:l])
            else:
                cs[s[i + l - 1]] += 1
            if cs == cp:
                indexs.append(i)
            cs[s[i]] -= 1
            if cs[s[i]] == 0:
                del cs[s[i]]
            i += 1
        return indexs
