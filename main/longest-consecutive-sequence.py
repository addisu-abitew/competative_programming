class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        for num in nums:
            if num+1 not in nums_set:
                cur_len = 1
                while num - cur_len in nums_set:
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len