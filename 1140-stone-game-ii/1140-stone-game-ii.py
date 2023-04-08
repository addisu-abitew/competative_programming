class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        return self.maxValue(piles, 0, 1, {})
    
    def maxValue(self, piles, l, M, mem):
        if 2*M + l >= len(piles):
            return sum(piles[l:])
        maxV = float('-inf')
        for i in range(2*M):
            v = sum(piles[l:l+i+1]) + self.minValue(piles, l+i+1, max(M, i+1), mem)
            if v > maxV:
                maxV = v
        return maxV
    
    def minValue(self, piles, l, M, mem):
        if 2*M + l >= len(piles):
            return 0
        minV = float('inf')
        for i in range(2*M):
            if '{}, {}'.format(l+i+1, max(M, i+1)) not in mem:
                mem['{}, {}'.format(l+i+1, max(M, i+1))] = self.maxValue(piles, l+i+1, max(M, i+1), mem)
            v = mem['{}, {}'.format(l+i+1, max(M, i+1))]
            if minV > v:
                minV = v
        return minV
    