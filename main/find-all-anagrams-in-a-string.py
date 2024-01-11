class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        window = Counter(s[:k])
        target = Counter(p)
        anagrams = []
        if window == target:
            anagrams.append(0)
        for i in range(k, len(s)):
            window[s[i-k]] -= 1
            window[s[i]] += 1
            if window == target:
                anagrams.append(i-k+1)
        return anagrams