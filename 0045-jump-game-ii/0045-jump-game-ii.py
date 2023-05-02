class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [10000]*(n)
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(1, min(n-i, nums[i]+1)):
                dp[i] = min(dp[i], dp[i+j]+1)
        # print(dp)
        return dp[0]
                