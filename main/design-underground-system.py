class UndergroundSystem:

    def __init__(self):
        self.checked_in = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checked_in[id]
        cur_time = t - start_time
        prev_time, size = self.times.get((start_station, stationName), (0, 0))
        self.times[(start_station, stationName)] = ((prev_time*size + cur_time)/(size+1), size+1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.times[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)