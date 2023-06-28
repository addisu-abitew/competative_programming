# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        mid = self.getLength(head)//2
        curr = head
        for _ in range(mid):
            curr = curr.next
        return curr
        
    def getLength(self, head):
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        return l