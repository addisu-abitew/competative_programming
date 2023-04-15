# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        if head and head.next :
            cur = last.next
            same = False
            while cur :
                if same and cur.val != last.val:
                    last.next = cur
                    last = cur
                    same = False
                elif cur.val != last.val:
                    last = cur                    
                else:
                    same = True
                cur = cur.next
            last.next = None
            
        return head
        