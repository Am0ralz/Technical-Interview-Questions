# Implement pow(x, n), which calculates x raised to the power n (xn).
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / (x * self.myPow(x, -(n + 1)))

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return x * self.myPow(x, n - 1)
