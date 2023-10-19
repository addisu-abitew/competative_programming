class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        currency = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        ans = 0
        cur = 0
        for i in range(len(s)-1, -1, -1):
            val = currency[s[i]]
            if val < cur:
                ans -= val
            else:
                cur = val
                ans += val
        return ans