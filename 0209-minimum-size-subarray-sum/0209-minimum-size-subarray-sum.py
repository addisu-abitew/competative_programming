class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, right = 0, 0
        min_len = len(nums) + 1
        cur_sum = 0
        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right-left+1)
                cur_sum -= nums[left]
                left += 1
            else:
                right += 1
        return min_len if min_len < len(nums)+1 else 0