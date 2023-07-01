class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, right = 0, 1
        min_len = len(nums) + 1
        cur_sum = nums[0]
        while right < len(nums):
            if cur_sum >= target:
                min_len = min(min_len, right-left)
                cur_sum -= nums[left]
                left += 1
            else:
                cur_sum += nums[right]
                right += 1
        while cur_sum >= target:
            min_len = min(min_len, right-left)
            cur_sum -= nums[left]
            left += 1 
        return min_len if min_len < len(nums)+1 else 0