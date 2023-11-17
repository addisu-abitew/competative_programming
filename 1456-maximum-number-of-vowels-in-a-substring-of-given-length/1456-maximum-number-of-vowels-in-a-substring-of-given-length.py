class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        maxCount = count = 0
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            if r >= k-1:
                maxCount = max(count, maxCount)
                if s[r-k+1] in vowels:
                    count -= 1
        return maxCount