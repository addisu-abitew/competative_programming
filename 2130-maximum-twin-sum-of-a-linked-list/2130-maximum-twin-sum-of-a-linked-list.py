# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        max_sum = 0
        for i in range(n//2):
            cur_sum = arr[i]+arr[n-1-i]
            if max_sum < cur_sum:
                max_sum = cur_sum
        return max_sum