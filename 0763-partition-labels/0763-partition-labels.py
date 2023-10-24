class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i, l in enumerate(s):
            dic[l] = i
        
        ans = []
        l, r = -1, 0
        for i in range(len(s)):
            r = max(r, dic[s[i]])
            if i == r:
                ans.append(r-l)
                l = r
        return ans