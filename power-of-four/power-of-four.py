class Solution(object):
    def isPowerOfFour(self, n):
        if n < 1: return False
        return math.log(n,4) - int(math.log(n,4)) == 0.0