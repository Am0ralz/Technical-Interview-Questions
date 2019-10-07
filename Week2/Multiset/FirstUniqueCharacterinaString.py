# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Examples:
#
# g = "leetcode"
# return 0.
#
# t = "loveleetcode"
# return 2.

from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sCounter = Counter(list(s))
        for count, ele in enumerate(s):
            if sCounter[ele] == 1:
                return count
        return -1
