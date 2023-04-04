"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        node = head
        while node:
            if node.child:
                n =  node.next
                node.next = node.child
                node.child.prev = node
                node.child = None
                node = self.flatten(node.next)
                while node.next:
                    node = node.next
                node.next = n
                if n:
                    n.prev = node
                
            node = node.next
        return head
                    