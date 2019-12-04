# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3 There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[
# A.length - 1] Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i]
# > A[i+1] > ... > A[A.length - 1].
# Example 1:
#
# i = [0, 2, 1, 0]
# Output: 1
# Example 2:
#
# Input: [0,2,1,0]
# Output: 1

class Solution(object):

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mi = 0
        ma = len(A) - 1
        peak = (ma + mi) // 2

        while mi < peak < ma:
            if A[peak - 1] < A[peak] > A[peak + 1]:
                return peak
            if A[peak] < A[peak + 1]:
                peak = peak + 1
            else:
                peak = peak - 1
        return peak
