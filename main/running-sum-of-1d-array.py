class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = [nums[0]]
        for num in nums[1:]:
            presum.append(presum[-1] + num)
        return presum