class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            m = int(math.log(n, 3) + 0.00000000001)
            if n == 3**m: return True
            if n >= 2 * 3**m: return False
            n -= 3**m
        return True