class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        targetIndices = []
        i = 0
        while i < len(nums) and nums[i] <= target:
            if nums[i] == target:
                targetIndices.append(i)
            i += 1
        return targetIndices