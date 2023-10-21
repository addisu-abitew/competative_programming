class RecentCounter:

    def __init__(self):
        self.times = []
        self.count = 0

    def ping(self, t: int) -> int:
        self.count += 1
        self.times.append(t)
        while len(self.times)>0 and self.times[0] + 3000 < t:
            self.times.pop(0)
            self.count -= 1
        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)