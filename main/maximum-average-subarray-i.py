class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = max_sum = sum(nums[:k])
        left = 0
        right = k
        while right < len(nums):
            cur_sum += nums[right] - nums[left]
            max_sum = max(max_sum, cur_sum)
            left += 1
            right += 1
        return max_sum/k