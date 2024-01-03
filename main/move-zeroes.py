class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder = 0
        while placeholder < len(nums) and nums[placeholder] != 0:
            placeholder += 1
        for seeker in range(len(nums)):
            if nums[seeker] != 0 and placeholder < seeker:
                nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
                placeholder += 1
                while placeholder < len(nums) and nums[placeholder] != 0:
                    placeholder += 1
        return nums