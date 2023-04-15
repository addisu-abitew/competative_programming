# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        if len(vals)==0: return
        vals.sort()
        sorted_list = ListNode(vals[0])
        last = sorted_list
        for i in range(1, len(vals)):
            last.next = ListNode(vals[i])
            last = last.next
        return sorted_list