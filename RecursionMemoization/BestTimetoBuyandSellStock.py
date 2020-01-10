# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
# I = [7, 1, 5, 3, 6, 4]


# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

def maxP(min, max, i, price):
    if i >= len(price):
        return max

    if min > price[i] and max < price[i] - min:
        return maxP(price[i], price[i] - min, i + 1, price)
    if min > price[i]:
        return maxP(price[i], max, i + 1, price)
    if max < price[i] - min:
        return maxP(min, price[i] - min, i + 1, price)
    return maxP(min, max, i+1, price)

class Solution(object):
    def maxProfit(self, prices):
        minx = float('inf')
        maxy = 0
        if len(prices) == 0:
            return 0
        else:
            return maxP(minx, maxy, 0, prices)
