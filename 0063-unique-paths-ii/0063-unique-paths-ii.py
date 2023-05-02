class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]: return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    if i+1<m:
                        dp[i][j] += dp[i+1][j]
                    if j+1<n:
                        dp[i][j] += dp[i][j+1]
        print(dp)
        return dp[0][0]