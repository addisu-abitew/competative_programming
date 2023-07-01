class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        while 0 in nums:
            nums.remove(0)
        nums += [0]*(l-len(nums))