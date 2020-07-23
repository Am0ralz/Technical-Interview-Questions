# 905  Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# a = [2, 5, 7, 4, 8, 9, 3, 2, 1, 7, 8, 9, 0, 6]


class Solution(object):

    def sortArrayByParity(self, A):
        b = []
        for i in A:
            if i % 2 == 0:
                b.insert(0, i)
            else:
                b.append(i)
        return b
