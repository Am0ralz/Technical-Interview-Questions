# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        h = []
        for i in lists:
            if i:
                while (i):
                    heapq.heappush(h, (i.val, i))
                    i = i.next
        head = prev = ListNode(0)
        while h:
            curr = heapq.heappop(h)[1]
            prev.next = curr
            prev = curr
        return head.next
