class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                l, r = j+1, n-1
                while l<r:
                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if cur_sum == target:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1
        return ans