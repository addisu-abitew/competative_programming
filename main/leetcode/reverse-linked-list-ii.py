# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            left_end = None
            prev = head
        else:
            left_end = head
            for _ in range(left-2):
                left_end = left_end.next
            prev = left_end.next
        
        cur = prev.next
        for _ in range(right-left):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        if left == 1:
            head.next = cur
            head = prev
        else:
            left_end.next.next = cur
            left_end.next = prev

        return head