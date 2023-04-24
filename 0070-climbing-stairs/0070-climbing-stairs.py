from math import factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        down, up = 1, 1
        for i in range(n-1):
            up, down = up+down, up
        return up