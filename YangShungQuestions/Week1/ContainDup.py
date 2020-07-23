# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if
# every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

a = [1, 2, 3, 1]
b = [1, 2, 3, 4]
c = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def containDuplicates(arr):
    if (len(set(arr))) == len(arr):
        return False
    return True


def containDuplicates1(arr):
    dict = {}
    for i in arr:
        if i in dict:
            return True
        dict[i] = 1
    return False


def containDuplicates2(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


print(containDuplicates(a))
print(containDuplicates(b))
print(containDuplicates(c))
print()
print(containDuplicates1(a))
print(containDuplicates1(b))
print(containDuplicates1(c))
print()
print(containDuplicates2(a))
print(containDuplicates2(b))
print(containDuplicates2(c))

# class Solution(object):
# def containsDuplicate(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     return len(nums) != len(set(nums))