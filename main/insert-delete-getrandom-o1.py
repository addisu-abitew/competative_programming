class RandomizedSet:

    def __init__(self):
        self.randSet = {}
        self.randArr = []

    def insert(self, val: int) -> bool:
        wasPresent = val in self.randSet
        if not wasPresent:
            self.randSet[val] = len(self.randSet)
            self.randArr.append(val)
        return not wasPresent

    def remove(self, val: int) -> bool:
        wasPresent = val in self.randSet
        if wasPresent:
            i = self.randSet[val]
            self.randArr[i] = None
            del self.randSet[val]
        return wasPresent

    def getRandom(self) -> int:
        while True:
            i = random.randint(0, len(self.randArr)-1)
            if self.randArr[i] != None:
                return self.randArr[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()