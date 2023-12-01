class Solution:
    def romanToInt(self, s: str) -> int:
        currency = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100,'D': 500,'M': 1000}
        ans = 0
        max_cur = 0
        for rom in s[::-1]:
            if currency[rom] < max_cur:
                ans -= currency[rom]
            else:
                max_cur = currency[rom]
                ans += currency[rom]
        return ans