# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        curA = headA
        while curA:
            visited.add(curA)
            curA = curA.next
        curB = headB
        while curB:
            if curB in visited: break
            curB = curB.next
        return curB