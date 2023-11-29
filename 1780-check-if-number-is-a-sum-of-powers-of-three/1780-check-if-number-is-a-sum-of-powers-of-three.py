class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            m = 0
            while 3**(m+1) <= n:
                m += 1
            if n == 3**m: return True
            if n >= 2 * 3**m: return False
            n -= 3**m
        return True