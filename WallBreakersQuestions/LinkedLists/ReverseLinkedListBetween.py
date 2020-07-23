# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        currNode = head
        prevNode = None

        for i in range(0, m - 1):
            prevNode = currNode
            currNode = currNode.next

        startLink = prevNode
        endLink = currNode

        for i in range(0, (n - m) + 1):
            tmpNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = tmpNode

        if startLink:
            startLink.next = prevNode
        else:
            head = prevNode
        endLink.next = currNode
        return head