# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None: return head
        prev = None
        node = head
        dup = None
        while node and node.next:
            tmp = node.next
            if node.val == node.next.val:
                dup = node.val
                if prev == None:
                    head = node.next.next
                else:
                    prev.next = node.next.next
                node = tmp.next
            elif dup != None and dup == node.val:
                if prev:
                    prev.next = node.next
                else:
                    head = head.next
                node = tmp
            else:
                dup = None
                prev = node
                node = node.next
        if dup != None and node and dup == node.val:
            if prev:
                prev.next = node.next
            else:
                head = head.next
        return head