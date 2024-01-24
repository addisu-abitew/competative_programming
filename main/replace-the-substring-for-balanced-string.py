class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        n = min_len = len(s)
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while left < n and self.isValid(count, n):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
        return min_len
            
    def isValid(self, count, n):
        for char in 'QWER':
            if count[char] > n/4:
                return False
        return True