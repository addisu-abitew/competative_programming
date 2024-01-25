class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_start = min([trip[1] for trip in trips])
        max_end = max([trip[2] for trip in trips])
        n = max_end-min_start+1
        total_passengers = [0]*n
        for passengers, start, end in trips:
            total_passengers[start-min_start] += passengers
            total_passengers[end-min_start] -= passengers
        if total_passengers[0] > capacity:
            return False
        for i in range(1, n):
            total_passengers[i] += total_passengers[i-1]
            if total_passengers[i] > capacity:
                return False
        return True