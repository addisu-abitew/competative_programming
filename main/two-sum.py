class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        pairs = [[nums[i], i] for i in range(n)]
        pairs.sort()
        l, r = 0, n-1
        while l < r:
            if pairs[l][0] + pairs[r][0] == target:
                return [pairs[l][1], pairs[r][1]]
            elif pairs[l][0] + pairs[r][0] > target:
                r -= 1
            else:
                l += 1