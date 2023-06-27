# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head == None: return
        t = self.getLength(head)
        r = k % t
        if r == 0: return head
        tmp = head
        for _ in range(t-r-1):
            tmp = tmp.next
        node = tmp.next
        tmp.next = None
        tmp = node
        while node and node.next:
            node = node.next
        node.next = head
        return tmp
        
    def getLength(self, head):
        i = 0
        node = head
        while node:
            i += 1
            node = node.next
        return i