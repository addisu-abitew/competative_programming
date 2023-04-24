class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))

    def robHelper(self, nums):
        one, two = 0, 0
        for n in nums:
            one, two = max(one, n+two), one
        return one