class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = {1: nums[0]}
        for i in range(1, len(nums)):
            for l in range(len(res), 0, -1):
                if nums[i] > res[l]:
                    res[l+1] = nums[i]
                    break
            if l == 1 and nums[i] < res[l]:
                res[l] = nums[i]
        return len(res)