class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1
        l = 0
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                partitions += 1
                l = r
                seen = set({s[r]})
            else:
                seen.add(s[r])
        return partitions