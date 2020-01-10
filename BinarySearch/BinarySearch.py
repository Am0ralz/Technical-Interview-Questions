# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search
# target in nums. If target exists, then return its index, otherwise return -1
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# n = [-1, 0, 3, 5, 9, 12]
# t = 2


# Output: -1
# Explanation: 2 does not exist in nums so return -1


class Solution(object):
    def search(self, nums, target):
        mins = 0
        maxs = len(nums)-1
        while mins <= maxs:
            guess = (mins+maxs)/2
            if target == nums[guess]:
                return guess
            if target < nums[guess]:
                maxs = guess - 1
            else:
                mins = guess +1
        return -1