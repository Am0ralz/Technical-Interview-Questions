# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next:
            currOdd = head
            startEven = head.next
            currEven = startEven
            currNode = head.next.next
            i = 3
            while currNode:
                if i % 2:
                    currOdd.next = currNode
                    currOdd = currOdd.next
                    currNode = currNode.next
                    i += 1
                else:
                    currEven.next = currNode
                    currEven = currEven.next
                    currNode = currNode.next
                    i += 1

            currEven.next = currNode
            currOdd.next = startEven

        return head