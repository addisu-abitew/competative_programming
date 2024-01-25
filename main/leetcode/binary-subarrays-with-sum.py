class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        last = -1
        ones = []
        subarray = 0
        for i in range(n):
            if nums[i] == 1:
                ones.append(i)
            if len(ones) > goal:
                last = ones.pop(0)
            if len(ones) == goal:
                if goal == 0:
                    subarray += i-last
                else:
                    subarray += ones[0]-last
        return subarray