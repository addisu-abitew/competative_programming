# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not(head and head.next): return head
        odd, even = head, head.next
        even_head = head.next
        while odd and odd.next and even and even.next:
            next_odd = even.next
            even.next = even.next.next
            odd.next = next_odd
            even = even.next
            odd = odd.next
        odd.next = even_head
        return head