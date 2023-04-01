class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        max_coin = 0
        for i in range(len(piles)//3, len(piles), 2):
            max_coin += piles[i]
        return max_coin