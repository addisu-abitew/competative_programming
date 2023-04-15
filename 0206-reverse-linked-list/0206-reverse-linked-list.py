# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head
        count = 0
        cur = head
        while cur.next:
            cur = cur.next
            count += 1
        new_head = ListNode(cur.val)
        last = new_head
        while count > 0:
            cur = head
            i = 1
            while i < count:
                cur = cur.next
                i += 1
            count -= 1
            last.next = ListNode(cur.val)
            last = last.next
        return new_head