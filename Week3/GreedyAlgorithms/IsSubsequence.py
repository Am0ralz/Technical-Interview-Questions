# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length
# ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
# Example 1:
# a = "abc"
# b = "ahbgdc"
#
# Return true.
#
# Example 2:
# c = "axc"
# d = "ahbgdc"
#
# Return false.


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s == "":
            s = list(s)
            for i in reversed(t):
                if s[-1] == i:
                    del [s[-1]]
                if not s:
                    return True
            return False
        else:
            return True

