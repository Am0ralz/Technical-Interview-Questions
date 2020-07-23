# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
# Note:
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.

# Example
# 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false


class Solution(object):
    def canPartition(self, nums):
        cache = {0}
        if sum(nums) % 2 != 0:
            return False

        sumSubset = sum(nums) / 2

        for num in nums:
            path = []

            for c in cache:

                if sumSubset == c + num:
                    return True

                if sumSubset > c + num:
                    path.append(c + num)

            cache.update(path)
        return False

