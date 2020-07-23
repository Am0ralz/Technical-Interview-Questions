# Given two arrays, write a function to compute their intersection.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
s1 = [4, 9, 5]
s2 = [9, 4, 9, 8, 4]


# Output: [9,4]


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))



