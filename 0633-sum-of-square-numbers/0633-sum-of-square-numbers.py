class Solution(object):
    def judgeSquareSum(self, c):
        i = 0
        while i**2 <= c:
            rem =  c - i**2
            if rem**0.5%1 == 0:
                return True
            i += 1
        return False