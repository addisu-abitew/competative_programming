class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[i]+nums[i])
        for i in range(1, len(presum)):
            if presum[i-1]==presum[-1]-presum[i]:
                return i-1;
        return -1