# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        solution = ListNode(0)
        prev = solution
        rem = 0
        while l1 or l2:
            s = rem
            if l1: s += l1.val
            if l2: s += l2.val
            rem = s//10
            prev.next = ListNode(s%10)
            prev = prev.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if rem: prev.next = ListNode(rem)
        return solution.next