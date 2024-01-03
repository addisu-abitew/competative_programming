class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        for num in nums:
            if num not in seen:
                nums[i] = num
                seen.add(num)
                i += 1
        return i