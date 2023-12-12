class OrderedStream:

    def __init__(self, n: int):
        self.stream = [''] * (n+1)
        self.index = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        chunk = []
        if idKey == self.index:
            while self.index < len(self.stream) and self.stream[self.index]:
                chunk.append(self.stream[self.index])
                self.index += 1
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)