# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head
        cur = head
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        new_head = ListNode(vals[-1])
        last = new_head
        for i in range(len(vals)-2,-1,-1):
            last.next = ListNode(vals[i])
            last = last.next
        return new_head