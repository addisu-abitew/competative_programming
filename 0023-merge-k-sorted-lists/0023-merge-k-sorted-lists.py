# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return
        if len(lists) == 1: return lists[0]
        min_i = -1
        # initialize min_i by the first non-null list head value
        for li in range(len(lists)):
            if lists[li]:
                min_i = li
                break
        if min_i == -1: return None
        
        # find the smallest value
        for i in range(len(lists)):
            if lists[i] and lists[i].val<lists[min_i].val:
                min_i = i
        
        sorted_list = ListNode(lists[min_i].val)
        lists[min_i] = lists[min_i].next
        last = sorted_list
        
        while True:
            min_i = -1
            for li in range(len(lists)):
                if lists[li]:
                    min_i = li
                    break
            if min_i == -1: break
            
            for i in range(len(lists)):
                if lists[i] and lists[i].val<lists[min_i].val:
                    min_i = i
            last.next = ListNode(lists[min_i].val)
            lists[min_i] = lists[min_i].next
            last = last.next           
        
        return sorted_list