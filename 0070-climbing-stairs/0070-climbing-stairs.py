from math import factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4: return n
        res = 0
        for twos in range(n//2, -1, -1):
            ones = n - 2*twos
            div = factorial(ones) * factorial(twos)
            res += factorial(ones+twos)//div
        return res