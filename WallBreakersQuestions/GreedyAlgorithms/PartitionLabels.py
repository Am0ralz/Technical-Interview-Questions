# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
# each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

t = "ababcbacadefegdehijhklij"


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        count = 0
        peak = 0
        for i, c in enumerate(S):
            count += 1
            if S.rfind(c) > peak:
                peak = S.rfind(c)
            if peak == i:
                ans.append(count)
                count = 0
        return(ans)



