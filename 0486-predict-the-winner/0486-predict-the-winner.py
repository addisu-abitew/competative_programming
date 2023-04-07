class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.maxValue(nums, 0, len(nums)-1) >= 0
    
    def value(self, nums, l, r, turn):
        # maximizer turn = 0
        # minimizer turn = 1
        if l==r: return nums[l]
        if turn == 0: return self.minValue(nums, l, r)
        if turn == 1: return self.maxValue(nums, l, r)
    
    def maxValue(self, nums, l, r):
        if l==r: return nums[l]
        leftValue = nums[l] - self.value(nums, l+1, r, 1)
        rightValue = nums[r] - self.value(nums, l, r-1, 1)
        if leftValue > rightValue:
            return leftValue
        else:
            return rightValue
        
    def minValue(self, nums, l, r):
        if l==r: return nums[l]
        leftValue = self.value(nums, l+1, r, 0) - nums[l]
        rightValue = self.value(nums, l, r-1, 0) -nums[r]
        if leftValue > rightValue:
            return rightValue
        else:
            return leftValue
