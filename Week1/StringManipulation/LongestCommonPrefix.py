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
        ans = ""
        a=len(min(strs, key=len))
        for i in range(0, a):
            for j in strs[1:]:
                if j[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans



