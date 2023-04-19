# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the length at first
        self.head = head
        node = head
        pointer = head
        iterator = pointer
        counter = 0
        while node:
            counter += 1
            node = node.next
            if counter%k == 0:
                for i in range(k-1):
                    for j in range(k-1-i):
                        iterator.next.val, iterator.val = iterator.val, iterator.next.val
                        iterator = iterator.next
                    iterator = pointer
                pointer = node
                iterator = pointer
        return head
    