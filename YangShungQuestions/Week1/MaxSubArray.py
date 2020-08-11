# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
# which is more subtle.

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = nums[0]

    for i in range(0, len(nums)):
        j = 0
        while j + i < len(nums):
            k = sum(nums[j:j + i + 1])
            if ans < k:
                ans = k
            j = j + 1
    print(ans)


maxSubArray([4, -1, 2, 1])

# This is Kadane's algorithm
#
# Example 1)
#     for i in range(1, len(nums)):
#         if nums[i-1] > 0:
#             nums[i] += nums[i-1]
#         return max(nums)


