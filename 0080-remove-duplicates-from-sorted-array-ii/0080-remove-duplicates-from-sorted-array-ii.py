class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:  # If there are 2 or fewer elements, no need to remove duplicates
            return len(nums)
        
        li = 2  # Pointer for the current position to overwrite
        for ri in range(2, len(nums)):
            if nums[li-2] != nums[ri]:
                nums[li] = nums[ri]
                li += 1
        
        return li