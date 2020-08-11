# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4] Output: [24,12,8,6] Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up: Could you solve it with constant space complexity? (The output array does not count as extra space for
# the purpose of space complexity analysis.)

import math


# def productExceptSelf(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     ans = []
#
#     for i in range(0, len(nums)):
#         right = 1
#         left = 1
#         if i < len(nums) - 1:
#             for j in range(i+1, len(nums)):
#                 right = nums[j] * right
#         if i > 0:
#             for k in range(0, i):
#                 left = nums[k] * left
#         ans.append(left * right)
#
#     return ans

#anser from leetcode
# def productExceptSelf(nums):
#     p = 1
#     n = len(nums)
#     output = []
#     for i in range(0, n):
#         print(p)
#         output.append(p)
#         p = p * nums[i]
#     p = 1
#     print(output)
#     for i in range(n - 1, -1, -1):
#         output[i] = output[i] * p
#         p = p * nums[i]
#         print(output)
#     return output


print(productExceptSelf([1, 2, 3, 4]))
