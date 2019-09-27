# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# n = [2, 7, 11, 15]
# t = 9


#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 1
        for i in range(0, len(nums) - 1):
            for j in range(k, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            k += 1

# dict1 = {}  # {num:index}
#
# for i, num in enumerate(nums):
#     if (target - num) in dict1:
#         return [i, dict1[target - num]]
#     else:
#         dict1[num] = i