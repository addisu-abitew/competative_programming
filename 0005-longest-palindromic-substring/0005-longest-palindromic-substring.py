class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        maxLen = 1
        for i in range(len(s)):
            # for odd length
            l, r = i-1, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1 > maxLen):
                    res = s[l:r+1]
                    maxLen = r-l+1
                l -= 1
                r += 1
            
            # for even length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1 > maxLen):
                    res = s[l:r+1]
                    maxLen = r-l+1
                l -= 1
                r += 1
        return res