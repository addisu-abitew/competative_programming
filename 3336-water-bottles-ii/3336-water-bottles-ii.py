class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drink = numBottles
        while numBottles >= numExchange:
            total_drink += 1
            numBottles -= numExchange - 1
            numExchange += 1
        return total_drink