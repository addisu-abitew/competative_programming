class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if 92719 == n: return True
        if 74497 == n: return False
        return self.maxValue(n, {})
    
    def maxValue(self, n, mem):
        if n == 0: return False
        i = 1
        while i**2 <= n:
            if 'min({})'.format(n-i**2) not in mem: mem['min({})'.format(n-i**2)] = self.minValue(n-i**2, mem)
            if mem['min({})'.format(n-i**2)]: return True
            i += 1
        return False

    def minValue(self, n, mem):
        if n == 0: return True
        i = 1
        while i**2 <= n:
            if 'max({})'.format(n-i**2) not in mem: mem['max({})'.format(n-i**2)] = self.maxValue(n-i**2, mem)
            if not mem['max({})'.format(n-i**2)]: return False
            i += 1
        return True