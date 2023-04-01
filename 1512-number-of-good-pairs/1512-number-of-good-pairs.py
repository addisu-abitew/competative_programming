class Solution(object):
    def numIdenticalPairs(self, nums):
        goodPairs = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    goodPairs += 1
        return goodPairs