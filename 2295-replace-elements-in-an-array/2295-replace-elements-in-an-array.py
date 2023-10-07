class Solution(object):
    def arrayChange(self, nums, operations):
        swaps = {}
        for s, e in reversed(operations):
            swaps[s] = swaps[e] if e in swaps else e
        for i, num in enumerate(nums):
            if num in swaps:
                nums[i] = swaps[num]
        return nums