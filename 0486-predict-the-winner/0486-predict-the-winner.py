class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        value = self.maxValue(nums, 0, len(nums)-1)
        # print(value)
        return value >= 0
    
    # def value(self, nums, l, r, turn):
    #     # maximizer turn = 0
    #     # minimizer turn = 1
    #     if l==r: return nums[l]
    #     if turn == 0: return self.minValue(nums, l, r)
    #     if turn == 1: return self.maxValue(nums, l, r)
    
    def maxValue(self, nums, l, r):
        if l==r: return nums[l]
        leftValue = nums[l] + self.minValue(nums, l+1, r)
        rightValue = nums[r] + self.minValue(nums, l, r-1)
        if leftValue > rightValue:
            return leftValue
        else:
            return rightValue
        
    def minValue(self, nums, l, r):
        if l==r: return nums[l]
        leftValue = self.maxValue(nums, l+1, r) - nums[l]
        rightValue = self.maxValue(nums, l, r-1) -nums[r]
        if leftValue > rightValue:
            return rightValue
        else:
            return leftValue
