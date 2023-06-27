# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        lesser, greater = None, None
        node = head
        while node:
            if node.val < x:
                if lesser == None:
                    lesser = ListNode(node.val)
                else:
                    temp = lesser
                    while temp and temp.next:
                        temp = temp.next
                    temp.next = ListNode(node.val)
            else:
                if greater == None:
                    greater = ListNode(node.val)
                else:
                    temp = greater
                    while temp and temp.next:
                        temp = temp.next
                    temp.next = ListNode(node.val)
            node = node.next
        if lesser == None: return greater
        node = lesser
        while node and node.next:
            node = node.next
        node.next = greater
        return lesser