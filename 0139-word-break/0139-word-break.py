class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp ={len(s): True}
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                # print(s[i:i+len(word)])
                if s[i:i+len(word)] == word:
                    # print(s[i:i+len(word)])
                    dp[i] = dp[i+len(word)]
                    if dp[i+len(word)]: break
                    # break
                else:
                    dp[i] = False
        # print(dp)
        return dp[0]