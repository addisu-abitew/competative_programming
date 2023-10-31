# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev = None
        cur = head
        length = 0
        while cur:
            node = ListNode(cur.val)
            node.next = prev
            prev = node
            cur = cur.next
            length += 1
        
        i = 1
        cur = head
        while i<length:
            tmp1, tmp2 = prev.next, cur.next
            cur.next = prev
            prev.next = tmp2
            i += 1
            if i < length:
                cur = tmp2
                i += 1
            else:
                cur = prev
            prev = tmp1
        cur.next = None
            