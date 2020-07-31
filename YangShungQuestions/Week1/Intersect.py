# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
numsa = [1,2,2,1]
numsb = [2,2]


# Output: [9,4]
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.


def intersection(nums1, nums2):
    """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
    return list(set(nums1).intersection(set(nums2)))


def intersection1(nums1, nums2):
    """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
    dic = {}
    lst = []
    for i in nums1:
        if i not in dic:
            dic[i] = 1
    for j in nums2:
        if j in dic and dic[j] == 1:
            lst.append(j)
            dic[j] = 0

    return lst


print(intersection1(numsa, numsb))
