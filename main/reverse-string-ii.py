class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        l = len(s)
        n = math.ceil(l/k)
        for i in range(n):
            part = s[k*i: k*i+k]
            if i % 2 == 0:
                ans += part[::-1]
            else:
                ans += part
        return ans