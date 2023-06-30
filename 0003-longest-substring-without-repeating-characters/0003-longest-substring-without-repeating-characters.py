class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        left, right = 0, 1
        max_len = 0
        while right < len(s):
            if s[right] not in s[left : right]:
                right += 1
                max_len = max(max_len, right - left)
            else:
                while s[right] in s[left : right]:
                    left += 1
        return max_len