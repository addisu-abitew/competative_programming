class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        one, two = 0, 0
        for n in nums:
            one, two = max(one, n+two), one
        return one