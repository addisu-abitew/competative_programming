# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            if cur.next:
                cur.val, cur.next.val = cur.next.val, cur.val
                cur = cur.next
            cur = cur.next
        return head