from itertools import permutations

# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# I = [1, 2, 3]

# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


from itertools import permutations


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        perm = permutations(nums)
        for j in list(perm):
            lst.append(list(j))
        return lst
