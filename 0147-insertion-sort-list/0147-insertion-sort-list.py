# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        sortedHead = None
        curr = head
        while curr:
            next_node = curr.next
            sortedHead = self.insert(sortedHead, curr.val)
            curr = next_node
        return sortedHead
    
    def insert(self, head, val):
        if head == None: return ListNode(val)
        newNode = ListNode(val)
        if head.val > val:
            newNode.next = head
            head = newNode
            return head
        curr = head
        while curr and curr.next and curr.next.val < val:
            curr = curr.next
        if curr and curr.next:
            newNode.next = curr.next
            curr.next = newNode
        else:
            curr.next = newNode
        return head
            