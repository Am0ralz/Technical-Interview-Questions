# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#
# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
# n = [1, 2, 2, 4]
# Output: [2,3]

from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        cCounter = Counter(nums + list(range(1,len(nums)+1)))
        a = cCounter.most_common()
        print(a)
        lst.append(a[0][0])
        lst.append(a[-1][0])
        return lst
