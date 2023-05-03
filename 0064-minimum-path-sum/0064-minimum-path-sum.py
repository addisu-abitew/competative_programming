class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = grid[i][j]
                if i+1<m and j+1<n:
                    dp[i][j] += min(dp[i+1][j], dp[i][j+1])
                elif i+1<m:
                    dp[i][j] += dp[i+1][j]
                elif j+1<n:
                    dp[i][j] += dp[i][j+1]
        # print(dp)
        return dp[0][0]