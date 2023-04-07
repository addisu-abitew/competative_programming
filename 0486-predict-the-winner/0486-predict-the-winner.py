class Solution:
    def __init__(self):
        self.calculated = {}
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.maxValue(nums, 0, len(nums)-1) >= 0
    
    def maxValue(self, nums, l, r):
        if l==r: return nums[l]
        if 'min({l}, {r})'.format(l = l+1, r = r) not in self.calculated:
            self.calculated['min({l}, {r})'.format(l = l+1, r = r)] = self.minValue(nums, l+1, r)
        if 'min({l}, {r})'.format(l = l, r = r-1) not in self.calculated:
            self.calculated['min({l}, {r})'.format(l = l, r = r-1)] = self.minValue(nums, l, r-1)
        leftValue = nums[l] + self.calculated['min({l}, {r})'.format(l = l+1, r = r)]
        rightValue = nums[r] + self.calculated['min({l}, {r})'.format(l = l, r = r-1)]
        if leftValue > rightValue:
            return leftValue
        else:
            return rightValue
        
    def minValue(self, nums, l, r):
        if l==r: return nums[l]
        if 'max({l}, {r})'.format(l = l+1, r = r) not in self.calculated:
            self.calculated['max({l}, {r})'.format(l = l+1, r = r)] = self.maxValue(nums, l+1, r)
        if 'max({l}, {r})'.format(l = l,r = r-1) not in self.calculated:
            self.calculated['max({l}, {r})'.format(l = l,r = r-1)] = self.maxValue(nums, l, r-1)
        leftValue = self.calculated['max({l}, {r})'.format(l = l+1, r = r)] - nums[l]
        rightValue = self.calculated['max({l}, {r})'.format(l = l,r = r-1)] - nums[r]
        if leftValue > rightValue:
            return rightValue
        else:
            return leftValue
