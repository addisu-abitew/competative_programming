# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        t = self.getLength(head)
        if t < n: return head
        d = t - n
        if d == 0:
            head = head.next
            return head
        node = head
        for _ in range(d-1):
            node = node.next
        node.next = node.next.next
        return head
        
    def getLength(self, head):
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        return l