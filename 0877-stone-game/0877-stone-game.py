class Solution:
    def stoneGame(self, piles: List[int], dif=0) -> bool:
        if len(piles)==1:
            return piles[0]
        elif len(piles)==2:
            return max(piles[0], piles[1])-min(piles[0], piles[1])
        # l = max(piles[0]-max(piles[1], piles[-1]), piles[-1] - max(piles[0], piles[-2]))
        l = 1 if piles[1] > piles[-1] else -1
        r = 0 if piles[0] > piles[-2] else -2
        x = 0 if piles[0]-piles[l] > piles[-1] - piles[r] else -1
        if x == 0:
            dif += piles[0]-piles[l]
            # print(dif, x, l)
            if l == 1:
                return self.stoneGame(piles[l+1:],dif)
            else:
                return self.stoneGame(piles[1:l], dif)
        else:
            dif += piles[-1]-piles[r]
            # print(dif, x, r)
            if r == 0:
                return self.stoneGame(piles[1:-1], dif)
            else:
                return self.stoneGame(piles[:-2], dif)