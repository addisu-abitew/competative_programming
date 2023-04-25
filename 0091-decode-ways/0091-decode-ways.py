class Solution:
    def numDecodings(self, s: str) -> int:
        m = {len(s): 1}
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0': m[i] = 0
            else:
                m[i] = m[i+1]
                if i+1<len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                    m[i] += m[i+2]
        return m[0]