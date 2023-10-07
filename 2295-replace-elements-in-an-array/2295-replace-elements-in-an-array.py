class Solution(object):
    def arrayChange(self, nums, operations):
        replacements = {}
        for x, y in reversed(operations):
            replacements[x] = replacements.get(y, y)
        for idx, val in enumerate(nums):
            if val in replacements:
                nums[idx] = replacements[val]
        return nums
