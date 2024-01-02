class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        bars = 0
        while i < len(costs) and coins > 0:
            if coins >= costs[i]:
                coins -= costs[i]
                bars += 1
            i += 1
        return bars