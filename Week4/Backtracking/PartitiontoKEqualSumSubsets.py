# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k
# non-empty subsets whose sums are all equal.
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


def SubSum(pos, sts, nums, subset):
    if pos == len(nums):
        return True

    for i, p in enumerate(sts):
        if p >= nums[pos]:
            if sts[i] == subset and (i - 1 >= 0 and sts[i - 1] == subset):
                break

            sts[i] -= nums[pos]

            if SubSum(pos + 1, sts, nums, subset):
                return True

            sts[i] += nums[pos]

    return False


def canPartitionKSubsets(self, nums, k):
    if sum(nums) % k != 0:
        return False

    subsum = sum(nums) / k
    parts = [subsum for i in range(k)]

    nums = sorted(nums)[::-1]

    return SubSum(0, parts, nums, subsum)
