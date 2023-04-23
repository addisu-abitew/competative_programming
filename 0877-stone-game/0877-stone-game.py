class Solution:
    def __init__(self):
        self.calculated = {}

    def stoneGame(self, piles: List[int]) -> bool:
        return self.maxValue(piles, 0, len(piles)-1) >= 0
    
    def maxValue(self, piles, l, r):
        if l==r: return piles[l]
        if 'min({l}, {r})'.format(l = l+1, r = r) not in self.calculated:
            self.calculated['min({l}, {r})'.format(l = l+1, r = r)] = self.minValue(piles, l+1, r)
        if 'min({l}, {r})'.format(l = l, r = r-1) not in self.calculated:
            self.calculated['min({l}, {r})'.format(l = l, r = r-1)] = self.minValue(piles, l, r-1)
        leftValue = piles[l] + self.calculated['min({l}, {r})'.format(l = l+1, r = r)]
        rightValue = piles[r] + self.calculated['min({l}, {r})'.format(l = l, r = r-1)]

        return max(leftValue, rightValue)
        
    def minValue(self, piles, l, r):
        if l==r: return 0
        if 'max({l}, {r})'.format(l = l+1, r = r) not in self.calculated:
            self.calculated['max({l}, {r})'.format(l = l+1, r = r)] = self.maxValue(piles, l+1, r)
        if 'max({l}, {r})'.format(l = l,r = r-1) not in self.calculated:
            self.calculated['max({l}, {r})'.format(l = l,r = r-1)] = self.maxValue(piles, l, r-1)
        leftValue = self.calculated['max({l}, {r})'.format(l = l+1, r = r)]
        rightValue = self.calculated['max({l}, {r})'.format(l = l,r = r-1)]
        if leftValue > rightValue:
            return rightValue
        else:
            return leftValue
