# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        currNode = head
        prevNode = None

        length = 0
        while currNode:
            length += 1
            currNode = currNode.next

        currNode = head
        startLink = prevNode
        endLink = currNode

        for i in range(0, length // k):
            for j in range(0, k):
                tmpNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = tmpNode

            if startLink:
                startLink.next = prevNode
                endLink.next = currNode
                startLink = endLink
                endLink = currNode
            else:
                endLink.next = currNode
                head = prevNode
                startLink = endLink
                endLink = currNode
        return head