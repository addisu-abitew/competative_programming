class FrequencyTracker:

    def __init__(self):
        self.dic = defaultdict(int)
        self.freq = defaultdict(set)
    def add(self, number: int) -> None:
        previous = self.dic[number] 
        if previous:
            self.freq[previous].remove(number)
        self.freq[previous+1].add(number)
        self.dic[number] += 1

    def deleteOne(self, number: int) -> None:
        previous = self.dic[number] 
        if previous:
            self.freq[previous].remove(number)
        if previous > 1:
            self.freq[previous-1].add(number)
        self.dic[number] -= 1 if self.dic[number] else 0
            

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)