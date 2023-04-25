class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = {0: 0}
        for a in range(1, amount+1):
            tot = amount+1
            for c in coins:
                if a-c >= 0:
                    tot = min(tot, m[a-c]+1)
            m[a] = tot
        return m[amount] if m[amount] != amount+1 else -1