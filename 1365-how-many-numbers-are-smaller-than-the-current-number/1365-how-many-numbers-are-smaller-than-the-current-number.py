class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    result[i] += 1
        return result