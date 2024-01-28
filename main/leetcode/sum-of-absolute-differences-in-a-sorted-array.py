class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        result =  []
        n = len(nums)
        for i in  range(n):
            left = i
            right = n-i-1
            result.append(nums[i]*left-presum[i] + presum[-1]-presum[i+1]-nums[i]*right)
        return result