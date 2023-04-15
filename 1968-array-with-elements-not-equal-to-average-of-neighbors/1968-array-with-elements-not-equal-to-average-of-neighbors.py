class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)-1):
            while i > 0 and (nums[i-1]+nums[i+1])/2 == nums[i]:
                nums[i], nums[i+ 1] = nums[i+1], nums[i]
                i -= 1
        return nums