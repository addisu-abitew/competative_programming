class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {0: -1}
        cur_sum = 0
        max_len = 0
        for i in range(len(nums)):
            cur_sum += 1 if nums[i] == 1 else -1
            if cur_sum in hash_map:
                max_len = max(max_len, i-hash_map[cur_sum])
            else:
                hash_map[cur_sum] = i
        return max_len