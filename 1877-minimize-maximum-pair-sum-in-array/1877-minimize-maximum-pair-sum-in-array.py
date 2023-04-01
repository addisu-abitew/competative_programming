class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        min_pair_sum = 0
        n = len(nums)
        for i in range(n):
            min_pair_sum = max(nums[i] + nums[n-i-1], min_pair_sum)
        return min_pair_sum
