# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not (list1 or list2):
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
        while list1 and list2:
            if list1.val < list2.val:
                node = head
                while node.next:
                    node = node.next
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node = head
                while node.next:
                    node = node.next
                node.next = ListNode(list2.val)
                list2 = list2.next
        if list1:
            node = head
            while node.next:
                node = node.next
            node.next = list1
        else:
            node = head
            while node.next:
                node = node.next
            node.next = list2
        return head