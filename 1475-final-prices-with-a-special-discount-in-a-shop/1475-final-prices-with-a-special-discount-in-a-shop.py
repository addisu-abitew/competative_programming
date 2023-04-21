class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        for i in range(len(prices)):
            while s and prices[s[-1]] >= prices[i]:
                j = s.pop()
                prices[j] -= prices[i]
            s.append(i)
        return prices  
            