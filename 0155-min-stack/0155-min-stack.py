class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = self.stack.copy()
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack2.append(val)
        self.stack2.sort()

    def pop(self) -> None:
        val = self.stack.pop()
        self.stack2.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print("stack2",self.stack2)
        return self.stack2[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()