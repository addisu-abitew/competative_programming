class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        for val in range(ord('A'), ord('A')+26):
            left = 0
            char = chr(val)
            non_char = 0
            for right in range(len(s)):
                if s[right] != char:
                    non_char += 1
                    while non_char > k:
                        if s[left] != char:
                            non_char -= 1
                        left += 1
                longest = max(longest, right - left + 1)
        return longest