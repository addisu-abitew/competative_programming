class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        dp.append(-10000)
        for i in range(n-1, -1, -1):
            dp[i] = nums[i]
            if dp[i+1] > 0: dp[i]+= dp[i+1]
        # print(dp)
        return max(dp)