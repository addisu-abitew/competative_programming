class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod ,z  = 1 ,0
        for num in nums:
            if num != 0 :
                prod *= num
            else:
                z += 1
        if z >= 2: return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = prod
            elif z >= 1 :nums[i] = 0
            else:nums[i] = prod //nums[i]
        return nums
            
            
        