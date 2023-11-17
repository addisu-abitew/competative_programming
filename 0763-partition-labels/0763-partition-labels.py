class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mem = {}
        for i in range(len(s)):
            mem[s[i]] = i
        l = -1
        r = 0
        ans = []
        while r < len(s):
            r = mem[s[r]]
            init_l = l
            while l < r:
                r = max(r, mem[s[l+1]])
                l += 1
            ans.append(mem[s[r]]-init_l)
            r += 1
        return ans