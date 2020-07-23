# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(" ")
        dct = {}
        if len(pattern) == len(str):
            for i in range(0, len(pattern)):
                if pattern[i] in dct:
                    if dct[pattern[i]] != str[i]:
                        return False
                elif str[i] in dct.values():
                    return False
                else:
                    dct[pattern[i]] = str[i]
            return True
        else:
            return False


