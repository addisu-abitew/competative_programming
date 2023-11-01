class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        for i in range(1, len(presum)):
            if presum[i-1] == presum[-1]-presum[i]:
                return i-1
        return -1