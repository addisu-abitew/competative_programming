# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        arr = self.getArr(head)
        mono_stack = []
        for i, num in enumerate(arr):
            if len(mono_stack) == 0:
                mono_stack.append((i, num))
            else:
                while len(mono_stack) > 0 and mono_stack[-1][1] < num:
                    index = mono_stack[-1][0]
                    arr[index] = num
                    mono_stack.pop()
                mono_stack.append((i, num))
        for i, _ in mono_stack:
            arr[i] = 0
        return arr
        
    def getArr(self, head):
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr