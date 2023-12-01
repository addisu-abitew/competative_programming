class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            if s[i] == '#':
                ans = ans[:-2]
                ans += chr(ord('a') + int(s[i-2]+s[i-1]) - 1)
            else:
                ans += chr(ord('a') + int(s[i]) - 1)
        return ans