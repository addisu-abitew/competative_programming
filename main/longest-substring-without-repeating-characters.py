class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        max_len = 0
        for val in s:
            while val in visited:
                visited.remove(s[left])
                left += 1
            visited.add(val)
            max_len = max(max_len, len(visited))
        return max_len