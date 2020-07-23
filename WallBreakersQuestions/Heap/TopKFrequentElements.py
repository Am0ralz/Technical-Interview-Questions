# Given a non-empty array of integers, return the k most frequent elements.
# Example 1:
#
from operator import itemgetter

n = [-1, -1, -1, 2, 2, 3]
t = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
from heapq import nlargest

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    c = nlargest(k, dic, key=dic.get)

    ans = [val for val in c]
    return ans


print(topKFrequent(n, t))
