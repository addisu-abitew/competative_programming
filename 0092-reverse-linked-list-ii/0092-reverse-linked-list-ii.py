# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        last_node = None if left==1 else head
        for _ in range(left-2):
            last_node = last_node.next

        first = last_node.next if last_node else head
        
        prev = None
        cur = first
        for _ in range(right-left+1):
            # print(cur.val)
            prev, cur.next, cur = cur, prev, cur.next
        
        first.next = cur
        
        if last_node:
            last_node.next = prev
            return head
        return prev