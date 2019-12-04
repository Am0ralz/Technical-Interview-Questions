# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


a = [[1, 3], [2, 6], [8, 10], [15, 18]]


class Solution(object):
    def merge(self, intervals):
        length = len(intervals)
        if length == 0:
            return ""
        if length == 1:
            return intervals

        intervals = sorted(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        lst = []
        for i in range(1, length):

            if end < intervals[i][0]:
                lst.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                if start > intervals[i][0]:
                    start = intervals[i][0]

                if end < intervals[i][1]:
                    end = intervals[i][1]

        lst.append([start, end])
        return lst