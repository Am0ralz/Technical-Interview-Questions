# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at
# most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be
# content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
# and the child i will be content. Your goal is to maximize the number of your content children and output the
# maximum number.
#
# a = [1, 8, 8, 8]
# c = [1, 1, 7, 8]
#
# Output: 1
#
# Input: [1,2], [1,2,3]
#
# Output: 2

class Solution(object):
    def findContentChildren(self, g, s):
        g.sort(reverse=True)
        s.sort(reverse=True)
        count = 0
        while s and g:
            if s[-1] < g[-1]:
                s.pop()
            else:
                count += 1
                s.pop()
                g.pop()
        return count



