class Node:
    def __init__(self, val, nex=None):
        self.val = val
        self.next = nex

class MyLinkedList(object):
    # singly linked list implementation
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        node = self.head
        for _ in range(index):
            print(node.val)
            node = node.next
        return node.val
        
    def addAtHead(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        newNode = Node(val)
        if self.head == None: self.head = newNode
        else:
            node = self.head
            while node and node.next:
                node = node.next
            node.next = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size: return
        elif index == 0: self.addAtHead(val)
        elif index == self.size: self.addAtTail(val)
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            newNode = Node(val)
            newNode.next = node.next
            node.next = newNode
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or  index >= self.size: return
        elif index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            node.next =node.next.next
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)