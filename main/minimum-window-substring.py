class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_s, count_t = Counter(), Counter(t)
        n = len(s)
        min_len = n+1
        left = 0
        for right in range(n):
            count_s[s[right]] += 1
            while left < n and self.isValid(count_s, count_t):
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    min_win = (left, right)
                count_s[s[left]] -= 1
                left += 1
        return '' if min_len == n+1 else s[min_win[0]:min_win[1]+1]
    
    def isValid(self, count_s, count_t):
        for char in count_t:
            if count_s[char] < count_t[char]:
                return False
        return True