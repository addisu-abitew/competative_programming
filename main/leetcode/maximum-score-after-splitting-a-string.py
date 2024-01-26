class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        cur_sum = max_score = 0
        for i in range(1, len(s)):
            cur_sum += int(s[i-1])
            left_score = i - cur_sum
            right_score = ones - cur_sum
            max_score = max(max_score, left_score + right_score)
        return max_score