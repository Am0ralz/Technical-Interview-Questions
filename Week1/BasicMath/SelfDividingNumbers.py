
# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
#
# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
import math

class Solution(object):
    def selfDividingNumbers(self, left, right):
        lst = []
        for i in range(left, right + 1):
            bol = True
            digits = int(math.log10(i)) + 1
            tmp = 0
            for j in range(digits):
                a = i // (10 ** (digits - 1 - j))
                digit = (a - (tmp * 10))
                tmp = a
                if digit == 0:
                    bol = False
                    break
                if i % digit != 0:
                    bol = False
                    break
            if bol:
                lst.append(i)
        return lst
