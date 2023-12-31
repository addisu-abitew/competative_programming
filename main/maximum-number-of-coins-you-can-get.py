class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        max_coin = 0
        for i in range(n//3, n, 2):
            max_coin += piles[i]
        return max_coin