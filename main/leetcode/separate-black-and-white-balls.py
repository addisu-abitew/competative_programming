class Solution:
    def minimumSteps(self, s: str) -> int:
        min_steps = left = 0
        for right in range(len(s)):
            if s[right] == '0':
                min_steps += right-left
                left += 1
        return min_steps