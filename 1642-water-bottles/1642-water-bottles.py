class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles:
            rem = numBottles % numExchange
            numBottles = numBottles // numExchange
            if numBottles == 0:
                break
            ans += numBottles
            numBottles += rem
        return ans
