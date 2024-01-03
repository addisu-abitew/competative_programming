class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li, ri = 0 , len(nums)-1
        while li < ri:
            cur_sum = nums[li] + nums[ri]
            if cur_sum == target:
                return [li+1, ri+1]
            elif cur_sum < target:
                li += 1
            else:
                ri -= 1