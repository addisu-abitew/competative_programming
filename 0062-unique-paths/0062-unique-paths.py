class Solution:
    def uniquePaths(self, m: int, n: int, visited = {(1,1):1}) -> int:
        if m==1 or n==1: return 1
        s = 0
        for i in range(1, m+1):
            if (i, n-1) not in visited:
                visited[(i, n-1)] = self.uniquePaths(i, n-1)
            s += visited[(i, n-1)]
        return s