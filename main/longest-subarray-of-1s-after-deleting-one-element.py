class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = -1
        zero_pos = -1
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                if zeros == 0:
                    zeros += 1
                else:
                    left = zero_pos
                zero_pos = right
            max_len = max(max_len, right-left-1)

        return max_len