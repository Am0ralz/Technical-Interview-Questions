from itertools import combinations

# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
# Example:
#
n = [1, 2, 3]


# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        for i in range(0, len(nums)+1):
            comb = list(combinations(nums, i))
            for j in list(comb):
                lst.append(list(j))
        return lst
