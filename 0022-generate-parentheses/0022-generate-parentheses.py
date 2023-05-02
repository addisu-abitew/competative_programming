class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[], ['()']]
        for i in range(2, n+1):
            dp.append([])
            for brac in dp[i-1]:
                dp[i].append('('+brac+')')
            for j in range(1, i):
                for k in range(1, i):
                    if i == j+k:
                        for b1 in dp[j]:
                            for b2 in dp[k]:
                                pair = b1 + b2
                                if pair not in dp[i]: dp[i].append(pair)
        print(dp)
        return dp[n]