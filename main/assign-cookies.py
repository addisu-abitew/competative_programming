class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for size in s:
            if i < len(g) and size >= g[i]:
                i += 1
        return i