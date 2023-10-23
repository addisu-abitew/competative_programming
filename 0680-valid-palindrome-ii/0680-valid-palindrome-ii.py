class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        l, r = 0, len(s)-1
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                lrem = s[:l]+s[l+1:]
                rrem = s[:r]+s[r+1:]
                return lrem == lrem[::-1] or rrem == rrem[::-1]
        # return True