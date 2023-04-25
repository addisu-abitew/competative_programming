class Solution:
    def numDecodings(self, s: str) -> int:
        m = {len(s): 1}
        def dfs(i):
            if i in m: return m[i]
            if s[i] == '0': return 0
            
            if i+1 == len(s): return 1
            
            res = dfs(i+1)
            if i+1<len(s) and s[i] == '1' or s[i] == '2' and int(s[i+1]) < 7:
                res += dfs(i+2)
            m[i] = res
            return res
        return dfs(0)