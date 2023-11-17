class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxLen = 0
        for maxUnique in range(1, len(set(s))+1):
            l = r = uniques = more_than_k = 0
            counter = Counter()
            while r < len(s):
                if uniques > maxUnique:
                    if counter[s[l]] == k:
                        more_than_k -= 1
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        uniques -= 1
                    l += 1
                else:
                    if counter[s[r]] == 0:
                        uniques += 1
                    counter[s[r]] += 1
                    if counter[s[r]] == k:
                        more_than_k += 1
                    r += 1
                if maxUnique == uniques and maxUnique == more_than_k:
                    maxLen = max(maxLen, r-l)
        return maxLen
    