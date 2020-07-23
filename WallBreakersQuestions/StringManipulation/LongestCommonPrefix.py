# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input = ["flower", "flow", "flight"]


# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        ans = ""
        a = min(strs, key=len)
        for i in range(len(a)):
            for word in strs:
                if word != a:
                    if word[i] != a[i]:
                        return ans
            ans += a[i]
        return ans