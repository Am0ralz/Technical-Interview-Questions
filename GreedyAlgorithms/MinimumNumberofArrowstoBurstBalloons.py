# There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the
# start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence
# the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most
# 104 balloons.
# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend
# bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
# arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be
# shot to burst all balloons.


lst = [[7, 15], [6, 14], [8, 12], [3, 4], [4, 13], [6, 14], [9, 11], [6, 12], [4, 13]]


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        if length == 0 or length == 1:
            return length
        points = sorted(points)
        start = points[0][0]
        end = points[0][1]
        count = 1

        for i in range(1, length):

            if end < points[i][0]:
                start = points[i][0]
                end = points[i][1]
                count += 1
            else:
                if start < points[i][0]:
                    start = points[i][0]

                if end > points[i][1]:
                    end = points[i][1]
        return count
