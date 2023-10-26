class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        closest = 0
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                cur_diff = abs(cur_sum - target)
                if cur_diff < diff:
                    diff = cur_diff
                    closest = cur_sum
                if cur_sum > target:
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    return cur_sum
        return closest